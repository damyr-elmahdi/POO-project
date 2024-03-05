from tkinter import*
from PIL import ImageTk, Image
import customtkinter
import tkinter
import csv
from tkinter import messagebox

class User_login():
    def page_user(self):
                win3 = Tk()
                win3.title("Page_user")
                
                img2=ImageTk.PhotoImage(Image.open("images/img2.png"))
                l1=customtkinter.CTkLabel(win3,image=img2)
                l1.pack()
                
                frame=customtkinter.CTkFrame(master = l1, width=340, height=450, corner_radius=6)
                frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

                button1 = customtkinter.CTkButton(frame, width=140, height=35, text="User", corner_radius=6, font=('Times New Roman',17,'bold'))
                button1.place(x=15, y=20)

                button2 = customtkinter.CTkButton(frame, width=140, height=35, text="Login", corner_radius=6, font=('Times New Roman',17,'bold'))
                button2.place(x=180, y=20)

                l2=customtkinter.CTkLabel(frame, text="Entrer votre information",font=('Times New Roman',25,'bold'))
                l2.place(x=40, y=90)

                Email= customtkinter.CTkEntry(frame, width=220, height=35, placeholder_text='Entrer votre email')
                Email.place(x=55, y=150)

                Password=customtkinter.CTkEntry(frame, width=220, height=35, placeholder_text='Entrer votre password', show="*")
                Password.place(x=55, y=215)
                
                entry2=customtkinter.CTkLabel(frame, text = "Forget password", font =('Century Gothic', 12))
                entry2.place(x=170, y=255)

                button3 = customtkinter.CTkButton(frame, width=220, height=35, text="Entrer", corner_radius=6, font=('Times New Roman',17,'bold'))
                button3.place(x=55, y=290)
                
                btn_login = customtkinter.CTkButton(frame, width=140, height=35, text="Login", corner_radius=6,fg_color="#db3e00", hover_color="#bc6202", font=('Times New Roman',17,'bold'))
                btn_login.place(x=15, y=355)

                button2 = customtkinter.CTkButton(frame, width=140, height=35, text="Sin up", corner_radius=6, fg_color="#db3e00", hover_color="#bc6202", font=('Times New Roman',17,'bold'))
                button2.place(x=180, y=355)
                
                but_back = customtkinter.CTkButton(frame,width=85, height=35, text="Back", corner_radius=6, font=('Times New Roman',17,'bold'))
                but_back.place(x=20, y=405)
                
                email = Email.get()
                password = Password.get()
                
                with open('document.csv', 'r') as file:
                    csv_reader = csv.reader(file)
                    for row in csv_reader:
                        if row[0] == email and row[1] == password:
                            Page_for_user()
                            return
                messagebox.showerror("Error", "Invalid email or password")
                
                def Page_for_user():
                    win3.destroy()  # Close the login window
                    second_window = Tk()
                    second_window.title("Second Interface")
                    second_window.geometry("400x200")


                    second_window.mainloop()
                
                win3.mainloop()
                
user1 = User_login()
user1.page_user()