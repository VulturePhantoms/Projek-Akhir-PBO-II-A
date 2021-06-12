import sqlite3

class DataManager:
	def __init__(self):
		self.conn = sqlite3.connect('Database.db')
		self.cursor = self.conn.cursor()
	def Jalankan(self, query, returnData = False):
		self.cursor.execute(query)
		result = self.cursor.fetchall()
		self.conn.commit()
		if returnData :
			return result

class Akun(DataManager):
	def setDataAkun(self, role, username, password, nama,alamat):
		self.query = 'INSERT INTO pengguna (role, username, password, nama,alamat) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' 
		self.query = self.query % (role, username, password, nama,alamat)
		self.Jalankan(self.query)


	def getDaftarAkun(self):
		self.query = 'SELECT * FROM pengguna'
		hasil = self.Jalankan(self.query, True)
		return hasil

	def updateAkun(self,id_user, role, username, password, nama,alamat):
		self.query = 'UPDATE pengguna SET role=\'%s\', username=\'%s\', password=\'%s\', nama=\'%s\', alamat=\'%s\' where id_user = %i;' 
		self.query = self.query % ( role, username, password, nama, alamat, int(id_user))
		self.Jalankan(self.query)

	def deleteAkun(self,id_user):
		self.query = 'DELETE FROM pengguna where id_user = %i' 
		self.query = self.query % (int(id_user))
		self.Jalankan(self.query)

class Barang(DataManager):
	def setDataBarang(self, NamaBarang, Harga, Jumlah):
		TotalHarga = int(Harga)*int(Jumlah)
		self.query = 'INSERT INTO barang (NamaBarang, Harga, Jumlah, TotalHarga) VALUES (\'%s\', \'%i\', \'%i\', \'%i\')' 
		self.query = self.query % (NamaBarang, int(Harga), int(Jumlah), int(TotalHarga))
		self.Jalankan(self.query)

	def getDaftarBarang(self):
		self.query = 'SELECT * FROM barang'
		hasil = self.Jalankan(self.query, True)
		return hasil

	def updateBarang(self,id_barang, NamaBarang, Harga, Jumlah):
		TotalHarga = int(Harga)*int(Jumlah)
		self.query = 'UPDATE barang SET NamaBarang=\'%s\', Harga=\'%i\', Jumlah=\'%i\', TotalHarga=\'%i\' where id_barang = %i;' 
		self.query = self.query % ( NamaBarang, int(Harga), int(Jumlah), int(TotalHarga),int(id_barang))
		self.Jalankan(self.query)

	def deleteBarang(self,id_barang):
		self.query = 'DELETE FROM barang where id_barang = %i' 
		self.query = self.query % (int(id_barang))
		self.Jalankan(self.query)

class Penjualan(DataManager):
	def setDataPenjualan(self, Tanggal, NamaPembeli, id_barang, harga,  JumlahTerjual):
		TotalPenghasilan = JumlahTerjual*harga
		self.query = 'INSERT INTO penjualan (Tanggal, NamaPembeli, id_barang, JumlahTerjual, TotalPenghasilan) VALUES (\'%s\', \'%s\', \'%i\', \'%i\', \'%i\')' 
		self.query = self.query % (Tanggal, NamaPembeli, int(id_barang), int(JumlahTerjual), int(TotalPenghasilan))
		self.Jalankan(self.query)

	def getDaftarPenjualan(self):
		self.query = 'SELECT t1.id_penjualan, t1.Tanggal, t1.NamaPembeli, t2.NamaBarang, t2.Harga, t1.JumlahTerjual, (t2.Harga*t1.JumlahTerjual) as TotalPenghasilan FROM penjualan t1 join barang t2 on t1.id_barang=t2.id_barang'
		hasil = self.Jalankan(self.query, True)
		return hasil

	def updatePenjualan(self,id_penjualan, Tanggal, NamaPembeli, id_barang, harga, JumlahTerjual):
		TotalPenghasilan = JumlahTerjual*harga
		self.query = 'UPDATE penjualan SET Tanggal=\'%s\', NamaPembeli=\'%s\', id_barang=\'%i\', JumlahTerjual=\'%i\', TotalPenghasilan=\'%i\' where id_penjualan = %i;' 
		self.query = self.query % ( Tanggal, NamaPembeli, int(id_barang), int(JumlahTerjual), int(TotalPenghasilan), int(id_penjualan))
		self.Jalankan(self.query)

	def deletePenjualan(self,id_penjualan):
		self.query = 'DELETE FROM penjualan where id_penjualan= %i' 
		self.query = self.query % (int(id_penjualan))
		self.Jalankan(self.query)
	