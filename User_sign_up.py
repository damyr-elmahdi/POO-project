from tkinter import*
from tkinter import messagebox
from PIL import ImageTk, Image
import customtkinter
import tkinter
import csv
# from page_book import pagse_books


class Sign_up:
    def page_user_sign(self):
                    # win3.destroy()
                    win4 = Tk()
                    win4.title("Page_user_sign")
                    
                    # def check_save_to_csv1():
                    #     win4.destroy()
                    #     import page_book
                        
                    
                        
                    def back_user_sign():
                        win4.destroy()
                        # Page1().page1()
                        
                        
                    # check and save to csv for interface page_user-sign :  
                    def check_save_to_csv1():
                        
                    #     win4.destroy()
                    #     import page_book  
                    
                        
                        
                        Email = Email1.get().strip()
                        Password = Password1.get().strip()
                        Nam = Name.get().strip()
                        Prén = Prénom.get().strip()
                        
                        if Email and Password:
                            with open("document.csv", "a") as file:
                                writer = csv.writer(file)
                                writer.writerow([Email, Password])
                        
                        
                        if not Nam:
                            messagebox.showerror("Error", "Please!!! write your information.") 
                        elif not Prén:
                            messagebox.showerror("Error", "Please!!! write your information.")
                        elif not Email:
                            messagebox.showerror("Error", "Please!!! write your information.") 
                        elif not Password:
                            messagebox.showerror("Error", "Please!!! write your information.")
                        
                        if Nam and Prén and Email and Password:
                            win4.destroy()
                            import page_book  
                    
                        
                        # check in email "@" : 
                        # if not "@" in Email:
                        #     messagebox.showerror("Error", "Please!!! write email correct")
    
                        # Email = Email1.get()
                        # Password = Password1.get()   
                         
                                  
                    
                    
                    img2=ImageTk.PhotoImage(Image.open("images/img2.png"))
                    l1=customtkinter.CTkLabel(win4,image=img2)
                    l1.pack()
                    
                    frame=customtkinter.CTkFrame(master = l1, width=340, height=450, corner_radius=6)
                    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

                    button1 = customtkinter.CTkButton(frame, width=140, height=35, text="User", corner_radius=6, font=('Times New Roman',17,'bold'))
                    button1.place(x=15, y=20)

                    button2 = customtkinter.CTkButton(frame, width=140, height=35, text="Sign up", corner_radius=6, font=('Times New Roman',17,'bold'))
                    button2.place(x=180, y=20)

                    l2=customtkinter.CTkLabel(frame, text="Entrer votre information",font=('Times New Roman',25,'bold'))
                    l2.place(x=40, y=90)

                    Name= customtkinter.CTkEntry(frame, width=150, height=35, placeholder_text='Entrer votre name')
                    Name.place(x=10, y=150)

                    Prénom=customtkinter.CTkEntry(frame, width=150, height=35, placeholder_text='Entrer votre prénom')
                    Prénom.place(x=175, y=150)
                    
                    Email1=customtkinter.CTkEntry(frame, width=230, height=35, placeholder_text='Entrer votre email')
                    Email1.place(x=45, y=200)
                    
                    Password1=customtkinter.CTkEntry(frame, width=230, height=35, placeholder_text='Entrer votre password', show="*")
                    Password1.place(x=45, y=250)
                    
                    entry2=customtkinter.CTkLabel(frame, text = "Forget password", font =('Century Gothic', 12))
                    entry2.place(x=170, y=285)

                    button3 = customtkinter.CTkButton(frame, width=220, height=35, text="Entrer", corner_radius=6, font=('Times New Roman',17,'bold'), command = check_save_to_csv1)
                    button3.place(x=55, y=320)
                    
                    btn_login = customtkinter.CTkButton(frame, width=140, height=35, text="Login", corner_radius=6,fg_color="#db3e00", hover_color="#bc6202", font=('Times New Roman',17,'bold'))
                    btn_login.place(x=15, y=370)

                    button2 = customtkinter.CTkButton(frame, width=140, height=35, text="Sing up", corner_radius=6, fg_color="#db3e00", hover_color="#bc6202", font=('Times New Roman',17,'bold'))
                    button2.place(x=180, y=370)
                    
                    but_back = customtkinter.CTkButton(frame,width=85, height=35, text="Back", corner_radius=6, font=('Times New Roman',17,'bold'), command= back_user_sign)
                    but_back.place(x=20, y=410)
                    
                    win4.mainloop()
                    
user1 = Sign_up()
user1.page_user_sign()




