# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class login
###########################################################################

class login ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Login", pos = wx.DefaultPosition, size = wx.Size( 204,216 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		bSizer6.Add( self.m_staticText26, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.txt_username = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer6.Add( self.txt_username, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		bSizer6.Add( self.m_staticText27, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.txt_password = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer6.Add( self.txt_password, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.login_btn = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer6.Add( self.login_btn, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.login_btn.Bind( wx.EVT_BUTTON, self.login_btnOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def login_btnOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Home
###########################################################################

class Home ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sistem Manajemen Toko Roti", pos = wx.DefaultPosition, size = wx.Size( 313,202 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		gSizer1 = wx.GridSizer( 0, 1, 0, 0 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Tampil Data Roti", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button2.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_LIST_VIEW, wx.ART_TOOLBAR ) )
		gSizer1.Add( self.m_button2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Ubah Data Roti", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button1.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_OPEN, wx.ART_TOOLBAR ) )
		gSizer1.Add( self.m_button1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button21 = wx.Button( self, wx.ID_ANY, u"Data Akun", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button21.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_DIR_UP, wx.ART_TOOLBAR ) )
		gSizer1.Add( self.m_button21, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button22 = wx.Button( self, wx.ID_ANY, u"Log Out", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button22.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_QUIT, wx.ART_TOOLBAR ) )
		gSizer1.Add( self.m_button22, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.SetSizer( gSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button2.Bind( wx.EVT_BUTTON, self.access_view )
		self.m_button1.Bind( wx.EVT_BUTTON, self.access_Barang )
		self.m_button21.Bind( wx.EVT_BUTTON, self.access_akun )
		self.m_button22.Bind( wx.EVT_BUTTON, self.access_logout )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def access_view( self, event ):
		event.Skip()

	def access_Barang( self, event ):
		event.Skip()

	def access_akun( self, event ):
		event.Skip()

	def access_logout( self, event ):
		event.Skip()


###########################################################################
## Class FrameAkun
###########################################################################

class FrameAkun ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Manajemen Data Akun", pos = wx.DefaultPosition, size = wx.Size( 664,282 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.panel_akun = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panel_akun.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		self.panel_akun.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		gSizer41 = wx.GridSizer( 0, 1, 0, 0 )

		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		gSizer61 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button32 = wx.Button( self.panel_akun, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button32.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GOTO_FIRST, wx.ART_TOOLBAR ) )
		self.m_button32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_button32.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		gSizer61.Add( self.m_button32, 0, wx.ALL, 5 )

		self.m_button42 = wx.Button( self.panel_akun, wx.ID_ANY, u"Tambah Data", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button42.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_NEW_DIR, wx.ART_TOOLBAR ) )
		self.m_button42.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_button42.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		gSizer61.Add( self.m_button42, 0, wx.ALL, 5 )

		gSizer81 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText52 = wx.StaticText( self.panel_akun, wx.ID_ANY, u"Jumlah Akun:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )

		gSizer81.Add( self.m_staticText52, 0, wx.ALL, 5 )

		self.count_akun = wx.StaticText( self.panel_akun, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.count_akun.Wrap( -1 )

		gSizer81.Add( self.count_akun, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gSizer61.Add( gSizer81, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		fgSizer3.Add( gSizer61, 1, wx.EXPAND, 5 )


		fgSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.table_akun = wx.grid.Grid( self.panel_akun, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.table_akun.CreateGrid( 5, 6 )
		self.table_akun.EnableEditing( True )
		self.table_akun.EnableGridLines( True )
		self.table_akun.EnableDragGridSize( False )
		self.table_akun.SetMargins( 0, 0 )

		# Columns
		self.table_akun.SetColSize( 0, 24 )
		self.table_akun.SetColSize( 1, 76 )
		self.table_akun.SetColSize( 2, 76 )
		self.table_akun.SetColSize( 3, 91 )
		self.table_akun.SetColSize( 4, 100 )
		self.table_akun.SetColSize( 5, 71 )
		self.table_akun.EnableDragColMove( False )
		self.table_akun.EnableDragColSize( True )
		self.table_akun.SetColLabelSize( 30 )
		self.table_akun.SetColLabelValue( 0, wx.EmptyString )
		self.table_akun.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.table_akun.EnableDragRowSize( True )
		self.table_akun.SetRowLabelSize( 80 )
		self.table_akun.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.table_akun.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer3.Add( self.table_akun, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		gSizer41.Add( fgSizer3, 1, wx.EXPAND, 5 )


		self.panel_akun.SetSizer( gSizer41 )
		self.panel_akun.Layout()
		gSizer41.Fit( self.panel_akun )
		bSizer7.Add( self.panel_akun, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button32.Bind( wx.EVT_BUTTON, self.access_Menu )
		self.m_button42.Bind( wx.EVT_BUTTON, self.add_btn_akun )
		self.table_akun.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.selectTableCellAkun )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def access_Menu( self, event ):
		event.Skip()

	def add_btn_akun( self, event ):
		event.Skip()

	def selectTableCellAkun( self, event ):
		event.Skip()


###########################################################################
## Class Frame
###########################################################################

class Frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sistem Manajemen Toko Roti", pos = wx.DefaultPosition, size = wx.Size( 674,424 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer2 = wx.GridSizer( 0, 1, 0, 0 )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.panel_barang = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panel_barang.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		gSizer4 = wx.GridSizer( 0, 1, 0, 0 )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		gSizer19 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button3 = wx.Button( self.panel_barang, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button3.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GOTO_FIRST, wx.ART_TOOLBAR ) )
		self.m_button3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_button3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		gSizer19.Add( self.m_button3, 0, wx.ALL, 5 )

		self.m_button4 = wx.Button( self.panel_barang, wx.ID_ANY, u"Tambah Data", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button4.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_NEW_DIR, wx.ART_TOOLBAR ) )
		self.m_button4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_button4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		gSizer19.Add( self.m_button4, 0, wx.ALL, 5 )

		gSizer8 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText5 = wx.StaticText( self.panel_barang, wx.ID_ANY, u"Jumlah Jenis Roti :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		gSizer8.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.count_jenis_barang = wx.StaticText( self.panel_barang, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.count_jenis_barang.Wrap( -1 )

		gSizer8.Add( self.count_jenis_barang, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText7 = wx.StaticText( self.panel_barang, wx.ID_ANY, u"Jumlah Semua Roti :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		gSizer8.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.count_total_barang = wx.StaticText( self.panel_barang, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.count_total_barang.Wrap( -1 )

		gSizer8.Add( self.count_total_barang, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText72 = wx.StaticText( self.panel_barang, wx.ID_ANY, u"Jumlah Laba Kotor :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText72.Wrap( -1 )

		gSizer8.Add( self.m_staticText72, 0, wx.ALL, 5 )

		self.count_laba = wx.StaticText( self.panel_barang, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.count_laba.Wrap( -1 )

		gSizer8.Add( self.count_laba, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		gSizer19.Add( gSizer8, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		fgSizer2.Add( gSizer19, 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.table_Barang = wx.grid.Grid( self.panel_barang, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.table_Barang.CreateGrid( 5, 5 )
		self.table_Barang.EnableEditing( True )
		self.table_Barang.EnableGridLines( True )
		self.table_Barang.EnableDragGridSize( False )
		self.table_Barang.SetMargins( 0, 0 )

		# Columns
		self.table_Barang.SetColSize( 0, 37 )
		self.table_Barang.SetColSize( 1, 76 )
		self.table_Barang.SetColSize( 2, 76 )
		self.table_Barang.SetColSize( 3, 91 )
		self.table_Barang.SetColSize( 4, 84 )
		self.table_Barang.EnableDragColMove( False )
		self.table_Barang.EnableDragColSize( True )
		self.table_Barang.SetColLabelSize( 30 )
		self.table_Barang.SetColLabelValue( 0, wx.EmptyString )
		self.table_Barang.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.table_Barang.EnableDragRowSize( True )
		self.table_Barang.SetRowLabelSize( 80 )
		self.table_Barang.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.table_Barang.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer2.Add( self.table_Barang, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )


		gSizer4.Add( fgSizer2, 1, wx.EXPAND, 5 )


		self.panel_barang.SetSizer( gSizer4 )
		self.panel_barang.Layout()
		gSizer4.Fit( self.panel_barang )
		self.m_notebook1.AddPage( self.panel_barang, u"Data Barang", True )
		self.panel_penjualan = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panel_penjualan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		self.panel_penjualan.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		gSizer41 = wx.GridSizer( 0, 1, 0, 0 )

		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		gSizer61 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button31 = wx.Button( self.panel_penjualan, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button31.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GOTO_FIRST, wx.ART_TOOLBAR ) )
		self.m_button31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_button31.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		gSizer61.Add( self.m_button31, 0, wx.ALL, 5 )

		self.m_button41 = wx.Button( self.panel_penjualan, wx.ID_ANY, u"Tambah Data", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button41.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_NEW_DIR, wx.ART_TOOLBAR ) )
		self.m_button41.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_button41.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		gSizer61.Add( self.m_button41, 0, wx.ALL, 5 )

		gSizer81 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText51 = wx.StaticText( self.panel_penjualan, wx.ID_ANY, u"Jumlah Transaksi:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		gSizer81.Add( self.m_staticText51, 0, wx.ALL, 5 )

		self.count_transaksi = wx.StaticText( self.panel_penjualan, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.count_transaksi.Wrap( -1 )

		gSizer81.Add( self.count_transaksi, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText71 = wx.StaticText( self.panel_penjualan, wx.ID_ANY, u"Jumlah Roti Terjual:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )

		gSizer81.Add( self.m_staticText71, 0, wx.ALL, 5 )

		self.count_total_penghasilan = wx.StaticText( self.panel_penjualan, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.count_total_penghasilan.Wrap( -1 )

		gSizer81.Add( self.count_total_penghasilan, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText721 = wx.StaticText( self.panel_penjualan, wx.ID_ANY, u"Jumlah Total Penghasilan :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText721.Wrap( -1 )

		gSizer81.Add( self.m_staticText721, 0, wx.ALL, 5 )

		self.count_laba1 = wx.StaticText( self.panel_penjualan, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.count_laba1.Wrap( -1 )

		gSizer81.Add( self.count_laba1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		gSizer61.Add( gSizer81, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		fgSizer3.Add( gSizer61, 1, wx.EXPAND, 5 )


		fgSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.table_Penjualan = wx.grid.Grid( self.panel_penjualan, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.table_Penjualan.CreateGrid( 5, 7 )
		self.table_Penjualan.EnableEditing( True )
		self.table_Penjualan.EnableGridLines( True )
		self.table_Penjualan.EnableDragGridSize( False )
		self.table_Penjualan.SetMargins( 0, 0 )

		# Columns
		self.table_Penjualan.SetColSize( 0, 24 )
		self.table_Penjualan.SetColSize( 1, 76 )
		self.table_Penjualan.SetColSize( 2, 76 )
		self.table_Penjualan.SetColSize( 3, 91 )
		self.table_Penjualan.SetColSize( 4, 100 )
		self.table_Penjualan.SetColSize( 5, 71 )
		self.table_Penjualan.EnableDragColMove( False )
		self.table_Penjualan.EnableDragColSize( True )
		self.table_Penjualan.SetColLabelSize( 30 )
		self.table_Penjualan.SetColLabelValue( 0, wx.EmptyString )
		self.table_Penjualan.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.table_Penjualan.EnableDragRowSize( True )
		self.table_Penjualan.SetRowLabelSize( 80 )
		self.table_Penjualan.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.table_Penjualan.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer3.Add( self.table_Penjualan, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		gSizer41.Add( fgSizer3, 1, wx.EXPAND, 5 )


		self.panel_penjualan.SetSizer( gSizer41 )
		self.panel_penjualan.Layout()
		gSizer41.Fit( self.panel_penjualan )
		self.m_notebook1.AddPage( self.panel_penjualan, u"Data Penjualan", False )

		gSizer2.Add( self.m_notebook1, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( gSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button3.Bind( wx.EVT_BUTTON, self.access_Menu )
		self.m_button4.Bind( wx.EVT_BUTTON, self.add_btn )
		self.table_Barang.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.selectTableCell )
		self.m_button31.Bind( wx.EVT_BUTTON, self.access_Menu )
		self.m_button41.Bind( wx.EVT_BUTTON, self.add_btn_jual )
		self.table_Penjualan.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.selectTableCellJual )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def access_Menu( self, event ):
		event.Skip()

	def add_btn( self, event ):
		event.Skip()

	def selectTableCell( self, event ):
		event.Skip()


	def add_btn_jual( self, event ):
		event.Skip()

	def selectTableCellJual( self, event ):
		event.Skip()


###########################################################################
## Class view_frame
###########################################################################

class view_frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sistem Manajemen Toko Roti", pos = wx.DefaultPosition, size = wx.Size( 694,485 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button3.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GOTO_FIRST, wx.ART_TOOLBAR ) )
		self.m_button3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_button3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer3.Add( self.m_button3, 0, wx.ALL, 5 )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Data Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		self.m_staticText26.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer1.Add( self.m_staticText26, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.table_Barang = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.table_Barang.CreateGrid( 5, 5 )
		self.table_Barang.EnableEditing( True )
		self.table_Barang.EnableGridLines( True )
		self.table_Barang.EnableDragGridSize( False )
		self.table_Barang.SetMargins( 0, 0 )

		# Columns
		self.table_Barang.EnableDragColMove( False )
		self.table_Barang.EnableDragColSize( True )
		self.table_Barang.SetColLabelSize( 30 )
		self.table_Barang.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.table_Barang.EnableDragRowSize( True )
		self.table_Barang.SetRowLabelSize( 80 )
		self.table_Barang.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.table_Barang.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer1.Add( self.table_Barang, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer3.Add( bSizer1, 1, wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"Data Penjualan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		self.m_staticText27.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer2.Add( self.m_staticText27, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.table_Penjualan = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.table_Penjualan.CreateGrid( 5, 7 )
		self.table_Penjualan.EnableEditing( True )
		self.table_Penjualan.EnableGridLines( True )
		self.table_Penjualan.EnableDragGridSize( False )
		self.table_Penjualan.SetMargins( 0, 0 )

		# Columns
		self.table_Penjualan.SetColSize( 0, 24 )
		self.table_Penjualan.SetColSize( 1, 76 )
		self.table_Penjualan.SetColSize( 2, 76 )
		self.table_Penjualan.SetColSize( 3, 91 )
		self.table_Penjualan.SetColSize( 4, 100 )
		self.table_Penjualan.SetColSize( 5, 71 )
		self.table_Penjualan.EnableDragColMove( False )
		self.table_Penjualan.EnableDragColSize( True )
		self.table_Penjualan.SetColLabelSize( 30 )
		self.table_Penjualan.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.table_Penjualan.EnableDragRowSize( True )
		self.table_Penjualan.SetRowLabelSize( 80 )
		self.table_Penjualan.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.table_Penjualan.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer2.Add( self.table_Penjualan, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer3.Add( bSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button3.Bind( wx.EVT_BUTTON, self.access_Menu )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def access_Menu( self, event ):
		event.Skip()


###########################################################################
## Class Dialog_barang
###########################################################################

class Dialog_barang ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tambah Data Roti", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Nama Roti", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		gSizer6.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.nama_brg = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.nama_brg, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Stok", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		gSizer6.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.jumlah_brg = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.jumlah_brg, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		gSizer6.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.harga_brg = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.harga_brg, 0, wx.ALL, 5 )


		gSizer5.Add( gSizer6, 1, wx.EXPAND, 5 )

		gSizer9 = wx.GridSizer( 0, 1, 0, 0 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.dialog_btn = wx.Button( self, wx.ID_ANY, u"TAMBAH", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.dialog_btn.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE, wx.ART_BUTTON ) )
		bSizer5.Add( self.dialog_btn, 0, wx.ALL, 5 )

		self.batal_btn = wx.Button( self, wx.ID_ANY, u"BATAL", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.batal_btn.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_UNDO, wx.ART_BUTTON ) )
		bSizer5.Add( self.batal_btn, 0, wx.ALL, 5 )


		gSizer9.Add( bSizer5, 1, wx.EXPAND, 5 )

		gSizer10 = wx.GridSizer( 0, 2, 0, 0 )

		self.edit_barangtext = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.edit_barangtext.Wrap( -1 )

		gSizer10.Add( self.edit_barangtext, 0, wx.ALL, 5 )

		self.edit_barangnum = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.edit_barangnum.Wrap( -1 )

		gSizer10.Add( self.edit_barangnum, 0, wx.ALL, 5 )


		gSizer9.Add( gSizer10, 1, wx.EXPAND, 5 )


		gSizer5.Add( gSizer9, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer5 )
		self.Layout()
		gSizer5.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.dialog_btn.Bind( wx.EVT_BUTTON, self.dialog_btnclick )
		self.batal_btn.Bind( wx.EVT_BUTTON, self.batal_btnOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def dialog_btnclick( self, event ):
		event.Skip()

	def batal_btnOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Dialog_penjualan
###########################################################################

class Dialog_penjualan ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tambah Data Pembelian", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Tanggal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		gSizer6.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.tanggal_jual = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.tanggal_jual, 0, wx.ALL, 5 )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Nama Pembeli", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		gSizer6.Add( self.m_staticText21, 0, wx.ALL, 5 )

		self.nama_pembeli = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.nama_pembeli, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"ID Roti", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		gSizer6.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.id_brg = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.id_brg, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Jumlah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		gSizer6.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.jumlah_jual = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.jumlah_jual, 0, wx.ALL, 5 )


		gSizer5.Add( gSizer6, 1, wx.EXPAND, 5 )

		gSizer9 = wx.GridSizer( 0, 1, 0, 0 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.dialog_btn = wx.Button( self, wx.ID_ANY, u"TAMBAH", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.dialog_btn.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE, wx.ART_BUTTON ) )
		bSizer4.Add( self.dialog_btn, 0, wx.ALL, 5 )

		self.batal_btn1 = wx.Button( self, wx.ID_ANY, u"BATAL", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.batal_btn1.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_UNDO, wx.ART_BUTTON ) )
		bSizer4.Add( self.batal_btn1, 0, wx.ALL, 5 )


		gSizer9.Add( bSizer4, 1, wx.EXPAND, 5 )

		gSizer10 = wx.GridSizer( 0, 2, 0, 0 )

		self.edit_jualtext = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.edit_jualtext.Wrap( -1 )

		gSizer10.Add( self.edit_jualtext, 0, wx.ALL, 5 )

		self.edit_jualnum = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.edit_jualnum.Wrap( -1 )

		gSizer10.Add( self.edit_jualnum, 0, wx.ALL, 5 )


		gSizer9.Add( gSizer10, 1, wx.EXPAND, 5 )


		gSizer5.Add( gSizer9, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer5 )
		self.Layout()
		gSizer5.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.dialog_btn.Bind( wx.EVT_BUTTON, self.dialog_btnclick_jual )
		self.batal_btn1.Bind( wx.EVT_BUTTON, self.batal_btn1OnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def dialog_btnclick_jual( self, event ):
		event.Skip()

	def batal_btn1OnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Dialog_akun
###########################################################################

class Dialog_akun ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tambah Data Akun", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText52 = wx.StaticText( self, wx.ID_ANY, u"Role", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )

		gSizer6.Add( self.m_staticText52, 0, wx.ALL, 5 )

		role_pilihChoices = [ u"Pekerja", u"Owner" ]
		self.role_pilih = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 110,-1 ), role_pilihChoices, 0 )
		self.role_pilih.SetSelection( 1 )
		gSizer6.Add( self.role_pilih, 0, wx.ALL, 5 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		gSizer6.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.username_txt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.username_txt, 0, wx.ALL, 5 )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		gSizer6.Add( self.m_staticText21, 0, wx.ALL, 5 )

		self.password_txt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.password_txt, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		gSizer6.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.nama_txt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.nama_txt, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		gSizer6.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.alamat_txt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.alamat_txt, 0, wx.ALL, 5 )


		gSizer5.Add( gSizer6, 1, wx.EXPAND, 5 )

		gSizer9 = wx.GridSizer( 0, 1, 0, 0 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.dialog_btn = wx.Button( self, wx.ID_ANY, u"TAMBAH", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.dialog_btn.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE, wx.ART_BUTTON ) )
		bSizer4.Add( self.dialog_btn, 0, wx.ALL, 5 )

		self.batal_btn1 = wx.Button( self, wx.ID_ANY, u"BATAL", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.batal_btn1.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_UNDO, wx.ART_BUTTON ) )
		bSizer4.Add( self.batal_btn1, 0, wx.ALL, 5 )


		gSizer9.Add( bSizer4, 1, wx.EXPAND, 5 )

		gSizer10 = wx.GridSizer( 0, 2, 0, 0 )

		self.edit_akuntext = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.edit_akuntext.Wrap( -1 )

		gSizer10.Add( self.edit_akuntext, 0, wx.ALL, 5 )

		self.edit_akunnum = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.edit_akunnum.Wrap( -1 )

		gSizer10.Add( self.edit_akunnum, 0, wx.ALL, 5 )


		gSizer9.Add( gSizer10, 1, wx.EXPAND, 5 )


		gSizer5.Add( gSizer9, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer5 )
		self.Layout()
		gSizer5.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.dialog_btn.Bind( wx.EVT_BUTTON, self.dialog_btnclick_akun )
		self.batal_btn1.Bind( wx.EVT_BUTTON, self.batal_btn2OnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def dialog_btnclick_akun( self, event ):
		event.Skip()

	def batal_btn2OnButtonClick( self, event ):
		event.Skip()


