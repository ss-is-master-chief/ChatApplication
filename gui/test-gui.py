import tkinter as tk

class ChatApplication(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MasterPage, RegisterUser):
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

        username_label = tk.Label(self, text="Username")
        username_label.pack(fill=tk.BOTH)

        username_field = tk.Entry(self)
        username_field.pack(fill=tk.BOTH)

        password_label = tk.Label(self, text="Password")
        password_label.pack(fill=tk.BOTH)

        password_field = tk.Entry(self, show="*")
        password_field.pack(fill=tk.BOTH)

        login_button = tk.Button(self, text='Login', command=self.quit)
        login_button.pack(pady=5)

        new_user_button = tk.Button(self, text='Register New User', 
                                    command=lambda: controller.show_frame(RegisterUser))
        new_user_button.pack(fill=tk.BOTH, pady=20)

class RegisterUser(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        username_label = tk.Label(self, text="Enter Username")
        username_label.pack(fill=tk.BOTH, expand=True)

        username_field = tk.Entry(self)
        username_field.pack(fill=tk.BOTH, expand=True)

        password_label = tk.Label(self, text="Enter Password")
        password_label.pack(fill=tk.BOTH, expand=True)

        password_field = tk.Entry(self, show="*")
        password_field.pack(fill=tk.BOTH, expand=True)

        confirm_password_label = tk.Label(self, text="Confirm Password")
        confirm_password_label.pack(fill=tk.BOTH, expand=True)

        confirm_password_field = tk.Entry(self, show="*")
        confirm_password_field.pack(fill=tk.BOTH, expand=True)

        register_button = tk.Button(self, text='Register New User', 
                                    command=lambda: controller.show_frame(RegisterUser))
        register_button.pack(fill=tk.BOTH, expand=True, pady=5)

        back_button = tk.Button(self, text='Back', 
                                command=lambda: controller.show_frame(MasterPage))
        back_button.pack(fill=tk.BOTH, expand=True, pady=5)


app = ChatApplication()
app.mainloop()