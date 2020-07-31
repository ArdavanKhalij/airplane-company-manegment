#######################################################################################################################
#                                                     Libraries                                                       #
#######################################################################################################################
from tkinter import *
from tkinter import ttk
import requests
import socket
import os
import urllib
import json
#######################################################################################################################
#                                                  Global Variables                                                   #
#######################################################################################################################
#######################################################################################################################
#                                                       Pages                                                         #
#######################################################################################################################
class all() :

    def users(self):
        self.usersRoot = Tk()
        self.usersRoot.title("کاربر ها")
        self.usersRoot['bg'] = 'orange'
        space = Label(self.usersRoot, text=" ", bg='orange')
        space1 = Label(self.usersRoot, text=" ", bg='orange')
        space2 = Label(self.usersRoot, text=" ", bg='orange')
        space3 = Label(self.usersRoot, text=" ", bg='orange')
        space4 = Label(self.usersRoot, text=" ", bg='orange')
        space5 = Label(self.usersRoot, text=" ", bg='orange')
        title = Label(self.usersRoot, text="کاربر ها", font=('IRANSans', '22'), fg="black", bg='orange')
        cols = ('سطح دسترسی', 'رمز عبور', 'نام کاربری')
        self.listBoxUser = ttk.Treeview(self.usersRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=self.listBoxUser.yview)
        self.listBoxUser.configure(yscrollcommand=vsb.set)
        self.listBoxUser.column("0", width=450, anchor="c")
        self.listBoxUser.column("1", width=450, anchor="c")
        self.listBoxUser.column("2", width=450, anchor="c")
        self.listBoxUser.config(height=20)
        for col in cols:
            self.listBoxUser.heading(col, text=col)
        url = 'http://www.rownaghsh.ir/req.php'
        data = {'table': 'users',
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
        }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        l = json.loads(r.text)
        print(r.text)
        print(data)
        for i in range(0, len(l)):
            if l[i]['levele']=='0':
                x='مدیر اصلی'
            elif l[i]['levele']=='1':
                x='مدیر'
            elif l[i]['levele']=='2':
                x='مشاهده کننده'
            else:
                x='سرویس جدید'
            self.listBoxUser.insert("", "end", values=(
                str(x),
                str(l[i]['pass']),
                str(l[i]['name'])
            ))
        sabt = Button(self.usersRoot, text="ثبت کاربر", font=('IRANSans', '13'), fg='white', bg='blue', command=self.sabtUser)
        sabt.config(height=1, width=20)
        delete = Button(self.usersRoot, text="حذف", font=('IRANSans', '13'), fg='white', bg='blue', command=self.deleteUser)
        delete.config(height=1, width=20)
        edit = Button(self.usersRoot, text="ویرایش", font=('IRANSans', '13'), fg='white', bg='blue', command=self.editUser)
        edit.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        self.listBoxUser.pack()
        space2.pack()
        sabt.pack()
        delete.pack()
        edit.pack()
        space3.pack()

    def editUser(self):
        self.listBoxUser.bind('<Button-1>', self.listBoxUser)
        curItem = self.listBoxUser.focus()
        k = self.listBoxUser.item(curItem)
        self.sabteUserPageRoot = Tk()
        self.sabteUserPageRoot.title("ویرایش هواپیما")
        self.sabteUserPageRoot.configure(bg='orange')
        title = Label(self.sabteUserPageRoot, text="ویرایش هواپیما", font=('IRANSans', '22'), bg='orange')
        space = Label(self.sabteUserPageRoot, text=" ", bg='orange')
        space1 = Label(self.sabteUserPageRoot, text=" ", bg='orange')
        space2 = Label(self.sabteUserPageRoot, text=" ", bg='orange')
        space3 = Label(self.sabteUserPageRoot, text=" ", bg='orange')
        space4 = Label(self.sabteUserPageRoot, text=" ", bg='orange')
        space5 = Label(self.sabteUserPageRoot, text=" ", bg='orange')
        space6 = Label(self.sabteUserPageRoot, text=" ", bg='orange')
        self.usern = Entry(self.sabteUserPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.usern.insert(0, k['values'][2])
        self.usern.config(state=DISABLED)
        self.passwd = Entry(self.sabteUserPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.passwd.insert(0, k['values'][1])
        sabt = Button(self.sabteUserPageRoot, text="ثبت", bg='blue', fg='white', font=('IRANSans', '20'),
                      command=self.editUser2)
        self.userclass = ttk.Combobox(self.sabteUserPageRoot, width=69, justify='right', font=('IRANSans', 16))
        self.userclass['values'] = ('مدریت اصلی',
                                    'مدریت',
                                    'مشاهده کننده',
                                    'دسترسی جدید')
        self.userclass.current(2)
        sabt.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        space2.pack()
        self.usern.pack()
        self.passwd.pack()
        self.userclass.pack()
        space3.pack()
        sabt.pack()
        space4.pack()

    def editUser2(self):
        if self.userclass.get() == 'مدریت اصلی':
            x = 0
        elif self.userclass.get() == 'مدریت':
            x = 1
        elif self.userclass.get() == 'مشاهده کننده':
            x = 2
        else:
            x = 3
        url = 'http://www.rownaghsh.ir/upd.php'
        data2 = {
            "add_users": self.usern.get(),
            "add_pass": self.passwd.get(),
            "levele": x
        }
        data = {"table": "users",
                "key": "name",
                "value": self.usern.get(),
                "columns": data2,
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        print(r.text)
        self.sabteUserPageRoot.destroy()
        self.usersRoot.destroy()
        self.users()

    def deleteUser(self):
        self.listBoxUser.bind('<Button-1>', self.listBoxUser)
        curItem = self.listBoxUser.focus()
        k = self.listBoxUser.item(curItem)
        url = 'http://www.rownaghsh.ir/del.php'
        data = {
            "table": "users",
            "key": "name",
            "value": str(k['values'][2]),
            "name_for_user": MyUsername,
            "password_for_user": MyPassword
        }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        print(r.text)
        self.usersRoot.destroy()
        self.users()

    def sabtUser(self):
        self.sabteUserPageRoot = Tk()
        self.sabteUserPageRoot.title("ثبت هواپیما")
        self.sabteUserPageRoot.configure(bg='orange')
        title = Label(self.sabteUserPageRoot, text="ثبت هواپیما", font=('IRANSans', '22'), bg='orange')
        space = Label(self.sabteUserPageRoot, text=" ", bg='orange')
        space1 = Label(self.sabteUserPageRoot, text=" ", bg='orange')
        space2 = Label(self.sabteUserPageRoot, text=" ", bg='orange')
        space3 = Label(self.sabteUserPageRoot, text=" ", bg='orange')
        space4 = Label(self.sabteUserPageRoot, text=" ", bg='orange')
        space5 = Label(self.sabteUserPageRoot, text=" ", bg='orange')
        space6 = Label(self.sabteUserPageRoot, text=" ", bg='orange')
        self.usern = Entry(self.sabteUserPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.usern.insert(0, "نام کاربری")
        self.passwd = Entry(self.sabteUserPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.passwd.insert(0, "رمز عبور")
        sabt = Button(self.sabteUserPageRoot, text="ثبت", bg='blue', fg='white', font=('IRANSans', '20'),
                      command=self.sabtUser2)
        self.userclass = ttk.Combobox(self.sabteUserPageRoot, width=69, justify='right', font=('IRANSans', 16))
        self.userclass['values'] = ('مدریت اصلی',
                                  'مدریت',
                                  'مشاهده کننده',
                                  'دسترسی جدید')
        self.userclass.current(2)
        sabt.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        space2.pack()
        self.usern.pack()
        self.passwd.pack()
        self.userclass.pack()
        space3.pack()
        sabt.pack()
        space4.pack()

    def sabtUser2(self):
        if self.userclass.get()=='مدریت اصلی':
            x=0
        elif self.userclass.get()=='مدریت':
            x=1
        elif self.userclass.get()=='مشاهده کننده':
            x=2
        else:
            x=3
        url='http://www.rownaghsh.ir/add_user.php'
        data={
            "add_users":self.usern.get(),
            "add_pass":self.passwd.get(),
            "levele":x,
            "name":MyUsername,
            "password":MyPassword
        }
        data1=json.dumps(data)
        r=requests.post(url, data1)
        print(r.text)
        print(MyUsername)
        print(MyPassword)
        self.sabteUserPageRoot.destroy()
        self.usersRoot.destroy()
        self.users()

    def airplansRootFunc(self):
        self.airplansRoot = Tk()
        self.airplansRoot.title("هواپیما ها")
        self.airplansRoot['bg'] = 'orange'
        space = Label(self.airplansRoot, text=" ", bg='orange')
        space1 = Label(self.airplansRoot, text=" ", bg='orange')
        space2 = Label(self.airplansRoot, text=" ", bg='orange')
        space3 = Label(self.airplansRoot, text=" ", bg='orange')
        space4 = Label(self.airplansRoot, text=" ", bg='orange')
        space5 = Label(self.airplansRoot, text=" ", bg='orange')
        title = Label(self.airplansRoot, text="هواپیما ها", font=('IRANSans', '22'), fg="black", bg='orange')
        cols = ('ظرفیت بار' ,'تعداد Economy class','تعداد Business class', 'تعداد First class', 'مدل', 'شماره هواپیما')
        self.listBoxAirplane = ttk.Treeview(self.airplansRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=self.listBoxAirplane.yview)
        self.listBoxAirplane.configure(yscrollcommand=vsb.set)
        self.listBoxAirplane.column("0", width=220, anchor="c")
        self.listBoxAirplane.column("1", width=220, anchor="c")
        self.listBoxAirplane.column("2", width=220, anchor="c")
        self.listBoxAirplane.column("3", width=220, anchor="c")
        self.listBoxAirplane.column("4", width=220, anchor="c")
        self.listBoxAirplane.column("5", width=220, anchor="c")
        self.listBoxAirplane.config(height=20)
        for col in cols:
            self.listBoxAirplane.heading(col, text=col)
        url = 'http://www.rownaghsh.ir/req_airplanes.php'
        data={'table':'airplane',"name_for_user":MyUsername,
"password_for_user":MyPassword}
        data1=json.dumps(data)
        r=requests.post(url, data=data1)
        l=json.loads(r.text)
        for i in range(0, len(l)):
            self.listBoxAirplane.insert("", "end", values=(
                str(l[i]['bar']),
                str(l[i]['economi']),
                str(l[i]['bisness']),
                str(l[i]['first_class']),
                str(l[i]['model']),
                str(l[i]['num_airplane'])
            ))
        sabt = Button(self.airplansRoot, text="ثبت هواپیما", font=('IRANSans', '13'), fg='white', bg='blue', command=self.sabteAirplane)
        sabt.config(height=1, width=20)
        delete = Button(self.airplansRoot, text="حذف", font=('IRANSans', '13'), fg='white', bg='blue', command=self.deleteAirplane)
        delete.config(height=1, width=20)
        edit = Button(self.airplansRoot, text="ثبت هواپیما از مدل موجود", font=('IRANSans', '13'), fg='white', bg='blue', command=self.sabteAirplane3)
        edit.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        self.listBoxAirplane.pack()
        space2.pack()
        sabt.pack()
        edit.pack()
        delete.pack()
        space3.pack()

    def deleteAirplane(self):
        self.listBoxAirplane.bind('<Button-1>', self.listBoxAirplane)
        curItem = self.listBoxAirplane.focus()
        k = self.listBoxAirplane.item(curItem)
        url='http://www.rownaghsh.ir/del.php'
        data = {
            "table":"airplanes",
            "key":"num_airplane",
            "value":str(k['values'][5]),
            "name_for_user": MyUsername,
            "password_for_user": MyPassword
        }
        data1=json.dumps(data)
        r=requests.post(url, data=data1)
        data2 = {
            "table": "airplane",
            "key": "model",
            "value": str(k['values'][4]),
            "name_for_user": MyUsername,
            "password_for_user": MyPassword
        }
        data3 = json.dumps(data2)
        r = requests.post(url, data=data3)
        self.airplansRoot.destroy()
        self.airplansRootFunc()

    def sabteAirplane(self):
        self.sabteAirplanePageRoot = Tk()
        self.sabteAirplanePageRoot.title("ثبت هواپیما")
        self.sabteAirplanePageRoot.configure(bg='orange')
        title = Label(self.sabteAirplanePageRoot, text="ثبت هواپیما", font=('IRANSans', '22'), bg='orange')
        space = Label(self.sabteAirplanePageRoot, text=" ", bg='orange')
        space1 = Label(self.sabteAirplanePageRoot, text=" ", bg='orange')
        space2 = Label(self.sabteAirplanePageRoot, text=" ", bg='orange')
        space3 = Label(self.sabteAirplanePageRoot, text=" ", bg='orange')
        space4 = Label(self.sabteAirplanePageRoot, text=" ", bg='orange')
        space5 = Label(self.sabteAirplanePageRoot, text=" ", bg='orange')
        space6 = Label(self.sabteAirplanePageRoot, text=" ", bg='orange')
        self.number = Entry(self.sabteAirplanePageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.number.insert(0, "شماره هوایما")
        self.model = Entry(self.sabteAirplanePageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.model.insert(0, "مدل هواپیما")
        self.tedadFirstClass = Entry(self.sabteAirplanePageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.tedadFirstClass.insert(0, "تعداد مسافران Fist class")
        self.tedadBusinessClass = Entry(self.sabteAirplanePageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.tedadBusinessClass.insert(0, "تعداد مسافران Business class")
        self.tedadEconomyClass = Entry(self.sabteAirplanePageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.tedadEconomyClass.insert(0, "تعداد مسافران Economy class")
        self.bar = Entry(self.sabteAirplanePageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.bar.insert(0, "ظرفیت بار")
        self.priceFirstClass = Entry(self.sabteAirplanePageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.priceFirstClass.insert(0, "قیمت First class")
        self.priceBusinessClass = Entry(self.sabteAirplanePageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.priceBusinessClass.insert(0, "قیمت Business class")
        self.priceEconomyClass = Entry(self.sabteAirplanePageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.priceEconomyClass.insert(0, "قیمت Economy class")
        sabt = Button(self.sabteAirplanePageRoot, text="ثبت", bg='blue', fg='white', font=('IRANSans', '20'), command=self.sabteAirplane2)
        sabt.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        space2.pack()
        self.number.pack()
        self.model.pack()
        self.tedadFirstClass.pack()
        self.tedadBusinessClass.pack()
        self.tedadEconomyClass.pack()
        self.bar.pack()
        # self.priceFirstClass.pack()
        # self.priceBusinessClass.pack()
        # self.priceEconomyClass.pack()
        space3.pack()
        sabt.pack()
        space4.pack()

    def sabteAirplane2(self):
        url='http://www.rownaghsh.ir/airplane.php'
        data={"num_airplanes":int(self.number.get()),
              "model":str(self.model.get()),
              "first_class":int(self.tedadFirstClass.get()),
              "bisness":int(self.tedadBusinessClass.get()),
              "bar":int(self.bar.get()),
              "economi":int(self.tedadEconomyClass.get()),
              "name_for_user": MyUsername,
              "password_for_user": MyPassword
              }
        data1=json.dumps(data)
        r=requests.post(url, data=data1)
        self.sabteAirplanePageRoot.destroy()
        self.airplansRoot.destroy()
        self.airplansRootFunc()

    def sabteAirplane3(self):
        self.sabteAirplane3PageRoot = Tk()
        self.sabteAirplane3PageRoot.title("ثبت هواپیما")
        self.sabteAirplane3PageRoot.configure(bg='orange')
        title = Label(self.sabteAirplane3PageRoot, text="ثبت هواپیما", font=('IRANSans', '22'), bg='orange')
        space = Label(self.sabteAirplane3PageRoot, text=" ", bg='orange')
        space1 = Label(self.sabteAirplane3PageRoot, text=" ", bg='orange')
        space2 = Label(self.sabteAirplane3PageRoot, text=" ", bg='orange')
        space3 = Label(self.sabteAirplane3PageRoot, text=" ", bg='orange')
        space4 = Label(self.sabteAirplane3PageRoot, text=" ", bg='orange')
        space5 = Label(self.sabteAirplane3PageRoot, text=" ", bg='orange')
        space6 = Label(self.sabteAirplane3PageRoot, text=" ", bg='orange')
        self.number2 = Entry(self.sabteAirplane3PageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.number2.insert(0, "شماره هوایما")
        self.model2 = Entry(self.sabteAirplane3PageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.model2.insert(0, "مدل هواپیما")
        sabt = Button(self.sabteAirplane3PageRoot, text="ثبت", bg='blue', fg='white', font=('IRANSans', '20'),
                      command=self.sabteAirplane4)
        sabt.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        space2.pack()
        self.number2.pack()
        self.model2.pack()
        space3.pack()
        sabt.pack()
        space4.pack()

    def sabteAirplane4(self):
        url = 'http://www.rownaghsh.ir/airplanes.php'
        data = {"num_airplane": int(self.number2.get()),
                "model": str(self.model2.get()),
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        self.sabteAirplane3PageRoot.destroy()
        self.airplansRoot.destroy()
        self.airplansRootFunc()

    def PilotRootFunc(self):
        self.PilotRoot = Tk()
        self.PilotRoot.title("خلبان ها")
        self.PilotRoot['bg'] = 'orange'
        space = Label(self.PilotRoot, text=" ", bg='orange')
        space1 = Label(self.PilotRoot, text=" ", bg='orange')
        space2 = Label(self.PilotRoot, text=" ", bg='orange')
        space3 = Label(self.PilotRoot, text=" ", bg='orange')
        space4 = Label(self.PilotRoot, text=" ", bg='orange')
        space5 = Label(self.PilotRoot, text=" ", bg='orange')
        title = Label(self.PilotRoot, text="خلبان ها", font=('IRANSans', '22'), bg='orange')
        cols = (
        'تلفن 3', 'نام آشنا 3', 'تلفن 2', 'نام آشنا 2', 'تلفن 1', 'نام آشنا1', 'تعداد فرزندان', 'شماره تلفن همسر',
        'کد ملی همسر', 'نام همسر', 'تاریخ تولد', 'شماره تلفن', 'شماره خلبان', 'کد ملی', 'جنسیت', 'نام خانوادگی',
        'نام')
        self.listBoxPilot = ttk.Treeview(self.PilotRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=self.listBoxPilot.yview)
        self.listBoxPilot.configure(yscrollcommand=vsb.set)
        self.listBoxPilot.column("0", width=80, anchor="c")
        self.listBoxPilot.column("1", width=80, anchor="c")
        self.listBoxPilot.column("2", width=80, anchor="c")
        self.listBoxPilot.column("3", width=80, anchor="c")
        self.listBoxPilot.column("4", width=80, anchor="c")
        self.listBoxPilot.column("5", width=80, anchor="c")
        self.listBoxPilot.column("6", width=80, anchor="c")
        self.listBoxPilot.column("7", width=80, anchor="c")
        self.listBoxPilot.column("8", width=80, anchor="c")
        self.listBoxPilot.column("9", width=80, anchor="c")
        self.listBoxPilot.column("10", width=80, anchor="c")
        self.listBoxPilot.column("11", width=80, anchor="c")
        self.listBoxPilot.column("12", width=80, anchor="c")
        self.listBoxPilot.column("13", width=80, anchor="c")
        self.listBoxPilot.column("14", width=80, anchor="c")
        self.listBoxPilot.column("15", width=80, anchor="c")
        self.listBoxPilot.column("16", width=80, anchor="c")
        self.listBoxPilot.config(height=20)
        for col in cols:
            self.listBoxPilot.heading(col, text=col)
        url = 'http://www.rownaghsh.ir/req_personel.php'
        data = {'table': 'pilot',
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        l = json.loads(r.text)
        for i in range(0, len(l)):
            if l[i]['gender']=='1':
                x='مرد'
            else:
                x='زن'
            self.listBoxPilot.insert("", "end", values=(
                str(l[i]['phon3']),
                str(l[i]['fname3']),
                str(l[i]['phon2']),
                str(l[i]['fname2']),
                str(l[i]['phon1']),
                str(l[i]['fname1']),
                str(l[i]['child']),
                str(l[i]['partner_phone']),
                str(l[i]['partner_mellicode']),
                str(l[i]['partner']),
                str(l[i]['birthdate']),
                str(l[i]['phone']),
                str(l[i]['num_pilot']),
                str(l[i]['mellicode']),
                x,
                str(l[i]['lname']),
                str(l[i]['fname'])
            ))
        sabt = Button(self.PilotRoot, text="ثبت خلبان", font=('IRANSans', '13'), fg='white', bg='blue',
                      command=self.sabtePilot)
        sabt.config(height=1, width=20)
        delete = Button(self.PilotRoot, text="حذف", font=('IRANSans', '13'), fg='white', bg='blue', command=self.deletePilot)
        delete.config(height=1, width=20)
        edit = Button(self.PilotRoot, text="ویرایش", font=('IRANSans', '13'), fg='white', bg='blue', command=self.editPilot)
        edit.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        self.listBoxPilot.pack()
        space2.pack()
        sabt.pack()
        edit.pack()
        delete.pack()
        space3.pack()

    def editPilot(self):
        self.listBoxPilot.bind('<Button-1>', self.listBoxPilot)
        curItem = self.listBoxPilot.focus()
        k = self.listBoxPilot.item(curItem)
        self.sabtepilotPageRoot = Tk()
        self.sabtepilotPageRoot.title("ویرایش خلبان")
        self.sabtepilotPageRoot.configure(bg='orange')
        title = Label(self.sabtepilotPageRoot, text="ویرایش خلبان", font=('IRANSans', '22'), bg='orange')
        space = Label(self.sabtepilotPageRoot, text=" ", bg='orange')
        space1 = Label(self.sabtepilotPageRoot, text=" ", bg='orange')
        space2 = Label(self.sabtepilotPageRoot, text=" ", bg='orange')
        space3 = Label(self.sabtepilotPageRoot, text=" ", bg='orange')
        space4 = Label(self.sabtepilotPageRoot, text=" ", bg='orange')
        space5 = Label(self.sabtepilotPageRoot, text=" ", bg='orange')
        space6 = Label(self.sabtepilotPageRoot, text=" ", bg='orange')
        self.pname = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pname.insert(0, k['values'][16])
        self.plname = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.plname.insert(0, k['values'][15])
        self.pgender = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pgender.insert(0, k['values'][14])
        self.pmellicode = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pmellicode.insert(0, k['values'][13])
        self.pcono = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pcono.insert(0, k['values'][12])
        self.pcono.config(state=DISABLED)
        self.pphno = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pphno.insert(0, k['values'][11])
        self.pbd = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pbd.insert(0, k['values'][10])
        self.pwn = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pwn.insert(0, k['values'][9])
        self.pmcw = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pmcw.insert(0, k['values'][8])
        self.pwphno = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pwphno.insert(0, k['values'][7])
        self.pcn = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pcn.insert(0, k['values'][6])
        self.pf1 = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pf1.insert(0, k['values'][5])
        self.pfph1 = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pfph1.insert(0, k['values'][4])
        self.pf2 = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pf2.insert(0, k['values'][3])
        self.pfph2 = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pfph2.insert(0, k['values'][2])
        self.pf3 = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pf3.insert(0, k['values'][1])
        self.pfph3 = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pfph3.insert(0, k['values'][0])
        sabt = Button(self.sabtepilotPageRoot, text="ثبت", bg='blue', fg='white', font=('IRANSans', '15'),
                      command=self.editPilot2)
        sabt.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        self.pname.pack()
        self.plname.pack()
        self.pgender.pack()
        self.pmellicode.pack()
        self.pcono.pack()
        self.pphno.pack()
        self.pbd.pack()
        self.pwn.pack()
        self.pmcw.pack()
        self.pwphno.pack()
        self.pcn.pack()
        self.pf1.pack()
        self.pfph1.pack()
        self.pf2.pack()
        self.pfph2.pack()
        self.pf3.pack()
        self.pfph3.pack()
        space3.pack()
        sabt.pack()
        space4.pack()

    def editPilot2(self):
        url = 'http://www.rownaghsh.ir/upd.php'
        if self.pgender.get() == "مرد":
            x = 1
        else:
            x = 0
        data2= {"fname": str(self.pname.get()),
                "lname": str(self.plname.get()),
                "gender": x,
                "mellicode": str(self.pmellicode.get()),
                "num_pilot": str(self.pcono.get()),
                "phone": str(self.pphno.get()),
                "birthdate": str(self.pbd.get()),
                "partner": str(self.pwn.get()),
                "partner_mellicode": str(self.pmcw.get()),
                "partner_phone": str(self.pwphno.get()),
                "child": int(self.pcn.get())
                }
        data3 = {
            "fname1": str(self.pf1.get()),
                "phon1": str(self.pfph1.get()),
                "fname2": str(self.pf2.get()),
                "phon2": str(self.pfph2.get()),
                "fname3": str(self.pf3.get()),
                "phon3": str(self.pfph3.get())
        }
        data = {"table": "pilot",
                "key": "num_pilot",
                "value": self.pcono.get(),
                "columns": data2,
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        data4 = {
            "table": "acquaintances_pilot",
            "key": "code_personel",
            "value": self.pcono.get(),
            "columns": data3,
            "name_for_user": MyUsername,
            "password_for_user": MyPassword
        }
        data5 = json.dumps(data4)
        r = requests.post(url, data=data1)
        r = requests.post(url, data=data5)
        print(r.text)
        print(data1)
        self.sabtepilotPageRoot.destroy()
        self.PilotRoot.destroy()
        self.PilotRootFunc()

    def deletePilot(self):
        self.listBoxPilot.bind('<Button-1>', self.listBoxPilot)
        curItem = self.listBoxPilot.focus()
        k = self.listBoxPilot.item(curItem)
        url = 'http://www.rownaghsh.ir/del.php'
        data = {
            "table": "pilot",
            "key": "num_pilot",
            "value": str(k['values'][12]),
            "name_for_user": MyUsername,
            "password_for_user": MyPassword
        }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        self.PilotRoot.destroy()
        self.PilotRootFunc()

    def sabtePilot(self):
        self.sabtepilotPageRoot = Tk()
        self.sabtepilotPageRoot.title("ثبت خلبان")
        self.sabtepilotPageRoot.configure(bg='orange')
        title = Label(self.sabtepilotPageRoot, text="ثبت خلبان", font=('IRANSans', '22'), bg='orange')
        space = Label(self.sabtepilotPageRoot, text=" ", bg='orange')
        space1 = Label(self.sabtepilotPageRoot, text=" ", bg='orange')
        space2 = Label(self.sabtepilotPageRoot, text=" ", bg='orange')
        space3 = Label(self.sabtepilotPageRoot, text=" ", bg='orange')
        space4 = Label(self.sabtepilotPageRoot, text=" ", bg='orange')
        space5 = Label(self.sabtepilotPageRoot, text=" ", bg='orange')
        space6 = Label(self.sabtepilotPageRoot, text=" ", bg='orange')
        self.pname = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pname.insert(0, "نام")
        self.plname = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.plname.insert(0, "نام خانوادگی")
        self.pgender = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pgender.insert(0, "جنسیت")
        self.pmellicode = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pmellicode.insert(0, "کدملی")
        self.pcono = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pcono.insert(0, "شماره خلبان")
        self.pphno = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pphno.insert(0, "شماره تلفن")
        self.pbd = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pbd.insert(0, "تاریخ تولد")
        self.pwn = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pwn.insert(0, "نام همسر")
        self.pmcw = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pmcw.insert(0, "کد ملی همسر")
        self.pwphno = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pwphno.insert(0, "شماره تلفن همسر")
        self.pcn = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pcn.insert(0, "تعداد فرزندان")
        self.pf1 = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pf1.insert(0, "نام آشنا 1")
        self.pfph1 = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pfph1.insert(0, "تلفن 1")
        self.pf2 = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pf2.insert(0, "نام آشنا 2")
        self.pfph2 = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pfph2.insert(0, "تلفن 2")
        self.pf3 = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pf3.insert(0, "نام آشنا 3")
        self.pfph3 = Entry(self.sabtepilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.pfph3.insert(0, "تلفن 3")
        sabt = Button(self.sabtepilotPageRoot, text="ثبت", bg='blue', fg='white', font=('IRANSans', '15'),
                      command=self.sabtePilot2)
        sabt.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        # space2.pack()
        self.pname.pack()
        self.plname.pack()
        self.pgender.pack()
        self.pmellicode.pack()
        self.pcono.pack()
        self.pphno.pack()
        self.pbd.pack()
        self.pwn.pack()
        self.pmcw.pack()
        self.pwphno.pack()
        self.pcn.pack()
        self.pf1.pack()
        self.pfph1.pack()
        self.pf2.pack()
        self.pfph2.pack()
        self.pf3.pack()
        self.pfph3.pack()
        space3.pack()
        sabt.pack()
        space4.pack()

    def sabtePilot2(self):
        url = 'http://www.rownaghsh.ir/pilot.php'
        if self.pgender.get()=="مرد":
            x=1
        else:
            x=0
        data =  {"fname": str(self.pname.get()),
                "lname": str(self.plname.get()),
                "gender": x,
                "mellicode": str(self.pmellicode.get()),
                "num_pilot": str(self.pcono.get()),
                "phone": str(self.pphno.get()),
                "birthdate": str(self.pbd.get()),
                "partner": str(self.pwn.get()),
                "partner_mellicode": str(self.pmcw.get()),
                "partner_phone": str(self.pwphno.get()),
                "child": int(self.pcn.get()),
                "fname1": str(self.pf1.get()),
                "phon1": str(self.pfph1.get()),
                "fname2": str(self.pf2.get()),
                "phon2": str(self.pfph2.get()),
                "fname3": str(self.pf3.get()),
                "phon3": str(self.pfph3.get()),
                 "name_for_user": MyUsername,
                 "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        print(r.text)
        print(data1)
        self.sabtepilotPageRoot.destroy()
        self.PilotRoot.destroy()
        self.PilotRootFunc()

    def CoPilotRootFunc(self):
        self.CoPilotRoot = Tk()
        self.CoPilotRoot.title("کمک خلبان ها")
        self.CoPilotRoot['bg'] = 'orange'
        space = Label(self.CoPilotRoot, text=" ", bg='orange')
        space1 = Label(self.CoPilotRoot, text=" ", bg='orange')
        space2 = Label(self.CoPilotRoot, text=" ", bg='orange')
        space3 = Label(self.CoPilotRoot, text=" ", bg='orange')
        space4 = Label(self.CoPilotRoot, text=" ", bg='orange')
        space5 = Label(self.CoPilotRoot, text=" ", bg='orange')
        title = Label(self.CoPilotRoot, text="کمک خلبان ها", font=('IRANSans', '22'), bg='orange')
        cols = ('تلفن 3','نام آشنا 3','تلفن 2','نام آشنا 2','تلفن 1','نام آشنا1','تعداد فرزندان','شماره تلفن همسر','کد ملی همسر','نام همسر','تاریخ تولد','شماره تلفن' ,'شماره کمک خلبان','کد ملی', 'جنسیت', 'نام خانوادگی', 'نام')
        self.listBoxCopilot = ttk.Treeview(self.CoPilotRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=self.listBoxCopilot.yview)
        self.listBoxCopilot.configure(yscrollcommand=vsb.set)
        self.listBoxCopilot.column("0", width=80, anchor="c")
        self.listBoxCopilot.column("1", width=80, anchor="c")
        self.listBoxCopilot.column("2", width=80, anchor="c")
        self.listBoxCopilot.column("3", width=80, anchor="c")
        self.listBoxCopilot.column("4", width=80, anchor="c")
        self.listBoxCopilot.column("5", width=80, anchor="c")
        self.listBoxCopilot.column("6", width=80, anchor="c")
        self.listBoxCopilot.column("7", width=80, anchor="c")
        self.listBoxCopilot.column("8", width=80, anchor="c")
        self.listBoxCopilot.column("9", width=80, anchor="c")
        self.listBoxCopilot.column("10", width=80, anchor="c")
        self.listBoxCopilot.column("11", width=80, anchor="c")
        self.listBoxCopilot.column("12", width=80, anchor="c")
        self.listBoxCopilot.column("13", width=80, anchor="c")
        self.listBoxCopilot.column("14", width=80, anchor="c")
        self.listBoxCopilot.column("15", width=80, anchor="c")
        self.listBoxCopilot.column("16", width=80, anchor="c")
        self.listBoxCopilot.config(height=20)
        for col in cols:
            self.listBoxCopilot.heading(col, text=col)
        url = 'http://www.rownaghsh.ir/req_personel.php'
        data = {'table': 'co_pilot',
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        l=json.loads(r.text)
        for i in range(0, len(l)):
            if l[i]['gender'] == '1':
                x = 'مرد'
            else:
                x = 'زن'
            self.listBoxCopilot.insert("", "end", values=(
                str(l[i]['phon3']),
                str(l[i]['fname3']),
                str(l[i]['phon2']),
                str(l[i]['fname2']),
                str(l[i]['phon1']),
                str(l[i]['fname1']),
                str(l[i]['child']),
                str(l[i]['partner_phone']),
                str(l[i]['partner_mellicode']),
                str(l[i]['partner']),
                str(l[i]['birthdate']),
                str(l[i]['phone']),
                str(l[i]['num_copilot']),
                str(l[i]['mellicode']),
                x,
                str(l[i]['lname']),
                str(l[i]['fname'])
            ))
        sabt = Button(self.CoPilotRoot, text="ثبت کمک خلبان", font=('IRANSans', '13'), fg='white', bg='blue', command=self.sabteCopilot)
        sabt.config(height=1, width=20)
        delete = Button(self.CoPilotRoot, text="حذف", font=('IRANSans', '13'), fg='white', bg='blue', command=self.deleteCopilot)
        delete.config(height=1, width=20)
        edit = Button(self.CoPilotRoot, text="ویرایش", font=('IRANSans', '13'), fg='white', bg='blue', command=self.editCopilot)
        edit.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        self.listBoxCopilot.pack()
        space2.pack()
        sabt.pack()
        edit.pack()
        delete.pack()
        space3.pack()

    def editCopilot(self):
        self.listBoxCopilot.bind('<Button-1>', self.listBoxCopilot)
        curItem = self.listBoxCopilot.focus()
        k = self.listBoxCopilot.item(curItem)
        self.sabteCopilotPageRoot = Tk()
        self.sabteCopilotPageRoot.title("ویرایش کمک خلبان")
        self.sabteCopilotPageRoot.configure(bg='orange')
        title = Label(self.sabteCopilotPageRoot, text="ویرایش کمک خلبان", font=('IRANSans', '22'), bg='orange')
        space = Label(self.sabteCopilotPageRoot, text=" ", bg='orange')
        space1 = Label(self.sabteCopilotPageRoot, text=" ", bg='orange')
        space2 = Label(self.sabteCopilotPageRoot, text=" ", bg='orange')
        space3 = Label(self.sabteCopilotPageRoot, text=" ", bg='orange')
        space4 = Label(self.sabteCopilotPageRoot, text=" ", bg='orange')
        space5 = Label(self.sabteCopilotPageRoot, text=" ", bg='orange')
        space6 = Label(self.sabteCopilotPageRoot, text=" ", bg='orange')
        self.name = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.name.insert(0, k['values'][16])
        self.lname = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.lname.insert(0, k['values'][15])
        self.gender = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.gender.insert(0, k['values'][14])
        self.mellicode = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.mellicode.insert(0, k['values'][13])
        self.cono = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.cono.insert(0, k['values'][12])
        self.cono.config(state=DISABLED)
        self.phno = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.phno.insert(0, k['values'][11])
        self.bd = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.bd.insert(0, k['values'][10])
        self.wn = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.wn.insert(0, k['values'][9])
        self.mcw = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.mcw.insert(0, k['values'][8])
        self.wphno = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.wphno.insert(0, k['values'][7])
        self.cn = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.cn.insert(0, k['values'][6])
        self.f1 = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.f1.insert(0, k['values'][5])
        self.fph1 = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fph1.insert(0, k['values'][4])
        self.f2 = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.f2.insert(0, k['values'][3])
        self.fph2 = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fph2.insert(0, k['values'][2])
        self.f3 = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.f3.insert(0, k['values'][1])
        self.fph3 = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fph3.insert(0, k['values'][0])
        sabt = Button(self.sabteCopilotPageRoot, text="ثبت", bg='blue', fg='white', font=('IRANSans', '15'),
                      command=self.editCopilot2)
        sabt.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        self.name.pack()
        self.lname.pack()
        self.gender.pack()
        self.mellicode.pack()
        self.cono.pack()
        self.phno.pack()
        self.bd.pack()
        self.wn.pack()
        self.mcw.pack()
        self.wphno.pack()
        self.cn.pack()
        self.f1.pack()
        self.fph1.pack()
        self.f2.pack()
        self.fph2.pack()
        self.f3.pack()
        self.fph3.pack()
        space3.pack()
        sabt.pack()
        space4.pack()

    def editCopilot2(self):
        url = 'http://www.rownaghsh.ir/upd.php'
        if self.gender.get() == "مرد":
            x = 1
        else:
            x = 0
        data2 = {"fname": str(self.name.get()),
                "lname": str(self.lname.get()),
                "gender": x,
                "mellicode": str(self.mellicode.get()),
                "num_copilot": str(self.cono.get()),
                "phone": str(self.phno.get()),
                "birthdate": str(self.bd.get()),
                "partner": str(self.wn.get()),
                "partner_mellicode": str(self.mcw.get()),
                "partner_phone": str(self.wphno.get()),
                "child": int(self.cn.get()),
                }
        data3 = {
            "fname1": str(self.f1.get()),
                "phon1": str(self.fph1.get()),
                "fname2": str(self.f2.get()),
                "phon2": str(self.fph2.get()),
                "fname3": str(self.f3.get()),
                "phon3": str(self.fph3.get())
        }
        data = {"table": "co_pilot",
                "key": "num_copilot",
                "value": self.cono.get(),
                "columns": data2,
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        data4 = {
            "table": "acquaintances_co_pilot",
            "key": "code_personel",
            "value": self.cono.get(),
            "columns": data3,
            "name_for_user": MyUsername,
            "password_for_user": MyPassword
        }
        data5 = json.dumps(data4)
        r = requests.post(url, data=data1)
        r = requests.post(url, data=data5)
        print(r.text)
        print(data1)
        self.sabteCopilotPageRoot.destroy()
        self.CoPilotRoot.destroy()
        self.CoPilotRootFunc()

    def deleteCopilot(self):
        self.listBoxCopilot.bind('<Button-1>', self.listBoxCopilot)
        curItem = self.listBoxCopilot.focus()
        k = self.listBoxCopilot.item(curItem)
        url = 'http://www.rownaghsh.ir/del.php'
        data = {
            "table": "co_pilot",
            "key": "num_copilot",
            "value": str(k['values'][12]),
            "name_for_user": MyUsername,
            "password_for_user": MyPassword
        }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        self.CoPilotRoot.destroy()
        self.CoPilotRootFunc()

    def sabteCopilot(self):
        self.sabteCopilotPageRoot = Tk()
        self.sabteCopilotPageRoot.title("ثبت کمک خلبان")
        self.sabteCopilotPageRoot.configure(bg='orange')
        title = Label(self.sabteCopilotPageRoot, text="ثبت کمک خلبان", font=('IRANSans', '22'), bg='orange')
        space = Label(self.sabteCopilotPageRoot, text=" ", bg='orange')
        space1 = Label(self.sabteCopilotPageRoot, text=" ", bg='orange')
        space2 = Label(self.sabteCopilotPageRoot, text=" ", bg='orange')
        space3 = Label(self.sabteCopilotPageRoot, text=" ", bg='orange')
        space4 = Label(self.sabteCopilotPageRoot, text=" ", bg='orange')
        space5 = Label(self.sabteCopilotPageRoot, text=" ", bg='orange')
        space6 = Label(self.sabteCopilotPageRoot, text=" ", bg='orange')
        self.name = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.name.insert(0, "نام")
        self.lname = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.lname.insert(0, "نام خانوادگی")
        self.gender = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.gender.insert(0, "جنسیت")
        self.mellicode = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.mellicode.insert(0, "کدملی")
        self.cono = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.cono.insert(0, "شماره کمک خلبان")
        self.phno = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.phno.insert(0, "شماره تلفن")
        self.bd = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.bd.insert(0, "تاریخ تولد")
        self.wn = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.wn.insert(0, "نام همسر")
        self.mcw = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.mcw.insert(0, "کد ملی همسر")
        self.wphno = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.wphno.insert(0, "شماره تلفن همسر")
        self.cn = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.cn.insert(0, "تعداد فرزندان")
        self.f1 = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.f1.insert(0, "نام آشنا 1")
        self.fph1 = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fph1.insert(0, "تلفن 1")
        self.f2 = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.f2.insert(0, "نام آشنا 2")
        self.fph2 = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fph2.insert(0, "تلفن 2")
        self.f3 = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.f3.insert(0, "نام آشنا 3")
        self.fph3 = Entry(self.sabteCopilotPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fph3.insert(0, "تلفن 3")
        sabt = Button(self.sabteCopilotPageRoot, text="ثبت", bg='blue', fg='white', font=('IRANSans', '15'),
                      command=self.sabteCopilot2)
        sabt.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        # space2.pack()
        self.name.pack()
        self.lname.pack()
        self.gender.pack()
        self.mellicode.pack()
        self.cono.pack()
        self.phno.pack()
        self.bd.pack()
        self.wn.pack()
        self.mcw.pack()
        self.wphno.pack()
        self.cn.pack()
        self.f1.pack()
        self.fph1.pack()
        self.f2.pack()
        self.fph2.pack()
        self.f3.pack()
        self.fph3.pack()
        space3.pack()
        sabt.pack()
        space4.pack()

    def sabteCopilot2(self):
        url = 'http://www.rownaghsh.ir/co_pilot.php'
        if self.gender.get()=="مرد":
            x=1
        else:
            x=0
        data = {"fname": str(self.name.get()),
                "lname": str(self.lname.get()),
                "gender": x,
                "mellicode": str(self.mellicode.get()),
                "num_copilot": str(self.cono.get()),
                "phone": str(self.phno.get()),
                "birthdate": str(self.bd.get()),
                "partner": str(self.wn.get()),
                "partner_mellicode": str(self.mcw.get()),
                "partner_phone": str(self.wphno.get()),
                "child": int(self.cn.get()),
                "fname1": str(self.f1.get()),
                "phon1": str(self.fph1.get()),
                "fname2": str(self.f2.get()),
                "phon2": str(self.fph2.get()),
                "fname3": str(self.f3.get()),
                "phon3": str(self.fph3.get()),
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        print(r.text)
        print(data1)
        self.sabteCopilotPageRoot.destroy()
        self.CoPilotRoot.destroy()
        self.CoPilotRootFunc()

    def FlightEngineerRootFunc(self):
        self.FlightEngineerRoot = Tk()
        self.FlightEngineerRoot.title("مهندسین پرواز")
        self.FlightEngineerRoot['bg'] = 'orange'
        space = Label(self.FlightEngineerRoot, text=" ", bg='orange')
        space1 = Label(self.FlightEngineerRoot, text=" ", bg='orange')
        space2 = Label(self.FlightEngineerRoot, text=" ", bg='orange')
        space3 = Label(self.FlightEngineerRoot, text=" ", bg='orange')
        space4 = Label(self.FlightEngineerRoot, text=" ", bg='orange')
        space5 = Label(self.FlightEngineerRoot, text=" ", bg='orange')
        title = Label(self.FlightEngineerRoot, text="مهندسین پرواز", font=('IRANSans', '22'), bg='orange')
        cols = (
            'تلفن 3', 'نام آشنا 3', 'تلفن 2', 'نام آشنا 2', 'تلفن 1', 'نام آشنا1', 'تعداد فرزندان', 'شماره تلفن همسر',
            'کد ملی همسر', 'نام همسر', 'تاریخ تولد', 'شماره تلفن', 'شماره مهندس پرواز', 'کد ملی', 'جنسیت', 'نام خانوادگی',
            'نام')
        self.listBoxFlightEngineer = ttk.Treeview(self.FlightEngineerRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=self.listBoxFlightEngineer.yview)
        self.listBoxFlightEngineer.configure(yscrollcommand=vsb.set)
        self.listBoxFlightEngineer.column("0", width=80, anchor="c")
        self.listBoxFlightEngineer.column("1", width=80, anchor="c")
        self.listBoxFlightEngineer.column("2", width=80, anchor="c")
        self.listBoxFlightEngineer.column("3", width=80, anchor="c")
        self.listBoxFlightEngineer.column("4", width=80, anchor="c")
        self.listBoxFlightEngineer.column("5", width=80, anchor="c")
        self.listBoxFlightEngineer.column("6", width=80, anchor="c")
        self.listBoxFlightEngineer.column("7", width=80, anchor="c")
        self.listBoxFlightEngineer.column("8", width=80, anchor="c")
        self.listBoxFlightEngineer.column("9", width=80, anchor="c")
        self.listBoxFlightEngineer.column("10", width=80, anchor="c")
        self.listBoxFlightEngineer.column("11", width=80, anchor="c")
        self.listBoxFlightEngineer.column("12", width=80, anchor="c")
        self.listBoxFlightEngineer.column("13", width=80, anchor="c")
        self.listBoxFlightEngineer.column("14", width=80, anchor="c")
        self.listBoxFlightEngineer.column("15", width=80, anchor="c")
        self.listBoxFlightEngineer.column("16", width=80, anchor="c")
        self.listBoxFlightEngineer.config(height=20)
        for col in cols:
            self.listBoxFlightEngineer.heading(col, text=col)
        url = 'http://www.rownaghsh.ir/req_personel.php'
        data = {'table': 'flight_engineer',
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        l = json.loads(r.text)
        for i in range(0, len(l)):
            if l[i]['gender'] == '1':
                x = 'مرد'
            else:
                x = 'زن'
            self.listBoxFlightEngineer.insert("", "end", values=(
                str(l[i]['phon3']),
                str(l[i]['fname3']),
                str(l[i]['phon2']),
                str(l[i]['fname2']),
                str(l[i]['phon1']),
                str(l[i]['fname1']),
                str(l[i]['child']),
                str(l[i]['partner_phone']),
                str(l[i]['partner_mellicode']),
                str(l[i]['partner']),
                str(l[i]['birthdate']),
                str(l[i]['phone']),
                str(l[i]['num_flight_engineer']),
                str(l[i]['mellicode']),
                x,
                str(l[i]['lname']),
                str(l[i]['fname'])
            ))
        sabt = Button(self.FlightEngineerRoot, text="ثبت مهندس پرواز", font=('IRANSans', '13'), fg='white', bg='blue',
                      command=self.sabteFlightEngineer)
        sabt.config(height=1, width=20)
        delete = Button(self.FlightEngineerRoot, text="حذف", font=('IRANSans', '13'), fg='white', bg='blue',
                        command=self.deleteFlightEngineer)
        delete.config(height=1, width=20)
        edit = Button(self.FlightEngineerRoot, text="ویرایش", font=('IRANSans', '13'), fg='white', bg='blue', command=self.editFlightEngineer)
        edit.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        self.listBoxFlightEngineer.pack()
        space2.pack()
        sabt.pack()
        edit.pack()
        delete.pack()
        space3.pack()

    def editFlightEngineer(self):
        self.listBoxFlightEngineer.bind('<Button-1>', self.listBoxFlightEngineer)
        curItem = self.listBoxFlightEngineer.focus()
        k = self.listBoxFlightEngineer.item(curItem)
        self.sabteّFlightEngineerPageRoot = Tk()
        self.sabteّFlightEngineerPageRoot.title("ویرایش مهندس پرواز")
        self.sabteّFlightEngineerPageRoot.configure(bg='orange')
        title = Label(self.sabteّFlightEngineerPageRoot, text="ویرایش مهندس پرواز", font=('IRANSans', '22'), bg='orange')
        space = Label(self.sabteّFlightEngineerPageRoot, text=" ", bg='orange')
        space1 = Label(self.sabteّFlightEngineerPageRoot, text=" ", bg='orange')
        space2 = Label(self.sabteّFlightEngineerPageRoot, text=" ", bg='orange')
        space3 = Label(self.sabteّFlightEngineerPageRoot, text=" ", bg='orange')
        space4 = Label(self.sabteّFlightEngineerPageRoot, text=" ", bg='orange')
        space5 = Label(self.sabteّFlightEngineerPageRoot, text=" ", bg='orange')
        space6 = Label(self.sabteّFlightEngineerPageRoot, text=" ", bg='orange')
        self.fename = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fename.insert(0, k['values'][16])
        self.felname = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.felname.insert(0, k['values'][15])
        self.fegender = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fegender.insert(0, k['values'][14])
        self.femellicode = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.femellicode.insert(0, k['values'][13])
        self.fecono = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fecono.insert(0, k['values'][12])
        self.fecono.config(state=DISABLED)
        self.fephno = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fephno.insert(0, k['values'][11])
        self.febd = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.febd.insert(0, k['values'][10])
        self.fewn = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fewn.insert(0, k['values'][9])
        self.femcw = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.femcw.insert(0, k['values'][8])
        self.fewphno = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fewphno.insert(0, k['values'][7])
        self.fecn = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fecn.insert(0, k['values'][6])
        self.fef1 = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fef1.insert(0, k['values'][5])
        self.fefph1 = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fefph1.insert(0, k['values'][4])
        self.fef2 = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fef2.insert(0, k['values'][3])
        self.fefph2 = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fefph2.insert(0, k['values'][2])
        self.fef3 = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fef3.insert(0, k['values'][1])
        self.fefph3 = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fefph3.insert(0, k['values'][0])
        sabt = Button(self.sabteّFlightEngineerPageRoot, text="ثبت", bg='blue', fg='white', font=('IRANSans', '15'),
                      command=self.editFlightEngineer2)
        sabt.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        # space2.pack()
        self.fename.pack()
        self.felname.pack()
        self.fegender.pack()
        self.femellicode.pack()
        self.fecono.pack()
        self.fephno.pack()
        self.febd.pack()
        self.fewn.pack()
        self.femcw.pack()
        self.fewphno.pack()
        self.fecn.pack()
        self.fef1.pack()
        self.fefph1.pack()
        self.fef2.pack()
        self.fefph2.pack()
        self.fef3.pack()
        self.fefph3.pack()
        space3.pack()
        sabt.pack()
        space4.pack()

    def editFlightEngineer2(self):
        url = 'http://www.rownaghsh.ir/upd.php'
        if self.fegender.get() == "مرد":
            x = 1
        else:
            x = 0
        data2 = {"fname": str(self.fename.get()),
                "lname": str(self.felname.get()),
                "gender": x,
                "mellicode": str(self.femellicode.get()),
                "num_flight_engineer": str(self.fecono.get()),
                "phone": str(self.fephno.get()),
                "birthdate": str(self.febd.get()),
                "partner": str(self.fewn.get()),
                "partner_mellicode": str(self.femcw.get()),
                "partner_phone": str(self.fewphno.get()),
                "child": int(self.fecn.get())
                }
        data3 = {
            "fname1": str(self.fef1.get()),
            "phon1": str(self.fefph1.get()),
            "fname2": str(self.fef2.get()),
            "phon2": str(self.fefph2.get()),
            "fname3": str(self.fef3.get()),
            "phon3": str(self.fefph3.get())
        }
        data = {"table": "flight_engineer",
                "key": "num_flight_engineer",
                "value": self.fecono.get(),
                "columns": data2,
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        data4 = {
            "table": "acquaintances_flight_engineer",
            "key": "code_personel",
            "value": self.fecono.get(),
            "columns": data3,
            "name_for_user": MyUsername,
            "password_for_user": MyPassword
        }
        data5 = json.dumps(data4)
        r = requests.post(url, data=data1)
        r = requests.post(url, data=data5)
        print(r.text)
        print(data1)
        self.sabteّFlightEngineerPageRoot.destroy()
        self.FlightEngineerRoot.destroy()
        self.FlightEngineerRootFunc()

    def deleteFlightEngineer(self):
        self.listBoxFlightEngineer.bind('<Button-1>', self.listBoxFlightEngineer)
        curItem = self.listBoxFlightEngineer.focus()
        k = self.listBoxFlightEngineer.item(curItem)
        url = 'http://www.rownaghsh.ir/del.php'
        data = {
            "table": "flight_engineer",
            "key": "num_flight_engineer",
            "value": str(k['values'][12]),
            "name_for_user": MyUsername,
            "password_for_user": MyPassword
        }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        self.FlightEngineerRoot.destroy()
        self.FlightEngineerRootFunc()

    def sabteFlightEngineer(self):
        self.sabteّFlightEngineerPageRoot = Tk()
        self.sabteّFlightEngineerPageRoot.title("ثبت مهندس پرواز")
        self.sabteّFlightEngineerPageRoot.configure(bg='orange')
        title = Label(self.sabteّFlightEngineerPageRoot, text="ثبت مهندس پرواز", font=('IRANSans', '22'), bg='orange')
        space = Label(self.sabteّFlightEngineerPageRoot, text=" ", bg='orange')
        space1 = Label(self.sabteّFlightEngineerPageRoot, text=" ", bg='orange')
        space2 = Label(self.sabteّFlightEngineerPageRoot, text=" ", bg='orange')
        space3 = Label(self.sabteّFlightEngineerPageRoot, text=" ", bg='orange')
        space4 = Label(self.sabteّFlightEngineerPageRoot, text=" ", bg='orange')
        space5 = Label(self.sabteّFlightEngineerPageRoot, text=" ", bg='orange')
        space6 = Label(self.sabteّFlightEngineerPageRoot, text=" ", bg='orange')
        self.fename = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fename.insert(0, "نام")
        self.felname = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.felname.insert(0, "نام خانوادگی")
        self.fegender = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fegender.insert(0, "جنسیت")
        self.femellicode = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.femellicode.insert(0, "کدملی")
        self.fecono = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fecono.insert(0, "شماره مهندس پرواز")
        self.fephno = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fephno.insert(0, "شماره تلفن")
        self.febd = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.febd.insert(0, "تاریخ تولد")
        self.fewn = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fewn.insert(0, "نام همسر")
        self.femcw = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.femcw.insert(0, "کد ملی همسر")
        self.fewphno = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fewphno.insert(0, "شماره تلفن همسر")
        self.fecn = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fecn.insert(0, "تعداد فرزندان")
        self.fef1 = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fef1.insert(0, "نام آشنا 1")
        self.fefph1 = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fefph1.insert(0, "تلفن 1")
        self.fef2 = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fef2.insert(0, "نام آشنا 2")
        self.fefph2 = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fefph2.insert(0, "تلفن 2")
        self.fef3 = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fef3.insert(0, "نام آشنا 3")
        self.fefph3 = Entry(self.sabteّFlightEngineerPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.fefph3.insert(0, "تلفن 3")
        sabt = Button(self.sabteّFlightEngineerPageRoot, text="ثبت", bg='blue', fg='white', font=('IRANSans', '15'),
                      command=self.sabteFlightEngineer2)
        sabt.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        # space2.pack()
        self.fename.pack()
        self.felname.pack()
        self.fegender.pack()
        self.femellicode.pack()
        self.fecono.pack()
        self.fephno.pack()
        self.febd.pack()
        self.fewn.pack()
        self.femcw.pack()
        self.fewphno.pack()
        self.fecn.pack()
        self.fef1.pack()
        self.fefph1.pack()
        self.fef2.pack()
        self.fefph2.pack()
        self.fef3.pack()
        self.fefph3.pack()
        space3.pack()
        sabt.pack()
        space4.pack()

    def sabteFlightEngineer2(self):
        url = 'http://www.rownaghsh.ir/flight_engineer.php'
        if self.fegender.get()=="مرد":
            x=1
        else:
            x=0
        data = {"fname": str(self.fename.get()),
                "lname": str(self.felname.get()),
                "gender": x,
                "mellicode": str(self.femellicode.get()),
                "num_flight_engineer": str(self.fecono.get()),
                "phone": str(self.fephno.get()),
                "birthdate": str(self.febd.get()),
                "partner": str(self.fewn.get()),
                "partner_mellicode": str(self.femcw.get()),
                "partner_phone": str(self.fewphno.get()),
                "child": int(self.fecn.get()),
                "fname1": str(self.fef1.get()),
                "phon1": str(self.fefph1.get()),
                "fname2": str(self.fef2.get()),
                "phon2": str(self.fefph2.get()),
                "fname3": str(self.fef3.get()),
                "phon3": str(self.fefph3.get()),
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        print(r.text)
        print(data1)
        self.sabteّFlightEngineerPageRoot.destroy()
        self.FlightEngineerRoot.destroy()
        self.FlightEngineerRootFunc()

    def StewardsRootFunc(self):
        self.StewardsRoot = Tk()
        self.StewardsRoot.title("مهمانداران")
        self.StewardsRoot['bg'] = 'orange'
        space = Label(self.StewardsRoot, text=" ", bg='orange')
        space1 = Label(self.StewardsRoot, text=" ", bg='orange')
        space2 = Label(self.StewardsRoot, text=" ", bg='orange')
        space3 = Label(self.StewardsRoot, text=" ", bg='orange')
        space4 = Label(self.StewardsRoot, text=" ", bg='orange')
        space5 = Label(self.StewardsRoot, text=" ", bg='orange')
        title = Label(self.StewardsRoot, text="مهمانداران", font=('IRANSans', '22'), bg='orange')
        cols = (
        'تلفن 3', 'نام آشنا 3', 'تلفن 2', 'نام آشنا 2', 'تلفن 1', 'نام آشنا1','وضعیت', 'تعداد فرزندان', 'شماره تلفن همسر',
        'کد ملی همسر', 'نام همسر', 'تاریخ تولد', 'شماره تلفن', 'شماره کمک خلبان', 'کد ملی', 'جنسیت', 'نام خانوادگی',
        'نام')
        self.listBoxStewartss = ttk.Treeview(self.StewardsRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=self.listBoxStewartss.yview)
        self.listBoxStewartss.configure(yscrollcommand=vsb.set)
        self.listBoxStewartss.column("0", width=75, anchor="c")
        self.listBoxStewartss.column("1", width=75, anchor="c")
        self.listBoxStewartss.column("2", width=75, anchor="c")
        self.listBoxStewartss.column("3", width=75, anchor="c")
        self.listBoxStewartss.column("4", width=75, anchor="c")
        self.listBoxStewartss.column("5", width=75, anchor="c")
        self.listBoxStewartss.column("6", width=75, anchor="c")
        self.listBoxStewartss.column("7", width=75, anchor="c")
        self.listBoxStewartss.column("8", width=75, anchor="c")
        self.listBoxStewartss.column("9", width=75, anchor="c")
        self.listBoxStewartss.column("10", width=75, anchor="c")
        self.listBoxStewartss.column("11", width=75, anchor="c")
        self.listBoxStewartss.column("12", width=75, anchor="c")
        self.listBoxStewartss.column("13", width=75, anchor="c")
        self.listBoxStewartss.column("14", width=75, anchor="c")
        self.listBoxStewartss.column("15", width=75, anchor="c")
        self.listBoxStewartss.column("16", width=75,anchor="c")
        self.listBoxStewartss.column("17", width=75, anchor="c")
        self.listBoxStewartss.config(height=20)
        for col in cols:
            self.listBoxStewartss.heading(col, text=col)
        url = 'http://www.rownaghsh.ir/req_personel.php'
        data = {'table': 'stewardess',
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        l = json.loads(r.text)
        for i in range(0, len(l)):
            if l[i]['gender'] == '1':
                x = 'مرد'
            else:
                x = 'زن'
            if l[i]['active'] == '1':
                y = 'فعال'
            else:
                y = 'آزاد'
            self.listBoxStewartss.insert("", "end", values=(
                str(l[i]['phon3']),
                str(l[i]['fname3']),
                str(l[i]['phon2']),
                str(l[i]['fname2']),
                str(l[i]['phon1']),
                str(l[i]['fname1']),
                y,
                str(l[i]['child']),
                str(l[i]['partner_phone']),
                str(l[i]['partner_mellicode']),
                str(l[i]['partner']),
                str(l[i]['birthdate']),
                str(l[i]['phone']),
                str(l[i]['num_stewardess']),
                str(l[i]['mellicode']),
                x,
                str(l[i]['lname']),
                str(l[i]['fname'])
            ))
        sabt = Button(self.StewardsRoot, text="ثبت مهماندار", font=('IRANSans', '13'), fg='white', bg='blue',
                      command=self.sabteSteward)
        sabt.config(height=1, width=20)
        delete = Button(self.StewardsRoot, text="حذف", font=('IRANSans', '13'), fg='white', bg='blue',
                      command=self.deleteStewardss)
        delete.config(height=1, width=20)
        edit = Button(self.StewardsRoot, text="ویرایش", font=('IRANSans', '13'), fg='white', bg='blue',
                      command=self.editStewardss)
        edit.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        self.listBoxStewartss.pack()
        space2.pack()
        sabt.pack()
        edit.pack()
        delete.pack()
        space3.pack()

    def editStewardss(self):
        self.listBoxStewartss.bind('<Button-1>', self.listBoxStewartss)
        curItem = self.listBoxStewartss.focus()
        k = self.listBoxStewartss.item(curItem)
        self.sabteStewardPageRoot = Tk()
        self.sabteStewardPageRoot.title("ویرایش مهماندار")
        self.sabteStewardPageRoot.configure(bg='orange')
        title = Label(self.sabteStewardPageRoot, text="ویرایش مهماندار", font=('IRANSans', '22'), bg='orange')
        space = Label(self.sabteStewardPageRoot, text=" ", bg='orange')
        space1 = Label(self.sabteStewardPageRoot, text=" ", bg='orange')
        space2 = Label(self.sabteStewardPageRoot, text=" ", bg='orange')
        space3 = Label(self.sabteStewardPageRoot, text=" ", bg='orange')
        space4 = Label(self.sabteStewardPageRoot, text=" ", bg='orange')
        space5 = Label(self.sabteStewardPageRoot, text=" ", bg='orange')
        space6 = Label(self.sabteStewardPageRoot, text=" ", bg='orange')
        self.sname = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.sname.insert(0, k['values'][17])
        self.slname = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.slname.insert(0, k['values'][16])
        self.sgender = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.sgender.insert(0, k['values'][15])
        self.smellicode = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.smellicode.insert(0, k['values'][14])
        self.scono = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.scono.insert(0, k['values'][13])
        self.scono.config(state=DISABLED)
        self.sphno = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.sphno.insert(0, k['values'][12])
        self.sbd = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.sbd.insert(0, k['values'][11])
        self.swn = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.swn.insert(0, k['values'][10])
        self.smcw = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.smcw.insert(0, k['values'][9])
        self.swphno = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.swphno.insert(0, k['values'][8])
        self.scn = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.scn.insert(0, k['values'][7])
        self.s = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.s.insert(0, k['values'][6])
        self.sf1 = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.sf1.insert(0, k['values'][5])
        self.sfph1 = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.sfph1.insert(0, k['values'][4])
        self.sf2 = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.sf2.insert(0, k['values'][3])
        self.sfph2 = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.sfph2.insert(0, k['values'][2])
        self.sf3 = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.sf3.insert(0, k['values'][1])
        self.sfph3 = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.sfph3.insert(0, k['values'][0])
        sabt = Button(self.sabteStewardPageRoot, text="ثبت", bg='blue', fg='white', font=('IRANSans', '15'),
                      command=self.editStewardss2)
        sabt.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        # space2.pack()
        self.sname.pack()
        self.slname.pack()
        self.sgender.pack()
        self.smellicode.pack()
        self.scono.pack()
        self.sphno.pack()
        self.sbd.pack()
        self.swn.pack()
        self.smcw.pack()
        self.swphno.pack()
        self.scn.pack()
        self.s.pack()
        self.sf1.pack()
        self.sfph1.pack()
        self.sf2.pack()
        self.sfph2.pack()
        self.sf3.pack()
        self.sfph3.pack()
        space3.pack()
        sabt.pack()
        space4.pack()

    def editStewardss2(self):
        url = 'http://www.rownaghsh.ir/upd.php'
        if self.sgender.get() == "مرد":
            x = 1
        else:
            x = 0
        if self.s.get() == "فعال":
            y = 1
        else:
            y = 0
        data2 = {"fname": str(self.sname.get()),
                "lname": str(self.slname.get()),
                "gender": x,
                "mellicode": str(self.smellicode.get()),
                "num_stewardess": str(self.scono.get()),
                "active": y,
                "phone": str(self.sphno.get()),
                "birthdate": str(self.sbd.get()),
                "partner": str(self.swn.get()),
                "partner_mellicode": str(self.smcw.get()),
                "partner_phone": str(self.swphno.get()),
                "child": int(self.scn.get())
                }
        data3 = {
            "fname1": str(self.sf1.get()),
            "phon1": str(self.sfph1.get()),
            "fname2": str(self.sf2.get()),
            "phon2": str(self.sfph2.get()),
            "fname3": str(self.sf3.get()),
            "phon3": str(self.sfph3.get())
        }
        data = {"table": "stewardess",
                "key": "num_stewardess",
                "value": self.scono.get(),
                "columns": data2,
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        data4 = {
            "table":"acquaintances_stewardess",
            "key":"code_personel",
            "value":self.scono.get(),
            "columns":data3,
            "name_for_user": MyUsername,
            "password_for_user": MyPassword
        }
        data5=json.dumps(data4)
        r = requests.post(url, data=data1)
        r = requests.post(url, data=data5)
        print(r.text)
        print(data1)
        self.sabteStewardPageRoot.destroy()
        self.StewardsRoot.destroy()
        self.StewardsRootFunc()

    def deleteStewardss(self):
        self.listBoxStewartss.bind('<Button-1>', self.listBoxStewartss)
        curItem = self.listBoxStewartss.focus()
        k = self.listBoxStewartss.item(curItem)
        url = 'http://www.rownaghsh.ir/del.php'
        data = {
            "table": "stewardess",
            "key": "num_stewardess",
            "value": str(k['values'][13]),
            "name_for_user": MyUsername,
            "password_for_user": MyPassword
        }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        self.StewardsRoot.destroy()
        self.StewardsRootFunc()

    def sabteSteward(self):
        self.sabteStewardPageRoot = Tk()
        self.sabteStewardPageRoot.title("ثبت مهماندار")
        self.sabteStewardPageRoot.configure(bg='orange')
        title = Label(self.sabteStewardPageRoot, text="ثبت مهماندار", font=('IRANSans', '22'), bg='orange')
        space = Label(self.sabteStewardPageRoot, text=" ", bg='orange')
        space1 = Label(self.sabteStewardPageRoot, text=" ", bg='orange')
        space2 = Label(self.sabteStewardPageRoot, text=" ", bg='orange')
        space3 = Label(self.sabteStewardPageRoot, text=" ", bg='orange')
        space4 = Label(self.sabteStewardPageRoot, text=" ", bg='orange')
        space5 = Label(self.sabteStewardPageRoot, text=" ", bg='orange')
        space6 = Label(self.sabteStewardPageRoot, text=" ", bg='orange')
        self.sname = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.sname.insert(0, "نام")
        self.slname = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.slname.insert(0, "نام خانوادگی")
        self.sgender = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.sgender.insert(0, "جنسیت")
        self.smellicode = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.smellicode.insert(0, "کدملی")
        self.scono = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.scono.insert(0, "شماره مهماندار")
        self.sphno = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.sphno.insert(0, "شماره تلفن")
        self.sbd = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.sbd.insert(0, "تاریخ تولد")
        self.swn = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.swn.insert(0, "نام همسر")
        self.smcw = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.smcw.insert(0, "کد ملی همسر")
        self.swphno = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.swphno.insert(0, "شماره تلفن همسر")
        self.scn = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.scn.insert(0, "تعداد فرزندان")
        self.s = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.s.insert(0, "وضعیت")
        self.sf1 = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.sf1.insert(0, "نام آشنا 1")
        self.sfph1 = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.sfph1.insert(0, "تلفن 1")
        self.sf2 = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.sf2.insert(0, "نام آشنا 2")
        self.sfph2 = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.sfph2.insert(0, "تلفن 2")
        self.sf3 = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.sf3.insert(0, "نام آشنا 3")
        self.sfph3 = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 10))
        self.sfph3.insert(0, "تلفن 3")
        sabt = Button(self.sabteStewardPageRoot, text="ثبت", bg='blue', fg='white', font=('IRANSans', '15'),
                      command=self.sabteSteward2)
        sabt.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        # space2.pack()
        self.sname.pack()
        self.slname.pack()
        self.sgender.pack()
        self.smellicode.pack()
        self.scono.pack()
        self.sphno.pack()
        self.sbd.pack()
        self.swn.pack()
        self.smcw.pack()
        self.swphno.pack()
        self.scn.pack()
        self.s.pack()
        self.sf1.pack()
        self.sfph1.pack()
        self.sf2.pack()
        self.sfph2.pack()
        self.sf3.pack()
        self.sfph3.pack()
        space3.pack()
        sabt.pack()
        space4.pack()

    def sabteSteward2(self):
        url = 'http://www.rownaghsh.ir/stewardess.php'
        if self.sgender.get()=="مرد":
            x=1
        else:
            x=0
        if self.s.get()=="فعال":
            y=1
        else:
            y=0
        data = {"fname": str(self.sname.get()),
                "lname": str(self.slname.get()),
                "gender": x,
                "mellicode": str(self.smellicode.get()),
                "num_stewardess": str(self.scono.get()),
                "active": y,
                "phone": str(self.sphno.get()),
                "birthdate": str(self.sbd.get()),
                "partner": str(self.swn.get()),
                "partner_mellicode": str(self.smcw.get()),
                "partner_phone": str(self.swphno.get()),
                "child": int(self.scn.get()),
                "fname1": str(self.sf1.get()),
                "phon1": str(self.sfph1.get()),
                "fname2": str(self.sf2.get()),
                "phon2": str(self.sfph2.get()),
                "fname3": str(self.sf3.get()),
                "phon3": str(self.sfph3.get()),
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        print(r.text)
        print(data1)
        self.sabteStewardPageRoot.destroy()
        self.StewardsRoot.destroy()
        self.StewardsRootFunc()

    def FlightsRootFunc(self):
        self.FlightsRoot = Tk()
        self.FlightsRoot.title("پرواز ها")
        self.FlightsRoot['bg'] = 'orange'
        space = Label(self.FlightsRoot, text=" ", bg='orange')
        space1 = Label(self.FlightsRoot, text=" ", bg='orange')
        space2 = Label(self.FlightsRoot, text=" ", bg='orange')
        space3 = Label(self.FlightsRoot, text=" ", bg='orange')
        space4 = Label(self.FlightsRoot, text=" ", bg='orange')
        space5 = Label(self.FlightsRoot, text=" ", bg='orange')
        title = Label(self.FlightsRoot, text="برنامه پرواز ها", font=('IRANSans', '22'), fg="Blue", bg='orange')
        cols = ('داخلی یا خارجی', 'وضعیت پرواز', 'وزن کل بار', 'مسافران First class', 'مسافران business class', 'مسافران Economy class',
                'شماره گروه مهمانداری', 'شماره مهندس پرواز', 'شماره کمک خلبان', 'شماره خلبان', 'شماره پروار')
        self.listBoxFlight = ttk.Treeview(self.FlightsRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=self.listBoxFlight.yview)
        self.listBoxFlight.configure(yscrollcommand=vsb.set)
        self.listBoxFlight.column("0", width=120, anchor="c")
        self.listBoxFlight.column("1", width=125, anchor="c")
        self.listBoxFlight.column("2", width=120, anchor="c")
        self.listBoxFlight.column("3", width=125, anchor="c")
        self.listBoxFlight.column("4", width=120, anchor="c")
        self.listBoxFlight.column("5", width=125, anchor="c")
        self.listBoxFlight.column("6", width=120, anchor="c")
        self.listBoxFlight.column("7", width=125, anchor="c")
        self.listBoxFlight.column("8", width=120, anchor="c")
        self.listBoxFlight.column("9", width=125, anchor="c")
        self.listBoxFlight.column("10", width=120, anchor="c")
        self.listBoxFlight.config(height=20)
        for col in cols:
            self.listBoxFlight.heading(col, text=col)
        url = 'http://www.rownaghsh.ir/req_flight.php'
        data = {'table': 'flight',
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        l = json.loads(r.text)
        for i in range(0, len(l)):
            if l[i]['internal']=='1':
                x='داخلی'
            else:
                x='خارجی'
            self.listBoxFlight.insert("", "end", values=(
                x,
                str(l[i]['Flight_status']),
                str(l[i]['all_weight_bar']),
                str(l[i]['first_class_passenger']),
                str(l[i]['bisness_passenger']),
                str(l[i]['normal_passenger']),
                str(l[i]['num_group']),
                str(l[i]['num_flight_engineer']),
                str(l[i]['num_copilot']),
                str(l[i]['num_pilot']),
                str(l[i]['num_flight'])
            ))
        sabt = Button(self.FlightsRoot, text="ثبت پرواز", font=('IRANSans', '13'), fg='white', bg='blue', command=self.sabteFlight)
        sabt.config(height=1, width=18)
        delete = Button(self.FlightsRoot, text="حذف", font=('IRANSans', '13'), fg='white', bg='blue', command=self.deleteFlight)
        delete.config(height=1, width=18)
        edit = Button(self.FlightsRoot, text="ویرایش", font=('IRANSans', '13'), fg='white', bg='blue', command=self.editFlight)
        edit.config(height=1, width=18)
        space.pack()
        title.pack()
        space1.pack()
        self.listBoxFlight.pack()
        space2.pack()
        sabt.pack()
        edit.pack()
        delete.pack()
        space3.pack()

    def editFlight(self):
        self.listBoxFlight.bind('<Button-1>', self.listBoxFlight)
        curItem = self.listBoxFlight.focus()
        k = self.listBoxFlight.item(curItem)
        self.sabteFlightPageRoot = Tk()
        self.sabteFlightPageRoot.title("ویرایش پرواز")
        self.sabteFlightPageRoot.configure(bg='orange')
        title = Label(self.sabteFlightPageRoot, text="ویرایش پرواز", font=('IRANSans', '22'), bg='orange')
        space = Label(self.sabteFlightPageRoot, text=" ", bg='orange')
        space1 = Label(self.sabteFlightPageRoot, text=" ", bg='orange')
        space2 = Label(self.sabteFlightPageRoot, text=" ", bg='orange')
        space3 = Label(self.sabteFlightPageRoot, text=" ", bg='orange')
        space4 = Label(self.sabteFlightPageRoot, text=" ", bg='orange')
        space5 = Label(self.sabteFlightPageRoot, text=" ", bg='orange')
        space6 = Label(self.sabteFlightPageRoot, text=" ", bg='orange')
        self.q1 = Entry(self.sabteFlightPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.q1.insert(0, k['values'][10])
        self.q1.config(state=DISABLED)
        self.q2 = Entry(self.sabteFlightPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.q2.insert(0, k['values'][9])
        self.q3 = Entry(self.sabteFlightPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.q3.insert(0, k['values'][8])
        self.q4 = Entry(self.sabteFlightPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.q4.insert(0, k['values'][7])
        self.q5 = Entry(self.sabteFlightPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.q5.insert(0, k['values'][6])
        self.q6 = Entry(self.sabteFlightPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.q6.insert(0, k['values'][5])
        self.q7 = Entry(self.sabteFlightPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.q7.insert(0, k['values'][4])
        self.q8 = Entry(self.sabteFlightPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.q8.insert(0, k['values'][3])
        self.q9 = Entry(self.sabteFlightPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.q9.insert(0, k['values'][2])
        self.q10 = Entry(self.sabteFlightPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.q10.insert(0, k['values'][1])
        self.q11 = Entry(self.sabteFlightPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.q11.insert(0, k['values'][0])
        sabt = Button(self.sabteFlightPageRoot, text="ثبت", bg='blue', fg='white', font=('IRANSans', '15'),
                      command=self.editFlight2)
        sabt.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        self.q1.pack()
        self.q2.pack()
        self.q3.pack()
        self.q4.pack()
        self.q5.pack()
        self.q6.pack()
        self.q7.pack()
        self.q8.pack()
        self.q9.pack()
        self.q10.pack()
        self.q11.pack()
        space3.pack()
        sabt.pack()
        space4.pack()

    def editFlight2(self):
        if self.q11.get() == 'داخلی':
            x = 1
        else:
            x = 0
        url = 'http://www.rownaghsh.ir/upd.php'
        data2 = {"num_flight": str(self.q1.get()),
                "num_pilot": str(self.q2.get()),
                "num_copilot": str(self.q3.get()),
                "num_flight_engineer": str(self.q4.get()),
                "num_group": str(self.q5.get()),
                "normal_passenger": int(self.q8.get()),
                "bisness_passenger": int(self.q7.get()),
                "first_class_passenger": int(self.q6.get()),
                "all_weight_bar": int(self.q9.get()),
                "Flight_status": str(self.q10.get()),
                "internal": x
                }
        data = {"table": "flight",
                "key": "num_flight",
                "value": self.q1.get(),
                "columns": data2,
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        print(r.text)
        print(data1)
        self.sabteFlightPageRoot.destroy()
        self.FlightsRoot.destroy()
        self.FlightsRootFunc()

    def deleteFlight(self):
        self.listBoxFlight.bind('<Button-1>', self.listBoxFlight)
        curItem = self.listBoxFlight.focus()
        k = self.listBoxFlight.item(curItem)
        url = 'http://www.rownaghsh.ir/del.php'
        data = {
            "table": "flight",
            "key": "num_flight",
            "value": str(k['values'][10]),
            "name_for_user": MyUsername,
            "password_for_user": MyPassword
        }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        self.FlightsRoot.destroy()
        self.FlightsRootFunc()

    def sabteFlight(self):
        self.sabteFlightPageRoot = Tk()
        self.sabteFlightPageRoot.title("ثبت پرواز")
        self.sabteFlightPageRoot.configure(bg='orange')
        title = Label(self.sabteFlightPageRoot, text="ثبت پرواز", font=('IRANSans', '22'), bg='orange')
        space = Label(self.sabteFlightPageRoot, text=" ", bg='orange')
        space1 = Label(self.sabteFlightPageRoot, text=" ", bg='orange')
        space2 = Label(self.sabteFlightPageRoot, text=" ", bg='orange')
        space3 = Label(self.sabteFlightPageRoot, text=" ", bg='orange')
        space4 = Label(self.sabteFlightPageRoot, text=" ", bg='orange')
        space5 = Label(self.sabteFlightPageRoot, text=" ", bg='orange')
        space6 = Label(self.sabteFlightPageRoot, text=" ", bg='orange')
        self.q1 = Entry(self.sabteFlightPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.q1.insert(0, "شماره پروار")
        self.q2 = Entry(self.sabteFlightPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.q2.insert(0, "شماره خلبان")
        self.q3 = Entry(self.sabteFlightPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.q3.insert(0, "شماره کمک خلبان")
        self.q4 = Entry(self.sabteFlightPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.q4.insert(0, "شماره مهندس پرواز")
        self.q5 = Entry(self.sabteFlightPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.q5.insert(0, "شماره گروه مهمانداری")
        self.q6 = Entry(self.sabteFlightPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.q6.insert(0, "مسافران First class")
        self.q7 = Entry(self.sabteFlightPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.q7.insert(0, "مسافران Business class")
        self.q8 = Entry(self.sabteFlightPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.q8.insert(0, "مسافران Economy class")
        self.q9 = Entry(self.sabteFlightPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.q9.insert(0, "وزن کل بار")
        self.q10 = Entry(self.sabteFlightPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.q10.insert(0, "وضعیت پرواز")
        self.q11 = Entry(self.sabteFlightPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.q11.insert(0, "داخلی یا خارجی")
        sabt = Button(self.sabteFlightPageRoot, text="ثبت", bg='blue', fg='white', font=('IRANSans', '15'),
                      command=self.sabteFlight2)
        sabt.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        self.q1.pack()
        self.q2.pack()
        self.q3.pack()
        self.q4.pack()
        self.q5.pack()
        self.q6.pack()
        self.q7.pack()
        self.q8.pack()
        self.q9.pack()
        self.q10.pack()
        self.q11.pack()
        space3.pack()
        sabt.pack()
        space4.pack()

    def sabteFlight2(self):
        if self.q11.get()=='داخلی':
            x=1
        else:
            x=0
        url = 'http://www.rownaghsh.ir/flight.php'
        data = {"num_flight": str(self.q1.get()),
                "num_pilot": str(self.q2.get()),
                "num_copilot": str(self.q3.get()),
                "num_flight_engineer": str(self.q4.get()),
                "num_group": str(self.q5.get()),
                "normal_passenger": int(self.q8.get()),
                "bisness_passenger": int(self.q7.get()),
                "first_class_passenger": int(self.q6.get()),
                "all_weight_bar": int(self.q9.get()),
                "Flight_status": str(self.q10.get()),
                "internal": x,
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        print(r.text)
        print(data1)
        self.sabteFlightPageRoot.destroy()
        self.FlightsRoot.destroy()
        self.FlightsRootFunc()

    def FlightSkechuleRootFunc(self):
        self.FlightSkechuleRoot = Tk()
        self.FlightSkechuleRoot.title("برنامه پرواز ها")
        self.FlightSkechuleRoot['bg'] = 'orange'
        space = Label(self.FlightSkechuleRoot, text=" ", bg='orange')
        space1 = Label(self.FlightSkechuleRoot, text=" ", bg='orange')
        space2 = Label(self.FlightSkechuleRoot, text=" ", bg='orange')
        space3 = Label(self.FlightSkechuleRoot, text=" ", bg='orange')
        space4 = Label(self.FlightSkechuleRoot, text=" ", bg='orange')
        space5 = Label(self.FlightSkechuleRoot, text=" ", bg='orange')
        title = Label(self.FlightSkechuleRoot, text="برنامه پرواز های آخرین هفته", font=('IRANSans', '22'), bg='orange')
        cols = ('تاریخ فرود','تاریخ پرواز','زمان نشستن', 'زمان پرواز', 'شماره پرواز', 'مقصد', 'مبدأ', 'شماره هواپیما')
        self.listBoxFS = ttk.Treeview(self.FlightSkechuleRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=self.listBoxFS.yview)
        self.listBoxFS.configure(yscrollcommand=vsb.set)
        self.listBoxFS.column("0", width=170, anchor="c")
        self.listBoxFS.column("1", width=170, anchor="c")
        self.listBoxFS.column("2", width=170, anchor="c")
        self.listBoxFS.column("3", width=170, anchor="c")
        self.listBoxFS.column("4", width=170, anchor="c")
        self.listBoxFS.column("5", width=170, anchor="c")
        self.listBoxFS.column("6", width=170, anchor="c")
        self.listBoxFS.column("7", width=170, anchor="c")
        self.listBoxFS.config(height=20)
        for col in cols:
            self.listBoxFS.heading(col, text=col)
        url = 'http://www.rownaghsh.ir/req_flight.php'
        data = {'table': 'flight',
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        l = json.loads(r.text)
        for i in range(0, len(l)):
            self.listBoxFS.insert("", "end", values=(
                str(l[i]['date_up']),
                str(l[i]['date_down']),
                str(l[i]['timer_up']),
                str(l[i]['timer_down']),
                str(l[i]['num_flight']),
                str(l[i]['destination']),
                str(l[i]['origin']),
                str(l[i]['num_airplane'])
            ))
        sabt = Button(self.FlightSkechuleRoot, text="ثبت پرواز", font=('IRANSans', '13'), fg='white', bg='blue', command=self.sabteFS)
        sabt.config(height=1, width=18)
        delete = Button(self.FlightSkechuleRoot, text="حذف", font=('IRANSans', '13'), fg='white', bg='blue', command=self.deleteFlightSkedule)
        delete.config(height=1, width=18)
        edit = Button(self.FlightSkechuleRoot, text="ویرایش", font=('IRANSans', '13'), fg='white', bg='blue', command=self.editFS)
        edit.config(height=1, width=18)
        space.pack()
        title.pack()
        space1.pack()
        self.listBoxFS.pack()
        space2.pack()
        sabt.pack()
        edit.pack()
        delete.pack()
        space3.pack()

    def editFS(self):
        self.listBoxFS.bind('<Button-1>', self.listBoxFS)
        curItem = self.listBoxFS.focus()
        k = self.listBoxFS.item(curItem)
        self.sabteFSPageRoot = Tk()
        self.sabteFSPageRoot.title("ویرایش برنامه پروازی")
        self.sabteFSPageRoot.configure(bg='orange')
        title = Label(self.sabteFSPageRoot, text="ویرایش برنامه پروازی", font=('IRANSans', '22'), bg='orange')
        space = Label(self.sabteFSPageRoot, text=" ", bg='orange')
        space1 = Label(self.sabteFSPageRoot, text=" ", bg='orange')
        space2 = Label(self.sabteFSPageRoot, text=" ", bg='orange')
        space3 = Label(self.sabteFSPageRoot, text=" ", bg='orange')
        space4 = Label(self.sabteFSPageRoot, text=" ", bg='orange')
        space5 = Label(self.sabteFSPageRoot, text=" ", bg='orange')
        space6 = Label(self.sabteFSPageRoot, text=" ", bg='orange')
        self.APNum = Entry(self.sabteFSPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.APNum.insert(0, k['values'][7])
        self.orig = Entry(self.sabteFSPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.orig.insert(0, k['values'][6])
        self.dest = Entry(self.sabteFSPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.dest.insert(0, k['values'][5])
        self.fnum = Entry(self.sabteFSPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.fnum.insert(0, k['values'][4])
        self.fnum.config(state=DISABLED)
        self.jt = Entry(self.sabteFSPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.jt.insert(0, k['values'][3])
        self.lt = Entry(self.sabteFSPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.lt.insert(0, k['values'][2])
        self.jd = Entry(self.sabteFSPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.jd.insert(0, k['values'][1])
        self.ld = Entry(self.sabteFSPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.ld.insert(0, k['values'][0])
        sabt = Button(self.sabteFSPageRoot, text="ثبت", bg='blue', fg='white', font=('IRANSans', '15'),
                      command=self.editFS2)
        sabt.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        # space2.pack()
        self.APNum.pack()
        self.orig.pack()
        self.dest.pack()
        self.fnum.pack()
        self.jt.pack()
        self.lt.pack()
        self.jd.pack()
        self.ld.pack()
        space3.pack()
        sabt.pack()
        space4.pack()

    def editFS2(self):
        url = 'http://www.rownaghsh.ir/upd.php'
        data2 = {"num_airplane": int(self.APNum.get()),
                "origin": str(self.orig.get()),
                "destination": str(self.dest.get()),
                "num_flight": str(self.fnum.get()),
                "timer_up": str(self.jt.get()),
                "timer_down": str(self.lt.get()),
                "date_up": str(self.jd.get()),
                "date_down": str(self.ld.get())
                }
        data = {"table": "flight_schedule",
                "key": "num_flight",
                "value": self.fnum.get(),
                "columns": data2,
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        print(r.text)
        print(data1)
        self.sabteFSPageRoot.destroy()
        self.FlightSkechuleRoot.destroy()
        self.FlightSkechuleRootFunc()

    def deleteFlightSkedule(self):
        self.listBoxFS.bind('<Button-1>', self.listBoxFS)
        curItem = self.listBoxFS.focus()
        k = self.listBoxFS.item(curItem)
        url = 'http://www.rownaghsh.ir/del.php'
        data = {
            "table": "flight",
            "key": "num_flight",
            "value": str(k['values'][4]),
            "name_for_user": MyUsername,
            "password_for_user": MyPassword
        }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        self.FlightSkechuleRoot.destroy()
        self.FlightSkechuleRootFunc()

    def sabteFS(self):
        self.sabteFSPageRoot = Tk()
        self.sabteFSPageRoot.title("ثبت برنامه پروازی")
        self.sabteFSPageRoot.configure(bg='orange')
        title = Label(self.sabteFSPageRoot, text="ثبت برنامه پروازی", font=('IRANSans', '22'), bg='orange')
        space = Label(self.sabteFSPageRoot, text=" ", bg='orange')
        space1 = Label(self.sabteFSPageRoot, text=" ", bg='orange')
        space2 = Label(self.sabteFSPageRoot, text=" ", bg='orange')
        space3 = Label(self.sabteFSPageRoot, text=" ", bg='orange')
        space4 = Label(self.sabteFSPageRoot, text=" ", bg='orange')
        space5 = Label(self.sabteFSPageRoot, text=" ", bg='orange')
        space6 = Label(self.sabteFSPageRoot, text=" ", bg='orange')
        self.APNum = Entry(self.sabteFSPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.APNum.insert(0, "شماره هواپیما")
        self.orig = Entry(self.sabteFSPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.orig.insert(0, "مبدأ")
        self.dest = Entry(self.sabteFSPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.dest.insert(0, "مقصد")
        self.fnum = Entry(self.sabteFSPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.fnum.insert(0, "شماره پرواز")
        self.jt = Entry(self.sabteFSPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.jt.insert(0, "زمان پرواز")
        self.lt = Entry(self.sabteFSPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.lt.insert(0, "زمان نشستن")
        self.jd = Entry(self.sabteFSPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.jd.insert(0, "تاریخ پرواز")
        self.ld = Entry(self.sabteFSPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.ld.insert(0, "تاریخ نشستن")
        sabt = Button(self.sabteFSPageRoot, text="ثبت", bg='blue', fg='white', font=('IRANSans', '15'),
                      command=self.sabteFS2)
        sabt.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        # space2.pack()
        self.APNum.pack()
        self.orig.pack()
        self.dest.pack()
        self.fnum.pack()
        self.jt.pack()
        self.lt.pack()
        self.jd.pack()
        self.ld.pack()
        space3.pack()
        sabt.pack()
        space4.pack()

    def sabteFS2(self):
        url = 'http://www.rownaghsh.ir/flight_schedule.php'
        data = {"num_airplane": int(self.APNum.get()),
                "origin": str(self.orig.get()),
                "destination": str(self.dest.get()),
                "num_flight": str(self.fnum.get()),
                "timer_up": str(self.jt.get()),
                "timer_down": str(self.lt.get()),
                "date_up": str(self.jd.get()),
                "date_down": str(self.ld.get()),
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        print(r.text)
        print(data1)
        self.sabteFSPageRoot.destroy()
        self.FlightSkechuleRoot.destroy()
        self.FlightSkechuleRootFunc()

    def AirportsRootFunc(self):
        self.AirportsRoot = Tk()
        self.AirportsRoot.title("فرودگاه ها")
        self.AirportsRoot['bg'] = 'orange'
        space = Label(self.AirportsRoot, text=" ", bg='orange')
        space1 = Label(self.AirportsRoot, text=" ", bg='orange')
        space2 = Label(self.AirportsRoot, text=" ", bg='orange')
        space3 = Label(self.AirportsRoot, text=" ", bg='orange')
        space4 = Label(self.AirportsRoot, text=" ", bg='orange')
        space5 = Label(self.AirportsRoot, text=" ", bg='orange')
        title = Label(self.AirportsRoot, text="فرودگاه ها", font=('IRANSans', '22'), bg='orange')
        cols = ('داخلی یا خارجی','آدرس','عرض جغرافیایی', 'طول جغرافیایی', 'کشور', 'شهر', 'شماره فرودگاه', 'نام فرودگاه')
        self.listBoxAirport = ttk.Treeview(self.AirportsRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=self.listBoxAirport.yview)
        self.listBoxAirport.configure(yscrollcommand=vsb.set)
        self.listBoxAirport.column("0", width=125, anchor="c")
        self.listBoxAirport.column("1", width=460, anchor="c")
        self.listBoxAirport.column("2", width=125, anchor="c")
        self.listBoxAirport.column("3", width=125, anchor="c")
        self.listBoxAirport.column("4", width=125, anchor="c")
        self.listBoxAirport.column("5", width=125, anchor="c")
        self.listBoxAirport.column("6", width=125, anchor="c")
        self.listBoxAirport.column("7", width=125, anchor="c")
        self.listBoxAirport.config(height=20)
        for col in cols:
            self.listBoxAirport.heading(col, text=col)
        url = 'http://www.rownaghsh.ir/req.php'
        data = {'table': 'origin_destination',
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        l = json.loads(r.text)
        for i in range(0, len(l)):
            if l[i]['internal']==1:
                x='داخلی'
            else:
                x='خارجی'
            self.listBoxAirport.insert("", "end", values=(
                x,
                str(l[i]['addresses']),
                str(l[i]['latitude']),
                str(l[i]['longitude']),
                str(l[i]['country']),
                str(l[i]['city']),
                str(l[i]['num_airport']),
                str(l[i]['name_airport'])
            ))
        sabt = Button(self.AirportsRoot, text="ثبت فرودگاه", font=('IRANSans', '13'), fg='white', bg='blue', command=self.sabteAirport)
        sabt.config(height=1, width=20)
        delete = Button(self.AirportsRoot, text="حذف", font=('IRANSans', '13'),fg='white', bg='blue', command=self.deleteAirport)
        delete.config(height=1, width=20)
        edit = Button(self.AirportsRoot, text="ویرایش", font=('IRANSans', '13'),fg='white', bg='blue', command=self.editAirport)
        edit.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        self.listBoxAirport.pack()
        space2.pack()
        sabt.pack()
        edit.pack()
        delete.pack()
        space3.pack()

    def editAirport(self):
        self.listBoxAirport.bind('<Button-1>', self.listBoxAirport)
        curItem = self.listBoxAirport.focus()
        k = self.listBoxAirport.item(curItem)
        self.sabteAirportPageRoot = Tk()
        self.sabteAirportPageRoot.title("ویرایش فرودگاه")
        self.sabteAirportPageRoot.configure(bg='orange')
        title = Label(self.sabteAirportPageRoot, text="ویرایش فرودگاه", font=('IRANSans', '22'), bg='orange')
        space = Label(self.sabteAirportPageRoot, text=" ", bg='orange')
        space1 = Label(self.sabteAirportPageRoot, text=" ", bg='orange')
        space2 = Label(self.sabteAirportPageRoot, text=" ", bg='orange')
        space3 = Label(self.sabteAirportPageRoot, text=" ", bg='orange')
        space4 = Label(self.sabteAirportPageRoot, text=" ", bg='orange')
        space5 = Label(self.sabteAirportPageRoot, text=" ", bg='orange')
        space6 = Label(self.sabteAirportPageRoot, text=" ", bg='orange')
        self.APN = Entry(self.sabteAirportPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.APN.insert(0, k['values'][7])
        self.APNO = Entry(self.sabteAirportPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.APNO.insert(0, k['values'][6])
        self.APNO.config(state=DISABLED)
        self.city = Entry(self.sabteAirportPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.city.insert(0, k['values'][5])
        self.country = Entry(self.sabteAirportPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.country.insert(0, k['values'][4])
        self.lon = Entry(self.sabteAirportPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.lon.insert(0, k['values'][3])
        self.lat = Entry(self.sabteAirportPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.lat.insert(0, k['values'][2])
        self.address = Entry(self.sabteAirportPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.address.insert(0, k['values'][1])
        self.inorout = Entry(self.sabteAirportPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.inorout.insert(0, k['values'][0])
        sabt = Button(self.sabteAirportPageRoot, text="ثبت", bg='blue', fg='white', font=('IRANSans', '15'),
                      command=self.editAirport2)
        sabt.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        # space2.pack()
        self.APN.pack()
        self.APNO.pack()
        self.city.pack()
        self.country.pack()
        self.lon.pack()
        self.lat.pack()
        self.address.pack()
        self.inorout.pack()
        space3.pack()
        sabt.pack()
        space4.pack()

    def editAirport2(self):
        url = 'http://www.rownaghsh.ir/upd.php'
        if self.inorout.get() == "داخلی":
            x = 1
        else:
            x = 0
        data2 = {"name_airport": str(self.APN.get()),
                "num_airport": str(self.APNO.get()),
                "city": str(self.city.get()),
                "country": str(self.country.get()),
                "latitude": float(self.lat.get()),
                "longitude": float(self.lon.get()),
                "addresses": str(self.address.get()),
                "internal": x
                }
        data = {"table": "origin_destination",
                "key": "num_airport",
                "value": self.APNO.get(),
                "columns": data2,
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        print(r.text)
        print(data1)
        self.sabteAirportPageRoot.destroy()
        self.AirportsRoot.destroy()
        self.AirportsRootFunc()

    def deleteAirport(self):
        self.listBoxAirport.bind('<Button-1>', self.listBoxAirport)
        curItem = self.listBoxAirport.focus()
        k = self.listBoxAirport.item(curItem)
        url = 'http://www.rownaghsh.ir/del.php'
        data = {
            "table": "origin_destination",
            "key": "num_airport",
            "value": str(k['values'][6]),
            "name_for_user": MyUsername,
            "password_for_user": MyPassword
        }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        self.AirportsRoot.destroy()
        self.AirportsRootFunc()

    def sabteAirport(self):
        self.sabteAirportPageRoot = Tk()
        self.sabteAirportPageRoot.title("ثبت فرودگاه")
        self.sabteAirportPageRoot.configure(bg='orange')
        title = Label(self.sabteAirportPageRoot, text="ثبت فرودگاه", font=('IRANSans', '22'), bg='orange')
        space = Label(self.sabteAirportPageRoot, text=" ", bg='orange')
        space1 = Label(self.sabteAirportPageRoot, text=" ", bg='orange')
        space2 = Label(self.sabteAirportPageRoot, text=" ", bg='orange')
        space3 = Label(self.sabteAirportPageRoot, text=" ", bg='orange')
        space4 = Label(self.sabteAirportPageRoot, text=" ", bg='orange')
        space5 = Label(self.sabteAirportPageRoot, text=" ", bg='orange')
        space6 = Label(self.sabteAirportPageRoot, text=" ", bg='orange')
        self.APN = Entry(self.sabteAirportPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.APN.insert(0, "نام فرودگاه")
        self.APNO = Entry(self.sabteAirportPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.APNO.insert(0, "شماره فرودگاه")
        self.city = Entry(self.sabteAirportPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.city.insert(0, "شهر")
        self.country = Entry(self.sabteAirportPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.country.insert(0, "کشور")
        self.lon = Entry(self.sabteAirportPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.lon.insert(0, "طول جغرافیایی")
        self.lat = Entry(self.sabteAirportPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.lat.insert(0, "عرض جغرافیایی")
        self.address = Entry(self.sabteAirportPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.address.insert(0, "آدرس")
        self.inorout = Entry(self.sabteAirportPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.inorout.insert(0, "داخلی یا خارجی")
        sabt = Button(self.sabteAirportPageRoot, text="ثبت", bg='blue', fg='white', font=('IRANSans', '15'),
                      command=self.sabteAirport2)
        sabt.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        # space2.pack()
        self.APN.pack()
        self.APNO.pack()
        self.city.pack()
        self.country.pack()
        self.lon.pack()
        self.lat.pack()
        self.address.pack()
        self.inorout.pack()
        space3.pack()
        sabt.pack()
        space4.pack()

    def sabteAirport2(self):
        url = 'http://www.rownaghsh.ir/origin_destination.php'
        if self.inorout.get()=='داخلی':
            x=1
        else:
            x=0
        data = {"name_airport": str(self.APN.get()),
                "num_airport": str(self.APNO.get()),
                "city": str(self.city.get()),
                "country": str(self.country.get()),
                "latitude": float(self.lat.get()),
                "longitude": float(self.lon.get()),
                "addresses": str(self.address.get()),
                "internal": x,
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        print(r.text)
        print(data1)
        self.sabteAirportPageRoot.destroy()
        self.AirportsRoot.destroy()
        self.AirportsRootFunc()

    def stewartsGroupRootFunc(self):
        self.stewartsGroupRoot = Tk()
        self.stewartsGroupRoot.title("گروه های مهمانداری")
        self.stewartsGroupRoot['bg'] = 'orange'
        space = Label(self.stewartsGroupRoot, text=" ", bg='orange')
        space1 = Label(self.stewartsGroupRoot, text=" ", bg='orange')
        space2 = Label(self.stewartsGroupRoot, text=" ", bg='orange')
        space3 = Label(self.stewartsGroupRoot, text=" ", bg='orange')
        space4 = Label(self.stewartsGroupRoot, text=" ", bg='orange')
        space5 = Label(self.stewartsGroupRoot, text=" ", bg='orange')
        title = Label(self.stewartsGroupRoot, text="گروه های مهمانداری", font=('IRANSans', '22'), bg='orange')
        cols = ('شماره مهماندار 6','شماره مهماندار 5','شماره مهماندار 4','شماره مهماندار 3','شماره مهماندار 2','شماره مهماندار 1','مدل هواپیما', 'تعداد مهمانداران Economy class',
                'تعداد مهمانداران Business class', 'تعداد مهمانداران First class', 'شماره گروه')
        self.listBoxSTG = ttk.Treeview(self.stewartsGroupRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=self.listBoxSTG.yview)
        self.listBoxSTG.configure(yscrollcommand=vsb.set)
        self.listBoxSTG.column("0", width=122, anchor="c")
        self.listBoxSTG.column("1", width=122, anchor="c")
        self.listBoxSTG.column("2", width=122, anchor="c")
        self.listBoxSTG.column("3", width=122, anchor="c")
        self.listBoxSTG.column("4", width=122, anchor="c")
        self.listBoxSTG.column("5", width=122, anchor="c")
        self.listBoxSTG.column("6", width=122, anchor="c")
        self.listBoxSTG.column("7", width=122, anchor="c")
        self.listBoxSTG.column("8", width=122, anchor="c")
        self.listBoxSTG.column("9", width=122, anchor="c")
        self.listBoxSTG.column("10", width=122, anchor="c")
        self.listBoxSTG.config(height=23)
        for col in cols:
            self.listBoxSTG.heading(col, text=col)
        url = 'http://www.rownaghsh.ir/memandaran.php'
        data = {'table': 'stewardess_group',
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        l = json.loads(r.text)
        print(l[1]['7'])
        for i in range(0, len(l)):
            if(len(l[i]['7'])==0):
                self.listBoxSTG.insert("", "end", values=(
                    '',
                    '',
                    '',
                    '',
                    '',
                    str(l[i]['1']),
                    str(l[i]['model']),
                    str(l[i]['stewardess_first_normal']),
                    str(l[i]['stewardess_first_bisness']),
                    str(l[i]['stewardess_first_class']),
                    str(l[i]['num_group'])
                ))
            elif(len(l[i]['7'])==1):
                self.listBoxSTG.insert("", "end", values=(
                    '',
                    '',
                    '',
                    '',
                    str(l[i]['7'][0]),
                    str(l[i]['1']),
                    str(l[i]['model']),
                    str(l[i]['stewardess_first_normal']),
                    str(l[i]['stewardess_first_bisness']),
                    str(l[i]['stewardess_first_class']),
                    str(l[i]['num_group'])
                ))
            elif(len(l[i]['7']) == 2):
                self.listBoxSTG.insert("", "end", values=(
                    '',
                    '',
                    '',
                    str(l[i]['7'][1]),
                    str(l[i]['7'][0]),
                    str(l[i]['1']),
                    str(l[i]['model']),
                    str(l[i]['stewardess_first_normal']),
                    str(l[i]['stewardess_first_bisness']),
                    str(l[i]['stewardess_first_class']),
                    str(l[i]['num_group'])
                ))
            elif(len(l[i]['7']) == 3):
                self.listBoxSTG.insert("", "end", values=(
                    '',
                    '',
                    str(l[i]['7'][2]),
                    str(l[i]['7'][1]),
                    str(l[i]['7'][0]),
                    str(l[i]['1']),
                    str(l[i]['model']),
                    str(l[i]['stewardess_first_normal']),
                    str(l[i]['stewardess_first_bisness']),
                    str(l[i]['stewardess_first_class']),
                    str(l[i]['num_group'])
                ))
            elif(len(l[i]['7']) == 4):
                self.listBoxSTG.insert("", "end", values=(
                    '',
                    str(l[i]['7'][3]),
                    str(l[i]['7'][2]),
                    str(l[i]['7'][1]),
                    str(l[i]['7'][0]),
                    str(l[i]['1']),
                    str(l[i]['model']),
                    str(l[i]['stewardess_first_normal']),
                    str(l[i]['stewardess_first_bisness']),
                    str(l[i]['stewardess_first_class']),
                    str(l[i]['num_group'])
                ))
            else:
                self.listBoxSTG.insert("", "end", values=(
                    str(l[i]['7'][4]),
                    str(l[i]['7'][3]),
                    str(l[i]['7'][2]),
                    str(l[i]['7'][1]),
                    str(l[i]['7'][0]),
                    str(l[i]['1']),
                    str(l[i]['model']),
                    str(l[i]['stewardess_first_normal']),
                    str(l[i]['stewardess_first_bisness']),
                    str(l[i]['stewardess_first_class']),
                    str(l[i]['num_group'])
                ))
        sabt = Button(self.stewartsGroupRoot, text="ثبت گروه مهمانداری", font=('IRANSans', '13'), fg='white', bg='blue', command=self.sabteStG)
        sabt.config(height=1, width=18)
        delete = Button(self.stewartsGroupRoot, text="حذف", font=('IRANSans', '13'), fg='white', bg='blue', command=self.deleteSTG)
        delete.config(height=1, width=18)
        # edit = Button(self.stewartsGroupRoot, text="ویرایش", font=('IRANSans', '13'), fg='white', bg='blue')
        # edit.config(height=1, width=18)
        space.pack()
        title.pack()
        space1.pack()
        self.listBoxSTG.pack()
        space2.pack()
        sabt.pack()
        # edit.pack()
        delete.pack()
        space3.pack()

    def deleteSTG(self):
        self.listBoxSTG.bind('<Button-1>', self.listBoxSTG)
        curItem = self.listBoxSTG.focus()
        k = self.listBoxSTG.item(curItem)
        url = 'http://www.rownaghsh.ir/del.php'
        data = {
            "table": "detail_stewardess_group",
            "key": "num_group",
            "value": str(k['values'][10]),
            "name_for_user": MyUsername,
            "password_for_user": MyPassword
        }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        self.stewartsGroupRoot.destroy()
        self.stewartsGroupRootFunc()

    def sabteStG(self):
        self.sabteSTGPageRoot = Tk()
        self.sabteSTGPageRoot.title("ثبت گروه مهمانداری")
        self.sabteSTGPageRoot.configure(bg='orange')
        title = Label(self.sabteSTGPageRoot, text="ثبت گروه مهمانداری", font=('IRANSans', '22'), bg='orange')
        space = Label(self.sabteSTGPageRoot, text=" ", bg='orange')
        space1 = Label(self.sabteSTGPageRoot, text=" ", bg='orange')
        space2 = Label(self.sabteSTGPageRoot, text=" ", bg='orange')
        space3 = Label(self.sabteSTGPageRoot, text=" ", bg='orange')
        space4 = Label(self.sabteSTGPageRoot, text=" ", bg='orange')
        space5 = Label(self.sabteSTGPageRoot, text=" ", bg='orange')
        space6 = Label(self.sabteSTGPageRoot, text=" ", bg='orange')
        self.gnofst = Entry(self.sabteSTGPageRoot, width=70, justify='right', font=('IRANSans', 13))
        self.gnofst.insert(0, "شماره گروه")
        self.nostffa = Entry(self.sabteSTGPageRoot, width=70, justify='right', font=('IRANSans', 13))
        self.nostffa.insert(0, "تعداد مهمانداران First class")
        self.nostfba = Entry(self.sabteSTGPageRoot, width=70, justify='right', font=('IRANSans', 13))
        self.nostfba.insert(0, "تعداد مهمانداران Business class")
        self.nostfea = Entry(self.sabteSTGPageRoot, width=70, justify='right', font=('IRANSans', 13))
        self.nostfea.insert(0, "تعداد مهمانداران Economy class")
        self.apmost = Entry(self.sabteSTGPageRoot, width=70, justify='right', font=('IRANSans', 13))
        self.apmost.insert(0, "مدل هواپیما")
        self.name1 = Entry(self.sabteSTGPageRoot, width=70, justify='right', font=('IRANSans', 13))
        self.name1.insert(0, "شماره مهماندار 1")
        self.name2 = Entry(self.sabteSTGPageRoot, width=70, justify='right', font=('IRANSans', 13))
        self.name2.insert(0, "شماره مهماندار 2")
        self.name3 = Entry(self.sabteSTGPageRoot, width=70, justify='right', font=('IRANSans', 13))
        self.name3.insert(0, "شماره مهماندار 3")
        self.name4 = Entry(self.sabteSTGPageRoot, width=70, justify='right', font=('IRANSans', 13))
        self.name4.insert(0, "شماره مهماندار 4")
        self.name5 = Entry(self.sabteSTGPageRoot, width=70, justify='right', font=('IRANSans', 13))
        self.name5.insert(0, "شماره مهماندار 5")
        self.name6 = Entry(self.sabteSTGPageRoot, width=70, justify='right', font=('IRANSans', 13))
        self.name6.insert(0, "شماره مهماندار 6")
        sabt = Button(self.sabteSTGPageRoot, text="ثبت", bg='blue', fg='white', font=('IRANSans', '13'),
                      command=self.sabteSTG2)
        sabt.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        space2.pack()
        self.gnofst.pack()
        self.nostffa.pack()
        self.nostfba.pack()
        self.nostfea.pack()
        self.apmost.pack()
        self.name1.pack()
        self.name2.pack()
        self.name3.pack()
        self.name4.pack()
        self.name5.pack()
        self.name6.pack()
        space3.pack()
        sabt.pack()
        space4.pack()

    def sabteSTG2(self):
        if self.name1.get()=='شماره مهماندار 1':
            x1=''
        else:
            x1=self.name1.get()
        if self.name2.get()=='شماره مهماندار 2':
            x2=''
        else:
            x2=self.name2.get()
        if self.name3.get()=='شماره مهماندار 3':
            x3=''
        else:
            x3=self.name3.get()
        if self.name4.get()=='شماره مهماندار 4':
            x4=''
        else:
            x4=self.name4.get()
        if self.name5.get()=='شماره مهماندار 5':
            x5=''
        else:
            x5=self.name5.get()
        if self.name6.get()=='شماره مهماندار 6':
            x6=''
        else:
            x6=self.name6.get()
        url = 'http://www.rownaghsh.ir/detail_stewardess_group.php'
        data = {"num_group": str(self.gnofst.get()),
                "stewardess_first_class": int(self.nostffa.get()),
                "stewardess_first_bisness": int(self.nostfba.get()),
                "stewardess_first_normal": int(self.nostfea.get()),
                "model": str(self.apmost.get()),
                "stewardess": [str(x1), str(x2),
                               str(x3), str(x4),
                               str(x5), str(x6)],
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        print(r.text)
        print(data1)
        self.sabteSTGPageRoot.destroy()
        self.stewartsGroupRoot.destroy()
        self.stewartsGroupRootFunc()

    def WagesGroupRootFunc(self):
        self.WagesGroupRoot = Tk()
        self.WagesGroupRoot.title("سمت ها و شغل ها")
        self.WagesGroupRoot['bg'] = 'orange'
        space = Label(self.WagesGroupRoot, text=" ", bg='orange')
        space1 = Label(self.WagesGroupRoot, text=" ", bg='orange')
        space2 = Label(self.WagesGroupRoot, text=" ", bg='orange')
        space3 = Label(self.WagesGroupRoot, text=" ", bg='orange')
        space4 = Label(self.WagesGroupRoot, text=" ", bg='orange')
        space5 = Label(self.WagesGroupRoot, text=" ", bg='orange')
        title = Label(self.WagesGroupRoot, text="سمت ها و شغل ها", font=('IRANSans', '22'), bg='orange')
        cols = ('توضیحات', 'مزایا', 'حقوق', 'نام شغل')
        self.listBoxWage = ttk.Treeview(self.WagesGroupRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=self.listBoxWage.yview)
        self.listBoxWage.configure(yscrollcommand=vsb.set)
        self.listBoxWage.column("0", width=970, anchor="c")
        self.listBoxWage.column("1", width=100, anchor="c")
        self.listBoxWage.column("2", width=100, anchor="c")
        self.listBoxWage.column("3", width=170, anchor="c")
        self.listBoxWage.config(height=20)
        for col in cols:
            self.listBoxWage.heading(col, text=col)
        url = 'http://www.rownaghsh.ir/req.php'
        data = {'table': 'wages',
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        l = json.loads(r.text)
        for i in range(0, len(l)):
            self.listBoxWage.insert("", "end", values=(
                str(l[i]['descript']),
                str(l[i]['Advantages']),
                str(l[i]['wage']),
                str(l[i]['job'])
            ))
        sabt = Button(self.WagesGroupRoot, text="ثبت شغل", font=('IRANSans', '13'), bg='blue', fg='white', command=self.sabteWage)
        sabt.config(height=1, width=20)
        delete = Button(self.WagesGroupRoot, text="حذف", font=('IRANSans', '13'), bg='blue', fg='white', command=self.deleteWage)
        delete.config(height=1, width=20)
        edit = Button(self.WagesGroupRoot, text="ویرایش", font=('IRANSans', '13'), bg='blue', fg='white', command=self.editWage)
        edit.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        self.listBoxWage.pack()
        space2.pack()
        sabt.pack()
        edit.pack()
        delete.pack()
        space3.pack()

    def editWage(self):
        self.listBoxWage.bind('<Button-1>', self.listBoxWage)
        curItem = self.listBoxWage.focus()
        k = self.listBoxWage.item(curItem)
        self.sabteWagesPageRoot = Tk()
        self.sabteWagesPageRoot.title("ویرایش شفل")
        self.sabteWagesPageRoot.configure(bg='orange')
        title = Label(self.sabteWagesPageRoot, text="ویرایش شغل", font=('IRANSans', '22'), bg='orange')
        space = Label(self.sabteWagesPageRoot, text=" ", bg='orange')
        space1 = Label(self.sabteWagesPageRoot, text=" ", bg='orange')
        space2 = Label(self.sabteWagesPageRoot, text=" ", bg='orange')
        space3 = Label(self.sabteWagesPageRoot, text=" ", bg='orange')
        space4 = Label(self.sabteWagesPageRoot, text=" ", bg='orange')
        space5 = Label(self.sabteWagesPageRoot, text=" ", bg='orange')
        space6 = Label(self.sabteWagesPageRoot, text=" ", bg='orange')
        self.jobn = Entry(self.sabteWagesPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.jobn.insert(0, k['values'][3])
        self.jobn.config(state=DISABLED)
        self.salary = Entry(self.sabteWagesPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.salary.insert(0, k['values'][2])
        self.benef = Entry(self.sabteWagesPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.benef.insert(0, k['values'][1])
        self.tozi = Entry(self.sabteWagesPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.tozi.insert(0, k['values'][0])
        sabt = Button(self.sabteWagesPageRoot, text="ثبت", bg='blue', fg='white', font=('IRANSans', '15'),
                      command=self.editWage2)
        sabt.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        space2.pack()
        self.jobn.pack()
        self.salary.pack()
        self.benef.pack()
        self.tozi.pack()
        space3.pack()
        sabt.pack()
        space4.pack()

    def editWage2(self):
        url = 'http://www.rownaghsh.ir/upd.php'
        data2 = {"job": str(self.jobn.get()),
                "wage": int(self.salary.get()),
                "Advantages": str(self.benef.get()),
                "descript": str(self.tozi.get())
                }
        data = {"table": "wages",
                "key": "job",
                "value": self.jobn.get(),
                "columns": data2,
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        print(r.text)
        print(data1)
        self.sabteWagesPageRoot.destroy()
        self.WagesGroupRoot.destroy()
        self.WagesGroupRootFunc()

    def deleteWage(self):
        self.listBoxWage.bind('<Button-1>', self.listBoxWage)
        curItem = self.listBoxWage.focus()
        k = self.listBoxWage.item(curItem)
        url = 'http://www.rownaghsh.ir/del.php'
        data = {
            "table": "wages",
            "key": "job",
            "value": str(k['values'][3]),
            "name_for_user": MyUsername,
            "password_for_user": MyPassword
        }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        self.WagesGroupRoot.destroy()
        self.WagesGroupRootFunc()

    def sabteWage(self):
        self.sabteWagesPageRoot = Tk()
        self.sabteWagesPageRoot.title("ثبت شفل")
        self.sabteWagesPageRoot.configure(bg='orange')
        title = Label(self.sabteWagesPageRoot, text="ثبت شغل", font=('IRANSans', '22'), bg='orange')
        space = Label(self.sabteWagesPageRoot, text=" ", bg='orange')
        space1 = Label(self.sabteWagesPageRoot, text=" ", bg='orange')
        space2 = Label(self.sabteWagesPageRoot, text=" ", bg='orange')
        space3 = Label(self.sabteWagesPageRoot, text=" ", bg='orange')
        space4 = Label(self.sabteWagesPageRoot, text=" ", bg='orange')
        space5 = Label(self.sabteWagesPageRoot, text=" ", bg='orange')
        space6 = Label(self.sabteWagesPageRoot, text=" ", bg='orange')
        self.jobn = Entry(self.sabteWagesPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.jobn.insert(0, "نام شغل")
        self.salary = Entry(self.sabteWagesPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.salary.insert(0, "حقوق")
        self.benef = Entry(self.sabteWagesPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.benef.insert(0, "مزایا")
        self.tozi = Entry(self.sabteWagesPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.tozi.insert(0, "توضیحات")
        sabt = Button(self.sabteWagesPageRoot, text="ثبت", bg='blue', fg='white', font=('IRANSans', '15'),
                      command=self.sabteWage2)
        sabt.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        space2.pack()
        self.jobn.pack()
        self.salary.pack()
        self.benef.pack()
        self.tozi.pack()
        space3.pack()
        sabt.pack()
        space4.pack()

    def sabteWage2(self):
        url = 'http://www.rownaghsh.ir/wages.php'
        data = {"job": str(self.jobn.get()),
                "wage": int(self.salary.get()),
                "Advantages": str(self.benef.get()),
                "descript": str(self.tozi.get()),
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        print(r.text)
        print(data1)
        self.sabteWagesPageRoot.destroy()
        self.WagesGroupRoot.destroy()
        self.WagesGroupRootFunc()

    def pricesRootFunc(self):
        self.pricesRoot = Tk()
        self.pricesRoot.title("قیمت ها")
        self.pricesRoot['bg'] = 'orange'
        space = Label(self.pricesRoot, text=" ", bg='orange')
        space1 = Label(self.pricesRoot, text=" ", bg='orange')
        space2 = Label(self.pricesRoot, text=" ", bg='orange')
        space3 = Label(self.pricesRoot, text=" ", bg='orange')
        space4 = Label(self.pricesRoot, text=" ", bg='orange')
        space5 = Label(self.pricesRoot, text=" ", bg='orange')
        title = Label(self.pricesRoot, text="قیمت ها", font=('IRANSans', '22'), bg='orange')
        cols = ('تاریخ ثبت','قیمت Economy class','قیمت Business class','قیمت First class', 'مدل هواپیما', 'کد فرودگاه مقصد', 'کد فرودگاه مبدأ')
        self.listBoxPrice = ttk.Treeview(self.pricesRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=self.listBoxPrice.yview)
        self.listBoxPrice.configure(yscrollcommand=vsb.set)
        self.listBoxPrice.column("0", width=188, anchor="c")
        self.listBoxPrice.column("1", width=188, anchor="c")
        self.listBoxPrice.column("2", width=188, anchor="c")
        self.listBoxPrice.column("3", width=188, anchor="c")
        self.listBoxPrice.column("4", width=188, anchor="c")
        self.listBoxPrice.column("5", width=188, anchor="c")
        self.listBoxPrice.column("6", width=188, anchor="c")
        self.listBoxPrice.config(height=22)
        for col in cols:
            self.listBoxPrice.heading(col, text=col)
        url = 'http://www.rownaghsh.ir/req.php'
        data = {'table': 'price',
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        l = json.loads(r.text)
        for i in range(0, len(l)):
            self.listBoxPrice.insert("", "end", values=(
                str(l[i]['date_price']),
                str(l[i]['price_economi']),
                str(l[i]['price_bisness']),
                str(l[i]['price_first_class']),
                str(l[i]['model']),
                str(l[i]['num_airport_destination']),
                str(l[i]['num_airport_origin'])
            ))
        sabt = Button(self.pricesRoot, text="ثبت قیمت", font=('IRANSans', '13'), fg='white', bg='blue', command=self.sabtePrice)
        sabt.config(height=1, width=20)
        delete = Button(self.pricesRoot, text="حذف", font=('IRANSans', '13'), fg='white', bg='blue', command=self.deletePrice)
        delete.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        self.listBoxPrice.pack()
        space2.pack()
        sabt.pack()
        delete.pack()
        space3.pack()

    def deletePrice(self):
        self.listBoxPrice.bind('<Button-1>', self.listBoxPrice)
        curItem = self.listBoxPrice.focus()
        k = self.listBoxPrice.item(curItem)
        url = 'http://www.rownaghsh.ir/del_price.php'
        data = {
            "num_airport_origin": str(k['values'][6]),
            "num_airport_destination": str(k['values'][5]),
            "model": str(k['values'][4]),
            "date_price": str(k['values'][0]),
            "name_for_user": MyUsername,
            "password_for_user": MyPassword
        }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        self.pricesRoot.destroy()
        self.pricesRootFunc()

    def sabtePrice(self):
        self.sabtePricePageRoot = Tk()
        self.sabtePricePageRoot.title("ثبت قیمت")
        self.sabtePricePageRoot.configure(bg='orange')
        title = Label(self.sabtePricePageRoot, text="ثبت قیمت", font=('IRANSans', '22'), bg='orange')
        space = Label(self.sabtePricePageRoot, text=" ", bg='orange')
        space1 = Label(self.sabtePricePageRoot, text=" ", bg='orange')
        space2 = Label(self.sabtePricePageRoot, text=" ", bg='orange')
        space3 = Label(self.sabtePricePageRoot, text=" ", bg='orange')
        space4 = Label(self.sabtePricePageRoot, text=" ", bg='orange')
        space5 = Label(self.sabtePricePageRoot, text=" ", bg='orange')
        space6 = Label(self.sabtePricePageRoot, text=" ", bg='orange')
        self.apnoor = Entry(self.sabtePricePageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.apnoor.insert(0, "شماره فرودگاه مبدا")
        self.apnode = Entry(self.sabtePricePageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.apnode.insert(0, "شماره فرودگاه مقصد")
        self.apmf = Entry(self.sabtePricePageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.apmf.insert(0, "مدل هواپیما")
        self.fcp = Entry(self.sabtePricePageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.fcp.insert(0, "قیمت First class")
        self.bcp = Entry(self.sabtePricePageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.bcp.insert(0, "قیمت Business class")
        self.ecp = Entry(self.sabtePricePageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.ecp.insert(0, "قیمت Economy class")
        self.dateop = Entry(self.sabtePricePageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.dateop.insert(0, "تاریخ ثبت")
        sabt = Button(self.sabtePricePageRoot, text="ثبت", bg='blue', fg='white', font=('IRANSans', '15'),
                      command=self.sabtePrice2)
        sabt.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        space2.pack()
        self.apnoor.pack()
        self.apnode.pack()
        self.apmf.pack()
        self.fcp.pack()
        self.bcp.pack()
        self.ecp.pack()
        self.dateop.pack()
        space3.pack()
        sabt.pack()
        space4.pack()

    def sabtePrice2(self):
        url = 'http://www.rownaghsh.ir/price.php'
        data = {"num_airport_origin": str(self.apnoor.get()),
                "num_airport_destination": int(self.apnode.get()),
                "model": str(self.apmf.get()),
                "date_price": str(self.dateop.get()),
                "price_bisness": int(self.bcp.get()),
                "price_first_class": int(self.fcp.get()),
                "price_economi": int(self.ecp.get()),
                "name_for_user": MyUsername,
                "password_for_user": MyPassword
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        print(r.text)
        print(data1)
        self.sabtePricePageRoot.destroy()
        self.pricesRoot.destroy()
        self.pricesRootFunc()

#######################################################################################################################
#                                             Make An Object From My Class                                            #
#######################################################################################################################
ALLPAGES = all()
#######################################################################################################################
#                                                          Root                                                       #
#######################################################################################################################
def MENU():
    Menu = Tk()
    Menu.state('zoomed')
    Menu.title("شرکت هواپیمایی")
    Menu['bg'] = 'orange'
    space = Label(Menu, text=" ", bg='orange')
    space1 = Label(Menu, text=" ", bg='orange')
    space2 = Label(Menu, text=" ", bg='orange')
    space3 = Label(Menu, text=" ", bg='orange')
    title = Label(Menu, text="شرکت هواپیمایی", font=('IRANSans', '22', 'bold'), bg='orange')

    users = Button(Menu, text="کاربر ها", font=('IRANSans', '13'), bg='Blue', fg='white', command=ALLPAGES.users)
    airplans = Button(Menu, text="هواپیما ها", font=('IRANSans', '13'), command=ALLPAGES.airplansRootFunc, bg='Blue',
                      fg='white')
    pilots = Button(Menu, text="خلبان ها", font=('IRANSans', '13'), command=ALLPAGES.PilotRootFunc, bg='Blue',
                    fg='white')
    co_pilots = Button(Menu, text="کمک خلبان ها", font=('IRANSans', '13'), command=ALLPAGES.CoPilotRootFunc, bg='Blue',
                       fg='white')
    flight_engineers = Button(Menu, text="مهندسین پرواز", font=('IRANSans', '13'),
                              command=ALLPAGES.FlightEngineerRootFunc, bg='Blue', fg='white')
    stewardess = Button(Menu, text="مهمانداران", font=('IRANSans', '13'), command=ALLPAGES.StewardsRootFunc, bg='Blue',
                        fg='white')
    flight_schedule = Button(Menu, text="برنامه ‌پرواز ها", font=('IRANSans', '13'),
                             command=ALLPAGES.FlightSkechuleRootFunc, bg='Blue',
                             fg='white')  # show 2 airports and airplane flight
    flights = Button(Menu, text="پرواز ها", font=('IRANSans', '13'), command=ALLPAGES.FlightsRootFunc, bg='Blue',
                     fg='white')  # show 2 airports and airplane flight passengers
    airports = Button(Menu, text="فرودگاه ها", font=('IRANSans', '13'), command=ALLPAGES.AirportsRootFunc, bg='Blue',
                      fg='white')
    stewardess_group = Button(Menu, text="گروه های مهمانداری", font=('IRANSans', '13'),
                              command=ALLPAGES.stewartsGroupRootFunc, bg='Blue', fg='white')  # etelaate mehmandaran
    wages = Button(Menu, text="سمت ها و شغل ها", font=('IRANSans', '13'), command=ALLPAGES.WagesGroupRootFunc,
                   bg='Blue', fg='white')
    prices = Button(Menu, text="قیمت ها", font=('IRANSans', '13'), command=ALLPAGES.pricesRootFunc, bg='Blue',
                    fg='white')

    users.config(height=1, width=80)
    airplans.config(height=1, width=80)
    pilots.config(height=1, width=80)
    co_pilots.config(height=1, width=80)
    flight_engineers.config(height=1, width=80)
    stewardess.config(height=1, width=80)
    flight_schedule.config(height=1, width=80)
    airports.config(height=1, width=80)
    stewardess_group.config(height=1, width=80)
    wages.config(height=1, width=80)
    flights.config(height=1, width=80)
    prices.config(height=1, width=80)

    space.pack()
    title.pack()
    space2.pack()
    users.pack()
    airplans.pack()
    pilots.pack()
    co_pilots.pack()
    flight_engineers.pack()
    stewardess.pack()
    flights.pack()
    flight_schedule.pack()
    airports.pack()
    stewardess_group.pack()
    wages.pack()
    prices.pack()
    space1.pack()

def MENUForOrdineriUsers():
    Menu = Tk()
    Menu.state('zoomed')
    Menu.title("شرکت هواپیمایی")
    Menu['bg'] = 'orange'
    space = Label(Menu, text=" ", bg='orange')
    space1 = Label(Menu, text=" ", bg='orange')
    space2 = Label(Menu, text=" ", bg='orange')
    space3 = Label(Menu, text=" ", bg='orange')
    title = Label(Menu, text="شرکت هواپیمایی", font=('IRANSans', '22', 'bold'), bg='orange')

    # users = Button(Menu, text="کاربر ها", font=('IRANSans', '13'), bg='Blue', fg='white', command=ALLPAGES.users)
    airplans = Button(Menu, text="هواپیما ها", font=('IRANSans', '13'), command=ALLPAGES.airplansRootFunc, bg='Blue',
                      fg='white')
    pilots = Button(Menu, text="خلبان ها", font=('IRANSans', '13'), command=ALLPAGES.PilotRootFunc, bg='Blue',
                    fg='white')
    co_pilots = Button(Menu, text="کمک خلبان ها", font=('IRANSans', '13'), command=ALLPAGES.CoPilotRootFunc, bg='Blue',
                       fg='white')
    flight_engineers = Button(Menu, text="مهندسین پرواز", font=('IRANSans', '13'),
                              command=ALLPAGES.FlightEngineerRootFunc, bg='Blue', fg='white')
    stewardess = Button(Menu, text="مهمانداران", font=('IRANSans', '13'), command=ALLPAGES.StewardsRootFunc, bg='Blue',
                        fg='white')
    flight_schedule = Button(Menu, text="برنامه ‌پرواز ها", font=('IRANSans', '13'),
                             command=ALLPAGES.FlightSkechuleRootFunc, bg='Blue',
                             fg='white')  # show 2 airports and airplane flight
    flights = Button(Menu, text="پرواز ها", font=('IRANSans', '13'), command=ALLPAGES.FlightsRootFunc, bg='Blue',
                     fg='white')  # show 2 airports and airplane flight passengers
    airports = Button(Menu, text="فرودگاه ها", font=('IRANSans', '13'), command=ALLPAGES.AirportsRootFunc, bg='Blue',
                      fg='white')
    stewardess_group = Button(Menu, text="گروه های مهمانداری", font=('IRANSans', '13'),
                              command=ALLPAGES.stewartsGroupRootFunc, bg='Blue', fg='white')  # etelaate mehmandaran
    wages = Button(Menu, text="سمت ها و شغل ها", font=('IRANSans', '13'), command=ALLPAGES.WagesGroupRootFunc,
                   bg='Blue', fg='white')
    prices = Button(Menu, text="قیمت ها", font=('IRANSans', '13'), command=ALLPAGES.pricesRootFunc, bg='Blue',
                    fg='white')

    # users.config(height=1, width=80)
    airplans.config(height=1, width=80)
    pilots.config(height=1, width=80)
    co_pilots.config(height=1, width=80)
    flight_engineers.config(height=1, width=80)
    stewardess.config(height=1, width=80)
    flight_schedule.config(height=1, width=80)
    airports.config(height=1, width=80)
    stewardess_group.config(height=1, width=80)
    wages.config(height=1, width=80)
    flights.config(height=1, width=80)
    prices.config(height=1, width=80)

    space.pack()
    title.pack()
    space2.pack()
    # users.pack()
    airplans.pack()
    pilots.pack()
    co_pilots.pack()
    flight_engineers.pack()
    stewardess.pack()
    flights.pack()
    flight_schedule.pack()
    airports.pack()
    stewardess_group.pack()
    wages.pack()
    prices.pack()
    space1.pack()

def checkuser():
    url='http://www.rownaghsh.ir/login.php'
    data={
        "name":username.get(),
        "password":password.get()
    }
    data1=json.dumps(data)
    r=requests.post(url, data=data1)
    l=json.loads(r.text)
    if l['ok']=='ok':
        global MyUsername
        MyUsername = username.get()
        global MyPassword
        MyPassword = password.get()
        if username.get()=='masterr' and password.get()=='1234':
            MENU()
        else:
            MENUForOrdineriUsers()
        root.destroy()
    else:
        warning.config(text="!نام کاربری و یا رمز عبور اشتباه است")

root = Tk()
root.state('zoomed')
root['bg'] = 'orange'
root.title(" شرکت هواپیمایی")
space = Label(root, text=" ", bg='orange')
space1 = Label(root, text=" ", bg='orange')
space2 = Label(root, text=" ", bg='orange')
space3 = Label(root, text=" ", bg='orange')
space4 = Label(root, text=" ", bg='orange')
space5 = Label(root, text=" ", bg='orange')
space6 = Label(root, text=" ", bg='orange')
space7 = Label(root, text=" ", bg='orange')
space8 = Label(root, text=" ", bg='orange')
space9 = Label(root, text=" ", bg='orange')
space10 = Label(root, text=" ", bg='orange')
space11 = Label(root, text=" ", bg='orange')
space12 = Label(root, text=" ", bg='orange')
space13 = Label(root, text=" ", bg='orange')
space14 = Label(root, text=" ", bg='orange')
title = Label(root, text=".سلام، خوش آمدید", font=('IRANSans', '20', 'bold'), bg='orange')
title1 = Label(root, text=".لطفاً نام کاربری و رمز عبور خود را وارد کنید", font=('IRANSans', '18'), bg='Orange')
warning = Label(root, font=('IRANSans', '18'), bg='Orange', fg='red')
username = Entry(root, width=60, justify='right', font=('IRANSans', 12))
username.insert(0, "نام کاربری")
password = Entry(root, width=60, justify='right', font=('IRANSans', 12))
password.insert(0, "رمزعبور")

sabtname = Button(root, text="ورود", bg='blue', fg='white', font=('IRANSans', '14'), command=checkuser)
sabtname.config(height=1, width=20)
space.pack()
title.pack()
space1.pack()
space2.pack()
space3.pack()
space4.pack()
space5.pack()
space6.pack()
title1.pack()
space7.pack()
space8.pack()
username.pack()
space9.pack()
password.pack()
space10.pack()
space11.pack()
sabtname.pack()
space12.pack()
space13.pack()
space14.pack()
warning.pack()
root.mainloop()
#######################################################################################################################
#                                                         End                                                         #
#######################################################################################################################