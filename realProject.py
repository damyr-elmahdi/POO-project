import tkinter as tk
from tkinter import filedialog

class App:
    def __init__(self, window):
        self.window = window
        self.window.title("Admin info")
        self.window.geometry("500x300")  # Set window size

        # Load user image
        self.user_image = tk.PhotoImage(file="POO project/Admin info.png")
        self.user_image_label = tk.Label(self.window, image=self.user_image)
        self.user_image_label.grid(row=0, columnspan=1)

        self.full_name_label = tk.Label(self.window, text="Full Name:")
        self.full_name_entry = tk.Entry(self.window)

        self.id_code_label = tk.Label(self.window, text="ID Code:")
        self.id_code_entry = tk.Entry(self.window)
        
        self.add_books_button = tk.Button(self.window, text="Add Books", bg="blue", command=self.add_book, height=2, width=20)
        self.modify_info_button = tk.Button(self.window, text="Modify Info", bg="light blue", command=self.modify_info, height=2, width=20)
        self.view_books_button = tk.Button(self.window, text="View Books", bg="green", height=2, width=20)
        self.delete_account_button = tk.Button(self.window, text="Delete Account", bg="red", command=self.delete_book, height=2, width=20)

        self.full_name_label.grid(row=0, column=1)
        self.full_name_entry.grid(row=0, column=2)
        self.id_code_label.grid(row=1, column=1)
        self.id_code_entry.grid(row=1, column=2)
        self.add_books_button.grid(row=3, column=0, pady=30 , padx=10)
        self.modify_info_button.grid(row=3, column=1, pady=30, padx=10)
        self.view_books_button.grid(row=4, column=0, pady=10, padx=10)
        self.delete_account_button.grid(row=4, column=1, pady=10, padx=10)

    def add_book(self):
        add_book_window = tk.Toplevel(self.window)
        add_book_window.geometry("350x400")
        add_book_window.title("Add a book to store")
        
        Title= tk.Label(add_book_window, text="Add a book to store", bg="blue",fg="white", font=('Helvetica', 10), height=2, width=20)
        
        cover_label = tk.Label(add_book_window, text="Cover of the book:")
        cover_button = tk.Button(add_book_window, text="Upload Image", command=filedialog.askopenfilename, height=2, width=20)

        title_label = tk.Label(add_book_window, text="Title of the book:")
        title_entry = tk.Entry(add_book_window)

        price_label = tk.Label(add_book_window, text="Price:")
        price_entry = tk.Entry(add_book_window)
        
        
        Title.grid(row=0, pady=10, padx=10)
        cover_label.grid(row=2, pady=10, padx=10)
        cover_button.grid(row=2,column=1 ,pady=10, padx=10)
        title_label.grid(row=3, pady=10, padx=10)
        title_entry.grid(row=3,column=1,  pady=10, padx=10)
        price_label.grid(row=4 ,pady=10, padx=10)
        price_entry.grid(row=4,column=1 ,pady=10, padx=10)

    def modify_info(self):
        modify_info_window = tk.Toplevel(self.window)
        modify_info_window.geometry("350x400")
        modify_info_window.title("Modify info")

        Title= tk.Label(modify_info_window, text="Modify info", bg="light blue",fg="black", font=('Helvetica', 10), height=2, width=20)
        
        cover_label = tk.Label(modify_info_window, text="Change Cover:")
        cover_button = tk.Button(modify_info_window, text="Upload Image", command=filedialog.askopenfilename, height=2, width=20)

        title_label = tk.Label(modify_info_window, text="Change Title ;")
        title_entry = tk.Entry(modify_info_window)

        price_label = tk.Label(modify_info_window, text="change Price:")
        price_entry = tk.Entry(modify_info_window)
        
        
        Title.grid(row=0, pady=10, padx=10)
        cover_label.grid(row=2, pady=10, padx=10)
        cover_button.grid(row=2,column=1 ,pady=10, padx=10)
        title_label.grid(row=3, pady=10, padx=10)
        title_entry.grid(row=3,column=1,  pady=10, padx=10)
        price_label.grid(row=4 ,pady=10, padx=10)
        price_entry.grid(row=4,column=1 ,pady=10, padx=10)
        
        
        
        
    def delete_book(self):
        delete_book_window = tk.Toplevel(self.window)
        delete_book_window.geometry("350x400")
        delete_book_window.title("Detete Book")

        Title= tk.Label(delete_book_window, text="Delete Book", bg="red",fg="white", font=('Helvetica', 10), height=2, width=20)
        
        cover_label = tk.Label(delete_book_window, text="Account :")
             
        
        Title.grid(row=0, pady=10, padx=10)
        cover_label.grid(row=2, pady=10, padx=10)

window = tk.Tk()
app = App(window)
window.mainloop()
