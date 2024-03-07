from tkinter import *
import customtkinter
import customtkinter as ctk
from tkinter import filedialog
from PIL import ImageTk, Image
import tkinter
import tkinter as tk
import os
import csv
import random
from tkinter import ttk



win1 = Tk()
img1=ImageTk.PhotoImage(Image.open("images/pattern.png"))

def but_quantité():
    win_qunt = Toplevel()
    win_qunt.geometry("950x370+200+280")


    main_frame = Frame(win_qunt)
    main_frame.pack(fill=BOTH,expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame =Frame(my_canvas)

    my_canvas.create_window((0,0), window=second_frame , anchor="nw")


    image=ImageTk.PhotoImage(Image.open("images/bg_book.jpg"))
    lb=customtkinter.CTkLabel(second_frame,image=image)
    lb.pack()

    frame1=customtkinter.CTkFrame(lb, width=130, height=175, corner_radius=15)
    frame1.place(x= 20, y= 20)
    img_old = Image.open("img_book/adv1.jfif")
    width,height = img_old.size
    width_new =int(120)
    height_new =int(130)
    img_resize = img_old.resize((width_new,height_new))
    my_img = ImageTk.PhotoImage(img_resize)
    my0 = Label(frame1, image= my_img)
    my0.pack()
    my0.place(y=5, x=3)
    write0 = customtkinter.CTkLabel(frame1, text="Quantité : ", font=('Century Gothic',15, 'bold'))
    write0.place(x=20, y=140)
    writ0 = customtkinter.CTkLabel(frame1, text="20", font=('Century Gothic',15, 'bold'))
    writ0.place(x=103, y=140)

    frame2=customtkinter.CTkFrame(lb, width=130, height=175, corner_radius=15)
    frame2.place(x= 195, y= 20)
    img_old1 = Image.open("img_book/Adv2.jfif")
    width,height = img_old1.size
    width_new1 =int(120)
    height_new1 =int(130)
    img_resize1 = img_old1.resize((width_new1,height_new1))
    my_img1 = ImageTk.PhotoImage(img_resize1)
    my1 = Label(frame2, image= my_img1)
    my1.pack()
    my1.place(y=5, x=5)
    write1 = customtkinter.CTkLabel(frame2, text="Quantié : ", font=('Century Gothic',15, 'bold'))
    write1.place(x=20, y=140)
    write2 = customtkinter.CTkLabel(frame2, text="15", font=('Century Gothic',15, 'bold'))
    write2.place(x=103, y=140)

    frame3=customtkinter.CTkFrame(lb, width=130, height=175, corner_radius=15)
    frame3.place(x= 370, y= 20)
    img_old2 = Image.open("img_book/Adv3.jfif")
    width,height = img_old2.size
    width_new2 =int(120)
    height_new2 =int(130)
    img_resize2 = img_old2.resize((width_new2,height_new2))
    my_img2 = ImageTk.PhotoImage(img_resize2)
    my2 = Label(frame3, image= my_img2)
    my2.pack()
    my2.place(y=5, x=5)
    write2 = customtkinter.CTkLabel(frame3, text="Quantité : ", font=('Century Gothic',15, 'bold'))
    write2.place(x=20, y=140)
    write3 = customtkinter.CTkLabel(frame3, text="14", font=('Century Gothic',15, 'bold'))
    write3.place(x=103, y=140)

    frame4=customtkinter.CTkFrame(lb, width=130, height=175, corner_radius=15)
    frame4.place(x= 545, y= 20)
    img_old3 = Image.open("img_book/img_6.jpg")
    width,height = img_old3.size
    width_new3 =int(120)
    height_new3 =int(130)
    img_resize3 = img_old3.resize((width_new3,height_new3))
    my_img3 = ImageTk.PhotoImage(img_resize3)
    my3 = Label(frame4, image= my_img3)
    my3.pack()
    my3.place(y=5, x=5)
    write3 = customtkinter.CTkLabel(frame4, text="Quantité : ", font=('Century Gothic',15, 'bold'))
    write3.place(x=20, y=140)
    write4 = customtkinter.CTkLabel(frame4, text="8", font=('Century Gothic',15, 'bold'))
    write4.place(x=103, y=140)

    frame5=customtkinter.CTkFrame(lb, width=130, height=175, corner_radius=15)
    frame5.place(x= 720, y= 20)
    img_old4 = Image.open("img_book/Adv5.jfif")
    width,height = img_old4.size
    width_new4 =int(120)
    height_new4 =int(130)
    img_resize4 = img_old4.resize((width_new4,height_new4))
    my_img4 = ImageTk.PhotoImage(img_resize4)
    my4 = Label(frame5, image= my_img4)
    my4.pack()
    my4.place(y=5, x=5)
    write4 = customtkinter.CTkLabel(frame5, text="Quntité : ", font=('Century Gothic',15, 'bold'))
    write4.place(x=20, y=140)
    write5 = customtkinter.CTkLabel(frame5, text="5", font=('Century Gothic',15, 'bold'))
    write5.place(x=103, y=140)

    frame6=customtkinter.CTkFrame(lb, width=130, height=175, corner_radius=15)
    frame6.place(x= 20, y= 235)
    img_old5 = Image.open("img_book/adv6.jfif")
    width,height = img_old5.size
    width_new5 =int(120)
    height_new5 =int(130)
    img_resize5 = img_old5.resize((width_new5,height_new5))
    my_img5 = ImageTk.PhotoImage(img_resize5)
    my5 = Label(frame6, image= my_img5)
    my5.pack()
    my5.place(y=5, x=5)
    write5 = customtkinter.CTkLabel(frame6, text="Quantité : ", font=('Century Gothic',15, 'bold'))
    write5.place(x=20, y=140)
    write6 = customtkinter.CTkLabel(frame6, text="20", font=('Century Gothic',15, 'bold'))
    write6.place(x=103, y=140)

    frame7=customtkinter.CTkFrame(lb, width=130, height=175, corner_radius=15)
    frame7.place(x= 195, y= 235)
    img_old7 = Image.open("img_book/adv7.jfif")
    width,height = img_old7.size
    width_new7 =int(120)
    height_new7 =int(130)
    img_resize7 = img_old7.resize((width_new7,height_new7))
    my_img7 = ImageTk.PhotoImage(img_resize7)
    my7 = Label(frame7, image= my_img7)
    my7.pack()
    my7.place(y=5, x=5)
    write7 = customtkinter.CTkLabel(frame7, text="Qunatité : ", font=('Century Gothic',15, 'bold'))
    write7.place(x=20, y=140)
    write7 = customtkinter.CTkLabel(frame7, text="3", font=('Century Gothic',15, 'bold'))
    write7.place(x=103, y=140)

    frame8=customtkinter.CTkFrame(lb, width=130, height=175, corner_radius=15)
    frame8.place(x= 370, y= 235)
    img_old8 = Image.open("img_book/adv8.jfif")
    width,height = img_old8.size
    width_new8 =int(120)
    height_new8 =int(130)
    img_resize8 = img_old8.resize((width_new8,height_new8))
    my_img8 = ImageTk.PhotoImage(img_resize8)
    my8 = Label(frame8, image= my_img8)
    my8.pack()
    my8.place(y=5, x=5)
    write8 = customtkinter.CTkLabel(frame8, text="Quantité : ", font=('Century Gothic',15, 'bold'))
    write8.place(x=20, y=140)
    write8 = customtkinter.CTkLabel(frame8, text="40", font=('Century Gothic',15, 'bold'))
    write8.place(x=103, y=140)

    frame9=customtkinter.CTkFrame(lb, width=130, height=175, corner_radius=15)
    frame9.place(x= 545, y= 235)
    img_old9 = Image.open("img_book/c1.jfif")
    width,height = img_old9.size
    width_new9 =int(120)
    height_new9 =int(130)
    img_resize9 = img_old9.resize((width_new9,height_new9))
    my_img9 = ImageTk.PhotoImage(img_resize9)
    my9 = Label(frame9, image= my_img9)
    my9.pack()
    my9.place(y=5, x=5)
    write9 = customtkinter.CTkLabel(frame9, text="Quantité : ", font=('Century Gothic',15, 'bold'))
    write9.place(x=20, y=140)
    write9 = customtkinter.CTkLabel(frame9, text="7", font=('Century Gothic',15, 'bold'))
    write9.place(x=103, y=140)

    frame10=customtkinter.CTkFrame(lb, width=130, height=175, corner_radius=15)
    frame10.place(x= 720, y= 235)
    img_old10 = Image.open("img_book/c2.jfif")
    width,height = img_old10.size
    width_new10 =int(120)
    height_new10 =int(130)
    img_resize10 = img_old10.resize((width_new10,height_new10))
    my_img10 = ImageTk.PhotoImage(img_resize10)
    my10 = Label(frame10, image= my_img10)
    my10.pack()
    my10.place(y=5, x=5)
    write10 = customtkinter.CTkLabel(frame10, text="Quantité : ", font=('Century Gothic',15, 'bold'))
    write10.place(x=20, y=140)
    write10 = customtkinter.CTkLabel(frame10, text="20", font=('Century Gothic',15, 'bold'))
    write10.place(x=103, y=140)

    frame11=customtkinter.CTkFrame(lb, width=130, height=175, corner_radius=15)
    frame11.place(x= 20, y= 450)
    img_old11 = Image.open("img_book/c3.jfif")
    width,height = img_old11.size
    width_new11 =int(120)
    height_new11 =int(130)
    img_resize11 = img_old11.resize((width_new11,height_new11))
    my_img11 = ImageTk.PhotoImage(img_resize11)
    my11 = Label(frame11, image= my_img11)
    my11.pack()
    my11.place(y=5, x=5)
    write11 = customtkinter.CTkLabel(frame11, text="Quantité : ", font=('Century Gothic',15, 'bold'))
    write11.place(x=20, y=140)
    write11 = customtkinter.CTkLabel(frame11, text="20", font=('Century Gothic',15, 'bold'))
    write11.place(x=103, y=140)

    frame12=customtkinter.CTkFrame(lb, width=130, height=175, corner_radius=15)
    frame12.place(x= 195, y= 450)
    img_old12 = Image.open("img_book/c4.jfif")
    width,height = img_old12.size
    width_new12 =int(120)
    height_new12 =int(130)
    img_resize12 = img_old12.resize((width_new12,height_new12))
    my_img12 = ImageTk.PhotoImage(img_resize12)
    my12 = Label(frame12, image= my_img12)
    my12.pack()
    my12.place(y=5, x=5)
    write12 = customtkinter.CTkLabel(frame12, text="Quantité : ", font=('Century Gothic',15, 'bold'))
    write12.place(x=20, y=140)
    write12 = customtkinter.CTkLabel(frame12, text="12", font=('Century Gothic',15, 'bold'))
    write12.place(x=103, y=140)

    frame13=customtkinter.CTkFrame(lb, width=130, height=175, corner_radius=15)
    frame13.place(x= 370, y= 450)
    img_old13 = Image.open("img_book/c5.jfif")
    width,height = img_old13.size
    width_new13 =int(120)
    height_new13 =int(130)
    img_resize13 = img_old13.resize((width_new13,height_new13))
    my_img13 = ImageTk.PhotoImage(img_resize13)
    my13 = Label(frame13, image= my_img13)
    my13.pack()
    my13.place(y=5, x=5)
    write13 = customtkinter.CTkLabel(frame13, text="Quantité : ", font=('Century Gothic',15, 'bold'))
    write13.place(x=20, y=140)
    write13 = customtkinter.CTkLabel(frame13, text="15", font=('Century Gothic',15, 'bold'))
    write13.place(x=103, y=140)

    frame14=customtkinter.CTkFrame(lb, width=130, height=175, corner_radius=15)
    frame14.place(x= 545, y= 450)
    img_old14 = Image.open("img_book/img_2.jpg")
    width,height = img_old14.size
    width_new14 =int(120)
    height_new14 =int(130)
    img_resize14 = img_old14.resize((width_new14,height_new14))
    my_img14 = ImageTk.PhotoImage(img_resize14)
    my14 = Label(frame14, image= my_img14)
    my14.pack()
    my14.place(y=5, x=5)
    write14 = customtkinter.CTkLabel(frame14, text="Quantité : ", font=('Century Gothic',15, 'bold'))
    write14.place(x=20, y=140)
    write14 = customtkinter.CTkLabel(frame14, text="9", font=('Century Gothic',15, 'bold'))
    write14.place(x=103, y=140)

    frame15=customtkinter.CTkFrame(lb, width=130, height=175, corner_radius=15)
    frame15.place(x= 720, y= 450)
    img_old15 = Image.open("img_book/c7.jfif")
    width,height = img_old15.size
    width_new15 =int(120)
    height_new15 =int(130)
    img_resize15 = img_old15.resize((width_new15,height_new15))
    my_img15 = ImageTk.PhotoImage(img_resize15)
    my15 = Label(frame15, image= my_img15)
    my15.pack()
    my15.place(y=5, x=5)
    write15 = customtkinter.CTkLabel(frame15, text="Quantité : ", font=('Century Gothic',15, 'bold'))
    write15.place(x=20, y=140)
    write15 = customtkinter.CTkLabel(frame15, text="22", font=('Century Gothic',15, 'bold'))
    write15.place(x=103, y=140)

    frame16=customtkinter.CTkFrame(lb, width=130, height=175, corner_radius=15)
    frame16.place(x= 20, y= 665)
    img_old16 = Image.open("img_book/c8.jfif")
    width,height = img_old16.size
    width_new16 =int(120)
    height_new16 =int(130)
    img_resize16 = img_old16.resize((width_new16,height_new16))
    my_img16 = ImageTk.PhotoImage(img_resize16)
    my16 = Label(frame16, image= my_img16)
    my16.pack()
    my16.place(y=5, x=5)
    write16 = customtkinter.CTkLabel(frame16, text="Quantité : ", font=('Century Gothic',15, 'bold'))
    write16.place(x=20, y=140)
    write16 = customtkinter.CTkLabel(frame16, text="30", font=('Century Gothic',15, 'bold'))
    write16.place(x=103, y=140)

    frame17=customtkinter.CTkFrame(lb, width=130, height=175, corner_radius=15)
    frame17.place(x= 195, y= 665)
    img_old17 = Image.open("img_book/img_2.jpg")
    width,height = img_old17.size
    width_new17 =int(120)
    height_new17 =int(130)
    img_resize17 = img_old17.resize((width_new17,height_new17))
    my_img17 = ImageTk.PhotoImage(img_resize17)
    my17 = Label(frame17, image= my_img17)
    my17.pack()
    my17.place(y=5, x=5)
    write17 = customtkinter.CTkLabel(frame17, text="Quantité : ", font=('Century Gothic',15, 'bold'))
    write17.place(x=20, y=140)
    write17 = customtkinter.CTkLabel(frame17, text="15", font=('Century Gothic',15, 'bold'))
    write17.place(x=103, y=140)

    frame18=customtkinter.CTkFrame(lb, width=130, height=175, corner_radius=15)
    frame18.place(x= 370, y= 665)
    img_old18 = Image.open("img_book/img_3.jpeg")
    width,height = img_old18.size
    width_new18 =int(120)
    height_new18 =int(130)
    img_resize18 = img_old18.resize((width_new18,height_new18))
    my_img18 = ImageTk.PhotoImage(img_resize18)
    my18 = Label(frame18, image= my_img18)
    my18.pack()
    my18.place(y=5, x=5)
    write18 = customtkinter.CTkLabel(frame18, text="Quantité : ", font=('Century Gothic',15, 'bold'))
    write18.place(x=20, y=140)
    write18 = customtkinter.CTkLabel(frame18, text="12", font=('Century Gothic',15, 'bold'))
    write18.place(x=103, y=140)

    frame19=customtkinter.CTkFrame(lb, width=130, height=175, corner_radius=15)
    frame19.place(x= 545, y= 665)
    img_old19 = Image.open("img_book/r8.jfif")
    width,height = img_old19.size
    width_new19 =int(120)
    height_new19 =int(130)
    img_resize19 = img_old19.resize((width_new19,height_new19))
    my_img19 = ImageTk.PhotoImage(img_resize19)
    my19 = Label(frame19, image= my_img19)
    my19.pack()
    my19.place(y=5, x=5)
    write19 = customtkinter.CTkLabel(frame19, text="Quantité : ", font=('Century Gothic',15, 'bold'))
    write19.place(x=20, y=140)
    write19 = customtkinter.CTkLabel(frame19, text="32", font=('Century Gothic',15, 'bold'))
    write19.place(x=103, y=140)

    frame20=customtkinter.CTkFrame(lb, width=130, height=175, corner_radius=15)
    frame20.place(x= 720, y= 665)
    img_old20 = Image.open("img_book/th8.jfif")
    width,height = img_old20.size
    width_new20 =int(120)
    height_new20 =int(130)
    img_resize20 = img_old20.resize((width_new20,height_new20))
    my_img20 = ImageTk.PhotoImage(img_resize20)
    my20 = Label(frame20, image= my_img20)
    my20.pack()
    my20.place(y=5, x=5)
    write20 = customtkinter.CTkLabel(frame20, text="Quantité : ", font=('Century Gothic',15, 'bold'))
    write20.place(x=20, y=140)
    write20 = customtkinter.CTkLabel(frame20, text="42", font=('Century Gothic',15, 'bold'))
    write20.place(x=103, y=140)

    win_qunt.mainloop() 
 
                   
l1=customtkinter.CTkLabel(win1,image=img1)
l1.pack()

frame=customtkinter.CTkFrame(master = l1, width=950, height=600, corner_radius=6)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

IMAGE_WIDTH = 100
IMAGE_HEIGHT = 100
IMAGE_PATH = 'images/profile.png'

your_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(IMAGE_PATH)), size=(IMAGE_WIDTH , IMAGE_HEIGHT))
label = customtkinter.CTkLabel(frame, image=your_image, text='')
label.place(x=50,y=25)

with open('document.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  
    email = next(reader)[0]
    name = email.split('@')[0]  

    hello_label = tk.Label(frame, text=f"Hello {name}", font=('Times New Roman',17,'bold'))
    hello_label.pack()
    hello_label.place(x=170, y=45)

    label_id = tk.Label(frame, text="ID : ", font=('Times New Roman',10,'bold'))
    label_id.pack()
    label_id.place(x=180, y=85)

    def verify_information():
        unique_id = ''.join(random.choices('0123456789', k=10))
        label_id.config(text="ID: " + unique_id)    


def add_book():

    add_book_window = Toplevel()
    add_book_window.geometry("350x450")
    add_book_window.title("Add a book to store")

    Title = ctk.CTkLabel(add_book_window , text="Add a book to store", fg_color="blue", font=('Helvetica', 30), height=20, width=200)
    Title.pack(pady=10)

    cover_label = ctk.CTkLabel(add_book_window, font=('Helvetica', 20), height=20, width=200,text="Cover of the book:")
    cover_label.pack(pady=10)
    cover_button =  ctk.CTkButton(add_book_window,font=('Helvetica', 20), height=20, width=200, text="Upload Image", command=filedialog.askopenfilename)
    cover_button.pack(pady=10)

    title_label = ctk.CTkLabel(add_book_window,font=('Helvetica', 20), height=20, width=200, text="Title of the book:")
    title_label.pack(pady=10)
    title_entry = ctk.CTkEntry(add_book_window)
    title_entry.pack(pady=10)

    price_label = ctk.CTkLabel(add_book_window,font=('Helvetica', 20), height=20, width=200, text="Price:")
    price_label.pack(pady=10)
    price_entry = ctk.CTkEntry(add_book_window)
    price_entry.pack(pady=10)
    
    confirm_button = ctk.CTkButton(add_book_window,font=('Helvetica', 20), height=20, width=200, text="Confirm")
    confirm_button.pack(pady=20)

def modify_info():
    
    modify_info_window = Toplevel()
    modify_info_window.geometry("350x450")
    modify_info_window.title("Modify info")

    Title= ctk.CTkLabel(modify_info_window, text="Modify info", fg_color="light blue",text_color="black", font=('Helvetica', 30), height=20, width=200)
    Title.pack(pady=10) 

    cover_label = ctk.CTkLabel(modify_info_window,font=('Helvetica', 20), height=20, width=200, text="Change Cover:")
    cover_label.pack(pady=10)    
    cover_button = ctk.CTkButton(modify_info_window, font=('Helvetica', 20), height=20, width=200, text="Upload Image", command=filedialog.askopenfilename)
    cover_button.pack(pady=10)

    title_label = ctk.CTkLabel(modify_info_window,font=('Helvetica', 20), height=20, width=200, text="Change Title ;")
    title_label.pack(pady=10)   
    title_entry = ctk.CTkEntry(modify_info_window, height=20, width=200)
    title_entry.pack(pady=10)

    price_label = ctk.CTkLabel(modify_info_window,font=('Helvetica', 20), height=20, width=200, text="change Price:")
    price_label.pack(pady=10)    
    price_entry = ctk.CTkEntry(modify_info_window, height=20, width=200)
    price_entry.pack(pady=10)

    confirm_button = ctk.CTkButton(modify_info_window, text="Confirm", font=('Helvetica', 20), height=60, width=200)
    confirm_button.pack(pady=25)

    

    
def delete_use():
    delete_book_window =  Toplevel()
    delete_book_window.geometry("350x450")
    delete_book_window.title("Delete Book")

    Title= ctk.CTkLabel(delete_book_window, text="Delete Book", fg_color="red",text_color="white", font=('Helvetica', 30), height=2, width=20)
    Title.pack()
    
    cover_label = ctk.CTkLabel(delete_book_window,font=('Helvetica', 20), height=20, width=200, text="Account :")
    cover_label.pack(pady=25)
    
    checkbox_1 = customtkinter.CTkCheckBox(delete_book_window, text="ahlak@gmail.com")
    checkbox_1.pack(pady=10)
    checkbox_2 = customtkinter.CTkCheckBox(delete_book_window, text="jilaali@.gmail.com")
    checkbox_2.pack(pady=10)
    checkbox_3 = customtkinter.CTkCheckBox(delete_book_window, text="dfdfsrf@.gmail.com")
    checkbox_3.pack(pady=10)
    checkbox_4 = customtkinter.CTkCheckBox(delete_book_window, text="sqfscv@.gmail.com")
    checkbox_4.pack(pady=10)
    checkbox_5 = customtkinter.CTkCheckBox(delete_book_window, text="dfcsfcfs@.gmail.com")
    checkbox_5.pack(pady=10)
    
    confirm_button = ctk.CTkButton(delete_book_window, text="Confirm", font=('Helvetica', 20), height=60, width=200)
    confirm_button.pack(pady=25)

Add_b = customtkinter.CTkButton(win1, text="Add book ", font=('Avantstile Regular', 20),text_color="black", fg_color="blue", command=add_book)

Add_b.place(x=385, y=355) 


quantité = customtkinter.CTkButton(frame, text="Quantité ", font=('Times New Roman',20),text_color="black",fg_color="green",command=but_quantité)
quantité.place(x=100, y=455) 

mod = customtkinter.CTkButton(win1, text="Modify book ",font=('Avantstile Regular', 20),text_color="black", fg_color="light green", command=modify_info)
mod.place(x=800, y=355) 

delet = customtkinter.CTkButton(win1, text="Delet user ",font=('Avantstile Regular', 20),text_color="black",fg_color="red", command=delete_use)
delet.place(x=800, y=555)                 
verify_information()

Add_b.configure(width=200, height=50)
quantité.configure(width=200, height=50)
mod.configure(width=200, height=50)
delet.configure(width=200, height=50)

win1.state("zoomed")
win1.mainloop()