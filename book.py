from tkinter import *
from PIL import ImageTk, Image
import customtkinter
import tkinter

class Books():
#*************** book 1 **************
    def book1(self):
        def card():
            frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
            frame3_bk1.place(x = 530,y=490)
            
            head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter your card : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=50, y=30)
            
            num_bk1= customtkinter.CTkEntry(frame3_bk1, width=210, height=35, placeholder_text='Enter card number')
            num_bk1.place(x=255, y=25)
            
            date_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='mm/yy')
            date_bk1.place(x=515, y=25)
            
            cod_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter security card')
            cod_bk1.place(x=255, y=75)
            
            adress_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter your adress')
            adress_bk1.place(x=515, y=75)
            
            buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
            buy_bk1.place(x= 355, y=140)
        
        def paypal():
            frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
            frame3_bk1.place(x = 530,y=490)
            
            head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter email from paypal : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=50, y=45)
            
            email_pay_bk1= customtkinter.CTkEntry(frame3_bk1, width=290, height=35, placeholder_text='Enter your email')
            email_pay_bk1.place(x=320, y=45)
            
            buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=175, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
            buy_bk1.place(x= 315, y=115)
        
        def Cntinue():
            head_bk1=customtkinter.CTkLabel(frame2_bk1, text="Choose your payment : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=85, y=350)
            
            img_visa = ImageTk.PhotoImage(Image.open("images/visa.jfif"))
            but_visa = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_visa,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
            but_visa.place(x=380, y=370)
            
            img_masterCard = ImageTk.PhotoImage(Image.open("images/mastercard.jfif"))
            but_masterCard = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_masterCard,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
            but_masterCard.place(x=510, y=370)
            
            img_paypal = ImageTk.PhotoImage(Image.open("images/paypal.jfif"))
            but_paypal = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_paypal,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=paypal)
            but_paypal.place(x=640, y=370)
            
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
        but_bk1 = customtkinter.CTkButton(frame2_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'), command=Cntinue)
        but_bk1.place(x=305, y=290)
                
        win_book1.state("zoomed")
        win_book1.mainloop()
        

#************ book2********************


    def book2(self):
            def card():
                frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
                frame3_bk1.place(x = 530,y=490)
                
                head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter your card : ",font=('Times New Roman',20,'bold'))
                head_bk1.place(x=50, y=30)
                
                num_bk1= customtkinter.CTkEntry(frame3_bk1, width=210, height=35, placeholder_text='Enter card number')
                num_bk1.place(x=255, y=25)
                
                date_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='mm/yy')
                date_bk1.place(x=515, y=25)
                
                cod_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter security card')
                cod_bk1.place(x=255, y=75)
                
                adress_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter your adress')
                adress_bk1.place(x=515, y=75)
                
                buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
                buy_bk1.place(x= 355, y=140)
            
            def paypal():
                frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
                frame3_bk1.place(x = 530,y=490)
                
                head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter email from paypal : ",font=('Times New Roman',20,'bold'))
                head_bk1.place(x=50, y=45)
                
                email_pay_bk1= customtkinter.CTkEntry(frame3_bk1, width=290, height=35, placeholder_text='Enter your email')
                email_pay_bk1.place(x=320, y=45)
                
                buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=175, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
                buy_bk1.place(x= 315, y=115)
            
            def Cntinue():
                head_bk1=customtkinter.CTkLabel(frame2_bk1, text="Choose your payment : ",font=('Times New Roman',20,'bold'))
                head_bk1.place(x=85, y=350)
                
                img_visa = ImageTk.PhotoImage(Image.open("images/visa.jfif"))
                but_visa = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_visa,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
                but_visa.place(x=380, y=370)
                
                img_masterCard = ImageTk.PhotoImage(Image.open("images/mastercard.jfif"))
                but_masterCard = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_masterCard,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
                but_masterCard.place(x=510, y=370)
                
                img_paypal = ImageTk.PhotoImage(Image.open("images/paypal.jfif"))
                but_paypal = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_paypal,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=paypal)
                but_paypal.place(x=640, y=370)
                
            win_book1 = Tk()

            img2=ImageTk.PhotoImage(Image.open("images/pattern.png"))
            l1=customtkinter.CTkLabel(win_book1,image=img2)
            l1.pack()
        
            frame=customtkinter.CTkFrame(master = win_book1, width=430, height=640, corner_radius=6)
            frame.place(x = 70,y=40)

            img_book1 = ImageTk.PhotoImage(Image.open("new_images/img-2.jfif"))
            label1 = Label(frame,image = img_book1, width=310, height=290)
            label1.pack()
            label1.place(x=60, y=25)
            
            desc_bk1=customtkinter.CTkLabel(frame, text="Description : ",font=('Times New Roman',25,'bold'))
            desc_bk1.place(x=25, y=335)
            
            desc_bk1=customtkinter.CTkLabel(frame, text="Treasure Island is a classic adventure novel written \nby Robert Louis Stevenson, first published as a book \nin 1883. Set in the 18th century, the story follows \nthe young protagonist Jim Hawkins as \nhe embarks on a thrilling \njourney in search of buried treasure.The tale begins \nwhen Jim Hawkins discovers a treasure map in the chest \nof a deceased pirate who stayed at his family's \ninn. Excited by the prospect of riches, Jim \njoins a crew led by the enigmatic Long John \nSilver aboard the Hispaniola, a ship bound for the \nfabled Treasure Island. However, unbeknownst to Jim, \nmany of the crew members are ruthless pirates \nwith their own efarious agendas.",font=('Times New Roman',15,'bold'))
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
            but_bk1 = customtkinter.CTkButton(frame2_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'), command=Cntinue)
            but_bk1.place(x=305, y=290)
                    
            win_book1.state("zoomed")
            win_book1.mainloop()
            
 #************ book 3 **************************           
    def book3(self):
            def card():
                frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
                frame3_bk1.place(x = 530,y=490)
                
                head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter your card : ",font=('Times New Roman',20,'bold'))
                head_bk1.place(x=50, y=30)
                
                num_bk1= customtkinter.CTkEntry(frame3_bk1, width=210, height=35, placeholder_text='Enter card number')
                num_bk1.place(x=255, y=25)
                
                date_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='mm/yy')
                date_bk1.place(x=515, y=25)
                
                cod_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter security card')
                cod_bk1.place(x=255, y=75)
                
                adress_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter your adress')
                adress_bk1.place(x=515, y=75)
                
                buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
                buy_bk1.place(x= 355, y=140)
            
            def paypal():
                frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
                frame3_bk1.place(x = 530,y=490)
                
                head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter email from paypal : ",font=('Times New Roman',20,'bold'))
                head_bk1.place(x=50, y=45)
                
                email_pay_bk1= customtkinter.CTkEntry(frame3_bk1, width=290, height=35, placeholder_text='Enter your email')
                email_pay_bk1.place(x=320, y=45)
                
                buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=175, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
                buy_bk1.place(x= 315, y=115)
            
            def Cntinue():
                head_bk1=customtkinter.CTkLabel(frame2_bk1, text="Choose your payment : ",font=('Times New Roman',20,'bold'))
                head_bk1.place(x=85, y=350)
                
                img_visa = ImageTk.PhotoImage(Image.open("images/visa.jfif"))
                but_visa = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_visa,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
                but_visa.place(x=380, y=370)
                
                img_masterCard = ImageTk.PhotoImage(Image.open("images/mastercard.jfif"))
                but_masterCard = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_masterCard,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
                but_masterCard.place(x=510, y=370)
                
                img_paypal = ImageTk.PhotoImage(Image.open("images/paypal.jfif"))
                but_paypal = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_paypal,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=paypal)
                but_paypal.place(x=640, y=370)
                
            win_book1 = Tk()

            img2=ImageTk.PhotoImage(Image.open("images/pattern.png"))
            l1=customtkinter.CTkLabel(win_book1,image=img2)
            l1.pack()
        
            frame=customtkinter.CTkFrame(master = win_book1, width=430, height=640, corner_radius=6)
            frame.place(x = 70,y=40)

            img_book1 = ImageTk.PhotoImage(Image.open("new_images/img-3.jfif"))
            label1 = Label(frame,image = img_book1, width=310, height=290)
            label1.pack()
            label1.place(x=60, y=25)
            
            desc_bk1=customtkinter.CTkLabel(frame, text="Description : ",font=('Times New Roman',25,'bold'))
            desc_bk1.place(x=25, y=335)
            
            desc_bk1=customtkinter.CTkLabel(frame, text="Magic of the Unicorn is a captivating \nfantasy novel that transports readers into \na world filled with wonder, adventure, \nand enchantment. Written by an imaginative \nauthor, it tells the tale of a young protagonist \nwho discovers a realm where unicorns, mystical \ncreatures of legend, exist.The story follows \nthe journey of a courageous protagonist, often \na child or teenager, who stumbles upon a \nhidden portal or magical artifact that \ngrants them access to the realm of unicorns. \nOnce there, they encounter breathtaking landscapes, \nancient forests, and shimmering meadows inhabited \nby these elusive creatures.",font=('Times New Roman',15,'bold'))
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
            but_bk1 = customtkinter.CTkButton(frame2_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'), command=Cntinue)
            but_bk1.place(x=305, y=290)
                    
            win_book1.state("zoomed")
            win_book1.mainloop()
            
    
#******************* book4 ******************
    def book4(self):
            def card():
                frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
                frame3_bk1.place(x = 530,y=490)
                
                head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter your card : ",font=('Times New Roman',20,'bold'))
                head_bk1.place(x=50, y=30)
                
                num_bk1= customtkinter.CTkEntry(frame3_bk1, width=210, height=35, placeholder_text='Enter card number')
                num_bk1.place(x=255, y=25)
                
                date_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='mm/yy')
                date_bk1.place(x=515, y=25)
                
                cod_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter security card')
                cod_bk1.place(x=255, y=75)
                
                adress_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter your adress')
                adress_bk1.place(x=515, y=75)
                
                buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
                buy_bk1.place(x= 355, y=140)
            
            def paypal():
                frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
                frame3_bk1.place(x = 530,y=490)
                
                head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter email from paypal : ",font=('Times New Roman',20,'bold'))
                head_bk1.place(x=50, y=45)
                
                email_pay_bk1= customtkinter.CTkEntry(frame3_bk1, width=290, height=35, placeholder_text='Enter your email')
                email_pay_bk1.place(x=320, y=45)
                
                buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=175, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
                buy_bk1.place(x= 315, y=115)
            
            def Cntinue():
                head_bk1=customtkinter.CTkLabel(frame2_bk1, text="Choose your payment : ",font=('Times New Roman',20,'bold'))
                head_bk1.place(x=85, y=350)
                
                img_visa = ImageTk.PhotoImage(Image.open("images/visa.jfif"))
                but_visa = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_visa,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
                but_visa.place(x=380, y=370)
                
                img_masterCard = ImageTk.PhotoImage(Image.open("images/mastercard.jfif"))
                but_masterCard = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_masterCard,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
                but_masterCard.place(x=510, y=370)
                
                img_paypal = ImageTk.PhotoImage(Image.open("images/paypal.jfif"))
                but_paypal = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_paypal,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=paypal)
                but_paypal.place(x=640, y=370)
                
            win_book1 = Tk()

            img2=ImageTk.PhotoImage(Image.open("images/pattern.png"))
            l1=customtkinter.CTkLabel(win_book1,image=img2)
            l1.pack()
        
            frame=customtkinter.CTkFrame(master = win_book1, width=430, height=640, corner_radius=6)
            frame.place(x = 70,y=40)

            img_book1 = ImageTk.PhotoImage(Image.open("new_images/img-4.jfif"))
            label1 = Label(frame,image = img_book1, width=310, height=290)
            label1.pack()
            label1.place(x=60, y=25)
            
            desc_bk1=customtkinter.CTkLabel(frame, text="Description : ",font=('Times New Roman',25,'bold'))
            desc_bk1.place(x=25, y=335)
            
            desc_bk1=customtkinter.CTkLabel(frame, text="Summer Adventure Stories is a collection of \nexhilarating tales crafted to ignite the spirit \nof adventure in readers of all ages. \nWithin its pages, readers embark on thrilling \njourneys to distant lands, embark on daring quests, \nand experience the magic of summertime\n escapades. Each story in the collection offers \na unique adventure, from exploring hidden treasure \ntroves in tropical islands to embarking on epic \nhikes through rugged mountain ranges. \nThe characters range from intrepid \nexplorers to curious children, \neach facing challenges and overcoming \nobstacles with bravery and determination.",font=('Times New Roman',15,'bold'))
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
            but_bk1 = customtkinter.CTkButton(frame2_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'), command=Cntinue)
            but_bk1.place(x=305, y=290)
                    
            win_book1.state("zoomed")
            win_book1.mainloop()
 
 
 #************* book 5*************
    def book5(self):
            def card():
                frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
                frame3_bk1.place(x = 530,y=490)
                
                head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter your card : ",font=('Times New Roman',20,'bold'))
                head_bk1.place(x=50, y=30)
                
                num_bk1= customtkinter.CTkEntry(frame3_bk1, width=210, height=35, placeholder_text='Enter card number')
                num_bk1.place(x=255, y=25)
                
                date_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='mm/yy')
                date_bk1.place(x=515, y=25)
                
                cod_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter security card')
                cod_bk1.place(x=255, y=75)
                
                adress_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter your adress')
                adress_bk1.place(x=515, y=75)
                
                buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
                buy_bk1.place(x= 355, y=140)
            
            def paypal():
                frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
                frame3_bk1.place(x = 530,y=490)
                
                head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter email from paypal : ",font=('Times New Roman',20,'bold'))
                head_bk1.place(x=50, y=45)
                
                email_pay_bk1= customtkinter.CTkEntry(frame3_bk1, width=290, height=35, placeholder_text='Enter your email')
                email_pay_bk1.place(x=320, y=45)
                
                buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=175, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
                buy_bk1.place(x= 315, y=115)
            
            def Cntinue():
                head_bk1=customtkinter.CTkLabel(frame2_bk1, text="Choose your payment : ",font=('Times New Roman',20,'bold'))
                head_bk1.place(x=85, y=350)
                
                img_visa = ImageTk.PhotoImage(Image.open("images/visa.jfif"))
                but_visa = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_visa,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
                but_visa.place(x=380, y=370)
                
                img_masterCard = ImageTk.PhotoImage(Image.open("images/mastercard.jfif"))
                but_masterCard = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_masterCard,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
                but_masterCard.place(x=510, y=370)
                
                img_paypal = ImageTk.PhotoImage(Image.open("images/paypal.jfif"))
                but_paypal = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_paypal,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=paypal)
                but_paypal.place(x=640, y=370)
                
            win_book1 = Tk()

            img2=ImageTk.PhotoImage(Image.open("images/pattern.png"))
            l1=customtkinter.CTkLabel(win_book1,image=img2)
            l1.pack()
        
            frame=customtkinter.CTkFrame(master = win_book1, width=430, height=640, corner_radius=6)
            frame.place(x = 70,y=40)

            img_book1 = ImageTk.PhotoImage(Image.open("new_images/img-5.jfif"))
            label1 = Label(frame,image = img_book1, width=310, height=290)
            label1.pack()
            label1.place(x=60, y=25)
            
            desc_bk1=customtkinter.CTkLabel(frame, text="Description : ",font=('Times New Roman',25,'bold'))
            desc_bk1.place(x=25, y=335)
            
            desc_bk1=customtkinter.CTkLabel(frame, text="Dragon Run is an enthralling young adult fantasy \nnovel that takes readers on an epic journey \nthrough a world filled with dragons, \nmagic, and adventure. Written by an acclaimed author, \nit follows the thrilling quest of a young \nprotagonist who must navigate a perilous landscape \nto save their kingdom from an ancient evil.\n The story unfolds in a land where dragons \nonce roamed freely, but have since been hunted \nto near extinction. The protagonist, often a \ncourageous and resourceful youth, discovers \nthat they have a special connection to these mythical \ncreatures, which sets them on a path of \ndiscovery and destiny.",font=('Times New Roman',15,'bold'))
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
            but_bk1 = customtkinter.CTkButton(frame2_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'), command=Cntinue)
            but_bk1.place(x=305, y=290)
                    
            win_book1.state("zoomed")
            win_book1.mainloop()
            
            
#********* book 6 ********
    def book6(self):
        def card():
            frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
            frame3_bk1.place(x = 530,y=490)
            
            head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter your card : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=50, y=30)
            
            num_bk1= customtkinter.CTkEntry(frame3_bk1, width=210, height=35, placeholder_text='Enter card number')
            num_bk1.place(x=255, y=25)
            
            date_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='mm/yy')
            date_bk1.place(x=515, y=25)
            
            cod_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter security card')
            cod_bk1.place(x=255, y=75)
            
            adress_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter your adress')
            adress_bk1.place(x=515, y=75)
            
            buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
            buy_bk1.place(x= 355, y=140)
        
        def paypal():
            frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
            frame3_bk1.place(x = 530,y=490)
            
            head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter email from paypal : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=50, y=45)
            
            email_pay_bk1= customtkinter.CTkEntry(frame3_bk1, width=290, height=35, placeholder_text='Enter your email')
            email_pay_bk1.place(x=320, y=45)
            
            buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=175, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
            buy_bk1.place(x= 315, y=115)
        
        def Cntinue():
            head_bk1=customtkinter.CTkLabel(frame2_bk1, text="Choose your payment : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=85, y=350)
            
            img_visa = ImageTk.PhotoImage(Image.open("images/visa.jfif"))
            but_visa = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_visa,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
            but_visa.place(x=380, y=370)
            
            img_masterCard = ImageTk.PhotoImage(Image.open("images/mastercard.jfif"))
            but_masterCard = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_masterCard,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
            but_masterCard.place(x=510, y=370)
            
            img_paypal = ImageTk.PhotoImage(Image.open("images/paypal.jfif"))
            but_paypal = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_paypal,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=paypal)
            but_paypal.place(x=640, y=370)
            
        win_book1 = Tk()

        img2=ImageTk.PhotoImage(Image.open("images/pattern.png"))
        l1=customtkinter.CTkLabel(win_book1,image=img2)
        l1.pack()
    
        frame=customtkinter.CTkFrame(master = win_book1, width=430, height=640, corner_radius=6)
        frame.place(x = 70,y=40)

        img_book1 = ImageTk.PhotoImage(Image.open("new_images/img-6.jfif"))
        label1 = Label(frame,image = img_book1, width=310, height=290)
        label1.pack()
        label1.place(x=60, y=25)
        
        desc_bk1=customtkinter.CTkLabel(frame, text="Description : ",font=('Times New Roman',25,'bold'))
        desc_bk1.place(x=25, y=335)
        
        desc_bk1=customtkinter.CTkLabel(frame, text="Abominable Snowman is a gripping adventure novel that \nexplores the legend of the mythical creature known as the \nYeti or the Abominable Snowman. Written by a renowned \nauthor, it follows a group of explorers and scientists as they \nembark on a daring expedition into the remote and \ntreacherous Himalayan mountains in search of the \nelusive creature. The story unfolds as \nthe expedition team faces the harsh and unforgiving \nconditions of the Himalayas, battling against extreme cold, \nrugged terrain, and the ever-present danger of avalanches \nand crevasses. As they delve deeper into the wilderness, \ntensions rise within the group as they grapple with their \nown fears and doubts, while also confronting the mysteries \nsurrounding the existence of the legendary creature.",font=('Times New Roman',15,'bold'))
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
        but_bk1 = customtkinter.CTkButton(frame2_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'), command=Cntinue)
        but_bk1.place(x=305, y=290)
                
        win_book1.state("zoomed")
        win_book1.mainloop()
        
        
#******** book 7 **************
    def book7(self):
        def card():
            frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
            frame3_bk1.place(x = 530,y=490)
            
            head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter your card : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=50, y=30)
            
            num_bk1= customtkinter.CTkEntry(frame3_bk1, width=210, height=35, placeholder_text='Enter card number')
            num_bk1.place(x=255, y=25)
            
            date_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='mm/yy')
            date_bk1.place(x=515, y=25)
            
            cod_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter security card')
            cod_bk1.place(x=255, y=75)
            
            adress_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter your adress')
            adress_bk1.place(x=515, y=75)
            
            buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
            buy_bk1.place(x= 355, y=140)
        
        def paypal():
            frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
            frame3_bk1.place(x = 530,y=490)
            
            head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter email from paypal : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=50, y=45)
            
            email_pay_bk1= customtkinter.CTkEntry(frame3_bk1, width=290, height=35, placeholder_text='Enter your email')
            email_pay_bk1.place(x=320, y=45)
            
            buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=175, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
            buy_bk1.place(x= 315, y=115)
        
        def Cntinue():
            head_bk1=customtkinter.CTkLabel(frame2_bk1, text="Choose your payment : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=85, y=350)
            
            img_visa = ImageTk.PhotoImage(Image.open("images/visa.jfif"))
            but_visa = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_visa,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
            but_visa.place(x=380, y=370)
            
            img_masterCard = ImageTk.PhotoImage(Image.open("images/mastercard.jfif"))
            but_masterCard = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_masterCard,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
            but_masterCard.place(x=510, y=370)
            
            img_paypal = ImageTk.PhotoImage(Image.open("images/paypal.jfif"))
            but_paypal = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_paypal,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=paypal)
            but_paypal.place(x=640, y=370)
            
        win_book1 = Tk()

        img2=ImageTk.PhotoImage(Image.open("images/pattern.png"))
        l1=customtkinter.CTkLabel(win_book1,image=img2)
        l1.pack()
    
        frame=customtkinter.CTkFrame(master = win_book1, width=430, height=640, corner_radius=6)
        frame.place(x = 70,y=40)

        img_book1 = ImageTk.PhotoImage(Image.open("new_images/adv7.jfif"))
        label1 = Label(frame,image = img_book1, width=310, height=290)
        label1.pack()
        label1.place(x=60, y=25)
        
        desc_bk1=customtkinter.CTkLabel(frame, text="Description : ",font=('Times New Roman',25,'bold'))
        desc_bk1.place(x=25, y=335)
        
        desc_bk1=customtkinter.CTkLabel(frame, text="The Chronicles of Narnia is a beloved fantasy \nseries written by C.S. Lewis that takes readers on \nan extraordinary journey through the magical \nland of Narnia. Comprising  seven books,the \nseries weaves together tales of \nadventure, courage, and redemption, \ncaptivating readers of all ages with its \nrichly imagined world and timeless themes. \nAt the heart of the series is the magical \nwardrobe, which serves as a portal \nto Narnia, a realm inhabited by talking \nanimals, mythical creatures, and powerful \nsorcery. Each book follows the adventures \nof different characters who discover Narnia \nand play pivotal roles in its history.",font=('Times New Roman',15,'bold'))
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
        but_bk1 = customtkinter.CTkButton(frame2_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'), command=Cntinue)
        but_bk1.place(x=305, y=290)
                
        win_book1.state("zoomed")
        win_book1.mainloop()
        
        
#******* book 8 ************
    def book8(self):
        def card():
            frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
            frame3_bk1.place(x = 530,y=490)
            
            head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter your card : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=50, y=30)
            
            num_bk1= customtkinter.CTkEntry(frame3_bk1, width=210, height=35, placeholder_text='Enter card number')
            num_bk1.place(x=255, y=25)
            
            date_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='mm/yy')
            date_bk1.place(x=515, y=25)
            
            cod_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter security card')
            cod_bk1.place(x=255, y=75)
            
            adress_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter your adress')
            adress_bk1.place(x=515, y=75)
            
            buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
            buy_bk1.place(x= 355, y=140)
        
        def paypal():
            frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
            frame3_bk1.place(x = 530,y=490)
            
            head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter email from paypal : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=50, y=45)
            
            email_pay_bk1= customtkinter.CTkEntry(frame3_bk1, width=290, height=35, placeholder_text='Enter your email')
            email_pay_bk1.place(x=320, y=45)
            
            buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=175, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
            buy_bk1.place(x= 315, y=115)
        
        def Cntinue():
            head_bk1=customtkinter.CTkLabel(frame2_bk1, text="Choose your payment : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=85, y=350)
            
            img_visa = ImageTk.PhotoImage(Image.open("images/visa.jfif"))
            but_visa = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_visa,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
            but_visa.place(x=380, y=370)
            
            img_masterCard = ImageTk.PhotoImage(Image.open("images/mastercard.jfif"))
            but_masterCard = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_masterCard,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
            but_masterCard.place(x=510, y=370)
            
            img_paypal = ImageTk.PhotoImage(Image.open("images/paypal.jfif"))
            but_paypal = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_paypal,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=paypal)
            but_paypal.place(x=640, y=370)
            
        win_book1 = Tk()

        img2=ImageTk.PhotoImage(Image.open("images/pattern.png"))
        l1=customtkinter.CTkLabel(win_book1,image=img2)
        l1.pack()
    
        frame=customtkinter.CTkFrame(master = win_book1, width=430, height=640, corner_radius=6)
        frame.place(x = 70,y=40)

        img_book1 = ImageTk.PhotoImage(Image.open("new_images/adv8.jfif"))
        label1 = Label(frame,image = img_book1, width=310, height=290)
        label1.pack()
        label1.place(x=60, y=25)
        
        desc_bk1=customtkinter.CTkLabel(frame, text="Description : ",font=('Times New Roman',25,'bold'))
        desc_bk1.place(x=25, y=335)
        
        desc_bk1=customtkinter.CTkLabel(frame, text="Underwater is a gripping contemporary novel \nthat delves into the complexities of \nhuman emotions and resilience in the face \nof adversity. Written by an acclaimed author, \nit follows the journey of a young protagonist \nas she navigates the aftermath of a traumatic \nevent and seeks to find healing and \nredemption. The story centers around \nthe protagonist, often a teenage girl or \nyoung woman, who finds herself struggling to \ncope with the aftermath of a devastating \nincident, such as a natural disaster, a personal loss, or a \ntraumatic experience. As she grapples with feelings of \nguilt, fear, and isolation, she embarks on a journey.",font=('Times New Roman',15,'bold'))
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
        but_bk1 = customtkinter.CTkButton(frame2_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'), command=Cntinue)
        but_bk1.place(x=305, y=290)
                
        win_book1.state("zoomed")
        win_book1.mainloop()
 
 
#********* book 9 **************
    def book9(self):
        def card():
            frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
            frame3_bk1.place(x = 530,y=490)
            
            head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter your card : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=50, y=30)
            
            num_bk1= customtkinter.CTkEntry(frame3_bk1, width=210, height=35, placeholder_text='Enter card number')
            num_bk1.place(x=255, y=25)
            
            date_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='mm/yy')
            date_bk1.place(x=515, y=25)
            
            cod_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter security card')
            cod_bk1.place(x=255, y=75)
            
            adress_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter your adress')
            adress_bk1.place(x=515, y=75)
            
            buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
            buy_bk1.place(x= 355, y=140)
        
        def paypal():
            frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
            frame3_bk1.place(x = 530,y=490)
            
            head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter email from paypal : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=50, y=45)
            
            email_pay_bk1= customtkinter.CTkEntry(frame3_bk1, width=290, height=35, placeholder_text='Enter your email')
            email_pay_bk1.place(x=320, y=45)
            
            buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=175, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
            buy_bk1.place(x= 315, y=115)
        
        def Cntinue():
            head_bk1=customtkinter.CTkLabel(frame2_bk1, text="Choose your payment : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=85, y=350)
            
            img_visa = ImageTk.PhotoImage(Image.open("images/visa.jfif"))
            but_visa = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_visa,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
            but_visa.place(x=380, y=370)
            
            img_masterCard = ImageTk.PhotoImage(Image.open("images/mastercard.jfif"))
            but_masterCard = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_masterCard,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
            but_masterCard.place(x=510, y=370)
            
            img_paypal = ImageTk.PhotoImage(Image.open("images/paypal.jfif"))
            but_paypal = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_paypal,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=paypal)
            but_paypal.place(x=640, y=370)
            
        win_book1 = Tk()

        img2=ImageTk.PhotoImage(Image.open("images/pattern.png"))
        l1=customtkinter.CTkLabel(win_book1,image=img2)
        l1.pack()
    
        frame=customtkinter.CTkFrame(master = win_book1, width=430, height=640, corner_radius=6)
        frame.place(x = 70,y=40)

        img_book1 = ImageTk.PhotoImage(Image.open("new_images/img-9.jfif"))
        label1 = Label(frame,image = img_book1, width=310, height=290)
        label1.pack()
        label1.place(x=60, y=25)
        
        desc_bk1=customtkinter.CTkLabel(frame, text="Description : ",font=('Times New Roman',25,'bold'))
        desc_bk1.place(x=25, y=335)
        
        desc_bk1=customtkinter.CTkLabel(frame, text="As If It Were a Movie is a thought-provoking \ncontemporary novel that delves into the complexities \nof identity, relationships, and the blurred lines between \nreality and fiction. Written by a talented \nauthor, it offers a unique narrative structure \nthat challenges traditional storytelling conventions. \nThe story follows the protagonist, often a \nyoung adult or teenager, who finds themselves grappling \nwith the challenges of growing up \nand navigating the complexities of modern \nlife. As they navigate relationships, school, and \nthe pursuit of their dreams, they also find themselves \ndrawn into a world of fantasy and imagination.",font=('Times New Roman',15,'bold'))
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
        but_bk1 = customtkinter.CTkButton(frame2_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'), command=Cntinue)
        but_bk1.place(x=305, y=290)
                
        win_book1.state("zoomed")
        win_book1.mainloop()
        
        
        
#*********** book 10 *************
    def book10(self):
        def card():
            frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
            frame3_bk1.place(x = 530,y=490)
            
            head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter your card : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=50, y=30)
            
            num_bk1= customtkinter.CTkEntry(frame3_bk1, width=210, height=35, placeholder_text='Enter card number')
            num_bk1.place(x=255, y=25)
            
            date_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='mm/yy')
            date_bk1.place(x=515, y=25)
            
            cod_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter security card')
            cod_bk1.place(x=255, y=75)
            
            adress_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter your adress')
            adress_bk1.place(x=515, y=75)
            
            buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
            buy_bk1.place(x= 355, y=140)
        
        def paypal():
            frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
            frame3_bk1.place(x = 530,y=490)
            
            head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter email from paypal : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=50, y=45)
            
            email_pay_bk1= customtkinter.CTkEntry(frame3_bk1, width=290, height=35, placeholder_text='Enter your email')
            email_pay_bk1.place(x=320, y=45)
            
            buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=175, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
            buy_bk1.place(x= 315, y=115)
        
        def Cntinue():
            head_bk1=customtkinter.CTkLabel(frame2_bk1, text="Choose your payment : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=85, y=350)
            
            img_visa = ImageTk.PhotoImage(Image.open("images/visa.jfif"))
            but_visa = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_visa,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
            but_visa.place(x=380, y=370)
            
            img_masterCard = ImageTk.PhotoImage(Image.open("images/mastercard.jfif"))
            but_masterCard = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_masterCard,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
            but_masterCard.place(x=510, y=370)
            
            img_paypal = ImageTk.PhotoImage(Image.open("images/paypal.jfif"))
            but_paypal = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_paypal,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=paypal)
            but_paypal.place(x=640, y=370)
            
        win_book1 = Tk()

        img2=ImageTk.PhotoImage(Image.open("images/pattern.png"))
        l1=customtkinter.CTkLabel(win_book1,image=img2)
        l1.pack()
    
        frame=customtkinter.CTkFrame(master = win_book1, width=430, height=640, corner_radius=6)
        frame.place(x = 70,y=40)

        img_book1 = ImageTk.PhotoImage(Image.open("new_images/img-10.jfif"))
        label1 = Label(frame,image = img_book1, width=310, height=290)
        label1.pack()
        label1.place(x=60, y=25)
        
        desc_bk1=customtkinter.CTkLabel(frame, text="Description : ",font=('Times New Roman',25,'bold'))
        desc_bk1.place(x=25, y=335)
        
        desc_bk1=customtkinter.CTkLabel(frame, text="Takings is a gripping legal thriller that follows the \njourney of a determined attorney as she takes on a high\n-stakes case that could change the course of her career \nand impact the lives of countless individuals. \nSet in the heart of a bustling city, the novel explores \nthemes of justice, power, and the ethical dilemmas faced \nby those in the legal profession. The story centers around \nSarah Williams, a brilliant and ambitious young lawyer who \nfinds herself thrust into the spotlight when she is \nassigned to represent a group of homeowners facing \neminent domain proceedings. As a powerful corporation \nseeks to acquire their properties for a lucrative development \nproject, Sarah must navigate a web of legal challenges, \npolitical intrigue, and personal conflicts.",font=('Times New Roman',15,'bold'))
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
        but_bk1 = customtkinter.CTkButton(frame2_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'), command=Cntinue)
        but_bk1.place(x=305, y=290)
                
        win_book1.state("zoomed")
        win_book1.mainloop()
 
 
 
 #********* book 11 ************
    def book11(self):
        def card():
            frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
            frame3_bk1.place(x = 530,y=490)
            
            head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter your card : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=50, y=30)
            
            num_bk1= customtkinter.CTkEntry(frame3_bk1, width=210, height=35, placeholder_text='Enter card number')
            num_bk1.place(x=255, y=25)
            
            date_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='mm/yy')
            date_bk1.place(x=515, y=25)
            
            cod_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter security card')
            cod_bk1.place(x=255, y=75)
            
            adress_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter your adress')
            adress_bk1.place(x=515, y=75)
            
            buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
            buy_bk1.place(x= 355, y=140)
        
        def paypal():
            frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
            frame3_bk1.place(x = 530,y=490)
            
            head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter email from paypal : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=50, y=45)
            
            email_pay_bk1= customtkinter.CTkEntry(frame3_bk1, width=290, height=35, placeholder_text='Enter your email')
            email_pay_bk1.place(x=320, y=45)
            
            buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=175, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
            buy_bk1.place(x= 315, y=115)
        
        def Cntinue():
            head_bk1=customtkinter.CTkLabel(frame2_bk1, text="Choose your payment : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=85, y=350)
            
            img_visa = ImageTk.PhotoImage(Image.open("images/visa.jfif"))
            but_visa = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_visa,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
            but_visa.place(x=380, y=370)
            
            img_masterCard = ImageTk.PhotoImage(Image.open("images/mastercard.jfif"))
            but_masterCard = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_masterCard,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
            but_masterCard.place(x=510, y=370)
            
            img_paypal = ImageTk.PhotoImage(Image.open("images/paypal.jfif"))
            but_paypal = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_paypal,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=paypal)
            but_paypal.place(x=640, y=370)
            
        win_book1 = Tk()

        img2=ImageTk.PhotoImage(Image.open("images/pattern.png"))
        l1=customtkinter.CTkLabel(win_book1,image=img2)
        l1.pack()
    
        frame=customtkinter.CTkFrame(master = win_book1, width=430, height=640, corner_radius=6)
        frame.place(x = 70,y=40)

        img_book1 = ImageTk.PhotoImage(Image.open("new_images/img-11.jpg"))
        label1 = Label(frame,image = img_book1, width=310, height=290)
        label1.pack()
        label1.place(x=60, y=25)
        
        desc_bk1=customtkinter.CTkLabel(frame, text="Description : ",font=('Times New Roman',25,'bold'))
        desc_bk1.place(x=25, y=335)
        
        desc_bk1=customtkinter.CTkLabel(frame, text="Solar Bones is a mesmerizing and thought-\nprovoking novel that unfolds as a single, \ncontinuous stream of consciousness. Written by \nacclaimed Irish author Mike McCormack, it offers \na unique and immersive reading experience that challenges \ntraditional narrative structures. The story centers \naround Marcus Conway, an engineer living in a small town \nin Ireland. As Marcus reflects on his life, memories, \nand experiences, the novel takes readers on a journey \nthrough his thoughts, emotions, and innermost reflections. \nFrom his childhood memories to his struggles with work, \nfamily, and mortality, Marcus's narrative offers a poignant \nand deeply personal exploration of the human condition.",font=('Times New Roman',15,'bold'))
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
        but_bk1 = customtkinter.CTkButton(frame2_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'), command=Cntinue)
        but_bk1.place(x=305, y=290)
                
        win_book1.state("zoomed")
        win_book1.mainloop()
 
 
 
 # **************** book 12 **************
    def book12(self):
        def card():
            frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
            frame3_bk1.place(x = 530,y=490)
            
            head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter your card : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=50, y=30)
            
            num_bk1= customtkinter.CTkEntry(frame3_bk1, width=210, height=35, placeholder_text='Enter card number')
            num_bk1.place(x=255, y=25)
            
            date_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='mm/yy')
            date_bk1.place(x=515, y=25)
            
            cod_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter security card')
            cod_bk1.place(x=255, y=75)
            
            adress_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter your adress')
            adress_bk1.place(x=515, y=75)
            
            buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
            buy_bk1.place(x= 355, y=140)
        
        def paypal():
            frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
            frame3_bk1.place(x = 530,y=490)
            
            head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter email from paypal : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=50, y=45)
            
            email_pay_bk1= customtkinter.CTkEntry(frame3_bk1, width=290, height=35, placeholder_text='Enter your email')
            email_pay_bk1.place(x=320, y=45)
            
            buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=175, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
            buy_bk1.place(x= 315, y=115)
        
        def Cntinue():
            head_bk1=customtkinter.CTkLabel(frame2_bk1, text="Choose your payment : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=85, y=350)
            
            img_visa = ImageTk.PhotoImage(Image.open("images/visa.jfif"))
            but_visa = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_visa,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
            but_visa.place(x=380, y=370)
            
            img_masterCard = ImageTk.PhotoImage(Image.open("images/mastercard.jfif"))
            but_masterCard = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_masterCard,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
            but_masterCard.place(x=510, y=370)
            
            img_paypal = ImageTk.PhotoImage(Image.open("images/paypal.jfif"))
            but_paypal = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_paypal,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=paypal)
            but_paypal.place(x=640, y=370)
            
        win_book1 = Tk()

        img2=ImageTk.PhotoImage(Image.open("images/pattern.png"))
        l1=customtkinter.CTkLabel(win_book1,image=img2)
        l1.pack()
    
        frame=customtkinter.CTkFrame(master = win_book1, width=430, height=640, corner_radius=6)
        frame.place(x = 70,y=40)

        img_book1 = ImageTk.PhotoImage(Image.open("new_images/img-12.jfif"))
        label1 = Label(frame,image = img_book1, width=310, height=290)
        label1.pack()
        label1.place(x=60, y=25)
        
        desc_bk1=customtkinter.CTkLabel(frame, text="Description : ",font=('Times New Roman',25,'bold'))
        desc_bk1.place(x=25, y=335)
        
        desc_bk1=customtkinter.CTkLabel(frame, text="Death Sentence is a gripping thriller that plunges \nreaders into a world of danger, intrigue, and moral \nambiguity. Written by a master of the genre, it follows \nthe pulse-pounding journey of a protagonist \nwho finds themselves caught \nin a deadly game of cat and mouse with a ruthless \nadversary. The story centers around John Smith, \nan ordinary man whose life is turned upside down \nwhen he receives a mysterious \npackage containing evidence of a crime he \ndidn't commit. As he delves deeper into the mystery, \nJohn discovers that he has become the target of a \npowerful and shadowy organization determined \nto silence him at any cost.",font=('Times New Roman',15,'bold'))
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
        but_bk1 = customtkinter.CTkButton(frame2_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'), command=Cntinue)
        but_bk1.place(x=305, y=290)
                
        win_book1.state("zoomed")
        win_book1.mainloop()
 
 
 
#***************** book 13 *********************
    def book13(self):
        def card():
            frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
            frame3_bk1.place(x = 530,y=490)
            
            head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter your card : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=50, y=30)
            
            num_bk1= customtkinter.CTkEntry(frame3_bk1, width=210, height=35, placeholder_text='Enter card number')
            num_bk1.place(x=255, y=25)
            
            date_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='mm/yy')
            date_bk1.place(x=515, y=25)
            
            cod_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter security card')
            cod_bk1.place(x=255, y=75)
            
            adress_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter your adress')
            adress_bk1.place(x=515, y=75)
            
            buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
            buy_bk1.place(x= 355, y=140)
        
        def paypal():
            frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
            frame3_bk1.place(x = 530,y=490)
            
            head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter email from paypal : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=50, y=45)
            
            email_pay_bk1= customtkinter.CTkEntry(frame3_bk1, width=290, height=35, placeholder_text='Enter your email')
            email_pay_bk1.place(x=320, y=45)
            
            buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=175, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
            buy_bk1.place(x= 315, y=115)
        
        def Cntinue():
            head_bk1=customtkinter.CTkLabel(frame2_bk1, text="Choose your payment : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=85, y=350)
            
            img_visa = ImageTk.PhotoImage(Image.open("images/visa.jfif"))
            but_visa = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_visa,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
            but_visa.place(x=380, y=370)
            
            img_masterCard = ImageTk.PhotoImage(Image.open("images/mastercard.jfif"))
            but_masterCard = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_masterCard,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
            but_masterCard.place(x=510, y=370)
            
            img_paypal = ImageTk.PhotoImage(Image.open("images/paypal.jfif"))
            but_paypal = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_paypal,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=paypal)
            but_paypal.place(x=640, y=370)
            
        win_book1 = Tk()

        img2=ImageTk.PhotoImage(Image.open("images/pattern.png"))
        l1=customtkinter.CTkLabel(win_book1,image=img2)
        l1.pack()
    
        frame=customtkinter.CTkFrame(master = win_book1, width=430, height=640, corner_radius=6)
        frame.place(x = 70,y=40)

        img_book1 = ImageTk.PhotoImage(Image.open("new_images/img-13.jpg"))
        label1 = Label(frame,image = img_book1, width=310, height=290)
        label1.pack()
        label1.place(x=60, y=25)
        
        desc_bk1=customtkinter.CTkLabel(frame, text="Description : ",font=('Times New Roman',25,'bold'))
        desc_bk1.place(x=25, y=335)
        
        desc_bk1=customtkinter.CTkLabel(frame, text="Heart Few is a tender and poignant love story that \nunfolds against the backdrop of a quaint coastal town. \nWritten by an acclaimed romance author, it follows the \nintertwined lives of two individuals whose paths \nunexpectedly cross, leading to a transformative journey \nof love, healing, and self-discovery. The story centers \naround Emily, a spirited young woman who has always \nharbored dreams of adventure and exploration, and Jack, a \nreserved yet compassionate artist struggling to overcome \nhis own past traumas. When Emily returns to her hometown \nto care for her ailing grandmother, she never expects \nto meet Jack, whose quiet strength and artistic soul \ncaptivate her from the moment they meet.",font=('Times New Roman',15,'bold'))
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
        but_bk1 = customtkinter.CTkButton(frame2_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'), command=Cntinue)
        but_bk1.place(x=305, y=290)
                
        win_book1.state("zoomed")
        win_book1.mainloop()
 
 
 
 #***************** book 14 ********************
    def book14(self):
        def card():
            frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
            frame3_bk1.place(x = 530,y=490)
            
            head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter your card : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=50, y=30)
            
            num_bk1= customtkinter.CTkEntry(frame3_bk1, width=210, height=35, placeholder_text='Enter card number')
            num_bk1.place(x=255, y=25)
            
            date_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='mm/yy')
            date_bk1.place(x=515, y=25)
            
            cod_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter security card')
            cod_bk1.place(x=255, y=75)
            
            adress_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter your adress')
            adress_bk1.place(x=515, y=75)
            
            buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
            buy_bk1.place(x= 355, y=140)
        
        def paypal():
            frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
            frame3_bk1.place(x = 530,y=490)
            
            head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter email from paypal : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=50, y=45)
            
            email_pay_bk1= customtkinter.CTkEntry(frame3_bk1, width=290, height=35, placeholder_text='Enter your email')
            email_pay_bk1.place(x=320, y=45)
            
            buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=175, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
            buy_bk1.place(x= 315, y=115)
        
        def Cntinue():
            head_bk1=customtkinter.CTkLabel(frame2_bk1, text="Choose your payment : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=85, y=350)
            
            img_visa = ImageTk.PhotoImage(Image.open("images/visa.jfif"))
            but_visa = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_visa,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
            but_visa.place(x=380, y=370)
            
            img_masterCard = ImageTk.PhotoImage(Image.open("images/mastercard.jfif"))
            but_masterCard = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_masterCard,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
            but_masterCard.place(x=510, y=370)
            
            img_paypal = ImageTk.PhotoImage(Image.open("images/paypal.jfif"))
            but_paypal = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_paypal,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=paypal)
            but_paypal.place(x=640, y=370)
            
        win_book1 = Tk()

        img2=ImageTk.PhotoImage(Image.open("images/pattern.png"))
        l1=customtkinter.CTkLabel(win_book1,image=img2)
        l1.pack()
    
        frame=customtkinter.CTkFrame(master = win_book1, width=430, height=640, corner_radius=6)
        frame.place(x = 70,y=40)

        img_book1 = ImageTk.PhotoImage(Image.open("new_images/img-14.jfif"))
        label1 = Label(frame,image = img_book1, width=310, height=290)
        label1.pack()
        label1.place(x=60, y=25)
        
        desc_bk1=customtkinter.CTkLabel(frame, text="Description : ",font=('Times New Roman',25,'bold'))
        desc_bk1.place(x=25, y=335)
        
        desc_bk1=customtkinter.CTkLabel(frame, text="The Dividing Line is a gripping psychological thriller \nthat delves into the darkest corners of the human \nmind and the blurred boundaries between truth and \ndeception. Written by a master storyteller, it weaves \na tale of suspense, intrigue, and moral ambiguity that \nkeeps readers on the edge of their seats until the very \nend. Set in a small town with its own secrets and \nscandals, the story follows the lives of several \ninterconnected characters whose fates become \nintertwined by a series of shocking events. \nAt the center of the narrative is a mysterious \ndividing line that separates the town into two distinct \nworlds, each with its own set of \nrules and expectations.",font=('Times New Roman',15,'bold'))
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
        but_bk1 = customtkinter.CTkButton(frame2_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'), command=Cntinue)
        but_bk1.place(x=305, y=290)
                
        win_book1.state("zoomed")
        win_book1.mainloop()
 
 
 
 #********************* book 15 *****************
    def book15(self):
        def card():
            frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
            frame3_bk1.place(x = 530,y=490)
            
            head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter your card : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=50, y=30)
            
            num_bk1= customtkinter.CTkEntry(frame3_bk1, width=210, height=35, placeholder_text='Enter card number')
            num_bk1.place(x=255, y=25)
            
            date_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='mm/yy')
            date_bk1.place(x=515, y=25)
            
            cod_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter security card')
            cod_bk1.place(x=255, y=75)
            
            adress_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter your adress')
            adress_bk1.place(x=515, y=75)
            
            buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
            buy_bk1.place(x= 355, y=140)
        
        def paypal():
            frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
            frame3_bk1.place(x = 530,y=490)
            
            head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter email from paypal : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=50, y=45)
            
            email_pay_bk1= customtkinter.CTkEntry(frame3_bk1, width=290, height=35, placeholder_text='Enter your email')
            email_pay_bk1.place(x=320, y=45)
            
            buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=175, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
            buy_bk1.place(x= 315, y=115)
        
        def Cntinue():
            head_bk1=customtkinter.CTkLabel(frame2_bk1, text="Choose your payment : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=85, y=350)
            
            img_visa = ImageTk.PhotoImage(Image.open("images/visa.jfif"))
            but_visa = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_visa,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
            but_visa.place(x=380, y=370)
            
            img_masterCard = ImageTk.PhotoImage(Image.open("images/mastercard.jfif"))
            but_masterCard = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_masterCard,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
            but_masterCard.place(x=510, y=370)
            
            img_paypal = ImageTk.PhotoImage(Image.open("images/paypal.jfif"))
            but_paypal = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_paypal,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=paypal)
            but_paypal.place(x=640, y=370)
            
        win_book1 = Tk()

        img2=ImageTk.PhotoImage(Image.open("images/pattern.png"))
        l1=customtkinter.CTkLabel(win_book1,image=img2)
        l1.pack()
    
        frame=customtkinter.CTkFrame(master = win_book1, width=430, height=640, corner_radius=6)
        frame.place(x = 70,y=40)

        img_book1 = ImageTk.PhotoImage(Image.open("new_images/img-15.jfif"))
        label1 = Label(frame,image = img_book1, width=310, height=290)
        label1.pack()
        label1.place(x=60, y=25)
        
        desc_bk1=customtkinter.CTkLabel(frame, text="Description : ",font=('Times New Roman',25,'bold'))
        desc_bk1.place(x=25, y=335)
        
        desc_bk1=customtkinter.CTkLabel(frame, text="The Billion Dollar Spy is a riveting non-fiction \nnarrative that unveils the gripping true story of \nespionage during the Cold War era. \nAuthored by PulitzerPrize-nominated journalist \nDavid E. Hoffman, this meticulously researched \nbook sheds light on one of the most significant \nintelligence operations of the 20th century. \nSet against the backdrop \nof the Cold War tensions between the United \nStates and the Soviet Union, the book follows the clandestine \nactivities of Adolf Tolkachev, a Soviet engineer who \nbecomes a top spy for the CIA. Tolkachev, driven by \ndisillusionment with the oppressive Soviet regime, risks \nhis life to provide crucial intelligence to the \nAmerican intelligence agency.",font=('Times New Roman',15,'bold'))
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
        but_bk1 = customtkinter.CTkButton(frame2_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'), command=Cntinue)
        but_bk1.place(x=305, y=290)
                
        win_book1.state("zoomed")
        win_book1.mainloop()
 



#****************** book 16 *****************
    def book16(self):
        def card():
            frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
            frame3_bk1.place(x = 530,y=490)
            
            head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter your card : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=50, y=30)
            
            num_bk1= customtkinter.CTkEntry(frame3_bk1, width=210, height=35, placeholder_text='Enter card number')
            num_bk1.place(x=255, y=25)
            
            date_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='mm/yy')
            date_bk1.place(x=515, y=25)
            
            cod_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter security card')
            cod_bk1.place(x=255, y=75)
            
            adress_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter your adress')
            adress_bk1.place(x=515, y=75)
            
            buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
            buy_bk1.place(x= 355, y=140)
        
        def paypal():
            frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
            frame3_bk1.place(x = 530,y=490)
            
            head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter email from paypal : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=50, y=45)
            
            email_pay_bk1= customtkinter.CTkEntry(frame3_bk1, width=290, height=35, placeholder_text='Enter your email')
            email_pay_bk1.place(x=320, y=45)
            
            buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=175, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
            buy_bk1.place(x= 315, y=115)
        
        def Cntinue():
            head_bk1=customtkinter.CTkLabel(frame2_bk1, text="Choose your payment : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=85, y=350)
            
            img_visa = ImageTk.PhotoImage(Image.open("images/visa.jfif"))
            but_visa = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_visa,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
            but_visa.place(x=380, y=370)
            
            img_masterCard = ImageTk.PhotoImage(Image.open("images/mastercard.jfif"))
            but_masterCard = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_masterCard,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
            but_masterCard.place(x=510, y=370)
            
            img_paypal = ImageTk.PhotoImage(Image.open("images/paypal.jfif"))
            but_paypal = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_paypal,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=paypal)
            but_paypal.place(x=640, y=370)
            
        win_book1 = Tk()

        img2=ImageTk.PhotoImage(Image.open("images/pattern.png"))
        l1=customtkinter.CTkLabel(win_book1,image=img2)
        l1.pack()
    
        frame=customtkinter.CTkFrame(master = win_book1, width=430, height=640, corner_radius=6)
        frame.place(x = 70,y=40)

        img_book1 = ImageTk.PhotoImage(Image.open("new_images/img-16.jpg"))
        label1 = Label(frame,image = img_book1, width=310, height=290)
        label1.pack()
        label1.place(x=60, y=25)
        
        desc_bk1=customtkinter.CTkLabel(frame, text="Description : ",font=('Times New Roman',25,'bold'))
        desc_bk1.place(x=25, y=335)
        
        desc_bk1=customtkinter.CTkLabel(frame, text="The House on the Lake is a gripping mystery novel \nthat unfolds gainst the backdrop of a secluded and \npicturesque lakeside retreat. Written by a master \nof suspense, it weaves a tale of secrets, betrayal, \nand redemption that keeps readers guessing until \nthe very end. The story follows the protagonist, often \na troubled individual seeking solace and a fresh start, \nwho discovers an idyllic house nestled by the tranquil \nwaters of a remote lake. Drawn by the promise of peace and \nsolitude, they soon find themselves entangled in a web of \nmystery and intrigue as they uncover the dark \nsecrets hidden within the walls of the house.",font=('Times New Roman',15,'bold'))
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
        but_bk1 = customtkinter.CTkButton(frame2_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'), command=Cntinue)
        but_bk1.place(x=305, y=290)
                
        win_book1.state("zoomed")
        win_book1.mainloop()



#*************** book 17 *****************
    def book17(self):
        def card():
            frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
            frame3_bk1.place(x = 530,y=490)
            
            head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter your card : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=50, y=30)
            
            num_bk1= customtkinter.CTkEntry(frame3_bk1, width=210, height=35, placeholder_text='Enter card number')
            num_bk1.place(x=255, y=25)
            
            date_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='mm/yy')
            date_bk1.place(x=515, y=25)
            
            cod_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter security card')
            cod_bk1.place(x=255, y=75)
            
            adress_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter your adress')
            adress_bk1.place(x=515, y=75)
            
            buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
            buy_bk1.place(x= 355, y=140)
        
        def paypal():
            frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
            frame3_bk1.place(x = 530,y=490)
            
            head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter email from paypal : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=50, y=45)
            
            email_pay_bk1= customtkinter.CTkEntry(frame3_bk1, width=290, height=35, placeholder_text='Enter your email')
            email_pay_bk1.place(x=320, y=45)
            
            buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=175, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
            buy_bk1.place(x= 315, y=115)
        
        def Cntinue():
            head_bk1=customtkinter.CTkLabel(frame2_bk1, text="Choose your payment : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=85, y=350)
            
            img_visa = ImageTk.PhotoImage(Image.open("images/visa.jfif"))
            but_visa = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_visa,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
            but_visa.place(x=380, y=370)
            
            img_masterCard = ImageTk.PhotoImage(Image.open("images/mastercard.jfif"))
            but_masterCard = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_masterCard,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
            but_masterCard.place(x=510, y=370)
            
            img_paypal = ImageTk.PhotoImage(Image.open("images/paypal.jfif"))
            but_paypal = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_paypal,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=paypal)
            but_paypal.place(x=640, y=370)
            
        win_book1 = Tk()

        img2=ImageTk.PhotoImage(Image.open("images/pattern.png"))
        l1=customtkinter.CTkLabel(win_book1,image=img2)
        l1.pack()
    
        frame=customtkinter.CTkFrame(master = win_book1, width=430, height=640, corner_radius=6)
        frame.place(x = 70,y=40)

        img_book1 = ImageTk.PhotoImage(Image.open("new_images/img-17.jfif"))
        label1 = Label(frame,image = img_book1, width=310, height=290)
        label1.pack()
        label1.place(x=60, y=25)
        
        desc_bk1=customtkinter.CTkLabel(frame, text="Description : ",font=('Times New Roman',25,'bold'))
        desc_bk1.place(x=25, y=335)
        
        desc_bk1=customtkinter.CTkLabel(frame, text="Mount Majestic is a captivating adventure novel that \ntransports readers to a magical island filled with mystery, \ndanger, and discovery. Written by an imaginative author, \nit follows the thrilling journey of a young protagonist \nas they embark on a quest to unravel \nthe secrets of a legendary mountain. Set on the \nenchanting island of Mount Majestic, \nthe story centers around a spirited protagonist, \noften a courageous child or teenager, who dreams \nof adventure and exploration. When strange occurrences \nbegin to disrupt the peace of the island, \nthe protagonist sets out on a daring quest to uncover \nthe truth behind the mysterious events.",font=('Times New Roman',15,'bold'))
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
        but_bk1 = customtkinter.CTkButton(frame2_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'), command=Cntinue)
        but_bk1.place(x=305, y=290)
                
        win_book1.state("zoomed")
        win_book1.mainloop()




#************* book 18 ***************
    def book18(self):
        def card():
            frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
            frame3_bk1.place(x = 530,y=490)
            
            head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter your card : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=50, y=30)
            
            num_bk1= customtkinter.CTkEntry(frame3_bk1, width=210, height=35, placeholder_text='Enter card number')
            num_bk1.place(x=255, y=25)
            
            date_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='mm/yy')
            date_bk1.place(x=515, y=25)
            
            cod_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter security card')
            cod_bk1.place(x=255, y=75)
            
            adress_bk1= customtkinter.CTkEntry(frame3_bk1, width=180, height=35, placeholder_text='Enter your adress')
            adress_bk1.place(x=515, y=75)
            
            buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
            buy_bk1.place(x= 355, y=140)
        
        def paypal():
            frame3_bk1=customtkinter.CTkFrame(win_book1, width=790, height=190, corner_radius=6)
            frame3_bk1.place(x = 530,y=490)
            
            head_bk1=customtkinter.CTkLabel(frame3_bk1, text="Enter email from paypal : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=50, y=45)
            
            email_pay_bk1= customtkinter.CTkEntry(frame3_bk1, width=290, height=35, placeholder_text='Enter your email')
            email_pay_bk1.place(x=320, y=45)
            
            buy_bk1 = customtkinter.CTkButton(frame3_bk1, width=175, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'))
            buy_bk1.place(x= 315, y=115)
        
        def Cntinue():
            head_bk1=customtkinter.CTkLabel(frame2_bk1, text="Choose your payment : ",font=('Times New Roman',20,'bold'))
            head_bk1.place(x=85, y=350)
            
            img_visa = ImageTk.PhotoImage(Image.open("images/visa.jfif"))
            but_visa = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_visa,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
            but_visa.place(x=380, y=370)
            
            img_masterCard = ImageTk.PhotoImage(Image.open("images/mastercard.jfif"))
            but_masterCard = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_masterCard,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=card)
            but_masterCard.place(x=510, y=370)
            
            img_paypal = ImageTk.PhotoImage(Image.open("images/paypal.jfif"))
            but_paypal = customtkinter.CTkButton(frame2_bk1, width=85, height=15, image = img_paypal,text="", corner_radius=6, font=('Times New Roman',17,'bold'),fg_color="white", command=paypal)
            but_paypal.place(x=640, y=370)
            
        win_book1 = Tk()

        img2=ImageTk.PhotoImage(Image.open("images/pattern.png"))
        l1=customtkinter.CTkLabel(win_book1,image=img2)
        l1.pack()
    
        frame=customtkinter.CTkFrame(master = win_book1, width=430, height=640, corner_radius=6)
        frame.place(x = 70,y=40)

        img_book1 = ImageTk.PhotoImage(Image.open("new_images/img-18.jfif"))
        label1 = Label(frame,image = img_book1, width=310, height=290)
        label1.pack()
        label1.place(x=60, y=25)
        
        desc_bk1=customtkinter.CTkLabel(frame, text="Description : ",font=('Times New Roman',25,'bold'))
        desc_bk1.place(x=25, y=335)
        
        desc_bk1=customtkinter.CTkLabel(frame, text="Joe Hill is a riveting psychological thriller that \nexplores the dark and twisted depths of the human psyche. \nWritten by an acclaimed author known for their mastery \nof suspense, this gripping novel follows \nthe tumultuous journey of Joe Hill, a seemingly ordinary \nman whose life takes a sinister turn when \nhe becomes entangled in a web of deception and \nbetrayal. \nSet against the backdrop of a small, close-knit \ncommunity, the story begins innocently \nenough, with Joe Hill leading a quiet and unassuming \nexistence. But when a series of shocking events unfolds, \nJoe finds himself thrust into a world of \ndanger and intrigue, where nothing is as it \nseems and trust is a luxury he can ill afford.",font=('Times New Roman',15,'bold'))
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
        but_bk1 = customtkinter.CTkButton(frame2_bk1, width=220, height=35, text="Continue", corner_radius=6, font=('Times New Roman',17,'bold'), command=Cntinue)
        but_bk1.place(x=305, y=290)
                
        win_book1.state("zoomed")
        win_book1.mainloop()



bk18 = Books()
bk18.book18()

# bk17 = Books()
# bk17.book17()

# bk16 = Books()
# bk16.book16()

# bk15 = Books()
# bk15.book15()

# bk14 = Books()
# bk14.book14()

# bk13 = Books()
# bk13.book13()
 
# bk12 = Books()
# bk12.book12()
 
# bk11 = Books()
# bk11.book11()
 
# bk10 = Books()
# bk10.book10()
 
# bk9 = Books()
# bk9.book9()
 
# bk8 = Books()
# bk8.book8()
 
# bk7 = Books()
# bk7.book7()
 
# bk5 = Books()
# bk5.book5()
 
# bk4 = Books()
# bk4.book4()
 
# bk3 = Books()
# bk.book3()
 
# bk2 = Books()
# bk2.book2()
            
# bk1 = Books()
# bk1.book1()
    
# bk6 = Books()
# bk6.book4()