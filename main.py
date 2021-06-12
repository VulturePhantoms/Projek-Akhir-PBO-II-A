import wx
import GridView
import control

class Login(GridView.login):
	def __init__(self,parent):
		GridView.login.__init__(self,parent)
		self.SetIcon(wx.Icon("logo.ico"))
		#self.database = {"user":"admin"}
	
	#def validasi(self):
		#self.username = self.txt_username.GetValue()
		#self.password = self.txt_password.GetValue()

	#def daftar_btnOnButtonClick(self,event):
		#self.validasi()
		#self.database[self.username] = self.password
		#wx.MessageBox("Pendaftaran Berhasil")

	def login_btnOnButtonClick(self,event):
		self.ceklogin()
		#try:
		# 	if self.database[self.username] == self.password:
		# 		wx.MessageBox("Login Berhasil")
		# 		self.sukseslogin()
		# 	else:
		# 		wx.MessageBox("Login Gagal")
		#except:
		# 	wx.MessageBox("Login Kacau")
	
	def ceklogin( self):
		user = True
		daftarAcc = control.Akun().getDaftarAkun()
		for acc_row in daftarAcc:
			#try:
				if self.txt_username.GetValue() == acc_row[2] and self.txt_password.GetValue() == acc_row[3]:
					wx.MessageBox('Login berhasil.', 'Sukses', wx.OK | wx.ICON_INFORMATION)
					if acc_row[1] == 'Owner':
						wx.MessageBox('Halo Owner.', 'Sukses', wx.OK | wx.ICON_INFORMATION)
						user = True
						self.sukseslogin(user)
						break
					else:
						wx.MessageBox('Halo Pekerja.', 'Sukses', wx.OK | wx.ICON_INFORMATION)
						user = False
						self.sukseslogin(user)
						break
				elif self.txt_username.GetValue() == acc_row[2] and self.txt_password.GetValue() != acc_row[3]:
					wx.MessageBox('Mohon cek kembali Password anda.', 'Kesalahan', wx.OK | wx.ICON_ERROR)
				#elif self.txt_username.GetValue() != acc_row[2]:
					#wx.MessageBox('Mohon periksa kembali Username dan Password.', 'Kesalahan', wx.OK | wx.ICON_ERROR)
			#except:
				#wx.MessageBox('Mohon periksa kembali Username dan Password.', 'Kesalahan', wx.OK | wx.ICON_ERROR)

	def sukseslogin(self,user):
		self.Destroy()
		if user == True:
			frame1 = Home(None)
			frame1.Show()
		else:
			#self.m_button21.Destroy()
			frame1 = Home(None).roleCek()
			frame1.Show()
			#Home.roleCek()



class Home(GridView.Home):
	def __init__(self,parent):
		GridView.Home.__init__(self,parent)
		self.SetIcon(wx.Icon("logo.ico"))
		#self.m_button21.Destroy()


	def roleCek( self ):
		self.m_button21.Destroy()

        
	def access_Barang(self,event):
		self.Destroy()
		frame2 = Frame(None)
		frame2.Show()
		
	def access_view(self, event):
		self.Destroy()
		frame3 = view_frame(None)
		frame3.Show()
	
	def access_akun(self, event):
		self.Destroy()
		frame5 = FrameAkun(None)
		frame5.Show()

	def access_logout(self, event):
		dlg = wx.MessageDialog(self,'Log Out', 'Informasi', style=wx.YES_NO )
		retval = dlg.ShowModal()
		if retval == wx.ID_YES:
			self.Destroy()
			frame4 = Login(None)
			frame4.Show()

class view_frame(GridView.view_frame):
	def __init__(self,parent):
		GridView.view_frame.__init__(self,parent)	
		self.readDataBarang()
		self.readDataPenjualan()
		self.SetIcon(wx.Icon("logo.ico"))

	def access_Menu(self,event):
		self.Destroy()
		frame1 = Home(None)
		frame1.Show()
		

	def readDataBarang(self):
		n_cols = self.table_Barang.GetNumberCols()
		n_rows = self.table_Barang.GetNumberRows()
		if n_cols > 0:
			self.table_Barang.DeleteCols(0, n_cols, True)        
		if n_rows > 0:
			self.table_Barang.DeleteRows(0, n_rows, True)   

		koloms = ['ID Roti', 'Nama Roti', 'Harga', 'Stok', 'Laba Kotor']
		self.table_Barang.AppendCols(len(koloms))
		for col in range(len(koloms)):
			self.table_Barang.SetColLabelValue(col, koloms[col])

		tot_jumlah = 0
		baris = 0
		daftarBrg = control.Barang().getDaftarBarang() 
		for brg_row in daftarBrg:
			self.table_Barang.AppendRows(1)
			id_barang,nama,harga,jumlah,tot_harga = brg_row
			self.table_Barang.SetCellValue(baris, 0, str(id_barang) )
			self.table_Barang.SetCellValue(baris, 1, str(nama) )
			self.table_Barang.SetCellValue(baris, 2, str(harga) )
			self.table_Barang.SetCellValue(baris, 3, str(jumlah) )
			self.table_Barang.SetCellValue(baris, 4, str(tot_harga) )
			tot_jumlah += jumlah
			baris += 1

	def readDataPenjualan(self):
		n_cols = self.table_Penjualan.GetNumberCols()
		n_rows = self.table_Penjualan.GetNumberRows()
		if n_cols > 0:
			self.table_Penjualan.DeleteCols(0, n_cols, True)        
		if n_rows > 0:
			self.table_Penjualan.DeleteRows(0, n_rows, True)   

		koloms = ['ID penjualan', 'Tanggal', 'Nama Pembeli', 'Nama Roti', 'Harga', 'Jumlah', 'Harga Total']
		self.table_Penjualan.AppendCols(len(koloms))
		for col in range(len(koloms)):
			self.table_Penjualan.SetColLabelValue(col, koloms[col])


		baris = 0
		daftarJual = control.Penjualan().getDaftarPenjualan() 
		for jual_row in daftarJual:
			self.table_Penjualan.AppendRows(1)
			id_penjualan,tanggal,namapembeli,nama,harga,jumlahterjual,tot_penghasilan = jual_row
			self.table_Penjualan.SetCellValue(baris, 0, str(id_penjualan) )
			self.table_Penjualan.SetCellValue(baris, 1, str(tanggal) )
			self.table_Penjualan.SetCellValue(baris, 2, str(namapembeli) )
			self.table_Penjualan.SetCellValue(baris, 3, str(nama) )
			self.table_Penjualan.SetCellValue(baris, 4, str(harga) )
			self.table_Penjualan.SetCellValue(baris, 5, str(jumlahterjual) )
			self.table_Penjualan.SetCellValue(baris, 6, str(tot_penghasilan) )
			baris += 1

class Frame(GridView.Frame):
	def __init__(self,parent):
		GridView.Frame.__init__(self,parent)
		self.readDataBarang()
		self.readDataPenjualan()
		self.AddButtonEditDelete()
		self.AddButtonEditDeleteJual()
		self.SetIcon(wx.Icon("logo.ico"))

	def access_Menu(self,event):
		self.Destroy()
		frame1 = Home(None)
		frame1.Show()


	def readDataBarang(self):
		n_cols = self.table_Barang.GetNumberCols()
		n_rows = self.table_Barang.GetNumberRows()
		if n_cols > 0:
			self.table_Barang.DeleteCols(0, n_cols, True)        
		if n_rows > 0:
			self.table_Barang.DeleteRows(0, n_rows, True)   

		koloms = ['ID Roti', 'Nama Roti', 'Harga', 'Stok', 'Laba Kotor']
		self.table_Barang.AppendCols(len(koloms))
		for col in range(len(koloms)):
			self.table_Barang.SetColLabelValue(col, koloms[col])

		tot_jumlah = 0
		tot_laba = 0
		baris = 0
		daftarBrg = control.Barang().getDaftarBarang() 
		for brg_row in daftarBrg:
			self.table_Barang.AppendRows(1)
			id_barang,nama,harga,jumlah,tot_harga = brg_row
			self.table_Barang.SetCellValue(baris, 0, str(id_barang) )
			self.table_Barang.SetCellValue(baris, 1, str(nama) )
			self.table_Barang.SetCellValue(baris, 2, str(harga) )
			self.table_Barang.SetCellValue(baris, 3, str(jumlah) )
			self.table_Barang.SetCellValue(baris, 4, str(tot_harga) )
			tot_jumlah += jumlah
			tot_laba += tot_harga
			baris += 1

		self.count_jenis_barang.SetLabel(str(baris))
		self.count_total_barang.SetLabel(str(tot_jumlah))
		self.count_laba.SetLabel(str(tot_laba))

	def readDataPenjualan(self):
		n_cols = self.table_Penjualan.GetNumberCols()
		n_rows = self.table_Penjualan.GetNumberRows()
		if n_cols > 0:
			self.table_Penjualan.DeleteCols(0, n_cols, True)        
		if n_rows > 0:
			self.table_Penjualan.DeleteRows(0, n_rows, True)   

		koloms = ['ID Penjualan', 'Tanggal', 'Nama Pembeli', 'Nama Roti', 'Harga', 'Jumlah', 'Harga Total']
		self.table_Penjualan.AppendCols(len(koloms))
		for col in range(len(koloms)):
			self.table_Penjualan.SetColLabelValue(col, koloms[col])

		tot_jumlah = 0
		tot_laba1 = 0
		baris = 0
		daftarJual = control.Penjualan().getDaftarPenjualan() 
		for jual_row in daftarJual:
			self.table_Penjualan.AppendRows(1)
			id_penjualan,tanggal,namapembeli,nama,harga,jumlahterjual,tot_penghasilan = jual_row
			self.table_Penjualan.SetCellValue(baris, 0, str(id_penjualan) )
			self.table_Penjualan.SetCellValue(baris, 1, str(tanggal) )
			self.table_Penjualan.SetCellValue(baris, 2, str(namapembeli) )
			self.table_Penjualan.SetCellValue(baris, 3, str(nama) )
			self.table_Penjualan.SetCellValue(baris, 4, str(harga) )
			self.table_Penjualan.SetCellValue(baris, 5, str(jumlahterjual) )
			self.table_Penjualan.SetCellValue(baris, 6, str(tot_penghasilan) )
			tot_jumlah += jumlahterjual
			tot_laba1 += tot_penghasilan
			baris += 1

		self.count_transaksi.SetLabel(str(baris))
		self.count_total_penghasilan.SetLabel(str(tot_jumlah))
		self.count_laba1.SetLabel(str(tot_laba1))

	def AddButtonEditDelete(self):		
		jmlKolom = self.table_Barang.GetNumberCols()
		self.table_Barang.AppendCols(2)
		colEdit = jmlKolom 
		colDelete = jmlKolom + 1

		self.table_Barang.SetColLabelValue(colEdit, '')
		self.table_Barang.SetColLabelValue(colDelete, '')

		for row in range (self.table_Barang.GetNumberRows()):
			self.table_Barang.SetCellValue(row,colEdit,'Edit')
			self.table_Barang.SetCellBackgroundColour(row,colEdit,wx.BLUE)
			self.table_Barang.SetCellTextColour(row,colEdit,wx.WHITE)

			self.table_Barang.SetCellValue(row,colDelete,'Delete')
			self.table_Barang.SetCellBackgroundColour(row,colDelete,wx.RED)
			self.table_Barang.SetCellTextColour(row,colDelete,wx.WHITE)

		self.table_Barang.Fit()

	def AddButtonEditDeleteJual(self):		
		jmlKolom = self.table_Penjualan.GetNumberCols()
		self.table_Penjualan.AppendCols(2)
		colEdit = jmlKolom 
		colDelete = jmlKolom + 1

		self.table_Penjualan.SetColLabelValue(colEdit, '')
		self.table_Penjualan.SetColLabelValue(colDelete, '')

		for row in range (self.table_Penjualan.GetNumberRows()):
			self.table_Penjualan.SetCellValue(row,colEdit,'Edit')
			self.table_Penjualan.SetCellBackgroundColour(row,colEdit,wx.BLUE)
			self.table_Penjualan.SetCellTextColour(row,colEdit,wx.WHITE)

			self.table_Penjualan.SetCellValue(row,colDelete,'Delete')
			self.table_Penjualan.SetCellBackgroundColour(row,colDelete,wx.RED)
			self.table_Penjualan.SetCellTextColour(row,colDelete,wx.WHITE)

		self.table_Penjualan.Fit()

	def add_btn( self, event ):
		dlg = Dialog_barang(self)
		dlg.SetLabel('Tambah Data Roti')
		dlg.dialog_btn.SetLabel('TAMBAH')
		dlg.ShowModal()

	def add_btn_jual( self, event ):
		dlg = Dialog_penjualan(self)
		dlg.SetLabel('Tambah Data Penjualan')
		dlg.dialog_btn.SetLabel('TAMBAH')
		dlg.ShowModal()

	def addDataBarang( self, NamaBarang, Harga, Jumlah ):
		control.Barang().setDataBarang(NamaBarang, Harga, Jumlah)
		self.readDataBarang()
		self.AddButtonEditDelete()
	
	def addDataPenjualan( self, Tanggal, NamaPembeli, id_barang, JumlahTerjual ):
		daftarBrg = control.Barang().getDaftarBarang()
		barangTersedia = False
		for brg_row in daftarBrg:
			if int(id_barang) == brg_row[0]:
				barangTersedia = True
				control.Penjualan().setDataPenjualan(Tanggal, NamaPembeli, id_barang, brg_row[2], JumlahTerjual)
				break
		if barangTersedia==False:
			wx.MessageBox('ID Roti Tidak Tersedia.', 'Kesalahan', wx.OK | wx.ICON_ERROR)
		self.readDataPenjualan()
		self.AddButtonEditDeleteJual()
		
	def updateDataBarang( self,id_barang, NamaBarang, Harga, Jumlah ):
		control.Barang().updateBarang(id_barang, NamaBarang, Harga, Jumlah)
		self.readDataBarang()
		self.AddButtonEditDelete()

	def updateDataPenjualan( self,id_penjualan, Tanggal, NamaPembeli, id_barang, JumlahTerjual ):
		daftarBrg = control.Barang().getDaftarBarang()
		barangTersedia = False
		for brg_row in daftarBrg:
			if int(id_barang) == brg_row[0]:
				barangTersedia = True
				control.Penjualan().updatePenjualan(id_penjualan, Tanggal, NamaPembeli, id_barang, brg_row[2], JumlahTerjual)
				break
		if barangTersedia==False:
			wx.MessageBox('ID Roti Tidak Tersedia.', 'Kesalahan', wx.OK | wx.ICON_ERROR)
		self.readDataPenjualan()
		self.AddButtonEditDeleteJual()

	def selectTableCell( self, event ):
		Row = event.GetRow()
		Col = event.GetCol()
		if Col == 5:	
			id_barang = self.table_Barang.GetCellValue(Row,0)
			nama = self.table_Barang.GetCellValue(Row,1) 
			harga = self.table_Barang.GetCellValue(Row,2)
			jumlah = self.table_Barang.GetCellValue(Row,3)
			dlg = Dialog_barang(self, id_barang)
			dlg.SetLabel('Edit Data Roti')
			dlg.dialog_btn.SetLabel('EDIT')
			dlg.edit_barangtext.SetLabel('ID Roti :')
			dlg.edit_barangnum.SetLabel(str(id_barang))
			dlg.editPreText(nama, harga, jumlah)
			dlg.ShowModal()
		elif Col == 6:
			id_barang = self.table_Barang.GetCellValue(Row,0)
			dlg = wx.MessageDialog(self,'Hapus data', 'Informasi', style=wx.YES_NO )
			retval = dlg.ShowModal()
			if retval == wx.ID_YES:
				control.Barang().deleteBarang(id_barang)
				self.readDataBarang()
				self.AddButtonEditDelete()

	def selectTableCellJual( self, event ):
		Row = event.GetRow()
		Col = event.GetCol()
		if Col == 7:	
			id_penjualan = self.table_Penjualan.GetCellValue(Row,0)
			tanggal = self.table_Penjualan.GetCellValue(Row,1)
			namapembeli = self.table_Penjualan.GetCellValue(Row,2)
			daftarBrg = control.Barang().getDaftarBarang()
			for brg_row in daftarBrg:
				if self.table_Penjualan.GetCellValue(Row,3) == brg_row[1]:
					id_barang = str(brg_row[0])
					break 
			jumlahTerjual = self.table_Penjualan.GetCellValue(Row,5)
			dlg = Dialog_penjualan(self, id_penjualan)
			dlg.SetLabel('Edit Data Penjualan')
			dlg.dialog_btn.SetLabel('EDIT')
			dlg.edit_jualtext.SetLabel('ID Penjualan :')
			dlg.edit_jualnum.SetLabel(str(id_penjualan))
			dlg.editPreTextJual(tanggal, namapembeli, id_barang, jumlahTerjual)
			dlg.ShowModal()
		elif Col == 8:
			id_penjualan = self.table_Penjualan.GetCellValue(Row,0)
			dlg = wx.MessageDialog(self,'Hapus data', 'Informasi', style=wx.YES_NO )
			retval = dlg.ShowModal()
			if retval == wx.ID_YES:
				control.Penjualan().deletePenjualan(id_penjualan)
				self.readDataPenjualan()
				self.AddButtonEditDeleteJual()

class FrameAkun(GridView.Frame):
	def __init__(self,parent):
		GridView.FrameAkun.__init__(self,parent)
		self.readDataAkun()
		self.AddButtonEditDeleteAkun()
		self.SetIcon(wx.Icon("logo.ico"))

	def access_Menu(self,event):
		self.Destroy()
		frame1 = Home(None)
		frame1.Show()

	def readDataAkun(self):
		n_cols = self.table_akun.GetNumberCols()
		n_rows = self.table_akun.GetNumberRows()
		if n_cols > 0:
			self.table_akun.DeleteCols(0, n_cols, True)        
		if n_rows > 0:
			self.table_akun.DeleteRows(0, n_rows, True)   

		koloms = ['ID Akun', 'Role', 'Username', 'Password', 'Nama', 'Alamat']
		self.table_akun.AppendCols(len(koloms))
		for col in range(len(koloms)):
			self.table_akun.SetColLabelValue(col, koloms[col])

		baris = 0
		daftarAkun = control.Akun().getDaftarAkun() 
		for akun_row in daftarAkun:
			self.table_akun.AppendRows(1)
			id_user,role,username,password,nama,alamat= akun_row
			self.table_akun.SetCellValue(baris, 0, str(id_user) )
			self.table_akun.SetCellValue(baris, 1, str(role) )
			self.table_akun.SetCellValue(baris, 2, str(username) )
			self.table_akun.SetCellValue(baris, 3, str(password) )
			self.table_akun.SetCellValue(baris, 4, str(nama) )
			self.table_akun.SetCellValue(baris, 5, str(alamat) )
			baris += 1

		self.count_akun.SetLabel(str(baris))
	
	def AddButtonEditDeleteAkun(self):		
		jmlKolom = self.table_akun.GetNumberCols()
		self.table_akun.AppendCols(2)
		colEdit = jmlKolom 
		colDelete = jmlKolom + 1

		self.table_akun.SetColLabelValue(colEdit, '')
		self.table_akun.SetColLabelValue(colDelete, '')

		for row in range (self.table_akun.GetNumberRows()):
			self.table_akun.SetCellValue(row,colEdit,'Edit')
			self.table_akun.SetCellBackgroundColour(row,colEdit,wx.BLUE)
			self.table_akun.SetCellTextColour(row,colEdit,wx.WHITE)

			self.table_akun.SetCellValue(row,colDelete,'Delete')
			self.table_akun.SetCellBackgroundColour(row,colDelete,wx.RED)
			self.table_akun.SetCellTextColour(row,colDelete,wx.WHITE)

		self.table_akun.Fit()
	
	def add_btn_akun( self, event ):
		dlg = Dialog_akun(self)
		dlg.SetLabel('Tambah Data Akun')
		dlg.dialog_btn.SetLabel('TAMBAH')
		dlg.ShowModal()
	
	def addDataAkun( self, role, username, password, nama, alamat ):
		control.Akun().setDataAkun(role, username, password, nama, alamat)
		self.readDataAkun()
		self.AddButtonEditDeleteAkun()

	def updateDataAkun( self,id_user, role, username, password, nama, alamat ):
		control.Akun().updateAkun(id_user, role, username, password, nama, alamat)
		self.readDataAkun()
		self.AddButtonEditDeleteAkun()
	
	def selectTableCellAkun( self, event ):
		Row = event.GetRow()
		Col = event.GetCol()
		if Col == 6:	
			id_user = self.table_akun.GetCellValue(Row,0)
			role = self.table_akun.GetCellValue(Row,1)
			username = self.table_akun.GetCellValue(Row,2)
			password = self.table_akun.GetCellValue(Row,3)
			nama = self.table_akun.GetCellValue(Row,4)
			alamat = self.table_akun.GetCellValue(Row,5)
			dlg = Dialog_akun(self, id_user)
			dlg.SetLabel('Edit Data User')
			dlg.dialog_btn.SetLabel('EDIT')
			dlg.edit_akuntext.SetLabel('ID User :')
			dlg.edit_akunnum.SetLabel(str(id_user))
			dlg.editPreTextAkun(role, username, password, nama, alamat)
			dlg.ShowModal()
		elif Col == 7:
			id_user = self.table_akun.GetCellValue(Row,0)
			dlg = wx.MessageDialog(self,'Hapus data', 'Informasi', style=wx.YES_NO )
			retval = dlg.ShowModal()
			if retval == wx.ID_YES:
				control.Akun().deleteAkun(id_user)
				self.readDataAkun()
				self.AddButtonEditDeleteAkun()



class Dialog_barang(GridView.Dialog_barang):
	def __init__(self, parent, id_barang=-1):
		GridView.Dialog_barang.__init__(self, parent)
		self.parent = parent 
		self.id_barang = id_barang

	def dialog_btnclick( self, event ):
		if self.id_barang == -1:
			self.parent.addDataBarang(self.nama_brg.GetValue(), self.harga_brg.GetValue(),self.jumlah_brg.GetValue())
		else:
			self.parent.updateDataBarang(self.id_barang,self.nama_brg.GetValue(), self.harga_brg.GetValue(),self.jumlah_brg.GetValue())
		self.Destroy()

	def batal_btnOnButtonClick( self, event ):
		self.Destroy()

	def editPreText(self, NamaBarang, Harga, Jumlah):
		self.nama_brg.SetValue(NamaBarang)
		self.harga_brg.SetValue(Harga)
		self.jumlah_brg.SetValue(Jumlah)

class Dialog_penjualan(GridView.Dialog_penjualan):
	def __init__(self, parent, id_penjualan=-1):
		GridView.Dialog_penjualan.__init__(self, parent)
		self.parent = parent 
		self.id_penjualan = id_penjualan

	def dialog_btnclick_jual( self, event ):
		if self.id_penjualan == -1:
			self.parent.addDataPenjualan(self.tanggal_jual.GetValue(), self.nama_pembeli.GetValue(), self.id_brg.GetValue(),self.jumlah_jual.GetValue())
		else:
			self.parent.updateDataPenjualan(self.id_penjualan,self.tanggal_jual.GetValue(), self.nama_pembeli.GetValue(), self.id_brg.GetValue(),self.jumlah_jual.GetValue())
		self.Destroy()

	def batal_btn1OnButtonClick( self, event ):
		self.Destroy()

	def editPreTextJual(self, Tanggal, NamaPembeli, id_barang, JumlahTerjual):
		self.tanggal_jual.SetValue(Tanggal)
		self.nama_pembeli.SetValue(NamaPembeli)
		self.id_brg.SetValue(id_barang)
		self.jumlah_jual.SetValue(JumlahTerjual)
	
class Dialog_akun(GridView.Dialog_akun):
	def __init__(self, parent, id_user=-1):
		GridView.Dialog_akun.__init__(self, parent)
		self.parent = parent 
		self.id_user = id_user

	def dialog_btnclick_akun( self, event ):
		if self.id_user == -1:
			self.parent.addDataAkun(self.role_pilih.GetStringSelection(), self.username_txt.GetValue(), self.password_txt.GetValue(),self.nama_txt.GetValue(),self.alamat_txt.GetValue())
		else:
			self.parent.updateDataAkun(self.id_user,self.role_pilih.GetStringSelection(), self.username_txt.GetValue(), self.password_txt.GetValue(),self.nama_txt.GetValue(),self.alamat_txt.GetValue())
		self.Destroy()

	def batal_btn2OnButtonClick( self, event ):
		self.Destroy()

	def editPreTextAkun(self, role, username, password, nama, alamat):
		self.role_pilih.SetStringSelection(role)
		self.username_txt.SetValue(username)
		self.password_txt.SetValue(password)
		self.nama_txt.SetValue(nama)
		self.alamat_txt.SetValue(alamat)

app = wx.App()
frame4 = Login(None)
frame4.Show()
app.MainLoop()