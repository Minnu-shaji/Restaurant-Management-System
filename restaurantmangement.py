import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import datetime as dt

db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="minnu123"
    )
cursor = db.cursor()
cursor.execute("create database if not exists restau");
cursor.execute("use restau");
cursor.execute("create table if not exists owner(user_name varchar(20) primary key,password varchar(20))")
cursor.execute("select * from owner")
if(cursor.fetchall()==0):
    cursor.execute("insert into owner values(%s,%s)",("owner","12345"))
cursor.execute("create table if not exists signup(id int auto_increment primary key,user_name varchar(30),email varchar(30),phone_num varchar(12),password varchar(20));");
cursor.execute("create table if not exists rest_empl(eid int auto_increment primary key,name varchar(20),position varchar(10),salary decimal(10,2));")
cursor.execute("create table if not exists menu(item_id int auto_increment primary key,item_name varchar(25),price decimal(10,2))");
cursor.execute("create table if not exists item_order(id int auto_increment primary key,cust_name varchar(30),item_id int ,quantity int,total_price decimal(10,2),time_stamp varchar(40),foreign key(item_id) references menu(item_id));")


LARGEFONT =("Verdana", 35)
class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
       
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
       
        # creating a container
        container = tk.Frame(self,bg="#333333")
        container.pack(fill="both",expand=True)
   

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 3)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2, page3, vemp, clogin,addempl,signup,vorder,additem,del_empl):
                        frame = F(container, self)                   
                        self.frames[F] = frame
                        frame.grid(row = 0, column = 0)
                        frame.config(padx=50,pady=70)
                        frame.grid_remove()
                               
        self.show_frame(StartPage)
       

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        for fme in self.frames:
                self.frames[fme].grid_remove()
        frame = self.frames[cont]
        frame.grid()

    def login(self, cont):
        '''for fme in self.frames:
                self.frames[fme].grid_remove()
        frame = self.frames[cont]
        frame.grid()'''
        cursor.execute("select * from owner")
        log=cursor.fetchone()
        username,passw=log[0],log[1]
        if user_entry.get()==username and pass_entry.get()==passw:
            for fme in self.frames:
                self.frames[fme].grid_remove()
            frame = self.frames[cont]
            frame.grid()
        else:
            messagebox.showerror(title="Error",message="Invalid login.")

    def cust_login(self,cont):
        cursor.execute("Select user_name,password from signup")
        datas=cursor.fetchall()
        f=0
        for data in datas:
            if use_entry.get()==data[0] and pas_entry.get()==data[1]:
                f=1
                for fme in self.frames:
                    self.frames[fme].grid_remove()
                frame = self.frames[cont]
                frame.grid()
        if f==0:
                messagebox.showerror(title="Error",message="Invalid login.\n If you haven't signed up yet,do sign up")

# first window frame startpage
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
       
        #here
        tk.Frame.__init__(self, parent,bg="#333333")
        welcome_label=tk.Label(self,text="WELCOME",bg="#333333",fg="#FF3399",font=("Arial",30))
        q_label=tk.Label(self,text="Are You a",bg="#333333",fg="#FFFFFF",font=("Arial",18))
        cust_button=tk.Button(self,text="Customer",bg="#FF3399",fg="#FFFFFF",font=("Arial",16),command = lambda : controller.show_frame(clogin))
        or_label=tk.Label(self,text="Or",bg="#333333",fg="#FFFFFF",font=("Arial",15))
        own_button=tk.Button(self,text="Owner",bg="#FF3399",fg="#FFFFFF",font=("Arial",16),command = lambda : controller.show_frame(Page1))



        welcome_label.grid(row=0,column=1,columnspan=1,sticky="news",pady=40,padx=10)
        q_label.grid(row=3,column=1,columnspan=1)
        cust_button.grid(row=4,column=0,pady=20)
        or_label.grid(row=4,column=1)
        own_button.grid(row=4,column=2)

# second window frame page1
class Page1(tk.Frame):
        def __init__(self, parent, controller):
                global user_entry,pass_entry
                tk.Frame.__init__(self, parent,bg="#333333")
                log_label=tk.Label(self,text="Login",bg="#333333",fg="#FF3399",font=("Arial",30))
                user_label=tk.Label(self,text="Username",bg="#333333",fg="#FFFFFF",font=("Arial",16))
                user_entry=tk.Entry(self,font=("Arial",16))
                pass_label=tk.Label(self,text="Password",bg="#333333",fg="#FFFFFF",font=("Arial",16))
                pass_entry=tk.Entry(self,show="*",font=("Arial",16))
                login_button=tk.Button(self,text="Login",bg="#FF3399",fg="#FFFFFF",font=("Arial",16),command = lambda : controller.login(page3))
                button2 = tk.Button(self, text ="Back to First page",bg="#FF3399",fg="#FFFFFF",font=("Arial",16),command = lambda : controller.show_frame(StartPage))
               
                log_label.grid(row=0,column=0,columnspan=2,sticky="news",pady=40)
                user_label.grid(row=1,column=0)
                user_entry.grid(row=1,column=1,pady=20)
                pass_label.grid(row=2,column=0)
                pass_entry.grid(row=2,column=1,pady=20)
                login_button.grid(row=3,column=0,columnspan=2,pady=30)
                button2.grid(row=4,column=0,columnspan=2)

class clogin(tk.Frame):
        def __init__(self, parent, controller):
                global use_entry,pas_entry
                tk.Frame.__init__(self, parent,bg="#333333")
                log_label=tk.Label(self,text="Login",bg="#333333",fg="#FF3399",font=("Arial",30))
                user_label=tk.Label(self,text="Username",bg="#333333",fg="#FFFFFF",font=("Arial",16))
                use_entry=tk.Entry(self,font=("Arial",16))
                pass_label=tk.Label(self,text="Password",bg="#333333",fg="#FFFFFF",font=("Arial",16))
                pas_entry=tk.Entry(self,show="*",font=("Arial",16))
                login_button=tk.Button(self,text="Login",bg="#FF3399",fg="#FFFFFF",font=("Arial",16),command = lambda : controller.cust_login(Page2))
                signup_button=tk.Button(self,text="Signup",bg="#FF3399",fg="#FFFFFF",font=("Arial",16),command = lambda : controller.show_frame(signup))
                button2 = tk.Button(self, text ="Back to First page",bg="#FF3399",fg="#FFFFFF",font=("Arial",16),command = lambda : controller.show_frame(StartPage))
               
                log_label.grid(row=0,column=0,columnspan=2,sticky="news",pady=40)
                user_label.grid(row=1,column=0)
                use_entry.grid(row=1,column=1,pady=20)
                pass_label.grid(row=2,column=0)
                pas_entry.grid(row=2,column=1,pady=20)
                login_button.grid(row=3,column=0,pady=30)
                signup_button.grid(row=3,column=1)
                button2.grid(row=4,column=0,columnspan=2)

class signup(tk.Frame):
     def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent,bg="#333333")
            global uname_entry
            def addcust():
            
                cust_name = uname_entry.get()
                email = email_entry.get()
                phn_num = phn_entry.get()
                password=pass_entry.get()

                if not cust_name or not email or not phn_num or not password:
                    messagebox.showwarning("Error", "Please fill in all fields.")
                    return

                try:
                
                    cursor.execute("select user_name,password from signup")
                    details=cursor.fetchall()
                    fl=0
                    for detail in details:
                        if detail[0]==cust_name:
                            fl=1
                            messagebox.showerror("Error", "Username is already in use")
                            break
                    if fl==0:        
                        query = "INSERT INTO signup (user_name,Email,phone_num,password )VALUES (%s, %s,%s,%s)"
                        data = (cust_name,email,phn_num,password)
                        cursor.execute(query, data)
                        db.commit()

                        messagebox.showinfo("Success", "Signed Up successfully!")
                        controller.show_frame(Page2)

                except mysql.connector.Error as e:
                    messagebox.showerror("Error", f"Error connecting to MySQL: {e}")

        

            tk.Label(self, text="User Name:").grid(row=0, column=0, padx=10, pady=10)
            uname_entry = tk.Entry(self)
            uname_entry.grid(row=0, column=1, padx=10, pady=10)

            tk.Label(self, text="Email").grid(row=1, column=0, padx=10, pady=10)
            email_entry = tk.Entry(self)
            email_entry.grid(row=1, column=1, padx=10, pady=10)

            tk.Label(self, text="Phone number").grid(row=2, column=0, padx=10, pady=10)
            phn_entry = tk.Entry(self)
            phn_entry.grid(row=2, column=1, padx=10, pady=10)

            tk.Label(self, text="Password").grid(row=3, column=0, padx=10, pady=10)
            pass_entry = tk.Entry(self)
            pass_entry.grid(row=3, column=1, padx=10, pady=10)


            s_button = tk.Button(self, text="Sign Up",command=lambda:addcust())
            s_button.grid(row=4, column=0, columnspan=2, pady=10)

            back_button=tk.Button(self,text="Previous page",bg="#FF3399",fg="#FFFFFF",font=("Arial",16),command = lambda : controller.show_frame(Page1))
            back_button.grid(row=7,column=2,columnspan=2,pady=30)

          
     
       
# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="#333333")
       
        def populate_menu():
            for item in menu_data:
                menu_treeview.insert('', 'end', values=item)

        def add_to_order():
            selected_item = menu_treeview.item(menu_treeview.selection(), 'values')
            if selected_item:
                item_id, item_name, item_price = selected_item

                for index, order_item in enumerate(order_items):
                    if order_item[0] == item_id:

                        new_quantity = order_item[1] + 1
                        total_price = float(item_price) * new_quantity

                        order_treeview.item(order_treeview.get_children()[index], values=(item_name, new_quantity, total_price))
                        order_items[index] = (item_id, new_quantity, total_price)

                        return

                quantity = 1
                total_price = float(item_price) * quantity
                order_item_data = (item_name, quantity, total_price)
                order_treeview.insert('', 'end', values=order_item_data)
                order_items.append((item_id, quantity, total_price))
                

        def calculate_total():
            total = sum(item[2] for item in order_items)
            total_label.config(text=f"Total: ${total:.2f}")
            for index, order_item in enumerate(order_items):
                item_id, new_quantity, total_price=order_items[index]
                cuname=use_entry.get()
                if not cuname:
                    cuname=uname_entry.get()
                dat = (cuname,item_id, new_quantity, total_price,dt.datetime.now())
                cursor.execute("INSERT INTO item_order (cust_name,item_id,quantity,total_price,time_stamp)VALUES (%s, %s,%s,%s,%s)", dat)
                db.commit()

                
            

        menu_treeview = ttk.Treeview(self, columns=('ID', 'Item', 'Price'), show='headings')
        menu_treeview.heading('ID', text='ID')
        menu_treeview.heading('Item', text='Item')
        menu_treeview.heading('Price', text='Price')

        menu_treeview.pack(padx=20, pady=10)

        order_treeview = ttk.Treeview(self, columns=('Item', 'Quantity', 'Total Price'), show='headings')
        order_treeview.heading('Item', text='Item')
        order_treeview.heading('Quantity', text='Quantity')
        order_treeview.heading('Total Price', text='Total Price')

        order_treeview.pack(padx=20, pady=5)

        cursor.execute("SELECT * FROM menu")
        menu_data = cursor.fetchall()

        populate_menu()

        order_button = tk.Button(self, text="Add to Order", command=add_to_order)
        order_button.pack(pady=5)

        calculate_button = tk.Button(self, text="Calculate Total", command=calculate_total)
        calculate_button.pack(pady=5)

        total_label = tk.Label(self, text="Total: $0.00")
        total_label.pack(pady=5)

        b_button = tk.Button(self, text="Back", command = lambda : controller.show_frame(clogin))
        b_button.pack(pady=5)


        order_items = []
       

class page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="#333333")

        option_label=tk.Label(self, text="What do you want to do?",bg="#FF3399",fg="#FFFFFF",font=("Arial",30),width=25)
        option_label.grid(row=0,column=0,columnspan=2,pady=50)

        emp_button=tk.Button(self,text="View Employee Details",bg="#FF3399",fg="#FFFFFF",font=("Arial",16),command = lambda : controller.show_frame(vemp))
        emp_button.grid(row=1,column=0,columnspan=2,pady=10)

        addemp_button=tk.Button(self,text="Add Employee",bg="#FF3399",fg="#FFFFFF",font=("Arial",16),command = lambda : controller.show_frame(addempl))
        addemp_button.grid(row=2,column=0,columnspan=2,pady=10)

        order_button=tk.Button(self,text="View Order Details",bg="#FF3399",fg="#FFFFFF",font=("Arial",16),command = lambda : controller.show_frame(vorder))
        order_button.grid(row=3,column=0,columnspan=2,pady=10)

        items_button=tk.Button(self,text="Add Items",bg="#FF3399",fg="#FFFFFF",font=("Arial",16),command = lambda : controller.show_frame(additem))
        items_button.grid(row=4,column=0,columnspan=2,pady=10)

        ba_button=tk.Button(self,text="Back",bg="#FF3399",fg="#FFFFFF",font=("Arial",16),command = lambda : controller.show_frame(Page1))
        ba_button.grid(row=5,column=0,columnspan=2,pady=10)



class addempl(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="#333333")
        def addempl():
           
            employee_name = name_entry.get()
            employee_position = position_entry.get()
            employee_salary = salary_entry.get()

            if not employee_name or not employee_position:
                messagebox.showwarning("Error", "Please fill in all fields.")
                return

            try:
                
                query = "INSERT INTO rest_empl(name,position,salary )VALUES (%s, %s,%s)"
                data = (employee_name, employee_position,employee_salary)
                cursor.execute(query, data)
                db.commit()

                messagebox.showinfo("Success", "Employee added successfully!")

            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Error connecting to MySQL: {e}")

           


        tk.Label(self, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        name_entry = tk.Entry(self)
        name_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self, text="Position:").grid(row=1, column=0, padx=10, pady=10)
        position_entry = tk.Entry(self)
        position_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self, text="Salary:").grid(row=2, column=0, padx=10, pady=10)
        salary_entry = tk.Entry(self)
        salary_entry.grid(row=2, column=1, padx=10, pady=10)

        add_button = tk.Button(self, text="Add Employee",command=addempl)
        add_button.grid(row=4, column=0, columnspan=2, pady=10)

        back_button=tk.Button(self,text="Previous page",bg="#FF3399",fg="#FFFFFF",font=("Arial",16),command = lambda : controller.show_frame(page3))
        back_button.grid(row=7,column=2,columnspan=2,pady=30)


   
class vemp(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="#333333")
        cursor.execute("SELECT * FROM rest_empl")
        i=0

        e_label=tk.Label(self, text="List of Employees",bg="#FF3399",fg="#FFFFFF",font=("Arial",30),width=15)
        e_label.grid(row=0,column=0,columnspan=4,pady=50)
       
        for emp in cursor:
            for j in range(len(emp)):
                e = tk.Entry(self, width=20, fg='blue')
                e.grid(row=i+1, column=j)
                e.insert(tk.END, emp[j])
            i=i+1
        back_button=tk.Button(self,text="Previous page",bg="#FF3399",fg="#FFFFFF",font=("Arial",16),command = lambda : controller.show_frame(page3))
        back_button.grid(row=i+1,column=2,columnspan=2,pady=30)

        del_button=tk.Button(self, text="Delete Employee",bg="#FF3399",fg="#FFFFFF",font=("Arial",16),command = lambda : controller.show_frame(del_empl))
        del_button.grid(row=i+1,column=0,columnspan=2,pady=50)


class vorder(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="#333333")
        cursor.execute("SELECT * FROM item_order")
        i=1

        e_label=tk.Label(self, text="List of Orders",bg="#FF3399",fg="#FFFFFF",font=("Arial",25),width=12)
        e_label.grid(row=0,column=0,columnspan=6,pady=50)
        attri=["Order_Id","cust_name","Item_Id","Quantity","Total_Price","Timestamp"]
        for j in range(0,6):
            e = tk.Entry(self, width=20, fg='blue')
            e.grid(row=1, column=j)
            e.insert(tk.END, attri[j])
            
        for orde in cursor:
            for j in range(len(orde)):
                e = tk.Entry(self, width=20, fg='blue')
                e.grid(row=i+1, column=j)
                e.insert(tk.END, orde[j])
            i=i+1
        back_button=tk.Button(self,text="Previous page",bg="#FF3399",fg="#FFFFFF",font=("Arial",16),command = lambda : controller.show_frame(page3))
        back_button.grid(row=i+1,column=2,columnspan=2,pady=30)

class additem(tk.Frame):
    def __init__(self, parent, controller):
         tk.Frame.__init__(self, parent,bg="#333333")
         def additem():
           
            item_name = iname_entry.get()
            item_price = price_entry.get()

            if not item_name or not item_price:
                messagebox.showwarning("Error", "Please fill in all fields.")
                return

            try:
               
                query = "INSERT INTO menu (item_name,price )VALUES (%s, %s)"
                data = (item_name,item_price)
                cursor.execute(query, data)
                db.commit()

                messagebox.showinfo("Success", "Item added successfully!")

            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Error connecting to MySQL: {e}")

          

         tk.Label(self, text="Item Name:").grid(row=0, column=0, padx=10, pady=10)
         iname_entry = tk.Entry(self)
         iname_entry.grid(row=0, column=1, padx=10, pady=10)

         tk.Label(self, text="Price:").grid(row=1, column=0, padx=10, pady=10)
         price_entry = tk.Entry(self)
         price_entry.grid(row=1, column=1, padx=10, pady=10)


                   
         add_button = tk.Button(self, text="Add Item",command=additem)
         add_button.grid(row=3, column=0, columnspan=2, pady=10)

         back_button=tk.Button(self,text="Previous page",command = lambda : controller.show_frame(page3))
         back_button.grid(row=3,column=2,columnspan=2,pady=30)

class del_empl(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="#333333")
        def del_empl():
            del_id=del_entry.get();
            try:
                cursor.execute("delete from rest_empl where eid=%s",(del_id,))
                db.commit()

                messagebox.showinfo("Success", "Employee deleted successfully!")
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Error connecting to MySQL: {e}")

            

        tk.Label(self, text="enter eid to be deleted").grid(row=0, column=0, padx=10, pady=10)
        del_entry = tk.Entry(self)
        del_entry.grid(row=0, column=1, padx=10, pady=10)

        delete_button = tk.Button(self, text="delete Employee",bg="#FF3399",fg="#FFFFFF",font=("Arial",16),command=del_empl)
        delete_button.grid(row=4, column=0, columnspan=2, pady=10)

        back_button=tk.Button(self,text="Previous page",bg="#FF3399",fg="#FFFFFF",font=("Arial",16),command = lambda : controller.show_frame(vemp))
        back_button.grid(row=4,column=2,columnspan=2,pady=10)

# Driver Code
app = tkinterApp()
app.mainloop()

