
from tkinter import *
import pyodbc
from tkinter.ttk import Combobox
cnxn = pyodbc.connect('Driver={SQL Server};'
'Server=DESKTOP-P8KDAQQ\TESTINSTANCE;'
'Database=test1;'
'Trusted_Connection=yes;')
cursor = cnxn.cursor()

def AdminHome():
    global Home,Get_Users,Get_Books,Get_Available
    Home = Toplevel(mainScreen)
    Home.configure(background="#80DEEA")
    Home.geometry("400x400")
    Home.title("Admin Home Page")
    value =["Librarian","Teacher","Student","All"]
    Get_Users = Combobox(Home,values=value,height=5,width=10)
    Get_Users.place(relx=0.1, rely=0.2, relwidth="0.25", relheight="0.1")
    User_lable = Label(Home, text="Users", font=("Alako-Bold", "15", "bold"), background="#80DEEA", foreground="#009688")
    User_lable.place(relx=0.0001, rely=0.1, relwidth=0.5, relheight=0.1)
    text = "SELECT Title from test1.dbo.Book"
    cursor.execute(text)
    result = cursor.fetchall()
    Get_Books =Combobox(Home,values=result,height=5,width=10)
    Get_Books.place(relx=0.65, rely=0.2, relwidth="0.25", relheight="0.1")
    Book_lable = Label(Home, text="All Books", font=("Alako-Bold", "15", "bold"), background="#80DEEA",
                       foreground="#009688")
    Book_lable.place(relx=0.55, rely=0.1, relwidth=0.5, relheight=0.1)
    text2 = "SELECT Title from test1.dbo.Book where Available =?"
    ava = 1
    cursor.execute(text2,ava)
    result2 = cursor.fetchall()
    Get_Available =Combobox(Home,values=result2,height=5,width=10)
    Get_Available.place(relx=0.35, rely=0.5, relwidth="0.25", relheight="0.1")
    ava_lable = Label(Home, text="Available Books", font=("Alako-Bold", "15", "bold"), background="#80DEEA",
                       foreground="#009688")
    ava_lable.place(relx=0.25, rely=0.4, relwidth=0.5, relheight=0.1)

    submit = Button(master=Home, text="Submit", command=Handle_Combo, relief=FLAT, activebackground="#E0F2F1",
                      background="#009688", foreground="#E0F2F1", activeforeground="#E0F2F1")
    submit.place(relx=0.75, rely=0.8, relwidth="0.2", relheight="0.1")
def Handle_Combo():
    global lista,user_mail,user_pass, Go_TO
    Go_TO = Toplevel(mainScreen)
    Go_TO.configure(background="#80DEEA")
    Go_TO.geometry("400x400")
    Go_TO.title("Go_TO")

    if Get_Users.get() == "Librarian":
        text = "SELECT * from test1.dbo.librarian"
        lista = Listbox(master=Go_TO, background="#80DEEA", foreground="#E0F2F1", selectmode=MULTIPLE)
        lista.place(relx=0, rely=0, relwidth="1", relheight="0.5")
        cursor.execute(text)
        result = cursor.fetchall()
        for i in range(0, len(result)):
            lista.insert(END, result[i])

        user_mail_label = Label(Go_TO, text="Email", font=("Alako-Bold", "15", "bold"), background="#80DEEA",foreground="#009688")
        user_mail_label.place(relx=0.001, rely=0.55, relwidth=0.4, relheight=0.1)
        user_mail= Entry(Go_TO)
        user_mail.place(relx=0.45, rely=0.55, relwidth=0.4)

        user_pas_lable = Label(Go_TO, text="Password", font=("Alako-Bold", "15", "bold"), background="#80DEEA",
                          foreground="#009688")
        user_pas_lable.place(relx=0.001, rely=0.68, relwidth=0.4, relheight=0.1)
        user_pass = Entry(Go_TO)
        user_pass.place(relx=0.45, rely=0.7, relwidth=0.4)

        insert= Button(master=Go_TO, text="Insert", command=insertt, relief=FLAT, activebackground="#E0F2F1",
                          background="#009688", foreground="#E0F2F1", activeforeground="#E0F2F1")
        insert.place(relx=0.4, rely=0.9, relwidth="0.1", relheight="0.05")
        delete= Button(master=Go_TO, text="Delete", command=deletee, relief=FLAT, activebackground="#E0F2F1",
                        background="#009688", foreground="#E0F2F1", activeforeground="#E0F2F1")
        delete.place(relx=0.6, rely=0.9, relwidth="0.1", relheight="0.05")

    elif Get_Users.get()=="Teacher":
        text = "SELECT * from test1.dbo.teacher"
        lista = Listbox(master=Go_TO,background="#80DEEA", foreground="#E0F2F1")
        lista.place(relx=0, rely=0, relwidth="1", relheight="0.5")
        cursor.execute(text)
        result = cursor.fetchall()
        print(result)
        for i in range (0,len(result)):
            lista.insert(END,result[i])
        user_mail_label = Label(Go_TO, text="Email", font=("Alako-Bold", "15", "bold"), background="#80DEEA",
                            foreground="#009688")
        user_mail_label.place(relx=0.001, rely=0.55, relwidth=0.4, relheight=0.1)
        user_mail = Entry(Go_TO)
        user_mail.place(relx=0.45, rely=0.55, relwidth=0.4)

        user_pas_lable = Label(Go_TO, text="Password", font=("Alako-Bold", "15", "bold"), background="#80DEEA",
                           foreground="#009688")
        user_pas_lable.place(relx=0.001, rely=0.68, relwidth=0.4, relheight=0.1)
        user_pass = Entry(Go_TO)
        user_pass.place(relx=0.45, rely=0.7, relwidth=0.4)

        insert = Button(master=Go_TO, text="Insert", command=insertt, relief=FLAT, activebackground="#E0F2F1",
                    background="#009688", foreground="#E0F2F1", activeforeground="#E0F2F1")
        insert.place(relx=0.4, rely=0.9, relwidth="0.1", relheight="0.05")
        delete = Button(master=Go_TO, text="Delete", command=deletee, relief=FLAT, activebackground="#E0F2F1",
                    background="#009688", foreground="#E0F2F1", activeforeground="#E0F2F1")
        delete.place(relx=0.6, rely=0.9, relwidth="0.1", relheight="0.05")

    elif Get_Users.get()=="Student":
        text = "SELECT * from test1.dbo.student"
        lista = Listbox(master=Go_TO,background="#80DEEA", foreground="#E0F2F1")
        lista.place(relx=0, rely=0, relwidth="1", relheight="0.5")
        cursor.execute(text)
        result = cursor.fetchall()
        print(result)
        for i in range (0,len(result)):
            lista.insert(END,result[i])
        print(lista.curselection())
        user_mail_label = Label(Go_TO, text="Email", font=("Alako-Bold", "15", "bold"), background="#80DEEA",
                                foreground="#009688")
        user_mail_label.place(relx=0.001, rely=0.55, relwidth=0.4, relheight=0.1)
        user_mail = Entry(Go_TO)
        user_mail.place(relx=0.45, rely=0.55, relwidth=0.4)

        user_pas_lable = Label(Go_TO, text="Password", font=("Alako-Bold", "15", "bold"), background="#80DEEA",
                               foreground="#009688")
        user_pas_lable.place(relx=0.001, rely=0.68, relwidth=0.4, relheight=0.1)
        user_pass = Entry(Go_TO)
        user_pass.place(relx=0.45, rely=0.7, relwidth=0.4)

        insert = Button(master=Go_TO, text="Insert", command=insertt, relief=FLAT, activebackground="#E0F2F1",
                        background="#009688", foreground="#E0F2F1", activeforeground="#E0F2F1")
        insert.place(relx=0.4, rely=0.9, relwidth="0.1", relheight="0.05")
        delete = Button(master=Go_TO, text="Delete", command=deletee, relief=FLAT, activebackground="#E0F2F1",
                        background="#009688", foreground="#E0F2F1", activeforeground="#E0F2F1")
        delete.place(relx=0.6, rely=0.9, relwidth="0.1", relheight="0.05")

    else:
        text = "SELECT mail,pass_word from librarian union select mail,pass_word from teacher union select mail,pass_word from student;"
        lista = Listbox(master=Go_TO, background="#80DEEA", foreground="#E0F2F1")
        lista.place(relx=0, rely=0, relwidth="1", relheight="0.5")
        cursor.execute(text)
        result = cursor.fetchall()
        print(result)
        for i in range(0, len(result)):
            lista.insert(END, result[i])
        user_mail_label = Label(Go_TO, text="Email", font=("Alako-Bold", "15", "bold"), background="#80DEEA",
                        foreground="#009688")
        user_mail_label.place(relx=0.001, rely=0.55, relwidth=0.4, relheight=0.1)
        user_mail = Entry(Go_TO)
        user_mail.place(relx=0.45, rely=0.55, relwidth=0.4)

        user_pas_lable = Label(Go_TO, text="Password", font=("Alako-Bold", "15", "bold"), background="#80DEEA",
                       foreground="#009688")
        user_pas_lable.place(relx=0.001, rely=0.68, relwidth=0.4, relheight=0.1)
        user_pass = Entry(Go_TO)
        user_pass.place(relx=0.45, rely=0.7, relwidth=0.4)

        insert = Button(master=Go_TO, text="Insert", command=insertt, relief=FLAT, activebackground="#E0F2F1",
                background="#009688", foreground="#E0F2F1", activeforeground="#E0F2F1")
        insert.place(relx=0.4, rely=0.9, relwidth="0.1", relheight="0.05")
        delete = Button(master=Go_TO, text="Delete", command=deletee, relief=FLAT, activebackground="#E0F2F1",
                background="#009688", foreground="#E0F2F1", activeforeground="#E0F2F1")
        delete.place(relx=0.6, rely=0.9, relwidth="0.1", relheight="0.05")
def insertt():
    if Get_Users.get() == "Librarian":
        text = "insert into test1.dbo.librarian (mail,pass_word) values(?,?)"
        vals =(user_mail.get(), user_pass.get())
        cursor.execute(text, vals)
        print(vals)
        cnxn.commit()
    elif Get_Users.get() == "Teacher":
        text = "insert into test1.dbo.teacher (mail,pass_word) values(?,?)"
        vals = (user_mail.get(), user_pass.get())
        cursor.execute(text, vals)
        print(vals)
        cnxn.commit()
    elif Get_Users.get() == "Student":
        text = "insert into test1.dbo.student (mail,pass_word) values(?,?)"
        vals =(user_mail.get(), user_pass.get())
        cursor.execute(text, vals)
        print(vals)
        cnxn.commit()
    else:
        print(1)
    Go_TO.destroy()
def deletee():
    if Get_Users.get() == "Librarian":
        x =lista.curselection()
        for i in x:
            text = "delete from test1.dbo.librarian where L_ID=?"
            cursor.execute(text,i+1)
            cnxn.commit()
    elif Get_Users.get() == "Teacher":
        x = lista.curselection()
        for i in x:
            text = "delete from test1.dbo.teacher where T_ID=?"
            cursor.execute(text, i + 1)
            cnxn.commit()
    elif Get_Users.get() == "Student":
        x = lista.curselection()
        for i in x:
            text = "delete from test1.dbo.student where S_ID=?"
            cursor.execute(text, i + 1)
            cnxn.commit()
    else:
        print(1)
    Go_TO.destroy()
def Log_A():
    text = "SELECT mail,pass_word from test1.dbo.Admins where mail=? and pass_word=?"
    vals = [mail_entry.get(),pas_entry.get()]
    if vals == ['','']:
        error_lable = Label(login, text="Please Enter Your Mail and Password", font=("Alako-Bold", "16", "bold"),background="#80DEEA",
                        foreground="#009688")
        error_lable.place(relx=0.01, rely=0.8, relwidth=1, relheight=0.1)
    elif vals!=['zein90@outlook.com','ze90n']:
        error_lable = Label(login, text="This account is not an Admin", font=("Alako-Bold", "16", "bold"), background="#80DEEA",
                           foreground="#009688")
        error_lable.place(relx=0.01, rely=0.8, relwidth=1, relheight=0.1)
    else:
        cursor.execute(text,tuple(vals))
        result = cursor.fetchall()
        if not result:
            text2 = "insert into test1.dbo.Admins (mail,pass_word) values(?,?)"
            cursor.execute(text2,vals)
            cnxn.commit()
        login.destroy()
        AdminHome()
def Adlog():
    global login,mail_entry,pas_entry
    login = Toplevel(mainScreen)
    login.configure(background="#80DEEA")
    login.geometry("400x400")
    login.title("Admin Login")

    mail_lable=Label(login,text="Email",font=("Alako-Bold", "15", "bold"),background="#80DEEA",foreground="#009688")
    mail_lable.place(relx=0.001,rely=0.1,relwidth=0.5,relheight=0.1)
    mail_entry=Entry(login)
    mail_entry.place(relx=0.45,rely=0.13,relwidth=0.4)

    pas_lable = Label(login, text="Password", font=("Alako-Bold", "15", "bold"), background="#80DEEA", foreground="#009688")
    pas_lable.place(relx=0.001, rely=0.3, relwidth=0.5, relheight=0.1)
    pas_entry=Entry(login)
    pas_entry.place(relx=0.45,rely=0.33,relwidth=0.4)
    register = Button(master=login, text="Register", command=Log_A, relief=FLAT, activebackground="#E0F2F1",
                     background="#009688", foreground="#E0F2F1", activeforeground="#E0F2F1")
    register.place(relx=0.27, rely=0.6, relwidth="0.5", relheight="0.1")
    print("Hi i am an admin")


def Borrow():
    x = lista1.curselection()
    for i in x:
        text = "update  test1.dbo.Book set Available = 0 where B_ID =? "
        cursor.execute(text,i+1)
        cnxn.commit()
    book.destroy()

"""""
def insert_new_book():
    text = "select Name from test1.dbo.Publisher where Name=?"
    val = (Publisher_entry.get())
    cursor.execute(text,val)
    result = cursor.fetchall()
    if not result:

        cnxn.commit()

    print(1)
"""""
def delete_book():
    print(1)
def book_handler():
    global lista1,lista2,book,Department_entry,Publisher_entry,Title_entry,Author_entry
    book = Toplevel(mainScreen)
    book.configure(background="#80DEEA")
    book.geometry("800x500")
    book.title("Books")
    all_label = Label(book, text="All Books", font=("Alako-Bold", "15", "bold"), background="#009688",
                         foreground="#80DEEA")
    all_label.place(relx=0.01, rely=0.01, relwidth=0.4, relheight=0.1)
    text = "select Title,Author,Publisher.Name as Publisher_name,Publisher.Adress,Department.Name as Department_name from Book,Publisher,Department where Book.P_ID = Publisher.P_ID and Book.D_ID = Department.D_ID;"
    lista1 = Listbox(master=book, background="#80DEEA", foreground="#E0F2F1", selectmode=MULTIPLE)
    lista1.place(relx=0, rely=0.1, relwidth="0.5", relheight="0.35", height=10)
    cursor.execute(text)
    result = cursor.fetchall()
    for i in range(0, len(result)):
        lista1.insert(END, result[i])

    available_label = Label(book, text="All available Books", font=("Alako-Bold", "15", "bold"), background="#009688",
                      foreground="#80DEEA")
    available_label.place(relx=0.54, rely=0.01, relwidth=0.4, relheight=0.1)
    text = "select Title,Author,Publisher.Name as Publisher_name,Publisher.Adress,Department.Name as Department_name from Book,Publisher,Department where Book.P_ID = Publisher.P_ID and Book.D_ID = Department.D_ID and Available = 1"
    lista2 = Listbox(master=book, background="#80DEEA", foreground="#E0F2F1", selectmode=MULTIPLE)
    lista2.place(relx=0.52, rely=0.1, relwidth="0.48", relheight="0.35", height=10)
    cursor.execute(text)
    result = cursor.fetchall()
    for i in range(0, len(result)):
        lista2.insert(END, result[i])
    borrowed = Button(master=book, text="Borrowed", command=Borrow, relief=FLAT, activebackground="#E0F2F1",
                    background="#009688", foreground="#E0F2F1", activeforeground="#E0F2F1")
    borrowed.place(relx=0.7, rely=0.5, relwidth="0.15", relheight="0.08")
    deleted = Button(master=book, text="Delete", command=delete_book, relief=FLAT, activebackground="#E0F2F1",
                      background="#009688", foreground="#E0F2F1", activeforeground="#E0F2F1")
    deleted.place(relx=0.2, rely=0.5, relwidth="0.15", relheight="0.08")

    Title_label = Label(book, text="Title", font=("Alako-Bold", "15", "bold"), background="#009688",
                            foreground="#80DEEA")
    Title_label.place(relx=0.1, rely=0.6, relwidth=0.1, relheight=0.1)

    Title_entry = Entry(book)
    Title_entry.place(relx=0.25, rely=0.6, relwidth=0.2)

    Author_label = Label(book, text="Author", font=("Alako-Bold", "15", "bold"), background="#009688",
                            foreground="#80DEEA")
    Author_label.place(relx=0.5, rely=0.6, relwidth=0.1, relheight=0.1)

    Author_entry = Entry(book)
    Author_entry.place(relx=0.62, rely=0.6, relwidth=0.2)
    ##
    Publisher_label = Label(book, text="Publisher", font=("Alako-Bold", "15", "bold"), background="#009688",
                        foreground="#80DEEA")
    Publisher_label.place(relx=0.1, rely=0.8, relwidth=0.1, relheight=0.1)

    Publisher_entry = Entry(book)
    Publisher_entry.place(relx=0.25, rely=0.8, relwidth=0.2)

    Department_label = Label(book, text="Department", font=("Alako-Bold", "14", "bold"), background="#009688",
                         foreground="#80DEEA")
    Department_label.place(relx=0.5, rely=0.8, relwidth=0.1, relheight=0.1)

    Department_entry = Entry(book)
    Department_entry.place(relx=0.62, rely=0.8, relwidth=0.2)

    insert_new = Button(master=book, text="Insert", command=insert_new_book, relief=FLAT, activebackground="#E0F2F1",
                      background="#009688", foreground="#E0F2F1", activeforeground="#E0F2F1")
    insert_new.place(relx=0.7, rely=0.9, relwidth="0.15", relheight="0.08")
def users():
    print(1)
def Edit_profile():
    global LiMail, Lipass,myProf
    myProf = Toplevel(mainScreen)
    myProf.configure(background="#80DEEA")
    myProf.geometry("400x400")
    myProf.title("My Profile")

    LiMail_label = Label(myProf, text="Password", font=("Alako-Bold", "15", "bold"), background="#80DEEA",
                           foreground="#009688")
    LiMail_label.place(relx=0.001, rely=0.55, relwidth=0.4, relheight=0.1)
    LiMail = Entry(myProf)
    LiMail.place(relx=0.45, rely=0.55, relwidth=0.4)

    LiPass_label = Label(myProf, text="Password", font=("Alako-Bold", "15", "bold"), background="#80DEEA",
                       foreground="#009688")
    LiPass_label.place(relx=0.001, rely=0.68, relwidth=0.4, relheight=0.1)
    Lipass= Entry(myProf)
    Lipass.place(relx=0.45, rely=0.7, relwidth=0.4)

    submit = Button(master=myProf, text="Submit", command=update, relief=FLAT, activebackground="#E0F2F1",
                      background="#009688", foreground="#E0F2F1", activeforeground="#E0F2F1")
    submit.place(relx=0.75, rely=0.85, relwidth="0.2", relheight="0.1")
def update():
    text1="update  test1.dbo.librarian set mail=? where mail=?"
    text2="update  test1.dbo.librarian set pass_word=? where pass_word=?"
    vals2= [LiMail.get()]+[vals[0]]
    vals3= [Lipass.get()]+[vals[1]]
    print(vals2)
    print(vals3)
    cursor.execute(text1,tuple(vals2))
    cursor.execute(text2, tuple(vals3))
    cnxn.commit()
    updated_label = Label(myProf, text="Your Data is successfully updated", font=("Alako-Bold", "15", "bold"), background="#80DEEA",
                         foreground="#009688")
    updated_label.place(relx=0.2, rely=0.75, relwidth=0.7, relheight=0.1)
def LibrarianHome():
    global librarian
    librarian = Toplevel(mainScreen)
    librarian.configure(background="#80DEEA")
    librarian.geometry("400x400")
    librarian.title("LibrarianHome")
    """
    value =["Librarian","Teacher","Student","All"]
    Get_Users = Combobox(Home,values=value,height=5,width=10)
    Get_Users.place(relx=0.1, rely=0.2, relwidth="0.25", relheight="0.1")
    User_lable = Label(Home, text="Users", font=("Alako-Bold", "15", "bold"), background="#80DEEA", foreground="#009688")
    User_lable.place(relx=0.0001, rely=0.1, relwidth=0.5, relheight=0.1)
    text = "SELECT Title from test1.dbo.Book"
    cursor.execute(text)
    result = cursor.fetchall()
    Get_Books =Combobox(Home,values=result,height=5,width=10)
    Get_Books.place(relx=0.65, rely=0.2, relwidth="0.25", relheight="0.1")
    """
    #Book_lable = Label(Home, text="All Books", font=("Alako-Bold", "15", "bold"), background="#80DEEA",
     #                  foreground="#009688")
    #Book_lable.place(relx=0.55, rely=0.1, relwidth=0.5, relheight=0.1)
    #text2 = "SELECT Title from test1.dbo.Book where Available =?"
    #ava = 1
    #cursor.execute(text2,ava)
    #result2 = cursor.fetchall()
    #Get_Available =Combobox(Home,values=result2,height=5,width=10)
    #Get_Available.place(relx=0.35, rely=0.5, relwidth="0.25", relheight="0.1")
    #ava_lable = Label(Home, text="Available Books", font=("Alako-Bold", "15", "bold"), background="#80DEEA",
     #                  foreground="#009688")
    #ava_lable.place(relx=0.25, rely=0.4, relwidth=0.5, relheight=0.1)

    Profile = Button(master=librarian, text="Edit Profile", command=Edit_profile, relief=FLAT, activebackground="#E0F2F1",
                      background="#009688", foreground="#E0F2F1", activeforeground="#E0F2F1")
    Profile.place(relx=0.2, rely=0.3, relwidth="0.3", relheight="0.1")

    Get_users_data = Button(master=librarian, text="Users", command=users, relief=FLAT, activebackground="#E0F2F1",
                    background="#009688", foreground="#E0F2F1", activeforeground="#E0F2F1")
    Get_users_data.place(relx=0.52, rely=0.3, relwidth="0.3", relheight="0.1")

    Books = Button(master=librarian, text="Books", command=book_handler, relief=FLAT, activebackground="#E0F2F1",
                      background="#009688", foreground="#E0F2F1", activeforeground="#E0F2F1")
    Books.place(relx=0.35, rely=0.42, relwidth="0.3", relheight="0.1")
def Log_L():
    global vals
    text = "SELECT mail,pass_word from test1.dbo.librarian where mail=? and pass_word=? "
    vals = [mail_entry.get(), pas_entry.get()]
    if vals == ['', '']:
        error_lable = Label(login, text="Please Enter Your Mail and Password", font=("Alako-Bold", "16", "bold"),
                            background="#80DEEA",
                            foreground="#009688")
        error_lable.place(relx=0.01, rely=0.8, relwidth=1, relheight=0.1)
    else:
        cursor.execute(text, tuple(vals))
        result = cursor.fetchall()
        if not result:
            error_lable = Label(login, text="This account is not registered as a Librarian", font=("Alako-Bold", "11", "bold"),
                                background="#80DEEA",
                                foreground="#009688")
            error_lable.place(relx=0.01, rely=0.8, relwidth=1, relheight=0.1)
        else:
            LibrarianHome()
            login.destroy()
def Lilog():
    global login,mail_entry,pas_entry
    login = Toplevel(mainScreen)
    login.configure(background="#80DEEA")
    login.geometry("400x400")
    login.title("Librarian Login")

    mail_lable = Label(login, text="Email", font=("Alako-Bold", "15", "bold"), background="#80DEEA", foreground="#009688")
    mail_lable.place(relx=0.001, rely=0.1, relwidth=0.5, relheight=0.1)
    mail_entry=Entry(login)
    mail_entry.place(relx=0.45,rely=0.13,relwidth=0.4)

    pas_lable = Label(login, text="Password", font=("Alako-Bold", "15", "bold"), background="#80DEEA", foreground="#009688")
    pas_lable.place(relx=0.001, rely=0.3, relwidth=0.5, relheight=0.1)
    pas_entry = Entry(login)
    pas_entry.place(relx=0.45, rely=0.33, relwidth=0.4)

    register = Button(master=login, text="Register", command=Log_L, relief=FLAT, activebackground="#E0F2F1",
                     background="#009688", foreground="#E0F2F1", activeforeground="#E0F2F1")
    register.place(relx=0.27, rely=0.6, relwidth="0.5", relheight="0.1")

    print("Hi i am a librarian")

def Log_T():
    text = "SELECT mail,pass_word from test1.dbo.teacher where mail=? and pass_word=? "
    vals = [mail_entry.get(), pas_entry.get()]
    if vals == ['', '']:
        error_lable = Label(login, text="Please Enter Your Mail and Password", font=("Alako-Bold", "16", "bold"),
                            background="#80DEEA",
                            foreground="#009688")
        error_lable.place(relx=0.01, rely=0.8, relwidth=1, relheight=0.1)
    else:
        cursor.execute(text, tuple(vals))
        result = cursor.fetchall()
        if not result:
            text2 = "insert into test1.dbo.teacher (mail,pass_word) values(?,?)"
            cursor.execute(text2, vals)

            cnxn.commit()

        login.destroy()
def Tlog():
    global login,mail_entry,pas_entry
    login = Toplevel(mainScreen)
    login.configure(background="#80DEEA")
    login.geometry("400x400")
    login.title("Teacher Login")

    mail_lable = Label(login, text="Email", font=("Alako-Bold", "15", "bold"), background="#80DEEA", foreground="#009688")
    mail_lable.place(relx=0.001, rely=0.1, relwidth=0.5, relheight=0.1)
    mail_entry=Entry(login)
    mail_entry.place(relx=0.45,rely=0.13,relwidth=0.4)


    pas_lable = Label(login, text="Password", font=("Alako-Bold", "15", "bold"), background="#80DEEA", foreground="#009688")
    pas_lable.place(relx=0.001, rely=0.3, relwidth=0.5, relheight=0.1)
    pas_entry = Entry(login)
    pas_entry.place(relx=0.45, rely=0.33, relwidth=0.4)

    register = Button(master=login, text="Register", command=Log_T, relief=FLAT, activebackground="#E0F2F1",
                      background="#009688", foreground="#E0F2F1", activeforeground="#E0F2F1")
    register.place(relx=0.27, rely=0.6, relwidth="0.5", relheight="0.1")

    print("Hi i am a teacher")

def Log_S():
    text = "SELECT mail,pass_word from test1.dbo.student where mail=? and pass_word=? "
    vals = [mail_entry.get(), pas_entry.get()]
    if vals == ['', '']:
        error_lable = Label(login, text="Please Enter Your Mail and Password", font=("Alako-Bold", "16", "bold"),
                            background="#80DEEA",
                            foreground="#009688")
        error_lable.place(relx=0.01, rely=0.8, relwidth=1, relheight=0.1)
    else:
        cursor.execute(text, tuple(vals))
        result = cursor.fetchall()
        if not result:
            text2 = "insert into test1.dbo.student (mail,pass_word) values(?,?)"
            cursor.execute(text2, vals)

            cnxn.commit()

        login.destroy()
def Slog():
    global login,mail_entry,pas_entry
    login = Toplevel(mainScreen)
    login.configure(background="#80DEEA")
    login.geometry("400x400")
    login.title("Student Login")

    mail_lable = Label(login, text="Email", font=("Alako-Bold", "15", "bold"), background="#80DEEA", foreground="#009688")
    mail_lable.place(relx=0.001, rely=0.1, relwidth=0.5, relheight=0.1)
    mail_entry = Entry(login)
    mail_entry.place(relx=0.45, rely=0.13, relwidth=0.4)

    pas_lable = Label(login, text="Password", font=("Alako-Bold", "15", "bold"), background="#80DEEA", foreground="#009688")
    pas_lable.place(relx=0.001, rely=0.3, relwidth=0.5, relheight=0.1)
    pas_entry = Entry(login)
    pas_entry.place(relx=0.45, rely=0.33, relwidth=0.4)


    register = Button(master=login, text="Register", command=Log_S, relief=FLAT, activebackground="#E0F2F1",
                      background="#009688", foreground="#E0F2F1", activeforeground="#E0F2F1")
    register.place(relx=0.27, rely=0.6, relwidth="0.5", relheight="0.1")

    print("Hi i am a student")

def main():
    global mainScreen
    mainScreen=Tk()
    mainScreen.configure(background="#80DEEA")
    mainScreen.geometry("400x400")
    mainScreen.title("Great Library")
    photo = PhotoImage(file="library.png")
    img = Label(master=mainScreen, borderwidth=0,image=photo, background="#00A288")
    img.place(relx=0.4, rely=0.00, relwidth="0.6", relheight="1")
    Admin = Button(master=mainScreen, text="Admin", command=Adlog, relief=FLAT, activebackground="#E0F2F1",
                    background="#009688", foreground="#E0F2F1", activeforeground="#E0F2F1")
    Admin.place(relx=0.1, rely=0.1, relwidth="0.2", relheight="0.1")
    Librarian = Button(master=mainScreen, text="Librarian", command=Lilog, relief=FLAT, activebackground="#E0F2F1",
                    background="#009688", foreground="#E0F2F1", activeforeground="#E0F2F1")
    Librarian.place(relx=0.1, rely=0.3, relwidth="0.2", relheight="0.1")
    Teacher= Button(master=mainScreen, text="Teacher", command=Tlog, relief=FLAT, activebackground="#E0F2F1",
                    background="#009688", foreground="#E0F2F1", activeforeground="#E0F2F1")
    Teacher.place(relx=0.1, rely=0.5, relwidth="0.2", relheight="0.1")
    Student = Button(master=mainScreen, text="Student", command=Slog, relief=FLAT, activebackground="#E0F2F1",
                    background="#009688", foreground="#E0F2F1", activeforeground="#E0F2F1")
    Student.place(relx=0.1, rely=0.7, relwidth="0.2", relheight="0.1")
    mainScreen.mainloop()
main()

