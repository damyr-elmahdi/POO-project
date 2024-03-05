from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from tkinter import Tk



win_book1 = Tk()

img2=ImageTk.PhotoImage(Image.open("images/pattern.png"))
l1=customtkinter.CTkLabel(win_book1,image=img2)
l1.pack()

frame=customtkinter.CTkFrame(master = win_book1, width=430, height=640, corner_radius=6)
frame.place(x = 70,y=40)

img_book1 = ImageTk.PhotoImage(Image.open("new_images/img-1.jpg"))
label1 = Label(frame,image = img_book1, width=310, height=290)
label1.pack()
label1.place(x=60, y=25)

desc_bk1=customtkinter.CTkLabel(frame, text="Description : ",font=('Times New Roman',25,'bold'))
desc_bk1.place(x=25, y=335)

desc_bk1=customtkinter.CTkLabel(frame, text="Darkest before the dawn is a gripping tale \nof resilience, hope, and redemption in the face \nof adversity. Written by an acclaimed author, \nit follows the journey of several interconnected characters as \nthey navigate through life's trials and tribulations.\nSet against the backdrop of a small, struggling \ntown, the narrative delves into the lives of \nits inhabitants, each grappling with \ntheir own personal demons. \nFrom a troubled teenager battling addiction to a \ndisillusioned war veteran haunted by his past, \nthe characters' stories intertwine in unexpected ways, \nultimately converging towards a powerful climax.",font=('Times New Roman',15,'bold'))
desc_bk1.place(x=25, y=375)

frame2_bk1=customtkinter.CTkFrame(master = win_book1, width=790, height=440, corner_radius=6)
frame2_bk1.place(x = 530,y=40)

head_bk1=customtkinter.CTkLabel(frame2_bk1, text="Enter your information",font=('Times New Roman',35,'bold'))
head_bk1.place(x=230, y=15)
name_bk1= customtkinter.CTkEntry(frame2_bk1, width=270, height=35, placeholder_text='Enter your username ')
name_bk1.place(x=95, y=95)
prenom_bk1= customtkinter.CTkEntry(frame2_bk1, width=270, height=35, placeholder_text='Enter your lastname')
prenom_bk1.place(x=420, y=95)
phone_bk1= customtkinter.CTkEntry(frame2_bk1, width=270, height=35, placeholder_text='Enter your phone')
phone_bk1.place(x=95, y=155)
city_bk1= customtkinter.CTkEntry(frame2_bk1, width=270, height=35, placeholder_text='Enter your city')
city_bk1.place(x=420, y=155)
email_bk1= customtkinter.CTkEntry(frame2_bk1, width=270, height=35, placeholder_text='Enter your email')
email_bk1.place(x=95, y=220)
but_bk1 = customtkinter.CTkButton(frame2_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
but_bk1.place(x=305, y=290)
        
win_book1.state("zoomed")
win_book1.mainloop()
        

