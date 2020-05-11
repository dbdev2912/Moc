from tkinter import*
from tkinter import ttk
import sqlite3, datetime

class app:
	def __init__(self, root):
		self.root=root
		self.file=open("data.db", 'a+')
		self.file.close()
		self.db=sqlite3.connect("data.db")
		self.database()

		self.clone=[]
		self.tensv=StringVar()
		self.tensv_clone=StringVar()
		self.thang=StringVar()
		self.tt=StringVar()
		self.tien=StringVar()
		self.time=datetime.datetime.today()
		self.lydo=StringVar()
		self.chi=StringVar()

		self.tree=ttk.Treeview(self.root, selectmode="browse")
		self.tree_sv()
		self.history_tree()
		self.clone_()
		self.add_his()
		self.history_tree_sv()
		self.them_thanh_vien()
		self.currency()

	def currency(self):
		cursor=self.db.cursor()
		cursor.execute("SELECT* FROM TONG;")
		cursor=cursor.fetchall()
		Label(self.root,bg="#d1e8ed", font=("Calibri", 20, "bold"),text="ĐÃ THU:").place(x=15, y=5)
		e1=Entry(self.root, font=("Calibri", 20, "bold"), width=10)
		e1.insert(END, cursor[0][0])
		e1.place(x=15, y=40)

		Label(self.root,bg="#d1e8ed", font=("Calibri", 20, "bold"),text="ĐÃ CHI: ").place(x=215+100, y=5)
		e1=Entry(self.root ,font=("Calibri", 20, "bold"), width=10)
		e1.insert(END, cursor[0][1])
		e1.place(x=315, y=40)


		Label(self.root,bg="#d1e8ed", font=("Calibri", 20, "bold"),text="SỐ DƯ HIỆN TẠI:").place(x=415+200, y=5)
		e1=Entry(self.root,font=("Calibri", 20, "bold"), width=10)
		e1.insert(END, cursor[0][2])
		e1.place(x=615, y=40)

	def submit(self):
		cur=self.db.cursor()
		cur.execute("UPDATE QUY SET T{0}='{1}' WHERE ID='{2}';".format(self.thang.get(), self.tien.get(), self.tt.get()))
		cur.execute("UPDATE TONG SET DATHU=DATHU+{0};".format(self.tien.get()))
		cur.execute("UPDATE TONG SET HIENTAI=HIENTAI+{0};".format(self.tien.get()))
		cur=self.db.execute("INSERT INTO LS_SV VALUES('{0}', '{1}', '{2}')".format("{0}-{1}-{2}".format(self.time.strftime("%Y"), self.time.strftime("%m"), self.time.strftime("%d")), self.tien.get(), self.thang.get()))
		self.db.commit()
		self.__init__(self.root)

	def clone_(self):
		Label(self.root,bg="#d1e8ed", font=("Calibri", 18, "bold"),text="FORM THU QUỸ: ").place(x=750, y=315)
		
		Label(self.root, bg="#d1e8ed",font=("Calibri", 12, "bold"), text="Tên sinh viên: ").place(x=550+200, y=350)
		e1=Entry(self.root, width=25, textvariable=self.tensv)
		e1.place(x=650+200, y=350)

		Label(self.root, bg="#d1e8ed",font=("Calibri", 12, "bold"), text="Tháng: ").place(x=550+200, y=380)
		e2=Entry(self.root, width=25, textvariable=self.thang)	
		e2.place(x=650+200, y=380)

		Label(self.root, bg="#d1e8ed",font=("Calibri", 12, "bold"), text="Tiền: ").place(x=550+200, y=410)
		e3=Entry(self.root, width=25, textvariable=self.tien)
		e3.place(x=650+200, y=410)

		Button(self.root,bg="black", fg="white", text="Thêm", width=10, command=self.submit).place(x=723+200, y=440)


	def select(self, event):
		self.clone=list(self.tree.item(self.tree.selection(), "values"))
		Label(self.root, bg="#d1e8ed",font=("Calibri", 12, "bold"), text="Tên sinh viên: ").place(x=550+200, y=350)
		e1=Entry(self.root, width=25, textvariable=self.tensv)
		e1.insert(END, "{0}".format(self.clone[0]))
		e1.place(x=650+200, y=350)

		Label(self.root, bg="#d1e8ed",font=("Calibri", 12, "bold"), text="Tháng: ").place(x=550+200, y=380)
		e2=Entry(self.root, width=25, textvariable=self.thang)
		e2.insert(END, "1")
		e2.place(x=650+200, y=380)

		Label(self.root, bg="#d1e8ed",font=("Calibri", 12, "bold"), text="Tiền: ").place(x=550+200, y=410)
		e3=Entry(self.root, width=25, textvariable=self.tien)
		e3.insert(END, "0")
		e3.place(x=650+200, y=410)

		self.tt.set(self.clone[13])
		Button(self.root, text="Thêm",bg="black", fg="white", width=10, command=self.submit).place(x=723+200, y=440)



	def tree_sv(self):	
		self.tree.place(x=15, y=80)
		self.tree['column']=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
		self.tree['show']="headings"
		self.tree.column('0', width=200, anchor="w")
		self.tree.column('1', width=65, anchor="w")
		self.tree.column('2', width=65, anchor="w")
		self.tree.column('3', width=65, anchor="w")
		self.tree.column('4', width=65, anchor="w")
		self.tree.column('5', width=65, anchor="w")
		self.tree.column('6', width=65, anchor="w")
		self.tree.column('7', width=65, anchor="w")
		self.tree.column('8', width=65, anchor="w")
		self.tree.column('9', width=65, anchor="w")
		self.tree.column('10', width=65, anchor="w")
		self.tree.column('11', width=65, anchor="w")
		self.tree.column('12', width=65, anchor="w")

		self.tree.heading('0', text="Họ tên", anchor='w')
		self.tree.heading('1', text="Tháng 5", anchor='w')
		self.tree.heading('2', text="Tháng 6", anchor='w')
		self.tree.heading('3', text="Tháng 7", anchor='w')
		self.tree.heading('4', text="Tháng 8", anchor='w')
		self.tree.heading('5', text="Tháng 9", anchor='w')
		self.tree.heading('6', text="Tháng 10", anchor='w')
		self.tree.heading('7', text="Tháng 11", anchor='w')
		self.tree.heading('8', text="Tháng 12", anchor='w')
		self.tree.heading('9', text="Tháng 1", anchor='w')
		self.tree.heading('10', text="Tháng 2", anchor='w')
		self.tree.heading('11', text="Tháng 3", anchor='w')
		self.tree.heading('12', text="Tháng 4", anchor='w')

		self.tree.bind("<Double-1>", self.select)

		cursor=self.db.cursor()
		cursor.execute("SELECT* FROM QUY;")
		for hh in cursor:
			self.tree.insert("", "end", values=("{0}".format(hh[1]), "{0}".format(hh[2]), "{0}".format(hh[3]), "{0}".format(hh[4]), "{0}".format(hh[5]), "{0}".format(hh[6]), "{0}".format(hh[7]), "{0}".format(hh[8]), "{0}".format(hh[9]), "{0}".format(hh[10]), "{0}".format(hh[11]), "{0}".format(hh[12]),"{0}".format(hh[13]), "{0}".format(hh[0])))



	def history_tree(self):
		Label(self.root,bg="#d1e8ed", font=("Calibri", 18, "bold"),text="LỊCH SỬ CHI: ").place(x=15, y=315)

		tree=ttk.Treeview(self.root, height=8, selectmode="browse")
		tree.place(x=15, y=350)
		tree["column"]=("0", "1", "2")
		tree["show"]="headings"
		tree.column('0', width=65, anchor="w")
		tree.column('1', width=65, anchor="w")
		tree.column('2', width=260, anchor='w')

		tree.heading('0', text="Ngày chi", anchor="w")
		tree.heading('1', text="Số chi", anchor="w")
		tree.heading('2', text="Lý do", anchor="w")

		
		cursor=self.db.cursor()
		cursor.execute("SELECT* FROM LS;")
		for ls in cursor:
			tree.insert("", "end", values=("{0}".format(ls[0]), "{0}".format(ls[1]), "{0}".format(ls[2])))

	def add_his_command(self):
		cur=self.db.execute("INSERT INTO LS VALUES('{0}', '{1}', '{2}')".format("{0}-{1}-{2}".format(self.time.strftime("%Y"), self.time.strftime("%m"), self.time.strftime("%d")), self.chi.get(), self.lydo.get()))
		cur.execute("UPDATE TONG SET HIENTAI=HIENTAI-{0};".format(self.chi.get()))
		cur.execute("UPDATE TONG SET DACHI=DACHI+{0};".format(self.chi.get()))
		self.db.commit()
		self.__init__(self.root)

	def add_his(self):
		Label(self.root,bg="#d1e8ed",font=("Calibri", 12, "bold"),text="Thêm: ").place(x=15, y=540)
		Entry(self.root, textvariable=self.chi, width=10).place(x=80, y=540)
		Entry(self.root, textvariable=self.lydo, width=35).place(x=145, y=540)
		Button(self.root, width=5,bg="black", fg="white", text="Thêm", command=self.add_his_command).place(x=362, y=539)


	def history_tree_sv(self):
		Label(self.root,bg="#d1e8ed", font=("Calibri", 18, "bold"),text="LỊCH SỬ THU: ").place(x=480, y=315)

		tree=ttk.Treeview(self.root, height=8, selectmode="browse")
		tree.place(x=480, y=350)
		tree["column"]=("0", "1", "2")
		tree["show"]="headings"
		tree.column('0', width=65, anchor="w")
		tree.column('1', width=65, anchor="w")
		tree.column('2', width=65, anchor='w')

		tree.heading('0', text="Ngày thu", anchor="w")
		tree.heading('1', text="Số thu", anchor="w")
		tree.heading('2', text="Tháng", anchor="w")

		
		cursor=self.db.cursor()
		cursor.execute("SELECT* FROM LS_SV;")
		for ls in cursor:
			tree.insert("", "end", values=("{0}".format(ls[0]), "{0}".format(ls[1]), "{0}".format(ls[2])))

	
	def submit_sv(self):
		cursor=self.db.cursor()
		id_=cursor.execute("SELECT COUNT(ID) FROM QUY;").fetchall()[0][0]
		id_=str(id_+1)
		cursor.execute("INSERT INTO QUY VALUES({0}, '{1}', 0,0,0,0,0,0,0,0,0,0,0,0);".format(id_, self.tensv_clone.get()))
		self.db.commit()
		self.__init__(self.root)

	def them_thanh_vien(self):
		Label(self.root,bg="#d1e8ed", font=("Calibri", 18, "bold"),text="FORM THÊM TV: ").place(x=750, y=500)
		
		Label(self.root, bg="#d1e8ed",font=("Calibri", 12, "bold"), text="Tên sinh viên: ").place(x=550+200, y=530)
		e1=Entry(self.root, width=25, textvariable=self.tensv_clone)
		e1.place(x=650+200, y=530)

		Button(self.root,bg="black", fg="white", text="Thêm", width=10, command=self.submit_sv).place(x=723+200, y=560)


	def database(self):
		cur=self.db.cursor()
		try:
			cur.execute("SELECT* FROM QUY;")
			# print(cur.fetchall())
		except sqlite3.OperationalError:
			sql=['''
			CREATE TABLE QUY 
			(
				ID SMALLINT PRIMARY KEY,
				NAME NVARCHAR(255),
				T5 MEDIUMINT,
				T6 MEDIUMINT,
				T7 MEDIUMINT,
				T8 MEDIUMINT,
				T9 MEDIUMINT,
				T10 MEDIUMINT,
				T11 MEDIUMINT,
				T12 MEDIUMINT,
				T1 MEDIUMINT,
				T2 MEDIUMINT,
				T3 MEDIUMINT,
				T4 MEDIUMINT
			);
			''', ''' CREATE TABLE LS 
			(
				NGAY DATE,
				SOCHI INT,
				LIDO NVARCHAR(255)
			);
			''',
			''' CREATE TABLE TONG
			(
				DATHU INT,
				DACHI INT,
				HIENTAI INT
			);
			''', 'INSERT INTO TONG VALUES(0,0,0);'
		, '''CREATE TABLE LS_SV 
			(
				NGAY DATE,
				SOCHI INT,
				LIDO NVARCHAR(255)
			);''']
			for i in sql:
				cur.execute(i)
			
			self.db.commit()

root=Tk()
root.configure(bg="#d1e8ed")
root.title("Một chiếc app bé bé cho đũy thủ quỷ")
a=app(root)
root.minsize(1000, 610)
root.resizable(False, False)
root.mainloop()