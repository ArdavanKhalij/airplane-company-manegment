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
    # def menu(self):
    #     addToNames = name2.get()
    #     myname2 = addToNames
    #     myname1 = name.get()
    #     isItInThere = False
    #     for i in valuelistForNamesOfComboBox:
    #         if i==addToNames:
    #             isItInThere = True
    #             break
    #         else:
    #             isItInThere = False
    #     if not isItInThere:
    #         valuelistForNamesOfComboBox.append(addToNames)
    #     with open('listfile.txt', 'w') as filehandle:
    #         for listitem in valuelistForNamesOfComboBox:
    #             if listitem!="" and listitem!= "  نام و نام خانوادگی":
    #                 filehandle.write('%s\n' % listitem)
    #     Menu = Tk()
    #     Menu.attributes("-fullscreen", True)
    #     Menu.title("شرکت هواپیمایی")
    #     Menu['bg'] = 'orange'
    #     space = Label(Menu, text=" ", bg='orange')
    #     space1 = Label(Menu, text=" ", bg='orange')
    #     space2 = Label(Menu, text=" ", bg='orange')
    #     space3 = Label(Menu, text=" ", bg='orange')
    #     title = Label(Menu, text="شرکت هواپیمایی", font=('IRANSans', '22', 'bold'))
    #
    #     airplans = Button(Menu, text="هواپیما ها", font=('IRANSans', '20'), command=self.airplansRootFunc, )
    #     pilots = Button(Menu, text="خلبان ها", font=('IRANSans', '20'), command=self.PilotRootFunc)
    #     co_pilots = Button(Menu, text="کمک خلبان ها", font=('IRANSans', '20'), command=self.CoPilotRootFunc)
    #     flight_engineers = Button(Menu, text="مهندسین پرواز", font=('IRANSans', '20'), command=self.FlightEngineerRootFunc)
    #     stewardess = Button(Menu, text="مهمانداران", font=('IRANSans', '20'), command=self.StewardsRootFunc)
    #     flight_schedule = Button(Menu, text="برنامه ‌پرواز های آخرین هفته", font=('IRANSans', '20'), command=self.FlightSkechuleRootFunc) #show 2 airports and airplane flight
    #     flights = Button(Menu, text="برنامه ‌پرواز ها", font=('IRANSans', '20'), command=self.FlightsRootFunc) #show 2 airports and airplane flight passengers
    #     airports = Button(Menu, text="فرودگاه ها", font=('IRANSans', '20'), command=self.AirportsRootFunc)
    #     stewardess_group = Button(Menu, text="گروه های مهمانداری", font=('IRANSans', '20'), command=self.stewartsGroupRootFunc) #etelaate mehmandaran
    #     wages = Button(Menu, text="سمت ها و شغل ها", font=('IRANSans', '20'), command=self.WagesGroupRootFunc)
    #     prices = Button(Menu, text="قیمت ها", font=('IRANSans', '20'), command=self.pricesRootFunc)
    #
    #     airplans.config(height=3, width=80)
    #     pilots.config(height=3, width=80)
    #     co_pilots.config(height=3, width=80)
    #     flight_engineers.config(height=3, width=80)
    #     stewardess.config(height=3, width=80)
    #     flight_schedule.config(height=3, width=80)
    #     airports.config(height=3, width=80)
    #     stewardess_group.config(height=3, width=80)
    #     wages.config(height=3, width=80)
    #     flights.config(height=3, width=80)
    #     prices.config(height=3, width=80)
    #
    #     space.pack()
    #     airplans.pack()
    #     pilots.pack()
    #     co_pilots.pack()
    #     flight_engineers.pack()
    #     stewardess.pack()
    #     flights.pack()
    #     flight_schedule.pack()
    #     airports.pack()
    #     stewardess_group.pack()
    #     wages.pack()
    #     prices.pack()
    #     space1.pack()
    #
    #     if myname1 != "  نام و نام خانوادگی" or myname1 != " ":
    #         global NameOfUser
    #         NameOfUser = myname1
    #     else:
    #         NameOfUser = myname2
    #     root.destroy()

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
        sabt = Button(airplansRoot, text="ثبت هواپیما", font=('IRANSans', '13'), fg='white', bg='blue', command=self.sabteAirplane)
        sabt.config(height=1, width=20)
        delete = Button(airplansRoot, text="حذف", font=('IRANSans', '13'), fg='white', bg='blue')
        delete.config(height=1, width=20)
        edit = Button(airplansRoot, text="ویرایش", font=('IRANSans', '13'), fg='white', bg='blue')
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
        listBox5.column("0", width=125, anchor="c")
        listBox5.column("1", width=125, anchor="c")
        listBox5.column("2", width=125, anchor="c")
        listBox5.column("3", width=125, anchor="c")
        listBox5.column("4", width=125, anchor="c")
        listBox5.column("5", width=125, anchor="c")
        listBox5.column("6", width=125, anchor="c")
        listBox5.column("7", width=125, anchor="c")
        listBox5.column("8", width=125, anchor="c")
        listBox5.column("9", width=125, anchor="c")
        listBox5.column("10", width=125, anchor="c")
        listBox5.config(height=28)
        for col in cols:
            listBox5.heading(col, text=col)
        sabt = Button(FlightsRoot, text="ثبت پرواز", font=('IRANSans', '20'))
        sabt.config(height=2, width=18)
        delete = Button(FlightsRoot, text="حذف", font=('IRANSans', '20'))
        delete.config(height=2, width=18)
        edit = Button(FlightsRoot, text="ویرایش", font=('IRANSans', '20'))
        edit.config(height=2, width=18)
        tozih = Button(FlightsRoot, text="مشخصات پرواز", font=('IRANSans', '20'), command=self.tozih2)
        tozih.config(height=2, width=18)
        space.pack()
        title.pack()
        space1.pack()
        listBox5.pack()
        space2.pack()
        sabt.pack()
        edit.pack()
        delete.pack()
        tozih.pack()
        space3.pack()

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
        title = Label(FlightSkechuleRoot, text="برنامه پرواز های آخرین هفته", font=('IRANSans', '22'), fg="Blue", bg='orange')
        cols = ('زمان نشستن', 'زمان پرواز', 'شماره پرواز', 'مقصد', 'مبدأ', 'شماره هواپیما')
        listBox6 = ttk.Treeview(FlightSkechuleRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=listBox6.yview)
        listBox6.configure(yscrollcommand=vsb.set)
        listBox6.column("0", width=230, anchor="c")
        listBox6.column("1", width=229, anchor="c")
        listBox6.column("2", width=229, anchor="c")
        listBox6.column("3", width=229, anchor="c")
        listBox6.column("4", width=229, anchor="c")
        listBox6.column("5", width=229, anchor="c")
        listBox6.config(height=28)
        for col in cols:
            listBox6.heading(col, text=col)
        sabt = Button(FlightSkechuleRoot, text="ثبت پرواز", font=('IRANSans', '20'))
        sabt.config(height=2, width=18)
        delete = Button(FlightSkechuleRoot, text="حذف", font=('IRANSans', '20'))
        delete.config(height=2, width=18)
        edit = Button(FlightSkechuleRoot, text="ویرایش", font=('IRANSans', '20'))
        edit.config(height=2, width=18)
        tozih = Button(FlightSkechuleRoot, text="مشخصات پرواز", font=('IRANSans', '20'), command=self.tozih2)
        tozih.config(height=2, width=18)
        space.pack()
        title.pack()
        space1.pack()
        listBox6.pack()
        space2.pack()
        sabt.pack()
        edit.pack()
        delete.pack()
        tozih.pack()
        space3.pack()

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
        title = Label(AirportsRoot, text="فرودگاه ها", font=('IRANSans', '22'), fg="Blue", bg='orange')
        cols = ('داخلی یا خارجی','آدرس','عرض جغرافیایی', 'طول جغرافیایی', 'کشور', 'شهر', 'شماره فرودگاه', 'نام فرودگاه')
        listBox7 = ttk.Treeview(AirportsRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=listBox7.yview)
        listBox7.configure(yscrollcommand=vsb.set)
        listBox7.column("0", width=175, anchor="c")
        listBox7.column("1", width=175, anchor="c")
        listBox7.column("2", width=175, anchor="c")
        listBox7.column("3", width=175, anchor="c")
        listBox7.column("4", width=175, anchor="c")
        listBox7.column("5", width=175, anchor="c")
        listBox7.column("6", width=175, anchor="c")
        listBox7.column("7", width=175, anchor="c")
        listBox7.config(height=30)
        for col in cols:
            listBox7.heading(col, text=col)
        sabt = Button(AirportsRoot, text="ثبت فرودگاه", font=('IRANSans', '20'))
        sabt.config(height=2, width=20)
        delete = Button(AirportsRoot, text="حذف", font=('IRANSans', '20'))
        delete.config(height=2, width=20)
        edit = Button(AirportsRoot, text="ویرایش", font=('IRANSans', '20'))
        edit.config(height=2, width=20)
        space.pack()
        title.pack()
        space1.pack()
        listBox7.pack()
        space2.pack()
        sabt.pack()
        edit.pack()
        delete.pack()
        space3.pack()

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
        title = Label(stewartsGroupRoot, text="گروه های مهمانداری", font=('IRANSans', '22'), fg="Blue", bg='orange')
        cols = ('مدل هواپیما', 'تعداد مهمانداران Economy class', 'تعداد مهمانداران Business class', 'تعداد مهمانداران First class', 'شماره گروه')
        listBox8 = ttk.Treeview(stewartsGroupRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=listBox8.yview)
        listBox8.configure(yscrollcommand=vsb.set)
        listBox8.column("0", width=280, anchor="c")
        listBox8.column("1", width=280, anchor="c")
        listBox8.column("2", width=280, anchor="c")
        listBox8.column("3", width=280, anchor="c")
        listBox8.column("4", width=280, anchor="c")
        listBox8.config(height=28)
        for col in cols:
            listBox8.heading(col, text=col)
        sabt = Button(stewartsGroupRoot, text="ثبت فرودگاه", font=('IRANSans', '20'))
        sabt.config(height=2, width=18)
        delete = Button(stewartsGroupRoot, text="حذف", font=('IRANSans', '20'))
        delete.config(height=2, width=18)
        edit = Button(stewartsGroupRoot, text="ویرایش", font=('IRANSans', '20'))
        edit.config(height=2, width=18)
        tozih = Button(stewartsGroupRoot, text="اطّلاعات مهمانداران", font=('IRANSans', '20'), command=self.tozih3)
        tozih.config(height=2, width=18)
        space.pack()
        title.pack()
        space1.pack()
        listBox8.pack()
        space2.pack()
        sabt.pack()
        edit.pack()
        tozih.pack()
        delete.pack()
        space3.pack()

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
        title = Label(WagesGroupRoot, text="سمت ها و شغل ها", font=('IRANSans', '22'), fg="Blue", bg='orange')
        cols = ('توضیحات', 'مزایا', 'حقوق', 'نام شغل')
        listBox9 = ttk.Treeview(WagesGroupRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=listBox9.yview)
        listBox9.configure(yscrollcommand=vsb.set)
        listBox9.column("0", width=1000, anchor="c")
        listBox9.column("1", width=110, anchor="c")
        listBox9.column("2", width=110, anchor="c")
        listBox9.column("3", width=180, anchor="c")
        listBox9.config(height=30)
        for col in cols:
            listBox9.heading(col, text=col)
        sabt = Button(WagesGroupRoot, text="ثبت شغل", font=('IRANSans', '20'))
        sabt.config(height=2, width=20)
        delete = Button(WagesGroupRoot, text="حذف", font=('IRANSans', '20'))
        delete.config(height=2, width=20)
        edit = Button(WagesGroupRoot, text="ویرایش", font=('IRANSans', '20'))
        edit.config(height=2, width=20)
        space.pack()
        title.pack()
        space1.pack()
        listBox9.pack()
        space2.pack()
        sabt.pack()
        edit.pack()
        delete.pack()
        space3.pack()

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
        title = Label(pricesRoot, text="قیمت ها", font=('IRANSans', '22'), fg="Blue", bg='orange')
        cols = ('تاریخ ثبت','قیمت Economy class','قیمت Business class','قیمت First class', 'مدل هواپیما', 'کد فرودگاه مقصد', 'کد فرودگاه مبدأ')
        listBox9 = ttk.Treeview(pricesRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=listBox9.yview)
        listBox9.configure(yscrollcommand=vsb.set)
        listBox9.column("0", width=200, anchor="c")
        listBox9.column("1", width=200, anchor="c")
        listBox9.column("2", width=200, anchor="c")
        listBox9.column("3", width=200, anchor="c")
        listBox9.column("4", width=200, anchor="c")
        listBox9.column("5", width=200, anchor="c")
        listBox9.column("6", width=200, anchor="c")
        listBox9.config(height=34)
        for col in cols:
            listBox9.heading(col, text=col)
        sabt = Button(pricesRoot, text="ثبت قیمت", font=('IRANSans', '20'))
        sabt.config(height=2, width=20)
        delete = Button(pricesRoot, text="حذف", font=('IRANSans', '20'))
        delete.config(height=2, width=20)
        space.pack()
        title.pack()
        space1.pack()
        listBox9.pack()
        space2.pack()
        sabt.pack()
        delete.pack()
        space3.pack()

    def tozih1(self):
        tozihoneroot = Tk()
        tozihoneroot.title("قیمت ها")
        tozihoneroot['bg'] = 'orange'
        space = Label(tozihoneroot, text=" ", bg='orange')
        space1 = Label(tozihoneroot, text=" ", bg='orange')
        space2 = Label(tozihoneroot, text=" ", bg='orange')
        space3 = Label(tozihoneroot, text=" ", bg='orange')
        space4 = Label(tozihoneroot, text=" ", bg='orange')
        space5 = Label(tozihoneroot, text=" ", bg='orange')
        title = Label(tozihoneroot, text="آشنایان", font=('IRANSans', '22'), fg="Blue", bg='orange')
        one = Label(tozihoneroot, text="نام آشنای اول: اردوان خلیج     شماره تلفن: ۰۹۱۲۰۸۶۴۰۵۴",
                      font=('IRANSans', '20'), bg='orange')
        two = Label(tozihoneroot, text="نام آشنای دوم: اردوان خلیج     شماره تلفن: ۰۹۱۲۰۸۶۴۰۵۴",
                      font=('IRANSans', '20'), bg='orange')
        three = Label(tozihoneroot, text="نام آشنای سوم: اردوان خلیج     شماره تلفن: ۰۹۱۲۰۸۶۴۰۵۴",
                      font=('IRANSans', '20'), bg='orange')
        space.pack()
        title.pack()
        space1.pack()
        space2.pack()
        one.pack()
        space3.pack()
        two.pack()
        space4.pack()
        three.pack()
        space5.pack()

    def tozih2(self):
        print("Ardavan Khalij")

    def tozih3(self):
        print("Ardavan Khalij")

#######################################################################################################################
#                                             Make An Object From My Class                                            #
#######################################################################################################################
ALLPAGES = all()
#######################################################################################################################
#                                                          Root                                                       #
#######################################################################################################################
# root = Tk()
# root.title("شرکت هواپیمایی")
# root['bg']='orange'
# space = Label(root, text=" ", bg='orange')
# space1 = Label(root, text=" ", bg='orange')
# space2 = Label(root, text=" ", bg='orange')
# space3 = Label(root, text=" ", bg='orange')
# space4 = Label(root, text=" ", bg='orange')
# title = Label(root, text="سلام، خوش آمدید.", font=('IRANSans_Bold', '22', 'bold'), bg='orange', fg='blue')
# title1 = Label(root, text="لطفاً نام و نام خانوادگی خود را در صورت موجود بودن در لیست انتخاب کنید",
#                    font=('IRANSans', '20'), bg='orange')
# title3 = Label(root, text="و در غیر این صورت نام و نام خانوادگی خود را وارد کنید.",
#                    font=('IRANSans', '20'), bg='orange')
#
# name2 = Entry(root, width=60, justify='right', font=('IRANSans', 12))
# name2.insert(0, "  نام و نام خانوادگی")
# name = ttk.Combobox(root, width=60, justify='right', font=('IRANSans', 12))
# valuelistForNamesOfComboBox.clear()
#
# with open('listfile.txt', 'r') as filehandle:
#     for line in filehandle:
#         currentPlace = line[:-1]
#         if currentPlace != "" and currentPlace != "  نام و نام خانوادگی":
#             valuelistForNamesOfComboBox.append(currentPlace)
#
# name['values'] = valuelistForNamesOfComboBox
# name.insert(0, "  نام و نام خانوادگی")
#
# sabtname = Button(root, text="ثبت", font=('IRANSans_Medium', '20'), command=ALLPAGES.menu)
# sabtname.config(height=2, width=25)
# space.pack()
# title.pack()
# space1.pack()
# title1.pack()
# title3.pack()
# space4.pack()
# name2.pack()
# name.pack()
# space2.pack()
# sabtname.pack()
# space3.pack()
# root.mainloop()
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