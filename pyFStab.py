# -*- coding: utf-8 -*-
#! /usr/bin/env python
import sys

from copy import copy
from PyQt4 import QtGui, QtCore, uic

_fromUtf8 = QtCore.QString.fromUtf8

class disk_class:
	def init(self):
	#See fstab documentation for more information
		self.uuid = ""
		self.path = ""
		self.mountPoint = ""
		self.fstype = ""
		#Options
		#Value 1 means "True", value 0 "False", value -1 "Not Assigned"
		self.defaults = -1
		self.sync = -1
		self.atime = -1
		self.relatime = -1
		self.strictatime = -1
		self.diratime = -1
		self.exe = -1
		self.dev = -1
		self.auto = -1
		self.mand = -1
		self.suid = -1
		self.user = -1
		self.write = -1
		self.dirsync = -1
		self.group = -1
		self.encryption = -1
		#!Options
		self.dump = 0
		self.pass_ = 0


def getWords(line, sep):
	result = []
	for word in line.split(sep):
		#delete this eol symbols for the justice
		if word.find("\n") != -1:
			word = word[:word.find("\n")]
		#delete empty words that appears between multiple spaces
		if word != "":
			result.append(word)
	return result


def getDisks(f):
	disks = []
	disk = disk_class()
	for line in f:
		disk.init()
		wordsList = getWords(line, " ")
		if wordsList[0]!="#":
			if wordsList[0].find("UUID=") != -1:
				disk.uuid = wordsList[0][5:]
			else:
				disk.path = wordsList[0]
			disk.mountPoint = wordsList[1]
			disk.fstype = wordsList[2]
			#Get options
			optionsList = getWords(wordsList[3], ",")
			for option in optionsList:
				if option == "defaults":
					disk.defaults = 1
				if option == "dirsync":
					disk.dirsync = 1
				if option == "group":
					disk.group = 1
				if option == "encryption":
					disk.encryption = 1
				if option == "dirsync":
					disk.dirsync = 1
				if option == "sync":
					disk.sync = 1
				if option == "async":
					disk.sync = 0
				if option == "atime":
					disk.atime = 1
				if option == "noatime":
					disk.atime = 0
				if option == "relatime":
					disk.relatime = 1
				if option == "norelatime":
					disk.relatime = 0
				if option == "strictatime":
					disk.strictatime = 1
				if option == "nostrictatime":
					disk.strictatime = 0
				if option == "diratime":
					disk.diratime = 1
				if option == "nodiratime":
					disk.diratime = 0
				if option == "exe":
					disk.exe = 1
				if option == "noexe":
					disk.exe = 0
				if option == "dev":
					disk.dev = 1
				if option == "nodev":
					disk.dev = 0
				if option == "auto":
					disk.auto = 1
				if option == "noauto":
					disk.auto = 0
				if option == "mand":
					disk.mand = 1
				if option == "nomand":
					disk.mand = 0
				if option == "suid":
					disk.suid = 1
				if option == "nosuid":
					disk.suid = 0
				if option == "rw":
					disk.write = 1
				if option == "ro":
					disk.write = 0
				if option == "user":
					disk.auto = 1
				if option == "nouser":
					disk.auto = 0
			disk.dump = int(wordsList[4])
			disk.pass_ = int(wordsList[5])
			disks.append(copy(disk))
	return disks

class MainWindow(QtGui.QMainWindow):
	def setUI(self):
		self.setObjectName(_fromUtf8("MainWindow"))
		self.resize(751, 411)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
		sizePolicy.setHorizontalStretch(1)
		sizePolicy.setVerticalStretch(1)
		sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
		self.setSizePolicy(sizePolicy)
		self.setMinimumSize(QtCore.QSize(751, 411))
		self.centralWidget = QtGui.QWidget(self)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(1)
		sizePolicy.setVerticalStretch(1)
		sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
		self.centralWidget.setSizePolicy(sizePolicy)
		self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
		self.gridLayout = QtGui.QGridLayout(self.centralWidget)
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
		self.verticalLayout_2 = QtGui.QVBoxLayout()
		self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
		self.horizontalLayout = QtGui.QHBoxLayout()
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.tableWidget = QtGui.QTableWidget(self.centralWidget)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
		self.tableWidget.setSizePolicy(sizePolicy)
		self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
		self.tableWidget.setBaseSize(QtCore.QSize(625, 0))
		self.tableWidget.setRowCount(1)
		self.tableWidget.setColumnCount(6)
		self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(0, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(0, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(1, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(2, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(3, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(4, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(5, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setItem(0, 0, item)
		self.tableWidget.horizontalHeader().setVisible(True)
		self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
		self.tableWidget.verticalHeader().setVisible(False)
		self.horizontalLayout.addWidget(self.tableWidget)
		self.verticalLayout = QtGui.QVBoxLayout()
		self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.pushButton_2 = QtGui.QPushButton(self.centralWidget)
		self.pushButton_2.setMaximumSize(QtCore.QSize(85, 27))
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
		self.verticalLayout.addWidget(self.pushButton_2)
		self.pushButton = QtGui.QPushButton(self.centralWidget)
		self.pushButton.setMaximumSize(QtCore.QSize(85, 27))
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.verticalLayout.addWidget(self.pushButton)
		self.pushButton_3 = QtGui.QPushButton(self.centralWidget)
		self.pushButton_3.setMaximumSize(QtCore.QSize(85, 27))
		self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
		self.verticalLayout.addWidget(self.pushButton_3)
		spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		self.verticalLayout.addItem(spacerItem)
		self.horizontalLayout.addLayout(self.verticalLayout)
		self.verticalLayout_2.addLayout(self.horizontalLayout)
		self.label = QtGui.QLabel(self.centralWidget)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
		self.label.setSizePolicy(sizePolicy)
		self.label.setMinimumSize(QtCore.QSize(0, 16))
		self.label.setMaximumSize(QtCore.QSize(16777215, 16))
		self.label.setObjectName(_fromUtf8("label"))
		self.verticalLayout_2.addWidget(self.label)
		self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
		self.setCentralWidget(self.centralWidget)
		self.menuBar = QtGui.QMenuBar(self)
		self.menuBar.setGeometry(QtCore.QRect(0, 0, 751, 25))
		self.menuBar.setObjectName(_fromUtf8("menuBar"))
		self.menuFile = QtGui.QMenu(self.menuBar)
		self.menuFile.setObjectName(_fromUtf8("menuFile"))
		self.menuEdit = QtGui.QMenu(self.menuBar)
		self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
		self.menuAbout = QtGui.QMenu(self.menuBar)
		self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
		self.setMenuBar(self.menuBar)
		self.mainToolBar = QtGui.QToolBar(self)
		self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
		self.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
		self.insertToolBarBreak(self.mainToolBar)
		self.statusBar = QtGui.QStatusBar(self)
		self.statusBar.setObjectName(_fromUtf8("statusBar"))
		self.setStatusBar(self.statusBar)
		self.actionExit = QtGui.QAction(self)
		self.actionExit.setObjectName(_fromUtf8("actionExit"))
		self.actionRefresh = QtGui.QAction(self)
		self.actionRefresh.setObjectName(_fromUtf8("actionRefresh"))
		self.actionSave = QtGui.QAction(self)
		self.actionSave.setObjectName(_fromUtf8("actionSave"))
		self.actionConfigure = QtGui.QAction(self)
		self.actionConfigure.setObjectName(_fromUtf8("actionConfigure"))
		self.actionAbout = QtGui.QAction(self)
		self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
		self.menuFile.addAction(self.actionSave)
		self.menuFile.addAction(self.actionRefresh)
		self.menuFile.addSeparator()
		self.menuFile.addAction(self.actionExit)
		self.menuEdit.addAction(self.actionConfigure)
		self.menuAbout.addAction(self.actionAbout)
		self.menuBar.addAction(self.menuFile.menuAction())
		self.menuBar.addAction(self.menuEdit.menuAction())
		self.menuBar.addAction(self.menuAbout.menuAction())

		self.retranslateUi()
		QtCore.QMetaObject.connectSlotsByName(self)


		self.retranslateUi()
		QtCore.QMetaObject.connectSlotsByName(self)

	def retranslateUi(self):
		self.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PyFStab", None, QtGui.QApplication.UnicodeUTF8))
		item = self.tableWidget.verticalHeaderItem(0)
		item.setText(QtGui.QApplication.translate("MainWindow", "Новая строка", None, QtGui.QApplication.UnicodeUTF8))
		item = self.tableWidget.horizontalHeaderItem(0)
		item.setText(QtGui.QApplication.translate("MainWindow", "Device", None, QtGui.QApplication.UnicodeUTF8))
		item = self.tableWidget.horizontalHeaderItem(1)
		item.setText(QtGui.QApplication.translate("MainWindow", "Mount Point", None, QtGui.QApplication.UnicodeUTF8))
		item = self.tableWidget.horizontalHeaderItem(2)
		item.setText(QtGui.QApplication.translate("MainWindow", "File System", None, QtGui.QApplication.UnicodeUTF8))
		item = self.tableWidget.horizontalHeaderItem(3)
		item.setText(QtGui.QApplication.translate("MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
		item = self.tableWidget.horizontalHeaderItem(4)
		item.setText(QtGui.QApplication.translate("MainWindow", "Dump", None, QtGui.QApplication.UnicodeUTF8))
		item = self.tableWidget.horizontalHeaderItem(5)
		item.setText(QtGui.QApplication.translate("MainWindow", "Pass", None, QtGui.QApplication.UnicodeUTF8))
		__sortingEnabled = self.tableWidget.isSortingEnabled()
		self.tableWidget.setSortingEnabled(False)
		self.tableWidget.setSortingEnabled(__sortingEnabled)
		self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
		self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
		self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
		self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
		self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
		self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
		self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
		self.actionRefresh.setText(QtGui.QApplication.translate("MainWindow", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
		self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
		self.actionConfigure.setText(QtGui.QApplication.translate("MainWindow", "Configure...", None, QtGui.QApplication.UnicodeUTF8))
		self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

#class MainWindow(QtGui.QMainWindow):
#	def __init__(self):
#		QtGui.QMainWindow.__init__(self)
#
#		self.resize(250, 150)
#		self.setWindowTitle('pyFStab')
#		exit = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Exit', self)
#		exit.setShortcut('Ctrl+Q')
#		exit.setStatusTip('Exit application')
#		self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
#
#		menubar = self.menuBar()
#		file = menubar.addMenu('&File')
#		file.addAction(exit)
#		table = QtGui.QPushButton('Close', self)

        #self.statusBar().showMessage('Ready')

disks = []
fileSystems = ("ext4","ext3","ext2","swap","ntfs","ntfs-3g","vfat","jfs",
"xfs","reiserfs","btrfs","iso9660","udf","auto")
path = "/home/keder/test/fstab"
f = open(path, "r+")
#ui = open("/home/keder/Projects/pyFStab.ui")
#pyui = open("/home/keder/Projects/ui.py","w")
disks = getDisks(f)
app = QtGui.QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.setWindowTitle("PyFStab")
mainWindow.setUI()
mainWindow.show()
sys.exit(app.exec_())
#uic.compileUi(ui,pyui)
#

#main.show()
#

#==============================================================================
# for i in range(len(disks)):
# 	print str(i) + ": " + disks[i].uuid + " " + disks[i].path + " " + disks[i].mountPoint + " " + str(disks[i].defaults)
#==============================================================================


