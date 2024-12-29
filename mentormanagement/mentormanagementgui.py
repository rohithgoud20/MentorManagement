from cgitb import text
#from curses.textpad import Textbox
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from mentormanagement import *
from tkinter import messagebox

root = Tk()
root.title('Mentor Management')
root.resizable(True, True)
root.geometry('1500x750')
root.configure(bg='ghost white')
#root.wm_attributes('-transparentcolor', '#ab23ff')

titleframe = LabelFrame(root)
titleframe.grid(row=0,column=0)

image=Image.open("3.jpg")

img=image.resize((1500, 600))
my_img=ImageTk.PhotoImage(img)
            # Show image using label
label1 = Label( root, image = my_img)
label1.image = my_img
label1.place(x = 0, y = 100)


image=Image.open("image2.png")

img=image.resize((200, 50))
my_img=ImageTk.PhotoImage(img)
            # Show image using label
label1 = Label( root, image = my_img,bg='ghost white')
label1.image = my_img
label1.place(x = 0, y = 19)

f= ("Arial", 25, "bold")
label1 = Label( root, text="MENTORING MANAGEMENT SYSTEM",font=f,bg="ghost white")
label1.place(x = 320, y = 10)

f= ("Times", 10, "bold")
label1 = Label( root, text="In recognition of the basic need for human connection"+"\n"+" a virtual mentorship program establishes deeper communication between mentors, mentees and parents!!",font=f,bg="ghost white")
label1.place(x = 300, y =60)
def adminframe():
        def adminpage():
            def assign1():
                global lgn_frame2
                #lgn_frame3.destroy()
                #lgn_frame4.destroy()
                lgn_frame2 = Frame(lgn_frame1, bg='ghost white', width=1390, height=600)
                lgn_frame2.place(x=400, y=100)
                global sid
                sid,mid=retrivestudentandmentor()

                clicked1 = StringVar()
                options=mid
                clicked1.set( options[0] )
                drop = OptionMenu( lgn_frame2 , clicked1 , *options )
                drop.place(x=50, y=50)

                clicked2 = StringVar()
                options=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
                clicked2.set( options[0] )
                drop = OptionMenu( lgn_frame2 , clicked2 , *options )
                drop.place(x=200, y=50)
                def assigned():
                    sid1=sid[:int(clicked2.get())]
                    assign(sid1,clicked1.get())
                    del sid[:int(clicked2.get())]
                    messagebox.showinfo("showinfo", "Successfully students assigned to mentor!")
                 
                lgn_button_label = Label(lgn_frame2, image=photo, bg='ghost white')
                lgn_button_label.image = photo
                lgn_button_label.place(x=100, y=100)
                login = Button(lgn_button_label, text='assign', font=("yu gothic ui", 13, "bold"), width=35, bd=0,
                                    bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=assigned)
                login.place(x=20, y=10)


            def view():
                    global lgn_frame3
                    #lgn_frame4.destroy()
                    #lgn_frame2.destroy()
                    lgn_frame3 = Frame(lgn_frame1, bg='ghost white', width=1390, height=600)
                    lgn_frame3.place(x=400, y=100)
                    clicked=StringVar()
                    options=["Student","Mentor","Parent"]
                    clicked.set( "Student")
                    
                    drop = OptionMenu( lgn_frame3 , clicked , *options )
                    drop.place(x=10, y=10)
                    def clear_all():
                        for item in tree.get_children():
                            tree.delete(item)
                    def view1():
                        clear_all()
                        connection,cur=db_connection()
                        if clicked.get()=="Student":
                            cur.execute("SELECT * FROM student")
                            data=cur.fetchall()
                            #data.insert(0,["ID","Name","Email","Password"])
                            for student in data:
                                tree.insert('', 'end', text="1", values=student)
                                tree.place(x=10,y=150)
                        if clicked.get()=="Mentor":
                            cur.execute("SELECT * FROM mentor")
                            data=cur.fetchall()
                            #data.insert(0,["ID","Name","Email","Password"])
                            for student in data:
                                tree.insert('', 'end', text="1", values=student)
                                tree.place(x=10,y=150)
                        if clicked.get()=="Parent":
                            cur.execute("SELECT * FROM parent")
                            data=cur.fetchall()
                            #data.insert(0,["ID","Name","Email","Password"])
                            for student in data:
                                tree.insert('', 'end', text="1", values=student)
                                tree.place(x=10,y=150)
                    lgn_button_label = Label(lgn_frame3, image=photo, bg='ghost white')
                    lgn_button_label.image = photo
                    lgn_button_label.place(x=10, y=50)
                    login = Button(lgn_button_label, text='View', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                        bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=view1)
                    login.place(x=20, y=10)

                    tree = ttk.Treeview(lgn_frame3, column=("ID", "Name", "EMail","Password"), show='headings', height=600)
                    tree.column("# 1", anchor=CENTER)
                    tree.heading("# 1", text="ID")
                    tree.column("# 2", anchor=CENTER)
                    tree.heading("# 2", text="Name")
                    tree.column("# 3", anchor=CENTER)
                    tree.heading("# 3", text="EMail")
                    tree.column("# 4", anchor=CENTER)
                    tree.heading("# 4", text="Password")



                    
                        
            def createaccounts():
                global lgn_frame4
                #lgn_frame2.destroy()
                #lgn_frame3.destroy()
                lgn_frame4 = Frame(lgn_frame1, bg='ghost white', width=1390, height=600)
                lgn_frame4.place(x=400, y=100)
                clicked = StringVar()
                name=StringVar()
                email=StringVar()
                password=StringVar()
                id=StringVar()
                def insertdata():
                    if clicked.get()=='Student':
                        studentregister(name.get(),email.get() ,password.get())
                        messagebox.showinfo("showinfo", "Successfully account Created")
                    if clicked.get()=='Mentor':
                        mentorregister(name.get(),email.get() ,password.get())
                        messagebox.showinfo("showinfo", "Successfully account Created")
                    if clicked.get()=='Parent':
                        parentregister(id.get(),name.get(),email.get() ,password.get())
                        messagebox.showinfo("showinfo", "Successfully account Created")
                        
                
                options=["Student","Mentor","Parent"]
                clicked.set( "Student" )
                
                drop = OptionMenu( lgn_frame4 , clicked , *options )
                drop.place(x=200, y=100)

                username_label = Label(lgn_frame4, text="ID", bg="ghost white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
                username_label.place(x=50, y=150)

                username_entry = Entry(lgn_frame4, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                            font=("yu gothic ui ", 12, "bold"),textvariable=id)
                username_entry.place(x=200, y=150, width=270)

                username_label = Label(lgn_frame4, text="*This field only for parent", bg="ghost white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
                username_label.place(x=300, y=150)

                username_label = Label(lgn_frame4, text="Name", bg="ghost white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
                username_label.place(x=50, y=200)

                username_entry = Entry(lgn_frame4, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                            font=("yu gothic ui ", 12, "bold"),textvariable=name)
                username_entry.place(x=200, y=200, width=270)

                username_label = Label(lgn_frame4, text="Email", bg="ghost white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
                username_label.place(x=50, y=258)

                username_entry = Entry(lgn_frame4, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                            font=("yu gothic ui ", 12, "bold"),textvariable=email)
                username_entry.place(x=200, y=258, width=270)

                username_label = Label(lgn_frame4, text="Password", bg="ghost white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
                username_label.place(x=50, y=318)

                username_entry = Entry(lgn_frame4, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                            font=("yu gothic ui ", 12, "bold"),textvariable=password)
                username_entry.place(x=200, y=318, width=270)
                
                lgn_button_label = Label(lgn_frame4, image=photo, bg='ghost white')
                lgn_button_label.image = photo
                lgn_button_label.place(x=80, y=350)
                login = Button(lgn_button_label, text='Create', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                    bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=insertdata)
                login.place(x=20, y=10)
            def assignstudent():
                lgn_frame8 = Frame(lgn_frame1, bg='ghost white', width=1390, height=600)
                lgn_frame8.place(x=400, y=100)
                tree = ttk.Treeview(lgn_frame8, column=("Student ID", "StudentName", "Mentor ID","Mentor Name"), show='headings', height=600)
                tree.column("# 1", anchor=CENTER)
                tree.heading("# 1", text="Student ID")
                tree.column("# 2", anchor=CENTER)
                tree.heading("# 2", text="Student Name")
                tree.column("# 3", anchor=CENTER)
                tree.heading("# 3", text="Mentor ID")
                tree.column("# 4", anchor=CENTER)
                tree.heading("# 4", text="Mentor Name")
                for i in retrieveassign2():

                    tree.insert('', 'end', text="1", values=i)
                    tree.place(x=10,y=50)
            def quit():
                lgn_frame1.destroy()

            lgn_frame1 = Frame(root, bg='ghost white', width=1390, height=600)
            lgn_frame1.place(x=0, y=100)
            lgn_button = Image.open('images\\btn1.png')
            photo = ImageTk.PhotoImage(lgn_button)
            lgn_button_label = Label(lgn_frame1, image=photo, bg='ghost white')
            lgn_button_label.image = photo
            lgn_button_label.place(x=30, y=50)
            login = Button(lgn_button_label, text='Create accounts', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=createaccounts)
            login.place(x=20, y=10)

            lgn_button_label = Label(lgn_frame1, image=photo, bg='ghost white')
            lgn_button_label.image = photo
            lgn_button_label.place(x=30, y=100)
            login = Button(lgn_button_label, text='View accounts', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=view)
            login.place(x=20, y=10)

            lgn_button_label = Label(lgn_frame1, image=photo, bg='ghost white')
            lgn_button_label.image = photo
            lgn_button_label.place(x=30, y=150)
            login = Button(lgn_button_label, text='Assign Students', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=assign1)
            login.place(x=20, y=10)

            lgn_button_label = Label(lgn_frame1, image=photo, bg='ghost white')
            lgn_button_label.image = photo
            lgn_button_label.place(x=30, y=200)
            login = Button(lgn_button_label, text='Assigned Students list', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=assignstudent)
            login.place(x=20, y=10)

            lgn_button_label = Label(lgn_frame1, image=photo, bg='ghost white')
            lgn_button_label.image = photo
            lgn_button_label.place(x=30, y=250)
            login = Button(lgn_button_label, text='Logout', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=quit)
            login.place(x=20, y=10)
        user=StringVar()
        pwd=StringVar()
        def adminlogin():
             if user.get()=="admin" and pwd.get()=="admin":
                adminpage()
        bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(bg_frame)
        bg_panel = Label(root, image=photo)
        bg_panel.image = photo
        bg_panel.place(x=0,y=100)
        # ====== Login Frame =========================
        lgn_frame = Frame(root, bg='ghost white', width=950, height=600)
        lgn_frame.place(x=200, y=100)

        # ========================================================================
        # ========================================================
        # ========================================================================
        txt = "Admin Login"
        heading = Label(lgn_frame, text=txt, font=('yu gothic ui', 25, "bold"), bg="ghost white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        heading.place(x=80, y=30, width=300, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(side_image)
        side_image_label = Label(lgn_frame, image=photo, bg='ghost white')
        side_image_label.image = photo
        side_image_label.place(x=5, y=150)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(sign_in_image)
        sign_in_image_label = Label(lgn_frame, image=photo, bg='ghost white')
        sign_in_image_label.image = photo
        sign_in_image_label.place(x=620, y=100)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        sign_in_label = Label(lgn_frame, text="Sign In", bg="ghost white", fg="black",
                                    font=("yu gothic ui", 17, "bold"))
        sign_in_label.place(x=650, y=240)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        username_label = Label(lgn_frame, text="Username", bg="ghost white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        username_label.place(x=550, y=300)

        username_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="ghost white", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"),textvariable=user)
        username_entry.place(x=580, y=335, width=270)

        username_line = Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        
        username_line.place(x=550, y=359)
        # ===== Username icon =========
        username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(username_icon)
        username_icon_label = Label(lgn_frame, image=photo, bg='ghost white')
        username_icon_label.image = photo
        username_icon_label.place(x=550, y=332)
        
        # ========================================================================
        # ============================password====================================
        # ========================================================================
        password_label = Label(lgn_frame, text="Password", bg="ghost white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        password_label.place(x=550, y=380)

        password_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="ghost white", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*",textvariable=pwd)
        password_entry.place(x=580, y=416, width=244)

        password_line = Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        password_line.place(x=550, y=440)
        # ======== Password icon ================
        password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(password_icon)
        password_icon_label = Label(lgn_frame, image=photo, bg='ghost white')
        password_icon_label.image = photo
        password_icon_label.place(x=550, y=414)
        # ========================================================================
        # ============================login button================================
        # ========================================================================
        lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(lgn_button)
        lgn_button_label = Label(lgn_frame, image=photo, bg='ghost white')
        lgn_button_label.image = photo
        lgn_button_label.place(x=550, y=450)
        login = Button(lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=adminlogin)
        login.place(x=20, y=10)

def studentframe():
        def studentpage():
            student_frame=Frame(root, bg='ghost white', width=1390, height=600)
            student_frame.place(x=0, y=100)
            def view1():
                student_frame1=Frame(student_frame, bg='ghost white', width=1390, height=600)
                student_frame1.place(x=500, y=100)
                clicked=StringVar()
                options=sretrieve1()
                clicked.set( sretrieve1()[0] )
                
                drop = OptionMenu( student_frame1 , clicked , *options )
                drop.place(x=100, y=50)
                def fetch():
                    textb=Text(student_frame1,height=50,width=100)
                    connection,cur=db_connection()
                    cur.execute("select * from studentdata where id=%s",(clicked.get(),))
                    data=cur.fetchall()
                    for i in data:

                        tree.insert('', 'end', text="1", values=i)
                        tree.place(x=0,y=200)
                tree = ttk.Treeview(student_frame1, column=("Student ID", "Student Name", "CGPA","Attendence Percentage"), show='headings', height=600)
                tree.column("# 1", anchor=CENTER)
                tree.heading("# 1", text="Student ID")
                tree.column("# 2", anchor=CENTER)
                tree.heading("# 2", text="Student Name")
                tree.column("# 3", anchor=CENTER)
                tree.heading("# 3", text="CGPA")
                tree.column("# 4", anchor=CENTER)
                tree.heading("# 4", text="Attendence Percentage")
                
                lgn_button = Image.open('images\\btn1.png')
                photo = ImageTk.PhotoImage(lgn_button)
                lgn_button_label = Label(student_frame1, image=photo, bg='#040405')
                lgn_button_label.image = photo
                lgn_button_label.place(x=100, y=100)
                login = Button(lgn_button_label, text='Submit', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=fetch)
                login.place(x=20, y=10)
            def createquery():
                student_frame2=Frame(student_frame, bg='ghost white', width=1390, height=600)
                student_frame2.place(x=500, y=100)

                id=StringVar(value="Enter your id")
                q=StringVar(value="Enter your query")
                username_entry = Entry(student_frame2,highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                            font=("yu gothic ui ", 12, "bold"),textvariable=id)
                username_entry.place(x=10, y=10, width=270)

                username_entry = Entry(student_frame2, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                            font=("yu gothic ui ", 12, "bold"),textvariable=q)
                username_entry.place(x=10, y=50, width=270)
                def cq():
                    studentquery(id.get(),q.get())
                    messagebox.showinfo("showinfo", "Succesfully added query")
                lgn_button = Image.open('images\\btn1.png')
                photo = ImageTk.PhotoImage(lgn_button)
                lgn_button_label = Label(student_frame2, image=photo, bg='ghost white')
                lgn_button_label.image = photo
                lgn_button_label.place(x=31, y=100)
                login = Button(lgn_button_label, text='Submit',
                                font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                    bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=cq)
                login.place(x=20, y=10)
            def quit():
                student_frame.destroy()
            def view():
                student_frame3=Frame(student_frame, bg='ghost white', width=1390, height=600)
                student_frame3.place(x=500, y=100)
                clicked=StringVar()
                options=sretrieve2()
                clicked.set( sretrieve2()[0] )
                
                drop = OptionMenu(student_frame3 , clicked , *options )
                drop.place(x=100, y=50)
                def fetch():
                    textb=Text(student_frame3,height=50,width=100)
                    connection,cur=db_connection()
                    cur.execute("select query from studentquery where id=%s",(clicked.get(),))
                    data=cur.fetchall()
                    for i in data:
                        textb.insert(END,i[0])
                        textb.place(x=0,y=200)
                lgn_button = Image.open('images\\btn1.png')
                photo = ImageTk.PhotoImage(lgn_button)
                lgn_button_label = Label(student_frame3, image=photo, bg='ghost white')
                lgn_button_label.image = photo
                lgn_button_label.place(x=100, y=100)
                login = Button(lgn_button_label, text='Submit', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=fetch)
                login.place(x=20, y=10)

            lgn_button = Image.open('images\\btn1.png')
            photo = ImageTk.PhotoImage(lgn_button)
            lgn_button_label = Label(student_frame, image=photo, bg='ghost white')
            lgn_button_label.image = photo
            lgn_button_label.place(x=30, y=50)
            login = Button(lgn_button_label, text='View Data', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=view1)
            login.place(x=20, y=10)

            lgn_button_label = Label(student_frame, image=photo, bg='ghost white')
            lgn_button_label.image = photo
            lgn_button_label.place(x=30, y=150)
            login = Button(lgn_button_label, text='create query', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=createquery)
            login.place(x=20, y=10)

            lgn_button_label = Label(student_frame, image=photo, bg='ghost white')
            lgn_button_label.image = photo
            lgn_button_label.place(x=30, y=200)
            login = Button(lgn_button_label, text='view query', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=view)
            login.place(x=20, y=10)

            lgn_button_label = Label(student_frame, image=photo, bg='ghost white')
            lgn_button_label.image = photo
            lgn_button_label.place(x=30, y=250)
            login = Button(lgn_button_label, text='Logout', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=quit)
            login.place(x=20, y=10)
        
        user3=StringVar()
        pwd3=StringVar()
        def studentlogin():
            connection,cur=db_connection()
            cur.execute("select email,password from student")
            data1=cur.fetchall()
            for i in data1:
                if user3.get() in i and pwd3.get() in i:
                        studentpage()
        bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(bg_frame)
        bg_panel = Label(root, image=photo)
        bg_panel.image = photo
        bg_panel.place(x=0,y=100)
        # ====== Login Frame =========================
        lgn_frame = Frame(root, bg='ghost white', width=950, height=600)
        lgn_frame.place(x=200, y=100)

        # ========================================================================
        # ========================================================
        # ========================================================================
        txt = "Student Login"
        heading = Label(lgn_frame, text=txt, font=('yu gothic ui', 25, "bold"), bg="ghost white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        heading.place(x=80, y=30, width=300, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(side_image)
        side_image_label = Label(lgn_frame, image=photo, bg='ghost white')
        side_image_label.image = photo
        side_image_label.place(x=5, y=150)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(sign_in_image)
        sign_in_image_label = Label(lgn_frame, image=photo, bg='ghost white')
        sign_in_image_label.image = photo
        sign_in_image_label.place(x=620, y=100)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        sign_in_label = Label(lgn_frame, text="Sign In", bg="ghost white", fg="black",
                                    font=("yu gothic ui", 17, "bold"))
        sign_in_label.place(x=650, y=240)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        username_label = Label(lgn_frame, text="Username", bg="ghost white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        username_label.place(x=550, y=300)

        username_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="ghost white", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"),textvariable=user3)
        username_entry.place(x=580, y=335, width=270)

        username_line = Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        username_line.place(x=550, y=359)
        # ===== Username icon =========
        username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(username_icon)
        username_icon_label = Label(lgn_frame, image=photo, bg='ghost white')
        username_icon_label.image = photo
        username_icon_label.place(x=550, y=332)
        
        # ========================================================================
        # ============================password====================================
        # ========================================================================
        password_label = Label(lgn_frame, text="Password", bg="ghost white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        password_label.place(x=550, y=380)

        password_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="ghost white", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*",textvariable=pwd3)
        password_entry.place(x=580, y=416, width=244)

        password_line = Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        password_line.place(x=550, y=440)
        # ======== Password icon ================
        password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(password_icon)
        password_icon_label = Label(lgn_frame, image=photo, bg='ghost white')
        password_icon_label.image = photo
        password_icon_label.place(x=550, y=414)
        # ========================================================================
        # ============================login button================================
        # ========================================================================
        lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(lgn_button)
        lgn_button_label = Label(lgn_frame, image=photo, bg='ghost white')
        lgn_button_label.image = photo
        lgn_button_label.place(x=550, y=450)
        login = Button(lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=studentlogin)
        login.place(x=20, y=10)

def mentorframe():
        def mentorpage():
            mentor_frame = Frame(root, bg='ghost white', width=1350, height=600)
            mentor_frame.place(x=10, y=100)
            def add():
                lgn_frame1 = Frame(mentor_frame, bg='ghost white', width=950, height=600)
                lgn_frame1.place(x=450, y=100)
                clicked = StringVar()
                name=StringVar()
                cgpa=StringVar()
                percentage=StringVar()
                #id=StringVar()
                def insertdata1():
                    student_data(clicked.get(),name.get(),cgpa.get(),percentage.get())
                    messagebox.showinfo("showinfo", "Student Deatils Stored Successfully!")
                options=sretrieve()
                clicked.set( sretrieve()[0] )
                
                drop = OptionMenu( lgn_frame1 , clicked , *options )
                drop.place(x=100, y=100)

                username_label = Label(lgn_frame1, text="Name", bg="ghost white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
                username_label.place(x=50, y=150)

                username_entry = Entry(lgn_frame1, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                            font=("yu gothic ui ", 12, "bold"),textvariable=name)
                username_entry.place(x=200, y=150, width=270)

                username_label = Label(lgn_frame1, text="CGPA", bg="ghost white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
                username_label.place(x=50, y=200)

                username_entry = Entry(lgn_frame1, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                            font=("yu gothic ui ", 12, "bold"),textvariable=cgpa)
                username_entry.place(x=200, y=200, width=270)

                username_label = Label(lgn_frame1, text="Attendence", bg="ghost white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
                username_label.place(x=50, y=258)

                username_entry = Entry(lgn_frame1, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                            font=("yu gothic ui ", 12, "bold"),textvariable=percentage)
                username_entry.place(x=200, y=258, width=270)

                
                
                lgn_button_label = Label(lgn_frame1, image=photo, bg='ghost white')
                lgn_button_label.image = photo
                lgn_button_label.place(x=80, y=350)
                login = Button(lgn_button_label, text='Add', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                    bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=insertdata1)
                login.place(x=20, y=10)
            def update():
                lgn_frame2 = Frame(mentor_frame, bg='ghost white', width=950, height=600)
                lgn_frame2.place(x=450, y=100)
                clicked = StringVar()
                
                #id=StringVar()
            
                
                options=sretrieve()
                clicked.set( sretrieve()[0] )
                
                drop = OptionMenu( lgn_frame2 , clicked , *options )
                drop.place(x=100, y=100)
                def click():
                    n,c,a=rdata(clicked.get())
                
                    name=StringVar(value=n[0])
                    cgpa=StringVar(value=c[0])
                    percentage=StringVar(value=a[0])
                    def insertdata1():
                        updatedata(name.get(),cgpa.get(),percentage.get(),clicked.get())
                        messagebox.showinfo("showinfo", "Updated Succesfully")
                    username_label = Label(lgn_frame2, text="Name", bg="ghost white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
                    username_label.place(x=50, y=150)

                    username_entry = Entry(lgn_frame2,  highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                                font=("yu gothic ui ", 12, "bold"),textvariable=name)
                
                
                    #username_entry.insert(-1,"sdfg")
                    username_entry.place(x=200, y=150, width=270)
                    
                    
                    

                    username_label = Label(lgn_frame2, text="CGPA", bg="ghost white", fg="#4f4e4d",
                                        font=("yu gothic ui", 13, "bold"))
                    username_label.place(x=50, y=200)

                    username_entry = Entry(lgn_frame2, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                                font=("yu gothic ui ", 12, "bold"),textvariable=cgpa)
                    username_entry.place(x=200, y=200, width=270)

                    username_label = Label(lgn_frame2, text="Attendence", bg="ghost white", fg="#4f4e4d",
                                        font=("yu gothic ui", 13, "bold"))
                    username_label.place(x=50, y=258)

                    username_entry = Entry(lgn_frame2, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                                font=("yu gothic ui ", 12, "bold"),textvariable=percentage)
                    username_entry.place(x=200, y=258, width=270)

                    
                    
                    lgn_button_label = Label(lgn_frame2, image=photo, bg='ghost white')
                    lgn_button_label.image = photo
                    lgn_button_label.place(x=80, y=350)
                    login = Button(lgn_button_label, text='Update', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                        bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=insertdata1)
                    login.place(x=20, y=10)
                lgn_button_label = Label(lgn_frame2, image=photo, bg='ghost white')
                lgn_button_label.image = photo
                lgn_button_label.place(x=300, y=100)
                login = Button(lgn_button_label, text='click', font=("yu gothic ui", 13, "bold"), width=15, bd=0,
                                    bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=click)
                login.place(x=20, y=10)
                
            def delete():
                lgn_frame3 = Frame(mentor_frame, bg='ghost white', width=950, height=600)
                lgn_frame3.place(x=450, y=100)
                #lgn_frame4.destroy()
                clicked=StringVar()
                options=sretrieve()
                clicked.set( sretrieve()[0] )
                
                drop = OptionMenu( lgn_frame3 , clicked , *options )
                drop.place(x=100, y=100)
                
            

                def insertdata2():
                    deletedata(clicked.get())
                    messagebox.showinfo("showinfo", "Successfully account deleted")
                lgn_button_label = Label(lgn_frame3, image=photo, bg='ghost white')
                lgn_button_label.image = photo
                lgn_button_label.place(x=80, y=350)
                login = Button(lgn_button_label, text='Delete', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                    bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=insertdata2)
                login.place(x=20, y=10)

            def viewlist():
                    global lgn_frame4
                    lgn_frame4 = Frame(mentor_frame, bg='ghost white', width=950, height=600)
                    lgn_frame4.place(x=450, y=100)
                    
                    tree = ttk.Treeview(lgn_frame4, column=("ID", "Name", "CGPA","Attendence Percentage"), show='headings', height=600)
                    tree.column("# 1", anchor=CENTER)
                    tree.heading("# 1", text="ID")
                    tree.column("# 2", anchor=CENTER)
                    tree.heading("# 2", text="Name")
                    tree.column("# 3", anchor=CENTER)
                    tree.heading("# 3", text="CGPA")
                    tree.column("# 4", anchor=CENTER)
                    tree.heading("# 4", text="Attendcence Percentage")

                    connection,cur=db_connection()
                    cur.execute("SELECT * FROM studentdata")
                    data=cur.fetchall()
                    #data.insert(0,["ID","Name","Email","Password"])
                    for student in data:
                        tree.insert('', 'end', text="1", values=student)
                        tree.place(x=100,y=150)
            def viewquery():
                global lgn_frame5

                lgn_frame5 = Frame(mentor_frame, bg='ghost white', width=950, height=600)
                lgn_frame5.place(x=450, y=100)
                clicked=StringVar()
                options=sretrieve()
                clicked.set( sretrieve()[0] )
                

                drop = OptionMenu( lgn_frame5, clicked , *options )
                drop.place(x=10, y=10)
                def view():
                    textb=Text(lgn_frame5, width=50, height=50)
                    connection,cur=db_connection()
                    cur.execute("SELECT query FROM studentquery where id=%s",(clicked.get(),))
                    data=cur.fetchall()
                    for i in data:
                        textb.insert(END,i[0])
                        textb.place(x=10,y=100)

                lgn_button_label = Label(lgn_frame5, image=photo, bg='ghost white')
                lgn_button_label.image = photo
                lgn_button_label.place(x=10, y=50)
                login = Button(lgn_button_label, text='View', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                    bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=view)
                login.place(x=20, y=10)
            def respondquery():
                id=StringVar(value="Enter your ID")
                query=StringVar(value="Answer to query")
                global lgn_frame6
             
                lgn_frame6= Frame(mentor_frame, bg='ghost white', width=950, height=600)
                lgn_frame6.place(x=450, y=100)

                username_entry = Entry(lgn_frame6, text="Enter your id",highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                            font=("yu gothic ui ", 12, "bold"),textvariable=id)
                username_entry.place(x=10, y=10, width=270)

                username_entry = Entry(lgn_frame6, text="enter your answer",highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                            font=("yu gothic ui ", 12, "bold"),textvariable=query)
                username_entry.place(x=10, y=50, width=270)
                def resquery():
                    respquery(id.get(),query.get())
                    messagebox.showinfo("showinfo", "Succesfully answered to query")
                lgn_button_label = Label(lgn_frame6, image=photo, bg='ghost white')
                lgn_button_label.image = photo
                lgn_button_label.place(x=10, y=100)
                login = Button(lgn_button_label, text='submit', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                    bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=resquery)
                login.place(x=20, y=10)
            def addcomment():
                id=StringVar(value="Enter student id")
                query=StringVar(value="Enter your comment")
               
             
                lgn_frame7= Frame(mentor_frame, bg='ghost white', width=950, height=600)
                lgn_frame7.place(x=450, y=100)

                username_entry = Entry(lgn_frame7, text="Enter your id",highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                            font=("yu gothic ui ", 12, "bold"),textvariable=id)
                username_entry.place(x=10, y=10, width=270)

                username_entry = Entry(lgn_frame7, text="enter your answer",highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                            font=("yu gothic ui ", 12, "bold"),textvariable=query)
                username_entry.place(x=10, y=50, width=270)
                def resquery():
                    comments(id.get(),query.get())
                    messagebox.showinfo("showinfo", "Succesfully added comment")

                lgn_button_label = Label(lgn_frame7, image=photo, bg='ghost white')
                lgn_button_label.image = photo
                lgn_button_label.place(x=10, y=100)
                login = Button(lgn_button_label, text='submit', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                    bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=resquery)
                login.place(x=20, y=10)
            def quit():
                mentor_frame.destroy()   
            
            lgn_button = Image.open('images\\btn1.png')
            photo = ImageTk.PhotoImage(lgn_button)
            lgn_button_label = Label(mentor_frame, image=photo, bg='ghost white')
            lgn_button_label.image = photo
            lgn_button_label.place(x=30, y=50)
            login = Button(lgn_button_label, text='Add student data', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=add)
            login.place(x=20, y=10)

            lgn_button_label = Label(mentor_frame, image=photo, bg='ghost white')
            lgn_button_label.image = photo
            lgn_button_label.place(x=30, y=100)
            login = Button(lgn_button_label, text='update', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=update)
            login.place(x=20, y=10)

            lgn_button_label = Label(mentor_frame, image=photo, bg='ghost white')
            lgn_button_label.image = photo
            lgn_button_label.place(x=30, y=150)
            login = Button(lgn_button_label, text='Delete', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=delete)
            login.place(x=20, y=10)

            lgn_button_label = Label(mentor_frame, image=photo, bg='ghost white')
            lgn_button_label.image = photo
            lgn_button_label.place(x=30, y=200)
            login = Button(lgn_button_label, text='View Student List', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=viewlist)
            login.place(x=20, y=10)

            lgn_button_label = Label(mentor_frame, image=photo, bg='ghost white')
            lgn_button_label.image = photo
            lgn_button_label.place(x=30, y=250)
            login = Button(lgn_button_label, text='View query', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=viewquery)
            login.place(x=20, y=10)

            lgn_button_label = Label(mentor_frame, image=photo, bg='ghost white')
            lgn_button_label.image = photo
            lgn_button_label.place(x=30, y=300)
            login = Button(lgn_button_label, text='Respond to query', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=respondquery)
            login.place(x=20, y=10)

            lgn_button_label = Label(mentor_frame, image=photo, bg='ghost white')
            lgn_button_label.image = photo
            lgn_button_label.place(x=30, y=350)
            login = Button(lgn_button_label, text='Add comments', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=addcomment)
            login.place(x=20, y=10)

            

            lgn_button_label = Label(mentor_frame, image=photo, bg='ghost white')
            lgn_button_label.image = photo
            lgn_button_label.place(x=30, y=400)
            login = Button(lgn_button_label, text='Logout', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=quit)
            login.place(x=20, y=10)
        user1=StringVar()
        pwd1=StringVar()
        def mentorlogin():
            
            connection,cur=db_connection()
            cur.execute("select email,password from mentor")
            data1=cur.fetchall()
            for i in data1:
                if user1.get() in i and pwd1.get() in i:
                        mentorpage()

        bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(bg_frame)
        bg_panel = Label(root, image=photo)
        bg_panel.image = photo
        bg_panel.place(x=0,y=100)
        # ====== Login Frame =========================
        lgn_frame = Frame(root, bg='ghost white', width=950, height=600)
        lgn_frame.place(x=200, y=100)

        # ========================================================================
        # ========================================================
        # ========================================================================
        txt = "Mentor Login"
        heading = Label(lgn_frame, text=txt, font=('yu gothic ui', 25, "bold"), bg="ghost white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        heading.place(x=80, y=30, width=300, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(side_image)
        side_image_label = Label(lgn_frame, image=photo, bg='ghost white')
        side_image_label.image = photo
        side_image_label.place(x=5, y=150)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(sign_in_image)
        sign_in_image_label = Label(lgn_frame, image=photo, bg='ghost white')
        sign_in_image_label.image = photo
        sign_in_image_label.place(x=620, y=100)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        sign_in_label = Label(lgn_frame, text="Sign In", bg="ghost white", fg="black",
                                    font=("yu gothic ui", 17, "bold"))
        sign_in_label.place(x=650, y=240)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        username_label = Label(lgn_frame, text="Username", bg="ghost white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        username_label.place(x=550, y=300)

        username_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="ghost white", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"),textvariable=user1)
        username_entry.place(x=580, y=335, width=270)

        username_line = Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        username_line.place(x=550, y=359)
        # ===== Username icon =========
        username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(username_icon)
        username_icon_label = Label(lgn_frame, image=photo, bg='ghost white')
        username_icon_label.image = photo
        username_icon_label.place(x=550, y=332)
        
        # ========================================================================
        # ============================password====================================
        # ========================================================================
        password_label = Label(lgn_frame, text="Password", bg="ghost white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        password_label.place(x=550, y=380)

        password_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="ghost white", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*",textvariable=pwd1)
        password_entry.place(x=580, y=416, width=244)

        password_line = Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        password_line.place(x=550, y=440)
        # ======== Password icon ================
        password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(password_icon)
        password_icon_label = Label(lgn_frame, image=photo, bg='ghost white')
        password_icon_label.image = photo
        password_icon_label.place(x=550, y=414)
        # ========================================================================
        # ============================login button================================
        # ========================================================================
        lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(lgn_button)
        lgn_button_label = Label(lgn_frame, image=photo, bg='ghost white')
        lgn_button_label.image = photo
        lgn_button_label.place(x=550, y=450)
        login = Button(lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=mentorlogin)
        login.place(x=20, y=10)

def parentframe():
        def parentpage():
            parent_frame=Frame(root, bg='ghost white', width=1390, height=600)
            parent_frame.place(x=0, y=100)
            def view():
                parent_frame1=Frame(parent_frame, bg='ghost white', width=1390, height=600)
                parent_frame1.place(x=500, y=100)
                clicked=StringVar()
                options=sretrieve1()
                clicked.set( sretrieve1()[0] )
                
                drop = OptionMenu( parent_frame1 , clicked , *options )
                drop.place(x=100, y=50)
                def fetch():
                    textb=Text(parent_frame1,height=50,width=100)
                    connection,cur=db_connection()
                    cur.execute("select * from studentdata where id=%s",(clicked.get(),))
                    data=cur.fetchall()
                    for i in data:
                        tree.insert('', 'end', text="1", values=i)
                        tree.place(x=0,y=200)
                tree = ttk.Treeview(parent_frame1, column=("Student ID", "Student Name", "CGPA","Attendence Percentage"), show='headings', height=600)
                tree.column("# 1", anchor=CENTER)
                tree.heading("# 1", text="Student ID")
                tree.column("# 2", anchor=CENTER)
                tree.heading("# 2", text="Student Name")
                tree.column("# 3", anchor=CENTER)
                tree.heading("# 3", text="CGPA")
                tree.column("# 4", anchor=CENTER)
                tree.heading("# 4", text="Attendence Percentage")
                
                lgn_button = Image.open('images\\btn1.png')
                photo = ImageTk.PhotoImage(lgn_button)
                lgn_button_label = Label(parent_frame1, image=photo, bg='ghost white')
                lgn_button_label.image = photo
                lgn_button_label.place(x=100, y=100)
                login = Button(lgn_button_label, text='Submit', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=fetch)
                login.place(x=20, y=10)
            def createquery():
                parent_frame2=Frame(parent_frame, bg='ghost white', width=1390, height=600)
                parent_frame2.place(x=500, y=100)
                clicked=StringVar()
                options=sretrieve1()
                clicked.set( sretrieve1()[0] )
                
                drop = OptionMenu( parent_frame2 , clicked , *options )
                drop.place(x=100, y=50)
                def fetch():
                    textb=Text(parent_frame2,height=50,width=100,font=("Arial",20,"bold"))
                    connection,cur=db_connection()
                    cur.execute("select comment from studentremarks where id=%s",(clicked.get(),))
                    data=cur.fetchall()
                    for i in data:
                        textb.insert(END,i[0])
                        textb.place(x=0,y=200)
                lgn_button = Image.open('images\\btn1.png')
                photo = ImageTk.PhotoImage(lgn_button)
                lgn_button_label = Label(parent_frame2, image=photo, bg='ghost white')
                lgn_button_label.image = photo
                lgn_button_label.place(x=100, y=100)
                login = Button(lgn_button_label, text='Submit', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=fetch)
                login.place(x=20, y=10)
            def quit():
                parent_frame.destroy()

            lgn_button = Image.open('images\\btn1.png')
            photo = ImageTk.PhotoImage(lgn_button)
            lgn_button_label = Label(parent_frame, image=photo, bg='ghost white')
            lgn_button_label.image = photo
            lgn_button_label.place(x=30, y=50)
            login = Button(lgn_button_label, text='View Data', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=view)
            login.place(x=20, y=10)

            lgn_button_label = Label(parent_frame, image=photo, bg='ghost white')
            lgn_button_label.image = photo
            lgn_button_label.place(x=30, y=150)
            login = Button(lgn_button_label, text='View Comments', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=createquery)
            login.place(x=20, y=10)

            lgn_button_label = Label(parent_frame, image=photo, bg='ghost white')
            lgn_button_label.image = photo
            lgn_button_label.place(x=30, y=200)
            login = Button(lgn_button_label, text='Logout', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=quit)
            login.place(x=20, y=10)
        user2=StringVar()
        pwd2=StringVar()
        def parentlogin():
            connection,cur=db_connection()
            cur.execute("select email,password from parent")
            data1=cur.fetchall()
            for i in data1:
                if user2.get() in i and pwd2.get() in i:
                        parentpage()
        bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(bg_frame)
        bg_panel = Label(root, image=photo)
        bg_panel.image = photo
        bg_panel.place(x=0,y=100)
        # ====== Login Frame =========================
        lgn_frame = Frame(root, bg='ghost white', width=950, height=600)
        lgn_frame.place(x=200, y=100)

        # ========================================================================
        # ========================================================
        # ========================================================================
        txt = "Parent Login"
        heading = Label(lgn_frame, text=txt, font=('yu gothic ui', 25, "bold"), bg="ghost white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        heading.place(x=80, y=30, width=300, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(side_image)
        side_image_label = Label(lgn_frame, image=photo, bg='ghost white')
        side_image_label.image = photo
        side_image_label.place(x=5, y=130)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(sign_in_image)
        sign_in_image_label = Label(lgn_frame, image=photo, bg='ghost white')
        sign_in_image_label.image = photo
        sign_in_image_label.place(x=620, y=100)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        sign_in_label = Label(lgn_frame, text="Sign In", bg="ghost white", fg="black",
                                    font=("yu gothic ui", 17, "bold"))
        sign_in_label.place(x=650, y=240)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        username_label = Label(lgn_frame, text="Username", bg="ghost white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        username_label.place(x=550, y=300)

        username_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="ghost white", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"),textvariable=user2)
        username_entry.place(x=580, y=335, width=270)

        username_line = Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        username_line.place(x=550, y=359)
        # ===== Username icon =========
        username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(username_icon)
        username_icon_label = Label(lgn_frame, image=photo, bg='ghost white')
        username_icon_label.image = photo
        username_icon_label.place(x=550, y=332)
        
        # ========================================================================
        # ============================password====================================
        # ========================================================================
        password_label = Label(lgn_frame, text="Password", bg="ghost white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        password_label.place(x=550, y=380)

        password_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="ghost white", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*",textvariable=pwd2)
        password_entry.place(x=580, y=416, width=244)

        password_line = Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        password_line.place(x=550, y=440)
        # ======== Password icon ================
        password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(password_icon)
        password_icon_label = Label(lgn_frame, image=photo, bg='ghost white')
        password_icon_label.image = photo
        password_icon_label.place(x=550, y=414)
        # ========================================================================
        # ============================login button================================
        # ========================================================================
        lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(lgn_button)
        lgn_button_label = Label(lgn_frame, image=photo, bg='ghost white')
        lgn_button_label.image = photo
        lgn_button_label.place(x=550, y=450)
        login = Button(lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=parentlogin)
        login.place(x=20, y=10)
def home():
    image=Image.open("3.jpg")

    img=image.resize((1500, 600))
    my_img=ImageTk.PhotoImage(img)
                # Show image using label
    label1 = Label( root, image = my_img)
    label1.image = my_img
    label1.place(x = 0, y = 100)

b= ("Arial", 10, "bold")
open_button = Button(root,text='Home',command=home,bd=0,bg="ghost white",font=b,fg='dark blue')
open_button.place(x=900,y=70)

open_button = Button(root,text='Admin',command=adminframe,bd=0,bg="ghost white",font=b,fg='dark blue')
open_button.place(x=1000,y=70)

open_button = Button(root,text='Student',command=studentframe,bd=0,bg="ghost white",font=b,fg='dark blue')
open_button.place(x=1100,y=70)

open_button = Button(root,text='Mentor',command=mentorframe,bd=0,bg="ghost white",font=b,fg='dark blue')
open_button.place(x=1200,y=70)

open_button = Button(root,text='Parent',command=parentframe,bd=0,bg="ghost white",font=b,fg='dark blue')
open_button.place(x=1300,y=70)

root.mainloop()
