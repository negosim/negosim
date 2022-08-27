from configurations import *
import tkinter as tk
from tkinter import ttk
from GUI import tournamentGUI, sessionGUI2, sessionGUI
import controller
from core.BidSpace import BidSpace
from tkinter import messagebox
from GUI.visualization.Charts import Charts
from core.Preference import Preference

EUBOA_SEPERATOR = ' ---> '
SELECT_PREFERENCE_2 = 'Please Select Preference 2'
SELECT_PREFERENCE_1 = 'Please Select Preference 1'


class View:
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        self.b = False
        self.init_GUI()

    def init_GUI(self):
        self.create_top_menu()
        self.create_main_window()

    def create_top_menu(self):
        self.menu_bar = tk.Menu(self.parent)
        self.create_start_menu()
        self.create_file_menu()
        self.create_help_menu()

    def create_start_menu(self):
        self.start_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.start_menu.add_command(
            label='Negotiation', command=self.session_window)
        self.start_menu.add_command(
            label='Tournament', command=self.tornument_window)

        # self.start_menu.add_command(
        #     label='Negotiation (Uncertain condition)', command=self.session_window_uncertain_condition)
        # self.start_menu.add_command(
        #     label='Tournament (Uncertain condition)', command=self.tornument_window)

        self.menu_bar.add_cascade(label='Start', menu=self.start_menu)
        self.parent.config(menu=self.menu_bar)

    def create_file_menu(self):
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(
            label='Add Domain', command=self.add_domain_file)
        self.file_menu.add_command(
            label='Add Elicitation Strategy', command=self.add_elicitation_strategy_file)
        self.file_menu.add_command(
            label='Add User GUIContent', command=self.add_user_model_file)
        self.file_menu.add_command(
            label='Add Bidding Strategy', command=self.add_bidding_strategy_file)
        self.file_menu.add_command(
            label='Add Opponent GUIContent', command=self.add_opponent_model_file)
        self.file_menu.add_command(
            label='Add Acceptance Strategy', command=self.add_acceptance_strategy_file)
        self.file_menu.add_command(
            label='Create Domain Set', command=self.create_domain_set)
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)
        self.parent.config(menu=self.menu_bar)

    def add_domain_file(self):
        tk.messagebox.showinfo('Try manually!',
                               'This part is not completed! \nYou have to add the domain file to Domains folder manually')

    def add_elicitation_strategy_file(self):
        tk.messagebox.showinfo('Try manually!', 'This part is not completed! \n'
                                                'You have to add the elicitation strategy file to the elicitation_strategies folder manually')

    def add_user_model_file(self):
        tk.messagebox.showinfo('Try manually!',
                               'This part is not completed! \nYou have to add the user model file to the users folder manually')

    def add_bidding_strategy_file(self):
        tk.messagebox.showinfo('Try manually!',
                               'This part is not completed! \nYou have to add the bidding strategy file to the bidding_strategies folder manually')

    def add_opponent_model_file(self):
        tk.messagebox.showinfo('Try manually!',
                               'This part is not completed! \nYou have to add the opponent model file to the opponent_models folder manually')

    def add_acceptance_strategy_file(self):
        tk.messagebox.showinfo('Try manually!',
                               'This part is not completed! \nYou have to add the acceptance strategy file to the acceptance_strategies folder manually')

    def create_domain_set(self):
        tk.messagebox.showinfo('Try manually!', 'This part is not completed!')

    def session_window(self):
        self.open_session_window()

    def session_window_uncertain_condition(self):
        self.open_session_window_uncertain_condition()

    # def open_session_window(self):
    #     window_session = tk.Toplevel(self.parent)
    #     # window_session.geometry("400x400")
    #     window_session.title("New Session")
    #     sessionGUI.Session(window_session)

    def open_session_window(self):
        window_session = tk.Toplevel(self.parent)
        # window_session.geometry("400x400")
        window_session.title("New Session")
        sessionGUI2.SessionGUI2(window_session)

    def open_session_window_uncertain_condition(self):
        window_session = tk.Toplevel(self.parent)
        # window_session.geometry("400x400")
        window_session.title("New Session (Uncertain condition)")
        sessionGUI.Session(window_session)

    def tornument_window(self):
        self.open_tornument_window()

    def open_tornument_window(self):
        tornument_window = tk.Toplevel(self.parent)
        tornument_window.geometry("400x400")
        tornument_window.title("New Tornument")
        tournamentGUI.Tournament(tornument_window)

    def create_help_menu(self):
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='Help', menu=self.help_menu)
        self.parent.config(menu=self.menu_bar)

    def create_main_window(self):

        frame_left_bottom = tk.Frame(self.parent)
        frame_left_bottom.pack(side='bottom', fill='x')

        frame_left = tk.Frame(self.parent)
        frame_left.pack(side='left')

        self.create_notebook_window(frame_left)

    def listbox_domain_clickEvent(self, event):
        selection = event.widget.curselection()
        if len(selection) > 0:
            index = selection[0]
            self.selected_domain_name = event.widget.get(index)
            preference_list = self.controller.fetch_preferences_of_domain(self.selected_domain_name)
            if len(preference_list) > 0:
                self.create_visualization_tools(preference_list)

    def create_visualization_tools(self, preference_lists):
        self.frame_visualization_tools.destroy()
        self.frame_visualization_tools = tk.Frame(master=self.frame_domain, width=100, height=10)
        self.frame_visualization_tools.pack(side='bottom')

        btn_preference_visualization = ttk.Button(master=self.frame_visualization_tools, text='Visualize', width=67,
                                                  command=lambda: self.create_chart(
                                                      btn_preference_visualization))

        btn_preference_visualization.pack(side='bottom', pady=2, padx=2, ipady=5)

        self.var_selected_preference2_name = tk.StringVar()
        self.var_selected_preference2_name.set(SELECT_PREFERENCE_2)
        optionMenu_select_preference2 = tk.OptionMenu(self.frame_visualization_tools,
                                                      self.var_selected_preference2_name, *preference_lists)
        optionMenu_select_preference2.pack(side='bottom')

        self.var_selected_preference1_name = tk.StringVar()
        self.var_selected_preference1_name.set(SELECT_PREFERENCE_1)
        optionMenu_select_preference1 = tk.OptionMenu(self.frame_visualization_tools,
                                                      self.var_selected_preference1_name, *preference_lists)
        optionMenu_select_preference1.pack(side='bottom')

    def create_notebook_window(self, frame):
        notebook_component = ttk.Notebook(frame, height=400)
        # notebook_component.grid(row=0, column=0)
        notebook_component.pack(side=tk.LEFT, fill=tk.BOTH)

        # frame_domain_set = ttk.Frame(notebook_component)
        self.frame_domain = ttk.Frame(notebook_component)
        frame_user = ttk.Frame(notebook_component)
        frame_euboa = ttk.Frame(notebook_component)
        frame_protocol = ttk.Frame(notebook_component)
        frame_analyses = ttk.Frame(notebook_component)
        frame_plugins = ttk.Frame(notebook_component)
        frame_tournament_plugins = ttk.Frame(notebook_component)

        listbox_domain = tk.Listbox(self.frame_domain)
        i = 1
        for item in self.controller.fetch_domains():
            listbox_domain.insert(i, item)
            i += 1
        listbox_domain.pack(fill='both')
        listbox_domain.bind('<<ListboxSelect>>', self.listbox_domain_clickEvent)
        self.frame_visualization_tools = tk.Frame(master=self.frame_domain, width=100, height=10)
        self.frame_visualization_tools.pack(side='bottom')

        listbox_user = tk.Listbox(frame_user)
        i = 1
        for item in self.controller.fetch_users():
            listbox_user.insert(i, item)
            i += 1
        listbox_user.pack(fill='both')

        listbox_euboa = tk.Listbox(frame_euboa)
        i = 1
        for item in self.controller.fetch_elicitation_strategies():
            listbox_euboa.insert(i, 'Elicitation Strategy' + EUBOA_SEPERATOR + item)
            i += 1
        for item in self.controller.fetch_user_models():
            listbox_euboa.insert(i, 'User Model' + EUBOA_SEPERATOR + item)
            i += 1
        for item in self.controller.fetch_bidding_strategies():
            listbox_euboa.insert(i, 'Bidding Strategy' + EUBOA_SEPERATOR + item)
            i += 1
        for item in self.controller.fetch_opponent_models():
            listbox_euboa.insert(i, 'Opponent Model' + EUBOA_SEPERATOR + item)
            i += 1
        for item in self.controller.fetch_acceptance_strategies():
            listbox_euboa.insert(i, 'Acceptance Strategy' + EUBOA_SEPERATOR + item)
            i += 1
        listbox_euboa.pack(fill='both')

        listbox_protocol = tk.Listbox(frame_protocol)
        i = 1
        for item in self.controller.fetch_protocols():
            listbox_protocol.insert(i, 'Protocol' + EUBOA_SEPERATOR + item)
        listbox_protocol.pack(fill='both')

        listbox_analysis = tk.Listbox(frame_analyses)
        i = 1
        for item in self.controller.fetch_analysis_men():
            listbox_analysis.insert(i, item)
        listbox_analysis.pack(fill='both')

        listbox_plugins = tk.Listbox(frame_plugins)
        i = 1
        for item in self.controller.fetch_session_gui_segments():
            listbox_plugins.insert(i, item)
        listbox_plugins.pack(fill='both')

        listbox_tournament_plugins = tk.Listbox(frame_tournament_plugins)
        i = 1
        for item in self.controller.fetch_tournament_gui_segments():
            listbox_tournament_plugins.insert(i, item)
        listbox_tournament_plugins.pack(fill='both')

        # notebook_component.add(frame_domain_set, text=' Domain Set ')
        notebook_component.add(self.frame_domain, text=' Domain ')
        notebook_component.add(frame_user, text=' User ')
        notebook_component.add(frame_euboa, text=' EUBOA Component')
        notebook_component.add(frame_protocol, text=' Protocols ')
        notebook_component.add(frame_analyses, text=' Analyses ')
        notebook_component.add(frame_plugins, text='Session theme plugins')
        notebook_component.add(frame_tournament_plugins, text='Tournament theme plugins')

    def close_diagram(self, btn_preference_visualization, frame_right):
        frame_right.destroy()
        btn_preference_visualization.config(state='active')

    def create_chart(self, btn_preference_visualization):

        if self.var_selected_preference1_name.get() == SELECT_PREFERENCE_1 or self.var_selected_preference2_name.get() == SELECT_PREFERENCE_2:
            return messagebox.showerror('Error', 'Please select both preference 1 and 2!')

        btn_preference_visualization.config(state='disable')

        frame_right = tk.Frame(self.parent)
        frame_right.pack(side='bottom', fill='x')

        ttk.Button(master=frame_right, text='Close',
                   command=lambda: self.close_diagram(btn_preference_visualization, frame_right)).pack(fill='x')

        # preference1 = self.controller.fetch_preference(self.selected_domain_name,
        #                                                self.var_selected_preference1_name.get())
        # preference2 = self.controller.fetch_preference(self.selected_domain_name,
        #                                                self.var_selected_preference2_name.get())

        preference1 = Preference(self.selected_domain_name, self.var_selected_preference1_name.get())
        preference2 = Preference(self.selected_domain_name, self.var_selected_preference2_name.get())


        bid_space1 = BidSpace(preference1)
        bid_space2 = BidSpace(preference2)
        data = {self.var_selected_preference1_name.get(): bid_space1.get_all_bids_utility(),
                self.var_selected_preference2_name.get(): bid_space2.get_all_bids_utility()
                }

        chart = Charts()
        chart.scatter_chart(data=data, col_name1=self.var_selected_preference1_name.get(),
                            col_name2=self.var_selected_preference2_name.get(), frame=frame_right, position='top')


if __name__ == '__main__':
    root = tk.Tk()
    # root.geometry(f'{WIDTH_GUI}x{HEIGHT_GUI}')
    root.title(PROGRAM_NAME)
    View(root, controller.Controller())
    root.mainloop()
