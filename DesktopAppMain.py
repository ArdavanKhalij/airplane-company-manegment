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
valuelistForNamesOfComboBox = []
myname1 = " "
myname2 = " "
NameOfUser = "ADMIN"
#######################################################################################################################
#                                                       Pages                                                         #
#######################################################################################################################
class all() :

    def airplansRootFunc(self):
        airplansRoot = Tk()
        airplansRoot.title("هواپیما ها")
        airplansRoot['bg'] = 'orange'
        space = Label(airplansRoot, text=" ", bg='orange')
        space1 = Label(airplansRoot, text=" ", bg='orange')
        space2 = Label(airplansRoot, text=" ", bg='orange')
        space3 = Label(airplansRoot, text=" ", bg='orange')
        space4 = Label(airplansRoot, text=" ", bg='orange')
        space5 = Label(airplansRoot, text=" ", bg='orange')
        title = Label(airplansRoot, text="هواپیما ها", font=('IRANSans', '22'), fg="black", bg='orange')
        cols = ('ظرفیت بار' ,'تعداد Economy class','تعداد Business class', 'تعداد First class', 'مدل', 'شماره هواپیما')
        listBox = ttk.Treeview(airplansRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=listBox.yview)
        listBox.configure(yscrollcommand=vsb.set)
        listBox.column("0", width=220, anchor="c")
        listBox.column("1", width=220, anchor="c")
        listBox.column("2", width=220, anchor="c")
        listBox.column("3", width=220, anchor="c")
        listBox.column("4", width=220, anchor="c")
        listBox.column("5", width=220, anchor="c")
        listBox.config(height=20)
        for col in cols:
            listBox.heading(col, text=col)
        url = 'http://www.rownaghsh.ir/req.php'
        data={'table':'airplane'}
        data1=json.dumps(data)
        r=requests.post(url, data=data1)
        l=json.loads(r.text)
        for i in range(0, len(l)):
            listBox.insert("", "end", values=(
                str(l[i]['bar']),
                str(l[i]['economi']),
                str(l[i]['bisness']),
                str(l[i]['first_class']),
                str(l[i]['model'])
                # str(l[i]['num_airplanes'])
            ))
        sabt = Button(airplansRoot, text="ثبت هواپیما", font=('IRANSans', '13'), fg='white', bg='blue', command=self.sabteAirplane)
        sabt.config(height=1, width=20)
        delete = Button(airplansRoot, text="حذف", font=('IRANSans', '13'), fg='white', bg='blue')
        delete.config(height=1, width=20)
        edit = Button(airplansRoot, text="ثبت هواپیما از مدل موجود", font=('IRANSans', '13'), fg='white', bg='blue', command=self.sabteAirplane3)
        edit.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        listBox.pack()
        space2.pack()
        sabt.pack()
        edit.pack()
        delete.pack()
        space3.pack()

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
              "economi":int(self.tedadEconomyClass.get())
              }
        data1=json.dumps(data)
        r=requests.post(url, data=data1)
        print(r.text)
        print(data)

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
                "model": str(self.model2.get())
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        print(r.text)
        print(data)

    def PilotRootFunc(self):
        PilotRoot = Tk()
        PilotRoot.title("خلبان ها")
        PilotRoot['bg'] = 'orange'
        space = Label(PilotRoot, text=" ", bg='orange')
        space1 = Label(PilotRoot, text=" ", bg='orange')
        space2 = Label(PilotRoot, text=" ", bg='orange')
        space3 = Label(PilotRoot, text=" ", bg='orange')
        space4 = Label(PilotRoot, text=" ", bg='orange')
        space5 = Label(PilotRoot, text=" ", bg='orange')
        title = Label(PilotRoot, text="خلبان ها", font=('IRANSans', '22'), bg='orange')
        cols = (
        'تلفن 3', 'نام آشنا 3', 'تلفن 2', 'نام آشنا 2', 'تلفن 1', 'نام آشنا1', 'تعداد فرزندان', 'شماره تلفن همسر',
        'کد ملی همسر', 'نام همسر', 'تاریخ تولد', 'شماره تلفن', 'شماره خلبان', 'کد ملی', 'جنسیت', 'نام خانوادگی',
        'نام')
        listBox2 = ttk.Treeview(PilotRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=listBox2.yview)
        listBox2.configure(yscrollcommand=vsb.set)
        listBox2.column("0", width=80, anchor="c")
        listBox2.column("1", width=80, anchor="c")
        listBox2.column("2", width=80, anchor="c")
        listBox2.column("3", width=80, anchor="c")
        listBox2.column("4", width=80, anchor="c")
        listBox2.column("5", width=80, anchor="c")
        listBox2.column("6", width=80, anchor="c")
        listBox2.column("7", width=80, anchor="c")
        listBox2.column("8", width=80, anchor="c")
        listBox2.column("9", width=80, anchor="c")
        listBox2.column("10", width=80, anchor="c")
        listBox2.column("11", width=80, anchor="c")
        listBox2.column("12", width=80, anchor="c")
        listBox2.column("13", width=80, anchor="c")
        listBox2.column("14", width=80, anchor="c")
        listBox2.column("15", width=80, anchor="c")
        listBox2.column("16", width=80, anchor="c")
        listBox2.config(height=20)
        for col in cols:
            listBox2.heading(col, text=col)
        sabt = Button(PilotRoot, text="ثبت خلبان", font=('IRANSans', '13'), fg='white', bg='blue',
                      command=self.sabtePilot)
        sabt.config(height=1, width=20)
        delete = Button(PilotRoot, text="حذف", font=('IRANSans', '13'), fg='white', bg='blue')
        delete.config(height=1, width=20)
        edit = Button(PilotRoot, text="ویرایش", font=('IRANSans', '13'), fg='white', bg='blue')
        edit.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        listBox2.pack()
        space2.pack()
        sabt.pack()
        edit.pack()
        delete.pack()
        space3.pack()

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
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        print(r.text)
        print(data1)

    def CoPilotRootFunc(self):
        CoPilotRoot = Tk()
        CoPilotRoot.title("کمک خلبان ها")
        CoPilotRoot['bg'] = 'orange'
        space = Label(CoPilotRoot, text=" ", bg='orange')
        space1 = Label(CoPilotRoot, text=" ", bg='orange')
        space2 = Label(CoPilotRoot, text=" ", bg='orange')
        space3 = Label(CoPilotRoot, text=" ", bg='orange')
        space4 = Label(CoPilotRoot, text=" ", bg='orange')
        space5 = Label(CoPilotRoot, text=" ", bg='orange')
        title = Label(CoPilotRoot, text="کمک خلبان ها", font=('IRANSans', '22'), bg='orange')
        cols = ('تلفن 3','نام آشنا 3','تلفن 2','نام آشنا 2','تلفن 1','نام آشنا1','تعداد فرزندان','شماره تلفن همسر','کد ملی همسر','نام همسر','تاریخ تولد','شماره تلفن' ,'شماره کمک خلبان','کد ملی', 'جنسیت', 'نام خانوادگی', 'نام')
        listBox2 = ttk.Treeview(CoPilotRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=listBox2.yview)
        listBox2.configure(yscrollcommand=vsb.set)
        listBox2.column("0", width=80, anchor="c")
        listBox2.column("1", width=80, anchor="c")
        listBox2.column("2", width=80, anchor="c")
        listBox2.column("3", width=80, anchor="c")
        listBox2.column("4", width=80, anchor="c")
        listBox2.column("5", width=80, anchor="c")
        listBox2.column("6", width=80, anchor="c")
        listBox2.column("7", width=80, anchor="c")
        listBox2.column("8", width=80, anchor="c")
        listBox2.column("9", width=80, anchor="c")
        listBox2.column("10", width=80, anchor="c")
        listBox2.column("11", width=80, anchor="c")
        listBox2.column("12", width=80, anchor="c")
        listBox2.column("13", width=80, anchor="c")
        listBox2.column("14", width=80, anchor="c")
        listBox2.column("15", width=80, anchor="c")
        listBox2.column("16", width=80, anchor="c")
        listBox2.config(height=20)
        for col in cols:
            listBox2.heading(col, text=col)
        sabt = Button(CoPilotRoot, text="ثبت کمک خلبان", font=('IRANSans', '13'), fg='white', bg='blue', command=self.sabteCopilot)
        sabt.config(height=1, width=20)
        delete = Button(CoPilotRoot, text="حذف", font=('IRANSans', '13'), fg='white', bg='blue')
        delete.config(height=1, width=20)
        edit = Button(CoPilotRoot, text="ویرایش", font=('IRANSans', '13'), fg='white', bg='blue')
        edit.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        listBox2.pack()
        space2.pack()
        sabt.pack()
        edit.pack()
        delete.pack()
        space3.pack()

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
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        print(r.text)
        print(data1)

    def FlightEngineerRootFunc(self):
        FlightEngineerRoot = Tk()
        FlightEngineerRoot.title("مهندسین پرواز")
        FlightEngineerRoot['bg'] = 'orange'
        space = Label(FlightEngineerRoot, text=" ", bg='orange')
        space1 = Label(FlightEngineerRoot, text=" ", bg='orange')
        space2 = Label(FlightEngineerRoot, text=" ", bg='orange')
        space3 = Label(FlightEngineerRoot, text=" ", bg='orange')
        space4 = Label(FlightEngineerRoot, text=" ", bg='orange')
        space5 = Label(FlightEngineerRoot, text=" ", bg='orange')
        title = Label(FlightEngineerRoot, text="مهندسین پرواز", font=('IRANSans', '22'), bg='orange')
        cols = (
            'تلفن 3', 'نام آشنا 3', 'تلفن 2', 'نام آشنا 2', 'تلفن 1', 'نام آشنا1', 'تعداد فرزندان', 'شماره تلفن همسر',
            'کد ملی همسر', 'نام همسر', 'تاریخ تولد', 'شماره تلفن', 'شماره مهندس پرواز', 'کد ملی', 'جنسیت', 'نام خانوادگی',
            'نام')
        listBox2 = ttk.Treeview(FlightEngineerRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=listBox2.yview)
        listBox2.configure(yscrollcommand=vsb.set)
        listBox2.column("0", width=80, anchor="c")
        listBox2.column("1", width=80, anchor="c")
        listBox2.column("2", width=80, anchor="c")
        listBox2.column("3", width=80, anchor="c")
        listBox2.column("4", width=80, anchor="c")
        listBox2.column("5", width=80, anchor="c")
        listBox2.column("6", width=80, anchor="c")
        listBox2.column("7", width=80, anchor="c")
        listBox2.column("8", width=80, anchor="c")
        listBox2.column("9", width=80, anchor="c")
        listBox2.column("10", width=80, anchor="c")
        listBox2.column("11", width=80, anchor="c")
        listBox2.column("12", width=80, anchor="c")
        listBox2.column("13", width=80, anchor="c")
        listBox2.column("14", width=80, anchor="c")
        listBox2.column("15", width=80, anchor="c")
        listBox2.column("16", width=80, anchor="c")
        listBox2.config(height=20)
        for col in cols:
            listBox2.heading(col, text=col)
        sabt = Button(FlightEngineerRoot, text="ثبت مهندس پرواز", font=('IRANSans', '13'), fg='white', bg='blue',
                      command=self.sabteFlightEngineer)
        sabt.config(height=1, width=20)
        delete = Button(FlightEngineerRoot, text="حذف", font=('IRANSans', '13'), fg='white', bg='blue')
        delete.config(height=1, width=20)
        edit = Button(FlightEngineerRoot, text="ویرایش", font=('IRANSans', '13'), fg='white', bg='blue')
        edit.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        listBox2.pack()
        space2.pack()
        sabt.pack()
        edit.pack()
        delete.pack()
        space3.pack()

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
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        print(r.text)
        print(data1)

    def StewardsRootFunc(self):
        StewardsRoot = Tk()
        StewardsRoot.title("مهمانداران")
        StewardsRoot['bg'] = 'orange'
        space = Label(StewardsRoot, text=" ", bg='orange')
        space1 = Label(StewardsRoot, text=" ", bg='orange')
        space2 = Label(StewardsRoot, text=" ", bg='orange')
        space3 = Label(StewardsRoot, text=" ", bg='orange')
        space4 = Label(StewardsRoot, text=" ", bg='orange')
        space5 = Label(StewardsRoot, text=" ", bg='orange')
        title = Label(StewardsRoot, text="مهمانداران", font=('IRANSans', '22'), fg="Blue", bg='orange')
        cols = (
        'تلفن 3', 'نام آشنا 3', 'تلفن 2', 'نام آشنا 2', 'تلفن 1', 'نام آشنا1','وضعیت', 'تعداد فرزندان', 'شماره تلفن همسر',
        'کد ملی همسر', 'نام همسر', 'تاریخ تولد', 'شماره تلفن', 'شماره کمک خلبان', 'کد ملی', 'جنسیت', 'نام خانوادگی',
        'نام')
        listBox2 = ttk.Treeview(StewardsRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=listBox2.yview)
        listBox2.configure(yscrollcommand=vsb.set)
        listBox2.column("0", width=75, anchor="c")
        listBox2.column("1", width=75, anchor="c")
        listBox2.column("2", width=75, anchor="c")
        listBox2.column("3", width=75, anchor="c")
        listBox2.column("4", width=75, anchor="c")
        listBox2.column("5", width=75, anchor="c")
        listBox2.column("6", width=75, anchor="c")
        listBox2.column("7", width=75, anchor="c")
        listBox2.column("8", width=75, anchor="c")
        listBox2.column("9", width=75, anchor="c")
        listBox2.column("10", width=75, anchor="c")
        listBox2.column("11", width=75, anchor="c")
        listBox2.column("12", width=75, anchor="c")
        listBox2.column("13", width=75, anchor="c")
        listBox2.column("14", width=75, anchor="c")
        listBox2.column("15", width=75, anchor="c")
        listBox2.column("16", width=75,anchor="c")
        listBox2.column("17", width=75, anchor="c")
        listBox2.config(height=20)
        for col in cols:
            listBox2.heading(col, text=col)
        sabt = Button(StewardsRoot, text="ثبت مهماندار", font=('IRANSans', '13'), fg='white', bg='blue',
                      command=self.sabteSteward)
        sabt.config(height=1, width=20)
        delete = Button(StewardsRoot, text="حذف", font=('IRANSans', '13'), fg='white', bg='blue')
        delete.config(height=1, width=20)
        edit = Button(StewardsRoot, text="ویرایش", font=('IRANSans', '13'), fg='white', bg='blue')
        edit.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        listBox2.pack()
        space2.pack()
        sabt.pack()
        edit.pack()
        delete.pack()
        space3.pack()

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
        self.sname = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.sname.insert(0, "نام")
        self.slname = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.slname.insert(0, "نام خانوادگی")
        self.sgender = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.sgender.insert(0, "جنسیت")
        self.smellicode = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.smellicode.insert(0, "کدملی")
        self.scono = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.scono.insert(0, "شماره مهماندار")
        self.sphno = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.sphno.insert(0, "شماره تلفن")
        self.sbd = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.sbd.insert(0, "تاریخ تولد")
        self.swn = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.swn.insert(0, "نام همسر")
        self.smcw = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.smcw.insert(0, "کد ملی همسر")
        self.swphno = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.swphno.insert(0, "شماره تلفن همسر")
        self.scn = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.scn.insert(0, "تعداد فرزندان")
        self.s = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.s.insert(0, "وضعیت")
        self.sf1 = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.sf1.insert(0, "نام آشنا 1")
        self.sfph1 = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.sfph1.insert(0, "تلفن 1")
        self.sf2 = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.sf2.insert(0, "نام آشنا 2")
        self.sfph2 = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.sfph2.insert(0, "تلفن 2")
        self.sf3 = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 13))
        self.sf3.insert(0, "نام آشنا 3")
        self.sfph3 = Entry(self.sabteStewardPageRoot, width=110, justify='right', font=('IRANSans', 13))
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
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        print(r.text)
        print(data1)

    def FlightsRootFunc(self):
        FlightsRoot = Tk()
        FlightsRoot.title("برنامه پرواز ها")
        FlightsRoot['bg'] = 'orange'
        space = Label(FlightsRoot, text=" ", bg='orange')
        space1 = Label(FlightsRoot, text=" ", bg='orange')
        space2 = Label(FlightsRoot, text=" ", bg='orange')
        space3 = Label(FlightsRoot, text=" ", bg='orange')
        space4 = Label(FlightsRoot, text=" ", bg='orange')
        space5 = Label(FlightsRoot, text=" ", bg='orange')
        title = Label(FlightsRoot, text="برنامه پرواز ها", font=('IRANSans', '22'), fg="Blue", bg='orange')
        cols = ('داخلی یا خارجی', 'وضعیت پرواز', 'وزن کل بار', 'مسافران First class', 'مسافران business class', 'مسافران Economy class',
                'شماره گروه مهمانداری', 'شماره مهندس پرواز', 'شماره کمک خلبان', 'شماره خلبان', 'شماره پروار')
        listBox5 = ttk.Treeview(FlightsRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=listBox5.yview)
        listBox5.configure(yscrollcommand=vsb.set)
        listBox5.column("0", width=120, anchor="c")
        listBox5.column("1", width=125, anchor="c")
        listBox5.column("2", width=120, anchor="c")
        listBox5.column("3", width=125, anchor="c")
        listBox5.column("4", width=120, anchor="c")
        listBox5.column("5", width=125, anchor="c")
        listBox5.column("6", width=120, anchor="c")
        listBox5.column("7", width=125, anchor="c")
        listBox5.column("8", width=120, anchor="c")
        listBox5.column("9", width=125, anchor="c")
        listBox5.column("10", width=120, anchor="c")
        listBox5.config(height=20)
        for col in cols:
            listBox5.heading(col, text=col)
        sabt = Button(FlightsRoot, text="ثبت پرواز", font=('IRANSans', '13'), fg='white', bg='blue', command=self.sabteFlight)
        sabt.config(height=1, width=18)
        delete = Button(FlightsRoot, text="حذف", font=('IRANSans', '13'), fg='white', bg='blue')
        delete.config(height=1, width=18)
        edit = Button(FlightsRoot, text="ویرایش", font=('IRANSans', '13'), fg='white', bg='blue')
        edit.config(height=1, width=18)
        space.pack()
        title.pack()
        space1.pack()
        listBox5.pack()
        space2.pack()
        sabt.pack()
        edit.pack()
        delete.pack()
        space3.pack()

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
                "internal": x
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        print(r.text)
        print(data1)

    def FlightSkechuleRootFunc(self):
        FlightSkechuleRoot = Tk()
        FlightSkechuleRoot.title("برنامه پرواز های آخرین هفته")
        FlightSkechuleRoot['bg'] = 'orange'
        space = Label(FlightSkechuleRoot, text=" ", bg='orange')
        space1 = Label(FlightSkechuleRoot, text=" ", bg='orange')
        space2 = Label(FlightSkechuleRoot, text=" ", bg='orange')
        space3 = Label(FlightSkechuleRoot, text=" ", bg='orange')
        space4 = Label(FlightSkechuleRoot, text=" ", bg='orange')
        space5 = Label(FlightSkechuleRoot, text=" ", bg='orange')
        title = Label(FlightSkechuleRoot, text="برنامه پرواز های آخرین هفته", font=('IRANSans', '22'), bg='orange')
        cols = ('تاریخ فرود','تاریخ پرواز','زمان نشستن', 'زمان پرواز', 'شماره پرواز', 'مقصد', 'مبدأ', 'شماره هواپیما')
        listBox6 = ttk.Treeview(FlightSkechuleRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=listBox6.yview)
        listBox6.configure(yscrollcommand=vsb.set)
        listBox6.column("0", width=170, anchor="c")
        listBox6.column("1", width=170, anchor="c")
        listBox6.column("2", width=170, anchor="c")
        listBox6.column("3", width=170, anchor="c")
        listBox6.column("4", width=170, anchor="c")
        listBox6.column("5", width=170, anchor="c")
        listBox6.column("6", width=170, anchor="c")
        listBox6.column("7", width=170, anchor="c")
        listBox6.config(height=20)
        for col in cols:
            listBox6.heading(col, text=col)
        sabt = Button(FlightSkechuleRoot, text="ثبت پرواز", font=('IRANSans', '13'), fg='white', bg='blue', command=self.sabteFS)
        sabt.config(height=1, width=18)
        delete = Button(FlightSkechuleRoot, text="حذف", font=('IRANSans', '13'), fg='white', bg='blue')
        delete.config(height=1, width=18)
        edit = Button(FlightSkechuleRoot, text="ویرایش", font=('IRANSans', '13'), fg='white', bg='blue')
        edit.config(height=1, width=18)
        space.pack()
        title.pack()
        space1.pack()
        listBox6.pack()
        space2.pack()
        sabt.pack()
        edit.pack()
        delete.pack()
        space3.pack()

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
        self.countr = Entry(self.sabteFSPageRoot, width=70, justify='right', font=('IRANSans', 16))
        self.countr.insert(0, "کشور")
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
        self.countr.pack()
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
                "date_down": str(self.ld.get())
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        print(r.text)
        print(data1)

    def AirportsRootFunc(self):
        AirportsRoot = Tk()
        AirportsRoot.title("فرودگاه ها")
        AirportsRoot['bg'] = 'orange'
        space = Label(AirportsRoot, text=" ", bg='orange')
        space1 = Label(AirportsRoot, text=" ", bg='orange')
        space2 = Label(AirportsRoot, text=" ", bg='orange')
        space3 = Label(AirportsRoot, text=" ", bg='orange')
        space4 = Label(AirportsRoot, text=" ", bg='orange')
        space5 = Label(AirportsRoot, text=" ", bg='orange')
        title = Label(AirportsRoot, text="فرودگاه ها", font=('IRANSans', '22'), bg='orange')
        cols = ('داخلی یا خارجی','آدرس','عرض جغرافیایی', 'طول جغرافیایی', 'کشور', 'شهر', 'شماره فرودگاه', 'نام فرودگاه')
        listBox7 = ttk.Treeview(AirportsRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=listBox7.yview)
        listBox7.configure(yscrollcommand=vsb.set)
        listBox7.column("0", width=125, anchor="c")
        listBox7.column("1", width=460, anchor="c")
        listBox7.column("2", width=125, anchor="c")
        listBox7.column("3", width=125, anchor="c")
        listBox7.column("4", width=125, anchor="c")
        listBox7.column("5", width=125, anchor="c")
        listBox7.column("6", width=125, anchor="c")
        listBox7.column("7", width=125, anchor="c")
        listBox7.config(height=20)
        for col in cols:
            listBox7.heading(col, text=col)
        url = 'http://www.rownaghsh.ir/req.php'
        data = {'table': 'origin_destination'}
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        l = json.loads(r.text)
        print(l)
        for i in range(0, len(l)):
            if l[i]['internal']==1:
                x='داخلی'
            else:
                x='خارجی'
            listBox7.insert("", "end", values=(
                x,
                str(l[i]['addresses']),
                str(l[i]['latitude']),
                str(l[i]['longitude']),
                str(l[i]['country']),
                str(l[i]['city']),
                str(l[i]['num_airport']),
                str(l[i]['name_airport'])
                # str(l[i]['num_airplanes'])
            ))
        sabt = Button(AirportsRoot, text="ثبت فرودگاه", font=('IRANSans', '13'), fg='white', bg='blue', command=self.sabteAirport)
        sabt.config(height=1, width=20)
        delete = Button(AirportsRoot, text="حذف", font=('IRANSans', '13'),fg='white', bg='blue')
        delete.config(height=1, width=20)
        edit = Button(AirportsRoot, text="ویرایش", font=('IRANSans', '13'),fg='white', bg='blue')
        edit.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        listBox7.pack()
        space2.pack()
        sabt.pack()
        edit.pack()
        delete.pack()
        space3.pack()

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
        if self.inorout.get()=="داخلی":
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
                "internal": x
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        print(r.text)
        print(data1)

    def stewartsGroupRootFunc(self):
        stewartsGroupRoot = Tk()
        stewartsGroupRoot.title("گروه های مهمانداری")
        stewartsGroupRoot['bg'] = 'orange'
        space = Label(stewartsGroupRoot, text=" ", bg='orange')
        space1 = Label(stewartsGroupRoot, text=" ", bg='orange')
        space2 = Label(stewartsGroupRoot, text=" ", bg='orange')
        space3 = Label(stewartsGroupRoot, text=" ", bg='orange')
        space4 = Label(stewartsGroupRoot, text=" ", bg='orange')
        space5 = Label(stewartsGroupRoot, text=" ", bg='orange')
        title = Label(stewartsGroupRoot, text="گروه های مهمانداری", font=('IRANSans', '22'), bg='orange')
        cols = ('نام 6','نام 5','نام 4','نام 3','نام 2','نام 1','مدل هواپیما', 'تعداد مهمانداران Economy class',
                'تعداد مهمانداران Business class', 'تعداد مهمانداران First class', 'شماره گروه')
        listBox8 = ttk.Treeview(stewartsGroupRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=listBox8.yview)
        listBox8.configure(yscrollcommand=vsb.set)
        listBox8.column("0", width=122, anchor="c")
        listBox8.column("1", width=122, anchor="c")
        listBox8.column("2", width=122, anchor="c")
        listBox8.column("3", width=122, anchor="c")
        listBox8.column("4", width=122, anchor="c")
        listBox8.column("5", width=122, anchor="c")
        listBox8.column("6", width=122, anchor="c")
        listBox8.column("7", width=122, anchor="c")
        listBox8.column("8", width=122, anchor="c")
        listBox8.column("9", width=122, anchor="c")
        listBox8.column("10", width=122, anchor="c")
        listBox8.config(height=20)
        for col in cols:
            listBox8.heading(col, text=col)
        sabt = Button(stewartsGroupRoot, text="ثبت گروه مهمانداری", font=('IRANSans', '13'), fg='white', bg='blue', command=self.sabteStG)
        sabt.config(height=1, width=18)
        delete = Button(stewartsGroupRoot, text="حذف", font=('IRANSans', '13'), fg='white', bg='blue')
        delete.config(height=1, width=18)
        edit = Button(stewartsGroupRoot, text="ویرایش", font=('IRANSans', '13'), fg='white', bg='blue')
        edit.config(height=1, width=18)
        space.pack()
        title.pack()
        space1.pack()
        listBox8.pack()
        space2.pack()
        sabt.pack()
        edit.pack()
        delete.pack()
        space3.pack()

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
        self.name1.insert(0, "نام 1")
        self.name2 = Entry(self.sabteSTGPageRoot, width=70, justify='right', font=('IRANSans', 13))
        self.name2.insert(0, "نام 2")
        self.name3 = Entry(self.sabteSTGPageRoot, width=70, justify='right', font=('IRANSans', 13))
        self.name3.insert(0, "نام 3")
        self.name4 = Entry(self.sabteSTGPageRoot, width=70, justify='right', font=('IRANSans', 13))
        self.name4.insert(0, "نام 4")
        self.name5 = Entry(self.sabteSTGPageRoot, width=70, justify='right', font=('IRANSans', 13))
        self.name5.insert(0, "نام 5")
        self.name6 = Entry(self.sabteSTGPageRoot, width=70, justify='right', font=('IRANSans', 13))
        self.name6.insert(0, "نام 6")
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
        url = 'http://www.rownaghsh.ir/detail_stewardess_group.php'
        data = {"num_group": str(self.gnofst.get()),
                "stewardess_first_class": int(self.nostffa.get()),
                "stewardess_first_bisness": int(self.nostfba.get()),
                "stewardess_first_normal": int(self.nostfea.get()),
                "model": str(self.apmost.get()),
                "stewardess": [str(self.name1.get()), str(self.name2.get()),
                               str(self.name3.get()), str(self.name4.get()),
                               str(self.name5.get()), str(self.name6.get())]
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        print(r.text)
        print(data1)

    def WagesGroupRootFunc(self):
        WagesGroupRoot = Tk()
        WagesGroupRoot.title("سمت ها و شغل ها")
        WagesGroupRoot['bg'] = 'orange'
        space = Label(WagesGroupRoot, text=" ", bg='orange')
        space1 = Label(WagesGroupRoot, text=" ", bg='orange')
        space2 = Label(WagesGroupRoot, text=" ", bg='orange')
        space3 = Label(WagesGroupRoot, text=" ", bg='orange')
        space4 = Label(WagesGroupRoot, text=" ", bg='orange')
        space5 = Label(WagesGroupRoot, text=" ", bg='orange')
        title = Label(WagesGroupRoot, text="سمت ها و شغل ها", font=('IRANSans', '22'), bg='orange')
        cols = ('توضیحات', 'مزایا', 'حقوق', 'نام شغل')
        listBox9 = ttk.Treeview(WagesGroupRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=listBox9.yview)
        listBox9.configure(yscrollcommand=vsb.set)
        listBox9.column("0", width=970, anchor="c")
        listBox9.column("1", width=100, anchor="c")
        listBox9.column("2", width=100, anchor="c")
        listBox9.column("3", width=170, anchor="c")
        listBox9.config(height=20)
        for col in cols:
            listBox9.heading(col, text=col)
        url = 'http://www.rownaghsh.ir/req.php'
        data = {'table': 'wages'}
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        l = json.loads(r.text)
        print(l)
        for i in range(0, len(l)):
            listBox9.insert("", "end", values=(
                str(l[i]['descript']),
                str(l[i]['Advantages']),
                str(l[i]['wage']),
                str(l[i]['job'])
                # str(l[i]['num_airplanes'])
            ))
        sabt = Button(WagesGroupRoot, text="ثبت شغل", font=('IRANSans', '13'), bg='blue', fg='white', command=self.sabteWage)
        sabt.config(height=1, width=20)
        delete = Button(WagesGroupRoot, text="حذف", font=('IRANSans', '13'), bg='blue', fg='white')
        delete.config(height=1, width=20)
        edit = Button(WagesGroupRoot, text="ویرایش", font=('IRANSans', '13'), bg='blue', fg='white')
        edit.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        listBox9.pack()
        space2.pack()
        sabt.pack()
        edit.pack()
        delete.pack()
        space3.pack()

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
                "descript": str(self.tozi.get())
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        print(r.text)
        print(data1)

    def pricesRootFunc(self):
        pricesRoot = Tk()
        pricesRoot.title("قیمت ها")
        pricesRoot['bg'] = 'orange'
        space = Label(pricesRoot, text=" ", bg='orange')
        space1 = Label(pricesRoot, text=" ", bg='orange')
        space2 = Label(pricesRoot, text=" ", bg='orange')
        space3 = Label(pricesRoot, text=" ", bg='orange')
        space4 = Label(pricesRoot, text=" ", bg='orange')
        space5 = Label(pricesRoot, text=" ", bg='orange')
        title = Label(pricesRoot, text="قیمت ها", font=('IRANSans', '22'), bg='orange')
        cols = ('تاریخ ثبت','قیمت Economy class','قیمت Business class','قیمت First class', 'مدل هواپیما', 'کد فرودگاه مقصد', 'کد فرودگاه مبدأ')
        listBox9 = ttk.Treeview(pricesRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=listBox9.yview)
        listBox9.configure(yscrollcommand=vsb.set)
        listBox9.column("0", width=188, anchor="c")
        listBox9.column("1", width=188, anchor="c")
        listBox9.column("2", width=188, anchor="c")
        listBox9.column("3", width=188, anchor="c")
        listBox9.column("4", width=188, anchor="c")
        listBox9.column("5", width=188, anchor="c")
        listBox9.column("6", width=188, anchor="c")
        listBox9.config(height=22)
        for col in cols:
            listBox9.heading(col, text=col)
        url = 'http://www.rownaghsh.ir/req.php'
        data = {'table': 'price'}
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        l = json.loads(r.text)
        print(l)
        for i in range(0, len(l)):
            listBox9.insert("", "end", values=(
                str(l[i]['date_price']),
                str(l[i]['price_economi']),
                str(l[i]['price_bisness']),
                str(l[i]['price_first_class']),
                str(l[i]['model']),
                str(l[i]['num_airport_destination']),
                str(l[i]['num_airport_origin'])
                # str(l[i]['num_airplanes'])
            ))
        sabt = Button(pricesRoot, text="ثبت قیمت", font=('IRANSans', '13'), fg='white', bg='blue', command=self.sabtePrice)
        sabt.config(height=1, width=20)
        delete = Button(pricesRoot, text="حذف", font=('IRANSans', '13'), fg='white', bg='blue')
        delete.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        listBox9.pack()
        space2.pack()
        sabt.pack()
        delete.pack()
        space3.pack()

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
                "price_economi": int(self.ecp.get())
                }
        data1 = json.dumps(data)
        r = requests.post(url, data=data1)
        print(r.text)
        print(data1)

#######################################################################################################################
#                                             Make An Object From My Class                                            #
#######################################################################################################################
ALLPAGES = all()
#######################################################################################################################
#                                                          Root                                                       #
#######################################################################################################################
Menu = Tk()
Menu.state('zoomed')
Menu.title("شرکت هواپیمایی")
Menu['bg'] = 'orange'
space = Label(Menu, text=" ", bg='orange')
space1 = Label(Menu, text=" ", bg='orange')
space2 = Label(Menu, text=" ", bg='orange')
space3 = Label(Menu, text=" ", bg='orange')
title = Label(Menu, text="شرکت هواپیمایی", font=('IRANSans', '22', 'bold'), bg='orange')

airplans = Button(Menu, text="هواپیما ها", font=('IRANSans', '14'), command=ALLPAGES.airplansRootFunc, bg='Blue', fg='white')
pilots = Button(Menu, text="خلبان ها", font=('IRANSans', '14'), command=ALLPAGES.PilotRootFunc, bg='Blue', fg='white')
co_pilots = Button(Menu, text="کمک خلبان ها", font=('IRANSans', '14'), command=ALLPAGES.CoPilotRootFunc, bg='Blue', fg='white')
flight_engineers = Button(Menu, text="مهندسین پرواز", font=('IRANSans', '14'), command=ALLPAGES.FlightEngineerRootFunc, bg='Blue', fg='white')
stewardess = Button(Menu, text="مهمانداران", font=('IRANSans', '14'), command=ALLPAGES.StewardsRootFunc, bg='Blue', fg='white')
flight_schedule = Button(Menu, text="برنامه ‌پرواز های آخرین هفته", font=('IRANSans', '14'), command=ALLPAGES.FlightSkechuleRootFunc, bg='Blue', fg='white') #show 2 airports and airplane flight
flights = Button(Menu, text="برنامه ‌پرواز ها", font=('IRANSans', '14'), command=ALLPAGES.FlightsRootFunc, bg='Blue', fg='white') #show 2 airports and airplane flight passengers
airports = Button(Menu, text="فرودگاه ها", font=('IRANSans', '14'), command=ALLPAGES.AirportsRootFunc, bg='Blue', fg='white')
stewardess_group = Button(Menu, text="گروه های مهمانداری", font=('IRANSans', '14'), command=ALLPAGES.stewartsGroupRootFunc, bg='Blue', fg='white') #etelaate mehmandaran
wages = Button(Menu, text="سمت ها و شغل ها", font=('IRANSans', '14'), command=ALLPAGES.WagesGroupRootFunc, bg='Blue', fg='white')
prices = Button(Menu, text="قیمت ها", font=('IRANSans', '14'), command=ALLPAGES.pricesRootFunc, bg='Blue', fg='white')

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

# space.pack()
title.pack()
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
Menu.mainloop()
#######################################################################################################################
#                                                         End                                                         #
#######################################################################################################################
