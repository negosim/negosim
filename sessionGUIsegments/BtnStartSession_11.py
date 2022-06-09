from GUI.AbstractGUISegment import AbstractGUISegment
import tkinter as tk
from tkinter import messagebox
from core.BilateralSession import BilateralSession
from core.BidSpace import BidSpace
from GUI.visualization.Charts import Charts
from controller import Controller
from core.Preference import Preference

PARTY_PREFERENCE_SEPERATOR = ' -> '


class BtnStartSession_11(AbstractGUISegment):

    def get_widget(self) -> tuple:
        self.first_clicked = False
        btn_start = tk.Button(master=self.get_frame(), text='Start Negotiation',
                              width=42, height=3, command=self.start_negotiation)
        return btn_start,

    def start_negotiation(self):
        protocol_strinVar = self.get_special_segment_special_StringVar(0, 0)
        self.protocol_name = protocol_strinVar.get()

        domain_strinVar = self.get_special_segment_special_StringVar(1, 0)
        self.domain_name = domain_strinVar.get()

        analysis_stringVar = self.get_special_segment_special_StringVar(2, 0)
        self.analysis_name = analysis_stringVar.get()

        deadline_var = self.get_special_segment_special_StringVar(10, 0)
        deadline = deadline_var.get()

        deadline_type_var = self.get_special_segment_special_StringVar(10, 1)
        deadline_type = deadline_type_var.get()

        message = self.check_errors()
        if message != 'Please select ':
            return messagebox.showerror('Error', message)

        listbox_party_preference = self.get_special_widget(8, 0)
        party_preference1_txt = self.get_text_from_listbox(listbox_party_preference, 0)
        self.party1_name, self.party1_preference_name = self.party_preference_text_separator(party_preference1_txt)

        party_preference2_txt = self.get_text_from_listbox(listbox_party_preference, 1)
        self.party2_name, self.party2_preference_name = self.party_preference_text_separator(party_preference2_txt)

        self.bilateral_session = BilateralSession(protocol_name=self.protocol_name,
                                                  analysis_man_name=self.analysis_name,
                                                  deadline=deadline,
                                                  deadline_type=deadline_type,
                                                  first_preference_name=self.party1_preference_name,
                                                  second_preference_name=self.party2_preference_name,
                                                  party1_name=self.party1_name,
                                                  party2_name=self.party2_name,
                                                  domain_name=self.domain_name)
        self.first_clicked = True

        self.bilateral_session.start_session()
        h_frame1 = self.get_special_horizontal_frame(1)
        if not self.first_clicked:
            self.create_visualization_window(h_frame1)
        else:
            h_frame_alternative1 = tk.Frame(master=self.get_root())
            self.replace_special_horizontal_frame(1, h_frame_alternative1)
            self.create_visualization_window(h_frame_alternative1)

    def check_errors(self):
        message = 'Please select '
        if self.protocol_name == 'Select a protocol':
            message += 'Protocol, '
        if self.analysis_name == 'Select a AnalysisMan':
            message += 'AnalysisMan, '
        m_participant_list = self.get_special_widget(8, 0)
        if m_participant_list.size() < 2:
            message += 'participant, '
        if self.domain_name == 'Select a Domain':
            message += 'Domain'
        return message

    def party_preference_text_separator(self, party_preference_text: str) -> tuple:
        temp = party_preference_text.split(PARTY_PREFERENCE_SEPERATOR)
        return temp[0], temp[1]

    def get_text_from_listbox(self, listbox_party_and_preference, row):
        text = listbox_party_and_preference.get(row)
        return text

    def create_visualization_window(self, frame):

        preference1 = Preference(self.domain_name, self.party1_preference_name)
        preference2 = Preference(self.domain_name, self.party2_preference_name)

        # ctrl = Controller()
        # preference1 = ctrl.fetch_preference(self.domain_name, self.party1_preference_name)
        # preference2 = ctrl.fetch_preference(self.domain_name, self.party2_preference_name)
        bid_space1 = BidSpace(preference1)
        bid_space2 = BidSpace(preference2)
        data = {self.party1_preference_name: bid_space1.get_all_bids_utility(),
                self.party2_preference_name: bid_space2.get_all_bids_utility()
                }

        chart = Charts()
        chart.scatter_chart(data=data, col_name1=self.party1_preference_name,
                            col_name2=self.party2_preference_name, frame=frame, position='top')

        protocol = self.bilateral_session.get_protocol()
        analysis_man = self.bilateral_session.get_analysis_man()

        all_offers = protocol.get_nego_table().get_offers_on_table()

        party1 = protocol.get_parties()[0]
        party2 = protocol.get_parties()[1]

        nego_state = protocol.get_nego_table().get_state_info().get_negotiation_state()
        s = ''
        if nego_state == 1:
            s += f"Agreement by {party2.get_name() if len(all_offers[party1]) == len(all_offers[party2]) else party1.get_name()}"
        else:
            s += "negotiation ended without agreement"
        tk.Label(master=frame, text=f'Status : {s}').pack(side='top')

        frame_left = tk.Frame(master=frame)
        frame_mid = tk.Frame(master=frame)
        frame_right = tk.Frame(master=frame)
        frame_left.pack(side='left', fill='both')
        frame_mid.pack(side='left')
        frame_right.pack(side='left', fill='both')

        tk.Label(master=frame_left, text=f'{party1.get_name()}').pack(side='top')
        tk.Label(master=frame_mid, text='  Vs  ').pack(side='top')
        tk.Label(master=frame_right, text=f'{party2.get_name()}').pack(side='top')

        analysis_data = analysis_man.get_analysis_data()

        scr1_horizontal = tk.Scrollbar(master=frame_left, orient=tk.HORIZONTAL)
        scr1_horizontal.pack(side='bottom', fill='x')
        listbox_party1_bids = tk.Listbox(master=frame_left, width=50)
        listbox_party1_bids.pack(side='left', fill='both')
        listbox_party1_bids.config(xscrollcommand=scr1_horizontal.set)
        scr1_horizontal.config(command=listbox_party1_bids.xview)
        scr1_vertical = tk.Scrollbar(master=frame_left)
        scr1_vertical.pack(side='right', fill='y')
        listbox_party1_bids.config(yscrollcommand=scr1_vertical.set)
        scr1_vertical.config(command=listbox_party1_bids.yview)
        listbox_party1_bids.insert(tk.END, *all_offers[party1])
        listbox_party1_bids.insert(tk.END, analysis_data)

        scr2_horizontal = tk.Scrollbar(master=frame_right, orient=tk.HORIZONTAL)
        scr2_horizontal.pack(side='bottom', fill='x')
        listbox_party2_bids = tk.Listbox(master=frame_right, width=50)
        listbox_party2_bids.pack(side='left', fill='both')
        listbox_party2_bids.config(xscrollcommand=scr2_horizontal.set)
        scr2_horizontal.config(command=listbox_party2_bids.xview)
        scr2_vertical = tk.Scrollbar(master=frame_right)
        scr2_vertical.pack(side='right', fill='y')
        listbox_party2_bids.config(yscrollcommand=scr2_vertical.set)
        scr2_vertical.config(command=listbox_party2_bids.yview)
        listbox_party2_bids.insert(tk.END, *all_offers[party2])
        listbox_party2_bids.insert(tk.END, analysis_data)

    def get_name(self):
        return 'BtnStartSession_11.py'
