import tkinter as tk
import csv
from datetime import datetime

class ChatApplication(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MasterPage, ChatWindow, RegisterUser, SuccessfulRegistration):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MasterPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class MasterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        photo = tk.PhotoImage(file="./assets/chat-logo.png")
        label = tk.Label(self, image=photo)
        label.image = photo
        label.pack(fill=tk.BOTH, expand=True)

        login_label_frame = tk.Frame(self)
        login_label_frame.pack(fill=tk.BOTH, expand=True, padx=3, pady=3)

        user_label_frame = tk.LabelFrame(login_label_frame, text="Enter Username")
        user_label_frame.pack(fill=tk.BOTH, expand=True)
        user_entry_field = tk.Entry(user_label_frame, bd=3)
        user_entry_field.pack(side=tk.BOTTOM, fill=tk.X, expand=True)
        # user_label = tk.Label(user_label_frame, text="Username")
        # user_label.pack(side=tk.LEFT, fill=tk.BOTH)
        pass_label_frame = tk.LabelFrame(login_label_frame, text="Enter Password")
        pass_label_frame.pack(fill=tk.BOTH, expand=True)
        pass_entry_field = tk.Entry(pass_label_frame, show="*", bd=3)
        pass_entry_field.pack(side=tk.BOTTOM, fill=tk.X, expand=True)

        login_button = tk.Button(self, text='Login', command=lambda: [controller.show_frame(ChatWindow), enter_data()])
        login_button.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=160, pady=10)

        new_user_button = tk.Button(self, text='New User? Sign Up', 
                                    command=lambda: controller.show_frame(RegisterUser))
        new_user_button.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=160, pady=10)

        def enter_data():
            with open('./data/login-data.csv','a', newline='') as fd:
                writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
                with open('./data/login-data.csv','r') as readfile:
                    csvreader = csv.reader(readfile, delimiter=",")
                    for row in csvreader:
                        if(user_entry_field.get() in row[0]):
                            writer.writerow([user_entry_field.get(), "Valid", datetime.now()])
                        else:
                            writer.writerow([user_entry_field.get(), "Invalid", datetime.now()])
                readfile.close()
            fd.close()

class ChatWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        chat_frame = tk.LabelFrame(self, text="CHAT ROOM", bg="#ebd1bc")
        chat_frame.pack(fill=tk.BOTH, padx=3, pady=3, expand=True)

        my_msg = tk.StringVar()  # For the messages to be sent.
        my_msg.set("")
        
        scrollbar = tk.Scrollbar(chat_frame)  # To navigate through past messages.
        msg_list = tk.Listbox(chat_frame, height=15, width=60, yscrollcommand=scrollbar.set)
        msg_list.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
        msg_list.pack(padx=5, pady=5)

        username_status_frame = tk.LabelFrame(self, text="ONLINE USERS")
        username_status_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=3, pady=3, expand=True)

        '''
        ENTER SCROLLBAR IN ONLINE USERS FRAME
        '''

        label = tk.Label(username_status_frame, text="User1\nUser2\nUser3")
        label.pack(side=tk.LEFT, expand=True)

        message_frame = tk.LabelFrame(self, text="CONSOLE")
        message_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=3, pady=3, expand=True)

        to_label_frame = tk.Frame(message_frame)
        to_label_frame.pack(fill=tk.BOTH, expand=True)
        to_label = tk.Label(to_label_frame, text="To User")
        to_label.pack(side=tk.LEFT, fill=tk.X)
        to_field = tk.Entry(to_label_frame, bd=3, width=45)
        #entry_field.bind("<Return>", send)
        to_field.pack(fill=tk.X, expand=True)

        message_label_frame = tk.Frame(message_frame)
        message_label_frame.pack(fill=tk.BOTH, expand=True)
        button_label = tk.Label(message_label_frame, text="Message")
        button_label.pack(side=tk.LEFT, fill=tk.X)
        entry_field = tk.Entry(message_label_frame, bd=3, width=45)
        #entry_field.bind("<Return>", send)
        entry_field.pack(fill=tk.X, expand=True)
        
        button_frame = tk.Frame(message_frame)
        button_frame.pack(fill=tk.BOTH, expand=True)
        send_button = tk.Button(button_frame, text="Send")
        send_button.pack(fill=tk.BOTH, pady=10, expand=True)

        logout_button = tk.Button(button_frame, text="Logout", command=lambda: controller.show_frame(MasterPage))
        logout_button.pack(fill=tk.BOTH, pady=3, expand=True)

class RegisterUser(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        photo = tk.PhotoImage(file="./assets/user-registration.png")
        label = tk.Label(self, image=photo)
        label.image = photo
        label.pack(fill=tk.BOTH, expand=True)

        regn_label_frame = tk.Frame(self)
        regn_label_frame.pack(fill=tk.BOTH, expand=True, padx=3, pady=3)

        reg_user_label_frame = tk.LabelFrame(regn_label_frame, text="Enter Username")
        reg_user_label_frame.pack(fill=tk.BOTH, expand=True)
        reg_user_entry_field = tk.Entry(reg_user_label_frame, bd=3)
        reg_user_entry_field.pack(fill=tk.X, expand=True)

        reg_pass_label_frame = tk.LabelFrame(regn_label_frame, text="Enter Password")
        reg_pass_label_frame.pack(fill=tk.BOTH, expand=True)
        reg_pass_entry_field = tk.Entry(reg_pass_label_frame, show="*", bd=3)
        reg_pass_entry_field.pack(fill=tk.X, expand=True)

        reg_confirm_pass_label_frame = tk.LabelFrame(regn_label_frame, text="Confrim Password")
        reg_confirm_pass_label_frame.pack(fill=tk.BOTH, expand=True)
        reg_confirm_pass_entry_field = tk.Entry(reg_confirm_pass_label_frame, show="*", bd=3)
        reg_confirm_pass_entry_field.pack(fill=tk.X, expand=True)

        register_button = tk.Button(self, text='Register New User', 
                                    command=lambda: [controller.show_frame(SuccessfulRegistration), enter_data()])
        register_button.pack(fill=tk.BOTH, expand=True, pady=5)

        def enter_data():
            with open('./data/registration-data.csv','a', newline='') as fd:
                writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
                writer.writerow([reg_user_entry_field.get(), reg_pass_entry_field.get(), datetime.now()])
            fd.close()

        back_button = tk.Button(self, text='Back', 
                                command=lambda: controller.show_frame(MasterPage))
        back_button.pack(fill=tk.BOTH, expand=True, pady=5)

class SuccessfulRegistration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        photo = tk.PhotoImage(file="./assets/green-tick.png")
        label = tk.Label(self, image=photo)
        label.image = photo
        label.pack(fill=tk.BOTH, expand=True)
        
        success_note = tk.Label(self, text="User Successfully Registered!")
        success_note.pack(fill=tk.BOTH, expand=True)
        
        back_button = tk.Button(self, text='Back', 
                                command=lambda: controller.show_frame(MasterPage))
        back_button.pack(fill=tk.BOTH, expand=True, pady=5)


app = ChatApplication()
app.title("ChatApplication")
app.mainloop()