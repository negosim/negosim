import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import controller
from core.BidSpace import BidSpace
from GUI.visualization.Charts import Charts
from core.BilateralSession import BilateralSession

WINDOW_NAME = 'New Session'
SELECT_USER_TEXT = 'Select a User'
SELECT_PROTOCOL_TEXT = 'Select a Protocol'
SELECT_DOMAIN_TEXT = 'Select a Domain'
SELECT_ANALYSE_TEXT = 'Select an Analyse'
ADD_PARTICIPANT_ERROR_MESSAGE = 'Please select both party and preference then click "Add Participant"'
ADD_PARTICIPANT_BUTTON_TEXT = 'Add Participant'
DELETE_PARTICIPANT_BUTTON_TEXT = 'Delete Participant'
SELECT_PARTY_TEXT = 'Select a Party'
SELECT_PREFERENCE_PROFILE = 'Select a Preference Profile'
WRONG_DIR_PATH_ERROR = 'The directory path is wrong!'
LESS_THAN_TWO_PREFERENCES = 'The directory path has less the two preferences!'
INEQUALITY_OF_TWO_DOMAINS_ERROR = 'Please Select both parties preferences from the same domain!'
SELECTED_DOMAIN_PROBLEM_ERROR = 'Your selected domain has problem, \n Please select another domain!'
SESSION_WITH_MORETHAN_TWO_PARTICIPATNT_ERROR = "Session can only run with two participant \n Please delete one of participants"
PARTY_DOMAINPREFERENCE_SEPARATOR_SYMBOL = ' -> '
DOMAIN_PREFERENCE_SEPARATOR_SYMBOL = '/'
MIN_MAX_PARTICIPANTS = 2
INITIAL_DEADLINE_TIME = 60
MAX_DEADLINE_TIME = 3600000


class Session:

    def __init__(self, window):
        self.my_row = 0
        self.window = window
        self.init_controller()
        self.create_session_gui()

    def init_controller(self):
        self.controller = controller.Controller()

    def create_visualization_window(self, frame):

        preference1 = self.controller.fetch_preference(self.var_domain_name.get(),
                                                       self.get_domain_preference(0)[1])
        preference2 = self.controller.fetch_preference(self.var_domain_name.get(),
                                                       self.get_domain_preference(1)[1])
        bid_space1 = BidSpace(preference1)
        bid_space2 = BidSpace(preference2)
        data = {self.get_domain_preference(0)[1]: bid_space1.get_all_bids_utility(),
                self.get_domain_preference(1)[1]: bid_space2.get_all_bids_utility()
                }

        chart = Charts()
        chart.scatter_chart(data=data, col_name1=self.get_domain_preference(0)[1],
                            col_name2=self.get_domain_preference(1)[1], frame=frame, position='top')

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

    # def create_progress_bar(self, row):
    #     self.my_row += 1
    #     self.progress = Progressbar(self.frame_session, orient=tk.HORIZONTAL, length=100, mode='determinate')
    #     self.progress.grid(row=row, column=0, columnspan=3, sticky='we', pady=10)
    #     self.my_row += 1

    def create_session_gui(self):

        self.frame_session = tk.Frame(self.window)
        self.frame_session.grid(
            row=0, column=0, columnspan=10, padx=40, pady=10)

        self.create_user_menu()

        # In order to make space
        tk.Label(self.frame_session, text='').grid(row=self.my_row, column=1)
        self.my_row += 1

        self.create_protocol_menu()
        self.create_domain_menu()
        self.create_analyse_menu()

        # In order to make space
        tk.Label(self.frame_session, text='').grid(row=self.my_row, column=1)
        self.my_row += 1

        # In order to show the rest content
        tk.Label(self.frame_session, text=' Participant ').grid(
            row=self.my_row, column=1)
        self.my_row += 1

        # In order to separate content
        ttk.Separator(self.frame_session, orient='horizontal').grid(
            row=self.my_row, column=0, columnspan=10, sticky='we')
        self.my_row += 1

        self.create_select_party()
        self.my_row += 2
        # Button in order to add participant
        self.btn_add_participant = ttk.Button(
            self.frame_session, text=ADD_PARTICIPANT_BUTTON_TEXT, command=self.add_participant)
        self.btn_add_participant.grid(
            row=self.my_row, column=0, columnspan=3, sticky='we', padx=2)
        self.my_row += 1

        # List box that show the negotiation participants
        self.listbox_party_and_preference = tk.Listbox(self.frame_session)
        self.listbox_party_and_preference.grid(
            row=self.my_row, column=0, columnspan=5, sticky='we', pady=2)
        self.my_row += 1

        # Delete Button in order to delete the participant
        btn_delete_participant = ttk.Button(self.frame_session, text=DELETE_PARTICIPANT_BUTTON_TEXT,
                                            command=self.delete_participant)
        btn_delete_participant.grid(
            row=self.my_row, column=0, columnspan=5, sticky='we')
        self.my_row += 1

        # In order to make space
        tk.Label(self.frame_session, text='', pady=5).grid(
            row=self.my_row, column=1)
        self.my_row += 1

        # Show Information to user
        tk.Label(self.frame_session, text=' Session Setting ',
                 pady=5).grid(row=self.my_row, column=1)
        self.my_row += 1

        # In order to separate content
        ttk.Separator(self.frame_session, orient='horizontal').grid(
            row=self.my_row, column=0, columnspan=10, sticky='we')
        self.my_row += 1

        self.create_deadline_menu()

        btn_start = ttk.Button(self.frame_session, text=' Start ',
                               padding=5, command=self.start_negotiation_session)
        btn_start.grid(row=self.my_row, column=0,
                       columnspan=5, sticky='we', pady=15)
        self.my_row += 1

    def delete_participant(self):
        self.listbox_party_and_preference.delete(tk.ANCHOR)
        self.btn_add_participant.config(state='enable')

    def create_user_menu(self):
        self.my_row += 1
        tk.Label(self.frame_session, text='User ').grid(
            row=self.my_row, column=0)
        user_list = self.controller.fetch_users()
        self.var_user_name = tk.StringVar()
        self.var_user_name.set(SELECT_USER_TEXT)
        self.optionMenu_user = tk.OptionMenu(
            self.frame_session, self.var_user_name, *user_list)
        self.optionMenu_user.config(width=25)
        self.optionMenu_user.grid(
            row=self.my_row, column=1, columnspan=2, sticky='we')
        self.my_row += 1

    # Option menu in order to select the protocol
    def create_protocol_menu(self):
        tk.Label(self.frame_session, text='Protocol ').grid(
            row=self.my_row, column=0)
        protocol_list = self.controller.fetch_protocols()
        self.var_protocol_name = tk.StringVar()
        self.var_protocol_name.set(SELECT_PROTOCOL_TEXT)
        self.optionMenu_protocol = tk.OptionMenu(
            self.frame_session, self.var_protocol_name, *protocol_list)
        self.optionMenu_protocol.config(width=25)
        self.optionMenu_protocol.grid(
            row=self.my_row, column=1, columnspan=2, sticky='we')
        self.my_row += 1

    # Option menu in order to select the domain
    def create_domain_menu(self):
        tk.Label(self.frame_session, text='Domain ').grid(
            row=self.my_row, column=0)
        domain_lists = self.controller.fetch_domains()
        self.var_domain_name = tk.StringVar()
        self.var_domain_name.set(SELECT_DOMAIN_TEXT)
        self.optionMenu_domain = tk.OptionMenu(
            self.frame_session, self.var_domain_name, *domain_lists, command=self.create_select_preference)
        self.optionMenu_domain.config(width=25)
        self.optionMenu_domain.grid(
            row=self.my_row, column=1, columnspan=2, sticky='we')
        self.my_row += 2

    # Option menu in order to select the analyse file
    def create_analyse_menu(self):
        tk.Label(self.frame_session, text='Analyse file ').grid(
            row=self.my_row, column=0)
        self.analyse_list = self.controller.fetch_analysis_men()
        self.var_analyse_name = tk.StringVar()
        self.var_analyse_name.set(SELECT_ANALYSE_TEXT)
        self.optionMenu_analyse = tk.OptionMenu(
            self.frame_session, self.var_analyse_name, *self.analyse_list)
        self.optionMenu_analyse.config(width=25)
        self.optionMenu_analyse.grid(
            row=self.my_row, column=1, columnspan=2, sticky='we')
        self.my_row += 1

    # Option menu in order to select the party
    def create_select_party(self):
        tk.Label(self.frame_session, text=' Party Name ', padx=15).grid(
            row=self.my_row, column=0)
        party_list = self.controller.fetch_agents()
        self.var_party_name = tk.StringVar()
        self.var_party_name.set(SELECT_PARTY_TEXT)
        self.optionMenu_party = tk.OptionMenu(
            self.frame_session, self.var_party_name, *party_list)
        self.optionMenu_party.config(width=25)
        self.optionMenu_party.grid(
            row=self.my_row, column=1, columnspan=2, sticky='we')
        self.my_row += 1

    # Option menu in order to select the preference profile
    def create_select_preference(self, selected_domain):
        self.var_preference_profile_name = tk.StringVar()
        preference_profile_list = self.controller.fetch_preferences_of_domain(
            selected_domain)
        if preference_profile_list == None:
            return messagebox.showerror('Error', WRONG_DIR_PATH_ERROR)
        if len(preference_profile_list) <= 1:
            return messagebox.showerror('Error', LESS_THAN_TWO_PREFERENCES)
        tk.Label(self.frame_session, text='Preference Profile').grid(
            row=11, column=0)
        self.var_preference_profile_name.set(SELECT_PREFERENCE_PROFILE)
        self.optionMenu_preference_profile = tk.OptionMenu(
            self.frame_session, self.var_preference_profile_name, *preference_profile_list)
        self.optionMenu_preference_profile.config(width=25)
        self.optionMenu_preference_profile.grid(
            row=11, column=1, columnspan=2, sticky='we')
        self.my_row += 1

    # Show Deadline time
    def create_deadline_menu(self):
        tk.Label(self.frame_session, text=' Deadline ',
                 pady=5).grid(row=self.my_row, column=0)
        self.var_deadline = tk.StringVar()
        self.spinbox_deadline = tk.Spinbox(
            self.frame_session, from_=1, to=MAX_DEADLINE_TIME, textvariable=self.var_deadline)
        self.spinbox_deadline.delete(0, 'end')
        self.spinbox_deadline.insert(0, INITIAL_DEADLINE_TIME)
        self.spinbox_deadline.grid(row=self.my_row, column=1)
        self.var_time_type = tk.StringVar()
        self.time_type = ttk.OptionMenu(
            self.frame_session, self.var_time_type, 's', *['s'])
        self.time_type.config(width=3)
        self.time_type.grid(row=self.my_row, column=2)
        self.my_row += 1

    # This method add participants if there is no error
    def add_participant(self):
        if self.var_domain_name.get() == SELECT_DOMAIN_TEXT:
            return messagebox.showerror('Error', 'Please ' + SELECT_DOMAIN_TEXT)
        if self.var_preference_profile_name.get() == '':
            return messagebox.showerror('Error', SELECTED_DOMAIN_PROBLEM_ERROR)

        number_of_items = self.listbox_party_and_preference.size()
        if self.var_party_name.get() == SELECT_PARTY_TEXT or self.var_preference_profile_name.get() == SELECT_PREFERENCE_PROFILE:
            return messagebox.showerror(
                title='Error!', message=ADD_PARTICIPANT_ERROR_MESSAGE)
        self.listbox_party_and_preference.insert(
            number_of_items + 1,
            f"{self.var_party_name.get()}{PARTY_DOMAINPREFERENCE_SEPARATOR_SYMBOL}{self.var_domain_name.get()}{DOMAIN_PREFERENCE_SEPARATOR_SYMBOL}{self.var_preference_profile_name.get()}")
        if self.listbox_party_and_preference.size() >= MIN_MAX_PARTICIPANTS:
            self.btn_add_participant.config(state='disable')

    def start_negotiation_session(self):

        message = 'Please select'
        if self.var_user_name.get() == SELECT_USER_TEXT:
            message += ' User,'
        if self.var_protocol_name.get() == SELECT_PROTOCOL_TEXT:
            message += ' Protocol,'
        if self.var_domain_name.get() == SELECT_DOMAIN_TEXT:
            message += ' domain,'
        if self.var_analyse_name.get() == SELECT_ANALYSE_TEXT:
            message += ' Analyse,'
        if self.listbox_party_and_preference.size() < MIN_MAX_PARTICIPANTS:
            message += ' 2 participatnts,'

        if message != 'Please select':
            return messagebox.showerror(
                title='Error!', message=message)

        if self.listbox_party_and_preference.size() > MIN_MAX_PARTICIPANTS:
            return messagebox.showerror(
                title='Error!', message=SESSION_WITH_MORETHAN_TWO_PARTICIPATNT_ERROR)

        first_domain_name, first_preference_name = self.get_domain_preference(0)
        second_domain_name, second_preference_name = self.get_domain_preference(1)
        if first_domain_name != second_domain_name:
            return messagebox.showerror(
                title='Error!', message=INEQUALITY_OF_TWO_DOMAINS_ERROR)

        self.frame_visualization = tk.Frame(self.window)
        self.frame_visualization.grid(row=0, column=11)
        self.start_negotiation1()
        self.create_visualization_window(self.frame_visualization)

    def start_negotiation1(self):
        first_domain_name, first_preference_name = self.get_domain_preference(0)
        second_domain_name, second_preference_name = self.get_domain_preference(1)
        protocol_name = self.var_protocol_name.get()
        analysis_man_name = self.var_analyse_name.get()
        file_name1 = self.get_party(0)
        file_name2 = self.get_party(1)
        deadline = float(self.var_deadline.get())
        self.bilateral_session = BilateralSession(protocol_name=protocol_name,
                                                  analysis_man_name=analysis_man_name,
                                                  deadline=deadline,
                                                  first_preference=first_preference_name,
                                                  second_preference=second_preference_name,
                                                  party1_name=file_name1, party2_name=file_name2,
                                                  domain_name=self.var_domain_name.get())
        self.bilateral_session.start_session()

    def get_text_from_listbox(self, row):
        text = self.listbox_party_and_preference.get(
            row)
        return text

    def text_splitor(self, text, separator):
        seperated_text_list = str(text).split(separator)
        return seperated_text_list

    def get_party(self, row):
        party_domain_preference_text = self.get_text_from_listbox(row)
        party_text = self.text_splitor(
            party_domain_preference_text, PARTY_DOMAINPREFERENCE_SEPARATOR_SYMBOL)[0]
        return party_text

    def get_domain_preference(self, row) -> str:
        """
        :param row:
        :return: elicited domain name and preference_name
        """
        party_domain_preference_text = self.get_text_from_listbox(row)
        domain_preference_text = self.text_splitor(
            party_domain_preference_text, PARTY_DOMAINPREFERENCE_SEPARATOR_SYMBOL)[1]
        domain_name, preference_name = self.text_splitor(
            domain_preference_text, DOMAIN_PREFERENCE_SEPARATOR_SYMBOL)
        return domain_name, preference_name


if __name__ == '__main__':
    root = tk.Tk()
    root.title(WINDOW_NAME)
    # root.geometry('400x400')
    Session(root)
    root.mainloop()
