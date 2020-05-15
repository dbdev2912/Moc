from tkinter import ttk 
from tkinter import* 
import sqlite3
import datetime

class app:
	def __init__(self, root, year):
		self.file=open("data_.db", 'a+')
		self.file.close()

		self.root=root
		self.year=year
		self.db=sqlite3.connect("data_.db")

		self.clone=list()
		self.in_hoten=StringVar()
		self.in_masv=StringVar()
		self.in_lop=StringVar()
		self.in_ngay=StringVar()
		self.in_thang=StringVar()
		self.in_nam=StringVar()
		self.in_gioitinh=StringVar()
		self.in_quequan=StringVar()
		self.in_dantoc=StringVar()
		self.in_tongiao=StringVar()
		self.in_ngay_doan=StringVar()
		self.in_thang_doan=StringVar()
		self.in_nam_doan=StringVar()
		self.in_ngay_dang=StringVar()
		self.in_thang_dang=StringVar()
		self.in_nam_dang=StringVar()
		self.in_chucvu=StringVar()
		self.clone_masv=StringVar()
		self.clone_tensv=StringVar()

		self.ngay_chi=StringVar()
		self.thang_chi=StringVar()
		self.nam_chi=StringVar()
		self.chi_moi=StringVar()
		self.lydochi=StringVar()

		self.T1=StringVar()
		self.T2=StringVar()
		self.T3=StringVar()
		self.T4=StringVar()
		self.T5=StringVar()
		self.T6=StringVar()
		self.T7=StringVar()
		self.T8=StringVar()
		self.T9=StringVar()
		self.T10=StringVar()
		self.T11=StringVar()
		self.T12=StringVar()
		self.var=StringVar()
		self.malop_c=StringVar()
		self.new_year=StringVar()
		try:
			self.select_year()
		except:
			pass
		self.tree=ttk.Treeview(self.root, height=10, selectmode="browse")
		self.tree_sv=ttk.Treeview(self.root, height=15, selectmode="browse")

		self.database()
		self.tree_sinh_vien()
		self.nhap_tv()
		self.tree_thu_quy()
		self.clone_thay_doi()
		self.add_new_year()
		try:
			self.top_content()
		except:
			pass
		self.menu()
		self.search_lop()

	def pro_search_lop(self):
		sv_root=Tk()
		sv_root.minsize(width=950, height=400)
		sv_root.resizable(False, False)
		tree_sv=ttk.Treeview(sv_root, height=18, selectmode="browse")
		tree_sv.place(x=2, y=2)
		vsb=Scrollbar(sv_root, orient="vertical", command=tree_sv.yview)
		vsb.place(x=931, y=2, height=390)
		tree_sv.configure(yscrollcommand=vsb.set)
		# horbar=Scrollbar(root)
		tree_sv["column"]=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
		tree_sv['show']="headings"
		tree_sv.column('0', width=55, anchor="w")
		tree_sv.column('1', width=150, anchor="w")
		tree_sv.column('2', width=80, anchor="w")
		tree_sv.column('3', width=60, anchor="w")
		tree_sv.column('4', width=80, anchor="w")
		tree_sv.column('5', width=80, anchor="w")
		tree_sv.column('6', width=80, anchor="w")
		tree_sv.column('7', width=80, anchor="w")
		tree_sv.column('8', width=80, anchor="w")
		tree_sv.column('9', width=88, anchor="w")
		tree_sv.column('10', width=80, anchor="w")	

		tree_sv.heading('0', text="MASV", anchor='w')
		tree_sv.heading('1', text="Họ tên", anchor='w')
		tree_sv.heading('2', text="Ngày Sinh", anchor='w')
		tree_sv.heading('3', text="Giới tính", anchor='w')
		tree_sv.heading('4', text="Quê Quán", anchor='w')
		tree_sv.heading('5', text="Dân tộc", anchor='w')
		tree_sv.heading('6', text="Tôn giáo", anchor='w')
		tree_sv.heading('7', text="NVĐoàn", anchor='w')
		tree_sv.heading('8', text="NVĐảng", anchor='w')
		tree_sv.heading('9', text="Chức vụ", anchor='w')
		tree_sv.heading('10', text="Lớp", anchor='w')

		# tree_sv.bind("<KeyPress-Delete>", delete)
		db=sqlite3.connect('data_.db')
		cur=db.cursor()
		cur.execute("SELECT* FROM THANHVIEN WHERE LOP='{0}'".format(self.malop_c.get()))
		for sv in cur:
			tree_sv.insert("", "end", values=(sv[0], sv[1], sv[2], sv[3], sv[4], sv[5], sv[6], sv[7], sv[8], sv[9], sv[10]))

	def search_lop(self):
		Label(self.root, text="Tìm theo lớp: ").place(x=945-200-50-50, y=400-10)
		Entry(self.root, textvariable=self.malop_c, width=24).place(x=945+85-200-50-50, y=400-10)
		Button(self.root, text="Tìm", width=5, command=self.pro_search_lop).place(x=1190-305, y=400-1-10)
	

	def chi_quy_windows(self):
		chi_root=Tk()
		chi_root.title("Chi quỹ")
		chi_root.minsize(515, 400)
		chi_root.resizable(False, False)
		tree=ttk.Treeview(chi_root, height=18, selectmode="browse")
		scb=ttk.Scrollbar(chi_root, orient="vertical", command=tree.yview)
		scb.place(x=492, y=2, height=390)
		tree.configure(yscrollcommand=scb.set)
		# chi_root.bind('<Button-1>',self.destroy)
		tree['column']=('1','2','3')
		tree['show']='headings'
		tree.place(x=2, y=2)
		tree.column('1', width=65, anchor="w")
		tree.column('2', width=85, anchor="w")
		tree.column('3', width=500-4-10-150, anchor='w')

		tree.heading('1', text="Ngày chi", anchor='w')
		tree.heading('2', text="Tiền chi", anchor='w')
		tree.heading('3', text="Mục đích chi", anchor='w')
		cur=self.db.cursor()
		cur.execute("SELECT NGAY, SOCHI, LIDO FROM LS;")
		for l in cur:
			tree.insert("", "end", values=(l[0], l[1], l[2]))


		# def insert():
		# 	print(self.ngay_chi.get())
		# 	cur=self.db.cursor()
		# 	cur.execute("INSERT INTO LS VALUES('{0}-{1}-{2}', {3}, '{4}');".format(self.nam_chi.get(), self.thang_chi.get(), self.ngay_chi.get(), self.chi_moi.get(), self.lydochi.get()))
		# show()

	def insert(self):
		ngay=self.ngay_chi.get()
		thang=self.thang_chi.get()
		nam=self.nam_chi.get()
		tien=self.chi_moi.get()
		lydo=self.lydochi.get()

		cur=self.db.cursor()
		cur.execute("INSERT INTO LS VALUES('{0}-{1}-{2}', '{3}', '{4}');".format(nam, thang, ngay, tien, lydo))
		cur.execute("UPDATE TONGQUY SET TONGCHI=TONGCHI+{0} WHERE NAM={1}".format(tien, self.year))
		self.db.commit()
		self.__init__(self.root, self.year)

	def menu(self):		
		Label(self.root, text="Tiền chi: ").place(x=945, y=540-1)
		Entry(self.root, textvariable=self.chi_moi, width=24).place(x=945+85, y=540-1)

		Button(self.root, text="Quỹ đã chi", width=25,command=self.chi_quy_windows).place(x=1040, y=660)
		Label(self.root, text="Ngày chi: ").place(x=945, y=570)
		Entry(self.root, textvariable=self.ngay_chi, width=4).place(x=85+945, y=570)
		Label(self.root, text="/").place(x=100+15+945, y=570)
		Entry(self.root, textvariable=self.thang_chi, width=4).place(x=115+15+945, y=570)
		Label(self.root, text='/').place(x=165+945, y=570)
		Entry(self.root, textvariable=self.nam_chi, width=8).place(x=180+945, y=570)

		Label(self.root, text="Lý do chi: ").place(x=2+945, y=600+3)
		Entry(self.root, textvariable=self.lydochi, width=24).place(x=85+945, y=600+1)
		Button(self.root, text="Chi", width=5, height=5, command=self.insert).place(x=1170, y=540-4)
	def add_year(self):
		cur=self.db.cursor()
		cur.execute("INSERT INTO TONGQUY VALUES({0},0,0);".format(self.new_year.get()))
		
		cur.execute("SELECT MASV FROM THANHVIEN")
		masv=[list(sv)[0] for sv in cur.fetchall()]
		for sv in masv:
			cur.execute("INSERT INTO CHITIETTHU VALUES('{0}', {1}, 0,0,0,0,0,0,0,0,0,0,0,0);".format(sv, self.new_year.get()))
		self.db.commit()
		self.__init__(self.root, self.year)
	def add_new_year(self):
		Label(self.root, text="Thêm năm mới: ").place(x=600, y=30)
		Entry(self.root, width=8, textvariable=self.new_year).place(x=750, y=30)
		Button(self.root, text="Thêm", command=self.add_year).place(x=800, y=28)
	
	def year_process(self, event):
		self.time=datetime.datetime.today()
		self.year=int(self.var.get())
		self.tree=ttk.Treeview(self.root, height=10, selectmode="browse")
		self.tree_sv=ttk.Treeview(self.root, height=15, selectmode="browse")

		self.__init__(self.root, self.year)

	def select_year(self):
		cur=self.db.cursor()
		years=list(cur.execute("SELECT NAM FROM TONGQUY;").fetchall())
		years=[y[0] for y in years]
		self.var.set(years[0])
		opt=OptionMenu(self.root, self.var, *years, command=self.year_process)
		opt.config(width=5)

		opt.place(x=900, y=28)


	def top_content(self):
		cur=self.db.cursor()
		cur.execute("SELECT TONGTHU, TONGCHI FROM TONGQUY WHERE NAM='{0}';".format(self.year))
		# print(cur.fetchall())
		thu=cur.fetchall()[0][0]
		Label(self.root, text="ĐÃ THU: ").place(x=15, y=30)
		Label(self.root, text="                ").place(x=60, y=30)
		Label(self.root, text="{0}".format(thu)).place(x=60, y=30)

		cur.execute("SELECT TONGTHU, TONGCHI FROM TONGQUY WHERE NAM='{0}';".format(self.year))
		chi=cur.fetchall()[0][1]
		Label(self.root, text="ĐÃ CHI: ").place(x=215, y=30)
		Label(self.root, text="                 ").place(x=260, y=30)
		Label(self.root, text="{0}".format(chi)).place(x=260, y=30)

		cur.execute("SELECT TONGTHU, TONGCHI FROM TONGQUY WHERE NAM='{0}';".format(self.year))
		
		Label(self.root, text="HIỆN CÓ: ").place(x=415, y=30)
		Label(self.root, text="                  ").place(x=480, y=30)
		Label(self.root, text="{0}".format(thu-chi)).place(x=480, y=30)

	def add_quy(self):
		cursor=self.db.cursor()
		cursor.execute("SELECT T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12 FROM CHITIETTHU WHERE MASV='{0}' AND YEAR={1}".format(self.clone[0], self.year))
		tong1=sum([int(x) for x in cursor.fetchall()[0]])

		cursor=self.db.cursor()
		cursor.execute("UPDATE CHITIETTHU SET T1={0}, T2={1}, T3={2}, T4={3}, T5={4}, T6={5}, T7={6}, T8={7}, T9={8}, T10={9}, T11={10}, T12={11} WHERE MASV='{12}' AND YEAR={13};".format(self.T1.get(), self.T2.get(), self.T3.get(), self.T4.get(), self.T5.get(), self.T6.get(), self.T7.get(), self.T8.get(), self.T9.get(), self.T10.get(), self.T11.get(), self.T12.get(), self.clone[0], self.year))
		cursor.execute("SELECT T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12 FROM CHITIETTHU")
		
		cursor=self.db.cursor()
		cursor.execute("SELECT T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12 FROM CHITIETTHU WHERE MASV='{0}' AND YEAR={1}".format(self.clone[0], self.year))
		tong2=sum([int(x) for x in cursor.fetchall()[0]])

		cursor=self.db.cursor()
		cursor.execute("UPDATE TONGQUY SET TONGTHU=TONGTHU+{0} WHERE NAM={1}".format(tong2-tong1, self.year))

		self.db.commit()
		self.__init__(self.root, self.year)

	def select(self, event):
		self.clone=list(self.tree.item(self.tree.selection(), "values"))

		masv=Label(self.root, text=str(self.clone[0]), fg="RED")
		masv.place(x=15, y=660)

		tensv=Label(self.root, text=str(self.clone[1]), fg="RED")
		tensv.place(x=70, y=660)

		t1=Entry(self.root, textvariable=self.T1)
		t1.insert(END, self.clone[2])
		t1.place(x=224, y=660)
		t2=Entry(self.root, textvariable=self.T2)
		t2.insert(END, self.clone[3])
		t2.place(x=283, y=660)
		t3=Entry(self.root, textvariable=self.T3)
		t3.insert(END, self.clone[4])
		t3.place(x=342, y=660)
		t4=Entry(self.root, textvariable=self.T4)
		t4.insert(END, self.clone[5])
		t4.place(x=401, y=660)
		t5=Entry(self.root, textvariable=self.T5)
		t5.insert(END, self.clone[6])
		t5.place(x=460, y=660)
		t6=Entry(self.root, textvariable=self.T6)
		t6.insert(END, self.clone[7])
		t6.place(x=519, y=660)
		t7=Entry(self.root, textvariable=self.T7)
		t7.insert(END, self.clone[8])
		t7.place(x=578, y=660)
		t8=Entry(self.root, textvariable=self.T8)
		t8.insert(END, self.clone[9])
		t8.place(x=637, y=660)
		t9=Entry(self.root, textvariable=self.T9)
		t9.insert(END, self.clone[10])
		t9.place(x=696, y=660)
		t10=Entry(self.root, textvariable=self.T10)
		t10.insert(END, self.clone[11])
		t10.place(x=755, y=660)
		t11=Entry(self.root, textvariable=self.T11)
		t11.insert(END, self.clone[12])
		t11.place(x=814, y=660)
		t12=Entry(self.root, width=7, textvariable=self.T12)
		t12.insert(END, self.clone[13])
		t12.place(x=873, y=660)

		Button(self.root, text="Thay đổi", command=self.add_quy).place(x=945, y=660+1)

	def clone_thay_doi(self):
		t1=Entry(self.root, textvariable=self.T1)
		t1.place(x=224, y=660)
		t2=Entry(self.root, textvariable=self.T2)
		t2.place(x=283, y=660)
		t3=Entry(self.root, textvariable=self.T3)
		t3.place(x=342, y=660)
		t4=Entry(self.root, textvariable=self.T4)
		t4.place(x=401, y=660)
		t5=Entry(self.root, textvariable=self.T5)
		t5.place(x=460, y=660)
		t6=Entry(self.root, textvariable=self.T6)
		t6.place(x=519, y=660)
		t7=Entry(self.root, textvariable=self.T7)
		t7.place(x=578, y=660)
		t8=Entry(self.root, textvariable=self.T8)
		t8.place(x=637, y=660)
		t9=Entry(self.root, textvariable=self.T9)
		t9.place(x=696, y=660)
		t10=Entry(self.root, textvariable=self.T10)
		t10.place(x=755, y=660)
		t11=Entry(self.root, textvariable=self.T11)
		t11.place(x=814, y=660)
		t12=Entry(self.root, width=7, textvariable=self.T12)
		t12.place(x=873, y=660)
		Button(self.root, text="Thay đổi").place(x=945, y=660+1)


	def delete(self, event):
		self.clone=list(self.tree_sv.item(self.tree_sv.selection(), 'values'))
		cursor=self.db.cursor()
		cursor.execute("DELETE FROM CHITIETTHU WHERE MASV='{0}';".format(self.clone[0]))
		cursor.execute("DELETE FROM THANHVIEN WHERE MASV='{0}';".format(self.clone[0]))
		self.db.commit()
		self.__init__(self.root, self.year)

	def tree_thu_quy(self):
		self.tree.place(x=15, y=420)
		vsb=Scrollbar(self.root, orient="vertical", command=self.tree.yview)
		vsb.place(x=931, y=420, height=230)
		self.tree.configure(yscrollcommand=vsb.set)
		# self.horbar=Scrollbar(self.root)
		self.tree['column']=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13')
		self.tree['show']="headings"
		self.tree.column('0', width=55, anchor="w")
		self.tree.column('1', width=150, anchor="w")
		self.tree.column('2', width=59, anchor="w")
		self.tree.column('3', width=59, anchor="w")
		self.tree.column('4', width=59, anchor="w")
		self.tree.column('5', width=59, anchor="w")
		self.tree.column('6', width=59, anchor="w")
		self.tree.column('7', width=59, anchor="w")
		self.tree.column('8', width=59, anchor="w")
		self.tree.column('9', width=59, anchor="w")
		self.tree.column('10', width=59, anchor="w")
		self.tree.column('11', width=59, anchor="w")
		self.tree.column('12', width=59, anchor="w")
		self.tree.column('13', width=59, anchor="w")

		self.tree.heading('0', text="MASV", anchor='w')
		self.tree.heading('1', text="Họ tên", anchor='w')
		self.tree.heading('2', text="Tháng 1", anchor='w')
		self.tree.heading('3', text="Tháng 2", anchor='w')
		self.tree.heading('4', text="Tháng 3", anchor='w')
		self.tree.heading('5', text="Tháng 4", anchor='w')
		self.tree.heading('6', text="Tháng 5", anchor='w')
		self.tree.heading('7', text="Tháng 6", anchor='w')
		self.tree.heading('8', text="Tháng 7", anchor='w')
		self.tree.heading('9', text="Tháng 8", anchor='w')
		self.tree.heading('10', text="Tháng 9", anchor='w')
		self.tree.heading('11', text="Tháng 10", anchor='w')
		self.tree.heading('12', text="Tháng 11", anchor='w')
		self.tree.heading('13', text="Tháng 12", anchor='w')

		self.tree.bind("<Double-1>", self.select)
		cursor=self.db.cursor()
		cursor.execute("SELECT T.MASV, TENSV, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12 FROM CHITIETTHU AS C INNER JOIN THANHVIEN AS T ON T.MASV=C.MASV WHERE YEAR={0};".format(self.year))
		for hh in cursor:
			self.tree.insert("", "end", values=("{0}".format(hh[0]), "{0}".format(hh[1]), "{0}".format(hh[2]), "{0}".format(hh[3]), "{0}".format(hh[4]), "{0}".format(hh[5]), "{0}".format(hh[6]), "{0}".format(hh[7]), "{0}".format(hh[8]), "{0}".format(hh[9]), "{0}".format(hh[10]),"{0}".format(hh[11]),"{0}".format(hh[12]), "{0}".format(hh[13])))


	def tree_sinh_vien(self):
		self.tree_sv.place(x=15, y=60)
		vsb=Scrollbar(self.root, orient="vertical", command=self.tree_sv.yview)
		vsb.place(x=931, y=60, height=325)
		self.tree_sv.configure(yscrollcommand=vsb.set)
		self.tree_sv["column"]=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
		self.tree_sv['show']="headings"
		self.tree_sv.column('0', width=55, anchor="w")
		self.tree_sv.column('1', width=150, anchor="w")
		self.tree_sv.column('2', width=80, anchor="w")
		self.tree_sv.column('3', width=60, anchor="w")
		self.tree_sv.column('4', width=80, anchor="w")
		self.tree_sv.column('5', width=80, anchor="w")
		self.tree_sv.column('6', width=80, anchor="w")
		self.tree_sv.column('7', width=80, anchor="w")
		self.tree_sv.column('8', width=80, anchor="w")
		self.tree_sv.column('9', width=88, anchor="w")
		self.tree_sv.column('10', width=80, anchor="w")	

		self.tree_sv.heading('0', text="MASV", anchor='w')
		self.tree_sv.heading('1', text="Họ tên", anchor='w')
		self.tree_sv.heading('2', text="Ngày Sinh", anchor='w')
		self.tree_sv.heading('3', text="Giới tính", anchor='w')
		self.tree_sv.heading('4', text="Quê Quán", anchor='w')
		self.tree_sv.heading('5', text="Dân tộc", anchor='w')
		self.tree_sv.heading('6', text="Tôn giáo", anchor='w')
		self.tree_sv.heading('7', text="NVĐoàn", anchor='w')
		self.tree_sv.heading('8', text="NVĐảng", anchor='w')
		self.tree_sv.heading('9', text="Chức vụ", anchor='w')
		self.tree_sv.heading('10', text="Lớp", anchor='w')

		self.tree_sv.bind("<KeyPress-Delete>", self.delete)

		cur=self.db.cursor()
		cur.execute("SELECT* FROM THANHVIEN")
		for sv in cur:
			self.tree_sv.insert("", "end", values=(sv[0], sv[1], sv[2], sv[3], sv[4], sv[5], sv[6], sv[7], sv[8], sv[9], sv[10]))

	def them_sv(self):
		hoten=self.in_hoten.get()
		masv=self.in_masv.get()
		lop=self.in_lop.get()
		ngay=self.in_ngay.get()
		thang=self.in_thang.get()
		nam=self.in_nam.get()
		gioitinh=self.in_gioitinh.get()
		quequan=self.in_quequan.get()
		dantoc=self.in_dantoc.get()
		tongiao=self.in_tongiao.get()
		ngay_doan=self.in_ngay_doan.get()
		thang_doan=self.in_thang_doan.get()
		nam_doan=self.in_nam_doan.get()
		ngay_dang=self.in_ngay_dang.get()
		thang_dang=self.in_thang_dang.get()
		nam_dang=self.in_nam_dang.get()
		chucvu=self.in_chucvu.get()
		cursor=self.db.cursor()
		cursor.execute("INSERT INTO THANHVIEN(TENSV, MASV, LOP, NGAYSINH, GIOITINH, QUEQUAN, DANTOC, TONGIAO, NGAYVAODOAN, NGAYVAODANG, CHUCVU) VALUES('{0}', '{1}', '{2}', '{3}-{4}-{5}', '{6}', '{7}', '{8}', '{9}', '{10}-{11}-{12}', '{13}-{14}-{15}', '{16}')".format(hoten, masv, lop, nam, thang, ngay, gioitinh, quequan, dantoc, tongiao, nam_doan, thang_doan, ngay_doan, nam_dang, thang_dang, ngay_dang, chucvu))
		cursor.execute("INSERT INTO CHITIETTHU VALUES('{0}', '{1}', 0,0,0,0,0,0,0,0,0,0,0,0)".format(masv, self.year))
		self.db.commit()

		self.__init__(self.root, self.year)
	def nhap_tv(self):
		Label(self.root, text="Họ tên: ").place(x=945, y=130-70)
		Entry(self.root, width=24, textvariable=self.in_hoten).place(x=1000, y=130-70)
		
		Label(self.root, text="MaSV:").place(x=945, y=160-70)
		Entry(self.root, width=8, textvariable=self.in_masv).place(x=1000, y=160-70)
		Label(self.root, text="Lớp:").place(x=945+100+5, y=160-70)
		Entry(self.root, width=10, textvariable=self.in_lop).place(x=1000+80+5-1, y=160-70)
		
		Label(self.root, text="Ngày sinh:").place(x=945, y=190-70)
		Entry(self.root, width=4, textvariable=self.in_ngay).place(x=1000+5, y=190-70)
		Label(self.root, text="/").place(x=1030, y=190-70)
		Entry(self.root, width=4, textvariable=self.in_thang).place(x=1000+50-10+5, y=190-70)
		Label(self.root, text="/").place(x=1080, y=190-70)
		Entry(self.root, width=8, textvariable=self.in_nam).place(x=1000+100+5-10, y=190-70)

		Label(self.root, text="Giới tính:").place(x=945, y=220-70)
		Label(self.root, text="Nam").place(x=1025, y=220-70)
		Radiobutton(self.root, variable=self.in_gioitinh, value="Nam").place(x=1000, y=220-70)
		Label(self.root, text="Nữ").place(x=1025+100, y=220-70)
		Radiobutton(self.root, variable=self.in_gioitinh, value="Nữ").place(x=1000+100, y=220-70)

		Label(self.root, text="Quê quán: ").place(x=945, y=250-70)
		Entry(self.root, textvariable=self.in_quequan).place(x=1025, y=250-70)

		Label(self.root, text="Dân tộc").place(x=945, y=280-70)
		Entry(self.root, textvariable=self.in_dantoc).place(x=1025, y=280-70)

		Label(self.root, text="Tôn giáo").place(x=945, y=310-70)
		Entry(self.root, textvariable=self.in_tongiao).place(x=1025, y=310-70)

		Label(self.root, text="NvĐoàn:").place(x=945, y=340-70)
		Entry(self.root, width=4, textvariable=self.in_ngay_doan).place(x=1000+5, y=340-70)
		Label(self.root, text="/").place(x=1030, y=340-70)
		Entry(self.root, width=4, textvariable=self.in_thang_doan).place(x=1000+50-10+5, y=340-70)
		Label(self.root, text="/").place(x=1080, y=340-70)
		Entry(self.root, width=8, textvariable=self.in_nam_doan).place(x=1000+100+5-10, y=340-70)

		Label(self.root, text="NvĐảng:").place(x=945, y=370-70)
		Entry(self.root, width=4, textvariable=self.in_ngay_dang).place(x=1000+5, y=370-70)
		Label(self.root, text="/").place(x=1030, y=370-70)
		Entry(self.root, width=4, textvariable=self.in_thang_dang).place(x=1000+50-10+5, y=370-70)
		Label(self.root, text="/").place(x=1080, y=370-70)
		Entry(self.root, width=8, textvariable=self.in_nam_dang).place(x=1000+100+5-10, y=370-70)

		Label(self.root, text="Chức vụ:").place(x=945, y=400-70)
		Entry(self.root, textvariable=self.in_chucvu).place(x=1025, y=400-70)

		Button(self.root, text="THÊM", command=self.them_sv).place(x=1080+26, y=400-50)

	def database(self):
		cur=self.db.cursor()
		try:
			cur.execute("SELECT* FROM THANHVIEN;")
			# print(cur.fetchall())
		except sqlite3.OperationalError:
			sql=['''
			CREATE TABLE THANHVIEN
			(
				MASV VARCHAR(15) PRIMARY KEY NOT NULL,
   				TENSV NVARCHAR(255),
    			NGAYSINH DATE,
    			GIOITINH NVARCHAR(5),
    			QUEQUAN NVARCHAR(255),
    			DANTOC NVARCHAR(30),
    			TONGIAO NVARCHAR(30) DEFAULT "Không",
    			NGAYVAODOAN DATE,
    			NGAYVAODANG DATE,
    			CHUCVU NVARCHAR(50),
    			LOP VARCHAR(30)
			);

			''', 
			''' CREATE TABLE CHITIETTHU
				(
					MASV VARCHAR(15), -- PK
    				YEAR INT, -- PK
    				T1 INT,
   		 			T2 INT,
    				T3 INT,
    				T4 INT,
    				T5 INT,
    				T6 INT,
    				T7 INT,
    				T8 INT,
    				T9 INT,
    				T10 INT,
    				T11 INT,
    				T12 INT
				);

			''', ''' CREATE TABLE LS 
			(
				NGAY DATE,
				SOCHI INT,
				LIDO NVARCHAR(255)
			);
			''',
			'''CREATE TABLE TONGQUY
				(
					NAM INT PRIMARY KEY,
					TONGTHU INT,
    				TONGCHI INT
				);
			''', '-- ALTER TABLE CHITIETTHU ADD CONSTRAINT PRIMARY KEY (NAM, MASV);'
		, '''--ALTER TABLE CHITIETTHU ADD CONSTRAINT FOREIGN KEY (MASV) REFERENCES THANHVIEN(MASV);''']
			for i in sql:
				cur.execute(i)
			
			self.db.commit()


root=Tk()
root.minsize(1230, 690)
a=app(root, 2020)
root.mainloop()