from tkinter import *
import customtkinter
import customtkinter as ctk
from tkinter import filedialog
from PIL import ImageTk, Image
import tkinter
import customtkinter as ctk
from tkinter import Toplevel
import tkinter as tk
import os
import csv
import random
from tkinter import ttk



win1 = Tk()
win1.title("HAVEN BOOK ")
win1.iconbitmap('images/icon.ico')
img1=ImageTk.PhotoImage(Image.open("images/background.png"))

quantité={
            "book1": 11,
            "book2": 12,
            "book3": 34,
            "book4": 18,
            "book5": 17,
            "book6": 16,
            "book7": 53,
            "book8": 55,
            "book9": 14,
            "book10": 12,
            "book11": 31,
            "book12": 20,
            "book13": 51,
            "book14": 72,
            "book15": 16,
            "book16": 17,
            "book17": 10,
            "book18": 45,
            "book19": 33,
            "book20": 54,
            
}

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
    writ0 = customtkinter.CTkLabel(frame1,  text=f"{quantité['book1']}", font=('Century Gothic',15, 'bold'))
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
    write2 = customtkinter.CTkLabel(frame2, text=f"{quantité['book2']}", font=('Century Gothic',15, 'bold'))
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
    write3 = customtkinter.CTkLabel(frame3, text=f"{quantité['book3']}", font=('Century Gothic',15, 'bold'))
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
    write4 = customtkinter.CTkLabel(frame4, text=f"{quantité['book4']}", font=('Century Gothic',15, 'bold'))
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
    write5 = customtkinter.CTkLabel(frame5,text=f"{quantité['book5']}", font=('Century Gothic',15, 'bold'))
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
    write6 = customtkinter.CTkLabel(frame6, text=f"{quantité['book6']}", font=('Century Gothic',15, 'bold'))
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
    write7 = customtkinter.CTkLabel(frame7, text=f"{quantité['book7']}", font=('Century Gothic',15, 'bold'))
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
    write8 = customtkinter.CTkLabel(frame8,text=f"{quantité['book8']}", font=('Century Gothic',15, 'bold'))
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
    write9 = customtkinter.CTkLabel(frame9,text=f"{quantité['book9']}", font=('Century Gothic',15, 'bold'))
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
    write10 = customtkinter.CTkLabel(frame10, text=f"{quantité['book10']}", font=('Century Gothic',15, 'bold'))
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
    write11 = customtkinter.CTkLabel(frame11, text=f"{quantité['book11']}", font=('Century Gothic',15, 'bold'))
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
    write12 = customtkinter.CTkLabel(frame12,text=f"{quantité['book12']}", font=('Century Gothic',15, 'bold'))
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
    write13 = customtkinter.CTkLabel(frame13, text=f"{quantité['book13']}", font=('Century Gothic',15, 'bold'))
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
    write14 = customtkinter.CTkLabel(frame14,text=f"{quantité['book14']}", font=('Century Gothic',15, 'bold'))
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
    write15 = customtkinter.CTkLabel(frame15, text=f"{quantité['book15']}", font=('Century Gothic',15, 'bold'))
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
    write16 = customtkinter.CTkLabel(frame16, text=f"{quantité['book16']}", font=('Century Gothic',15, 'bold'))
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
    write17 = customtkinter.CTkLabel(frame17, text=f"{quantité['book17']}", font=('Century Gothic',15, 'bold'))
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
    write18 = customtkinter.CTkLabel(frame18, text=f"{quantité['book18']}", font=('Century Gothic',15, 'bold'))
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
    write19 = customtkinter.CTkLabel(frame19, text=f"{quantité['book19']}", font=('Century Gothic',15, 'bold'))
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
    write20 = customtkinter.CTkLabel(frame20, text=f"{quantité['book20']}", font=('Century Gothic',15, 'bold'))
    write20.place(x=103, y=140)

    win_qunt.mainloop() 
 

                   
l1=customtkinter.CTkLabel(win1,image=img1)
l1.pack()

frame=customtkinter.CTkFrame(master = l1, width=950, height=600, corner_radius=6)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

imgage=ImageTk.PhotoImage(Image.open("images/Haven.png"))
lb=customtkinter.CTkLabel(frame,image=imgage)
lb.pack()

IMAGE_WIDTH = 100
IMAGE_HEIGHT = 100
IMAGE_PATH = 'images/profile.png'

your_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(IMAGE_PATH)), size=(IMAGE_WIDTH , IMAGE_HEIGHT))
label = customtkinter.CTkLabel(frame, image=your_image, text='')
label.place(x=50,y=25)

with open('user.csv', 'r') as file:
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

def add():
    def upload_image():
        filepath = filedialog.askopenfilename()
        if filepath:
            cover_button.file_path = filepath 

    def confirm():
        image_path = getattr(cover_button, 'file_path', None)
        price = price_entry.get()
        if image_path and price:
           
            x, y = calculate_coordinates('books.csv')
            with open('books.csv', mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([image_path, price, x, y])

    def calculate_coordinates(csv_filename):
        try:
            with open(csv_filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                entries = list(reader)
                
                num_rows = len(entries) - 1  
                x = (num_rows % 5) * 230 + 20  
                y = (num_rows // 5) * 230 + 100
                return x, y
        except FileNotFoundError:
            
            return 20, 100
        
        with open('books.csv', mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([image_path, price])

    add_book_window = Tk()
    add_book_window.geometry("350x450")
    add_book_window.title("Add a book to store")

    Title = ctk.CTkLabel(add_book_window, text="Add a book to store", fg_color="blue", font=('Helvetica', 30), height=20, width=200)
    Title.pack(pady=10)

    cover_label = ctk.CTkLabel(add_book_window, font=('Helvetica', 20), height=20, width=200, text="Cover of the book:")
    cover_label.pack(pady=10)

    cover_button = ctk.CTkButton(add_book_window, font=('Helvetica', 20), height=20, width=200, text="Upload Image", command=upload_image)
    cover_button.pack(pady=10)

    price_label = ctk.CTkLabel(add_book_window, font=('Helvetica', 20), height=20, width=200, text="Price:")
    price_label.pack(pady=10)

    price_entry = ctk.CTkEntry(add_book_window)
    price_entry.pack(pady=10)

    confirm_button = ctk.CTkButton(add_book_window, font=('Helvetica', 20), height=20, width=200, text="Confirm", command=confirm)
    confirm_button.pack(pady=20)

    add_book_window.mainloop()


Books = {
    "book1": 11, "book2": 12, "book3": 16, "book4": 18, "book5": 17,
    "book6": 16, "book7": 16, "book8": 15, "book9": 14, "book10": 12,
    "book11": 31, "book12": 14, "book13": 51, "book14": 72, "book15": 16,
    "book16": 17, "book17": 10, "book18": 11,
}


booksdesc = {
"book1": "Darkest before the dawn is a gripping tale \nof resilience, hope, and redemption in the face \nof adversity. Written by an acclaimed author, \nit follows the journey of several interconnected characters as \nthey navigate through life's trials and tribulations.\nSet against the backdrop of a small, struggling \ntown, the narrative delves into the lives of \nits inhabitants, each grappling with \ntheir own personal demons. \nFrom a troubled teenager battling addiction to a \ndisillusioned war veteran haunted by his past, \nthe characters' stories intertwine in unexpected ways, \nultimately converging towards a powerful climax.",
"book2": "Darkest before the dawn is a gripping tale \nof resilience, hope, and redemption in the face \nof adversity. Written by an acclaimed author, \nit follows the journey of several interconnected characters as \nthey navigate through life's trials and tribulations.\nSet against the backdrop of a small, struggling \ntown, the narrative delves into the lives of \nits inhabitants, each grappling with \ntheir own personal demons. \nFrom a troubled teenager battling addiction to a \ndisillusioned war veteran haunted by his past, \nthe characters' stories intertwine in unexpected ways, \nultimately converging towards a powerful climax.",
"book3": "Magic of the Unicorn is a captivating \nfantasy novel that transports readers into \na world filled with wonder, adventure, \nand enchantment. Written by an imaginative \nauthor, it tells the tale of a young protagonist \nwho discovers a realm where unicorns, mystical \ncreatures of legend, exist.The story follows \nthe journey of a courageous protagonist, often \na child or teenager, who stumbles upon a \nhidden portal or magical artifact that \ngrants them access to the realm of unicorns. \nOnce there, they encounter breathtaking landscapes, \nancient forests, and shimmering meadows inhabited \nby these elusive creatures.",
"book4": "Summer Adventure Stories is a collection of \nexhilarating tales crafted to ignite the spirit \nof adventure in readers of all ages. \nWithin its pages, readers embark on thrilling \njourneys to distant lands, embark on daring quests, \nand experience the magic of summertime\n escapades. Each story in the collection offers \na unique adventure, from exploring hidden treasure \ntroves in tropical islands to embarking on epic \nhikes through rugged mountain ranges. \nThe characters range from intrepid \nexplorers to curious children, \neach facing challenges and overcoming \nobstacles with bravery and determination.",
"book5": "Dragon Run is an enthralling young adult fantasy \nnovel that takes readers on an epic journey \nthrough a world filled with dragons, \nmagic, and adventure. Written by an acclaimed author, \nit follows the thrilling quest of a young \nprotagonist who must navigate a perilous landscape \nto save their kingdom from an ancient evil.\n The story unfolds in a land where dragons \nonce roamed freely, but have since been hunted \nto near extinction. The protagonist, often a \ncourageous and resourceful youth, discovers \nthat they have a special connection to these mythical \ncreatures, which sets them on a path of \ndiscovery and destiny.",
"book6": "Abominable Snowman is a gripping adventure novel that \nexplores the legend of the mythical creature known as the \nYeti or the Abominable Snowman. Written by a renowned \nauthor, it follows a group of explorers and scientists as they \nembark on a daring expedition into the remote and \ntreacherous Himalayan mountains in search of the \nelusive creature. The story unfolds as \nthe expedition team faces the harsh and unforgiving \nconditions of the Himalayas, battling against extreme cold, \nrugged terrain, and the ever-present danger of avalanches \nand crevasses. As they delve deeper into the wilderness, \ntensions rise within the group as they grapple with their \nown fears and doubts, while also confronting the mysteries \nsurrounding the existence of the legendary creature.",
"book7": "The Chronicles of Narnia is a beloved fantasy \nseries written by C.S. Lewis that takes readers on \nan extraordinary journey through the magical \nland of Narnia. Comprising  seven books,the \nseries weaves together tales of \nadventure, courage, and redemption, \ncaptivating readers of all ages with its \nrichly imagined world and timeless themes. \nAt the heart of the series is the magical \nwardrobe, which serves as a portal \nto Narnia, a realm inhabited by talking \nanimals, mythical creatures, and powerful \nsorcery. Each book follows the adventures \nof different characters who discover Narnia \nand play pivotal roles in its history.",
"book8": "Underwater is a gripping contemporary novel \nthat delves into the complexities of \nhuman emotions and resilience in the face \nof adversity. Written by an acclaimed author, \nit follows the journey of a young protagonist \nas she navigates the aftermath of a traumatic \nevent and seeks to find healing and \nredemption. The story centers around \nthe protagonist, often a teenage girl or \nyoung woman, who finds herself struggling to \ncope with the aftermath of a devastating \nincident, such as a natural disaster, a personal loss, or a \ntraumatic experience. As she grapples with feelings of \nguilt, fear, and isolation, she embarks on a journey.",
"book9": "As If It Were a Movie is a thought-provoking \ncontemporary novel that delves into the complexities \nof identity, relationships, and the blurred lines between \nreality and fiction. Written by a talented \nauthor, it offers a unique narrative structure \nthat challenges traditional storytelling conventions. \nThe story follows the protagonist, often a \nyoung adult or teenager, who finds themselves grappling \nwith the challenges of growing up \nand navigating the complexities of modern \nlife. As they navigate relationships, school, and \nthe pursuit of their dreams, they also find themselves \ndrawn into a world of fantasy and imagination.",
"book10": "Takings is a gripping legal thriller that follows the \njourney of a determined attorney as she takes on a high\n-stakes case that could change the course of her career \nand impact the lives of countless individuals. \nSet in the heart of a bustling city, the novel explores \nthemes of justice, power, and the ethical dilemmas faced \nby those in the legal profession. The story centers around \nSarah Williams, a brilliant and ambitious young lawyer who \nfinds herself thrust into the spotlight when she is \nassigned to represent a group of homeowners facing \neminent domain proceedings. As a powerful corporation \nseeks to acquire their properties for a lucrative development \nproject, Sarah must navigate a web of legal challenges, \npolitical intrigue, and personal conflicts.",
"book11": "Solar Bones is a mesmerizing and thought-\nprovoking novel that unfolds as a single, \ncontinuous stream of consciousness. Written by \nacclaimed Irish author Mike McCormack, it offers \na unique and immersive reading experience that challenges \ntraditional narrative structures. The story centers \naround Marcus Conway, an engineer living in a small town \nin Ireland. As Marcus reflects on his life, memories, \nand experiences, the novel takes readers on a journey \nthrough his thoughts, emotions, and innermost reflections. \nFrom his childhood memories to his struggles with work, \nfamily, and mortality, Marcus's narrative offers a poignant \nand deeply personal exploration of the human condition.",
"book12": "Death Sentence is a gripping thriller that plunges \nreaders into a world of danger, intrigue, and moral \nambiguity. Written by a master of the genre, it follows \nthe pulse-pounding journey of a protagonist \nwho finds themselves caught \nin a deadly game of cat and mouse with a ruthless \nadversary. The story centers around John Smith, \nan ordinary man whose life is turned upside down \nwhen he receives a mysterious \npackage containing evidence of a crime he \ndidn't commit. As he delves deeper into the mystery, \nJohn discovers that he has become the target of a \npowerful and shadowy organization determined \nto silence him at any cost",
"book13": "Heart Few is a tender and poignant love story that \nunfolds against the backdrop of a quaint coastal town. \nWritten by an acclaimed romance author, it follows the \nintertwined lives of two individuals whose paths \nunexpectedly cross, leading to a transformative journey \nof love, healing, and self-discovery. The story centers \naround Emily, a spirited young woman who has always \nharbored dreams of adventure and exploration, and Jack, a \nreserved yet compassionate artist struggling to overcome \nhis own past traumas. When Emily returns to her hometown \nto care for her ailing grandmother, she never expects \nto meet Jack, whose quiet strength and artistic soul \ncaptivate her from the moment they meet.",
"book14": "The Dividing Line is a gripping psychological thriller \nthat delves into the darkest corners of the human \nmind and the blurred boundaries between truth and \ndeception. Written by a master storyteller, it weaves \na tale of suspense, intrigue, and moral ambiguity that \nkeeps readers on the edge of their seats until the very \nend. Set in a small town with its own secrets and \nscandals, the story follows the lives of several \ninterconnected characters whose fates become \nintertwined by a series of shocking events. \nAt the center of the narrative is a mysterious \ndividing line that separates the town into two distinct \nworlds, each with its own set of \nrules and expectations.",
"book15": "The Billion Dollar Spy is a riveting non-fiction \nnarrative that unveils the gripping true story of \nespionage during the Cold War era. \nAuthored by PulitzerPrize-nominated journalist \nDavid E. Hoffman, this meticulously researched \nbook sheds light on one of the most significant \nintelligence operations of the 20th century. \nSet against the backdrop \nof the Cold War tensions between the United \nStates and the Soviet Union, the book follows the clandestine \nactivities of Adolf Tolkachev, a Soviet engineer who \nbecomes a top spy for the CIA. Tolkachev, driven by \ndisillusionment with the oppressive Soviet regime, risks \nhis life to provide crucial intelligence to the \nAmerican intelligence agency.",
"book16": "The House on the Lake is a gripping mystery novel \nthat unfolds gainst the backdrop of a secluded and \npicturesque lakeside retreat. Written by a master \nof suspense, it weaves a tale of secrets, betrayal, \nand redemption that keeps readers guessing until \nthe very end. The story follows the protagonist, often \na troubled individual seeking solace and a fresh start, \nwho discovers an idyllic house nestled by the tranquil \nwaters of a remote lake. Drawn by the promise of peace and \nsolitude, they soon find themselves entangled in a web of \nmystery and intrigue as they uncover the dark \nsecrets hidden within the walls of the house.",
"book17": "Mount Majestic is a captivating adventure novel that \ntransports readers to a magical island filled with mystery, \ndanger, and discovery. Written by an imaginative author, \nit follows the thrilling journey of a young protagonist \nas they embark on a quest to unravel \nthe secrets of a legendary mountain. Set on the \nenchanting island of Mount Majestic, \nthe story centers around a spirited protagonist, \noften a courageous child or teenager, who dreams \nof adventure and exploration. When strange occurrences \nbegin to disrupt the peace of the island, \nthe protagonist sets out on a daring quest to uncover \nthe truth behind the mysterious events.",
"book18": "Joe Hill is a riveting psychological thriller that \nexplores the dark and twisted depths of the human psyche. \nWritten by an acclaimed author known for their mastery \nof suspense, this gripping novel follows \nthe tumultuous journey of Joe Hill, a seemingly ordinary \nman whose life takes a sinister turn when \nhe becomes entangled in a web of deception and \nbetrayal. \nSet against the backdrop of a small, close-knit \ncommunity, the story begins innocently \nenough, with Joe Hill leading a quiet and unassuming \nexistence. But when a series of shocking events unfolds, \nJoe finds himself thrust into a world of \ndanger and intrigue, where nothing is as it \nseems and trust is a luxury he can ill afford.",

}
    
def modify_info():
    modify_info_window = Toplevel()
    modify_info_window.geometry("350x600")
    modify_info_window.title("Modify info")

    Title = ctk.CTkLabel(modify_info_window, text="Modify info", fg_color="light blue", text_color="black", font=('Helvetica', 30), height=20, width=200)
    Title.pack(pady=10)

    book_label = ctk.CTkLabel(modify_info_window, text="Select Book:", font=('Helvetica', 20), height=20, width=200)
    book_label.pack(pady=10)

    book_combo = ctk.CTkComboBox(modify_info_window, values=list(Books.keys()), height=20, width=200)
    book_combo.pack(pady=10)

    price_label = ctk.CTkLabel(modify_info_window, font=('Helvetica', 20), height=20, width=200, text="Change Price:")
    price_label.pack(pady=10)
    
    price_entry = ctk.CTkEntry(modify_info_window, height=20, width=200)
    price_entry.pack(pady=10)
    
    book_combo = ctk.CTkComboBox(modify_info_window, values=list(booksdesc.keys()), height=20, width=200)
    book_combo.pack(pady=10)

    desc_text = Text(modify_info_window, height=10, width=40)
    desc_text.pack(pady=10)

    def update_desc():
        selected_book = book_combo.get()
        new_desc = desc_text.get("1.0", "end-1c")
        if selected_book in booksdesc:
            booksdesc[selected_book] = new_desc  

          
            with open('desc.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';') 
                writer.writerow(['book', 'description']) 
                for book, desc in booksdesc.items():
                    writer.writerow([book, desc])  

    def update_price():
      
        selected_book = book_combo.get()
        new_price = price_entry.get()
   
        if new_price.isdigit():
            
            books_data = []
            with open('book_pr.csv', mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == selected_book:
               
                        books_data.append([selected_book, new_price])
                    else:
                        books_data.append(row)
            
            
            with open('book_pr.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(books_data)

    confirm_button = ctk.CTkButton(modify_info_window, text="Confirm", font=('Helvetica', 20), height=60, width=200, command=lambda: [update_price(), update_desc()])
    confirm_button.pack(pady=25)



    
def delete_use():
    
    import delet_user
    
    

    

Add_b = customtkinter.CTkButton(win1, text="Add book ", font=('Avantstile Regular', 20),text_color="#EADCCE", corner_radius=30 ,bg_color="#634937", fg_color="#B68B73", command=add)

Add_b.place(x=385, y=355) 


quantité = customtkinter.CTkButton(frame, text="Quantité ", font=('Times New Roman',20),text_color="#EADCCE", corner_radius=30 ,bg_color="#634937",fg_color="#B68B73",command=but_quantité)
quantité.place(x=100, y=455) 

mod = customtkinter.CTkButton(win1, text="Modify book ",font=('Avantstile Regular', 20),text_color="#EADCCE", corner_radius=30 ,bg_color="#634937", fg_color="#B68B73", command=modify_info)
mod.place(x=800, y=355) 

delet = customtkinter.CTkButton(win1, text="Delet user ",font=('Avantstile Regular', 20),text_color="#EADCCE", corner_radius=30,bg_color="#634937",fg_color="#B68B73", command=delete_use)
delet.place(x=800, y=555)                 
verify_information()

Add_b.configure(width=200, height=50)
quantité.configure(width=200, height=50)
mod.configure(width=200, height=50)
delet.configure(width=200, height=50)

win1.state("zoomed")
win1.mainloop()
