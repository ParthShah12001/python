from tkinter import *
from PIL import ImageTk,Image
import sqlite3


def correct():

    root = Tk()
    root.title('DataBase')
    root.geometry("500x500")


    #c.execute("""CREATE TABLE addresses(
    #          site text,
    #           id text,
    #       password text)""")


    #Text boxes
    site_n = Entry(root,width=60)
    site_n.grid(row=0,column=1,padx=20,pady=10)

    id_text = Entry(root,width=60)
    id_text.grid(row=1,column=1,pady=10,padx=10)

    password_text = Entry(root,width=60)
    password_text.grid(row=2,column=1,pady=10,padx=10)

    delete_text = Entry(root,width=60)
    delete_text.grid(row=6,column=1,pady=10,padx=10)

    #labels
    site_l = Label(root,text='Site')
    site_l.grid(row=0,column=0,pady=10,padx=10)

    id_label = Label(root,text="User_id")
    id_label.grid(row=1,column=0,pady=10,padx=10)

    password_label = Label(root,text='Password')
    password_label.grid(row=2,column=0,pady=10,padx=10)

    delete_label = Label(root,text="Enter ID")
    delete_label.grid(row=6,column=0,pady=10,padx=10)

    #submit
    def submit():
        # connecting to database
        conn = sqlite3.connect('address_book.db')

        # create cursor
        c = conn.cursor()

        c.execute("INSERT INTO addresses VALUES (:site_n, :id_text, :password_text)",
                  {
                      "site_n": site_n.get(),
                      "id_text": id_text.get(),
                      "password_text":password_text.get()
                  })




        site_n.delete(0,END)
        id_text.delete(0,END)
        password_text.delete(0,END)

        conn.commit()
        conn.close()

    #display
    def display():

        conn = sqlite3.connect('address_book.db')

        # create cursor
        c = conn.cursor()

        c.execute("SELECT *, oid FROM addresses")
        record = c.fetchall()

        print_record=""
        a = """\nplaceholder\t\tSite\t\tUser_id\t\tPassword"""
        for i in record:
            print_record += str(i[3])+"\t\t"+str(i[0]) + """\t\t""" + str(i[1])+"""\t\t"""+str(i[2])+"\n"+"\n"

        a_label = Label(root,text=a)
        a_label.grid(row=8,column=0,columnspan=2,pady=10)
        print_label = Label(root,text=print_record)
        print_label.grid(row=9,column=0,columnspan=2)

        conn.commit()
        conn.close()


    #delete
    def delete():
        conn = sqlite3.connect('address_book.db')

        # create cursor
        c = conn.cursor()

        c.execute("DELETE from addresses WHERE oid="+delete_text.get())




        conn.commit()
        conn.close()



    #submit
    submit_btn = Button(root, text="Add", command=submit)
    submit_btn.grid(row=4,column=0,columnspan=2,pady=10,padx=10,ipadx=215)

    #display
    display_btn = Button(root,text="display record",command=display)
    display_btn.grid(row=5,column=0,columnspan=2,pady=10,padx=10,ipadx=190)

    #delete
    delete_btn = Button(root,text="Delete record",command=delete)
    delete_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=192)


    root.mainloop()

def login_in():
    root = Tk()
    root.title("Login")
    root.geometry("250x200")

    #Labels
    user_label = Label(root,text="User_ID")
    user_label.grid(row=0,column=0,padx=10,pady=10)

    password_label = Label(root,text="Password")
    password_label.grid(row=1,column=0,padx=10,pady=10)

    #Textbox
    user_text = Entry(root,width=20)
    user_text.grid(row=0,column=1,padx=10,pady=10)

    password_text = Entry(root,width=20)
    password_text.grid(row=1,column=1,padx=10,pady=10)



    def validation():
        if user_text.get()=="Admin":
            if password_text.get()=="Abc#123":
                correct()
            else:
                a = "Invalid Password"
                a_label = Label(root,text=a)
                a_label.grid(row=3,column=0,columnspan=2,padx=10,pady=10)
        else:
            b = "Invalid Password"
            b_label = Label(root, text=b)
            b_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    submit_btn = Button(root, text="Submit", command=validation)
    submit_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

    root.mainloop()
login_in()