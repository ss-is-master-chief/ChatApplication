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

        username_label = tk.Label(self, text="Username")
        username_label.pack(fill=tk.BOTH)

        username_field = tk.Entry(self, bd=3, justify="center")
        username_field.pack(fill=tk.BOTH, padx=5)

        password_label = tk.Label(self, text="Password")
        password_label.pack(fill=tk.BOTH)

        password_field = tk.Entry(self, show="*", bd=3, justify="center")
        password_field.pack(fill=tk.BOTH, padx=5)

        login_button = tk.Button(self, text='Login', command=lambda: [controller.show_frame(ChatWindow), enter_data()])
        login_button.pack(pady=10)

        new_user_button = tk.Button(self, text='Sign Up', 
                                    command=lambda: controller.show_frame(RegisterUser))
        new_user_button.pack(fill=tk.BOTH, pady=20)

        def enter_data():
            with open('./data/login-data.csv','a', newline='') as fd:
                writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
                with open('./data/login-data.csv','r') as readfile:
                    csvreader = csv.reader(readfile, delimiter=",")
                    for row in csvreader:
                        if(username_field.get() in row[0]):
                            writer.writerow([username_field.get(), "Valid", datetime.now()])
                        else:
                            writer.writerow([username_field.get(), "Invalid", datetime.now()])
                readfile.close()
            fd.close()

class ChatWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        messages_frame = tk.Frame(self)

        my_msg = tk.StringVar()  # For the messages to be sent.
        my_msg.set("")
        
        scrollbar = tk.Scrollbar(messages_frame)  # To navigate through past messages.
        msg_list = tk.Listbox(messages_frame, height=15, width=60, yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        msg_list.pack(side=tk.TOP, fill=tk.BOTH)
        
        msg_list.pack()

        messages_frame.pack(fill=tk.BOTH)
        button_label = tk.Label(self, text="Enter Message:")
        button_label.pack()
        entry_field = tk.Entry(self, bd=3)
        #entry_field.bind("<Return>", send)
        entry_field.pack()
        send_button = tk.Button(self, text="Send")
        send_button.pack()

        quit_button = tk.Button(self, text="Quit", command=lambda: controller.show_frame(MasterPage))
        quit_button.pack()

class RegisterUser(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        photo = tk.PhotoImage(file="./assets/user-registration.png")
        label = tk.Label(self, image=photo)
        label.image = photo
        label.pack(fill=tk.BOTH, expand=True)

        username_label = tk.Label(self, text="Enter Username")
        username_label.pack(fill=tk.BOTH, expand=True)

        username_field = tk.Entry(self, justify="center")
        username_field.pack(fill=tk.BOTH, expand=True)

        password_label = tk.Label(self, text="Enter Password")
        password_label.pack(fill=tk.BOTH, expand=True)

        password_field = tk.Entry(self, show="*", justify="center")
        password_field.pack(fill=tk.BOTH, expand=True)

        confirm_password_label = tk.Label(self, text="Confirm Password")
        confirm_password_label.pack(fill=tk.BOTH, expand=True)

        confirm_password_field = tk.Entry(self, show="*", justify="center")
        confirm_password_field.pack(fill=tk.BOTH, expand=True)

        register_button = tk.Button(self, text='Register New User', 
                                    command=lambda: [controller.show_frame(SuccessfulRegistration), enter_data()])
        register_button.pack(fill=tk.BOTH, expand=True, pady=5)

        def enter_data():
            with open('./data/registration-data.csv','a', newline='') as fd:
                writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
                writer.writerow([username_field.get(), password_field.get(), datetime.now()])
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
app.mainloop()