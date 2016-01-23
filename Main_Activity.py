import urllib2
import urllib
from PyQt4 import QtGui,QtCore
from download_manager import Ui_MainWindow

proxy = urllib2.ProxyHandler({'http': '10.3.100.207:8080'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

class download_manager(QtGui.QMainWindow):
	def __init__(self):
		super(download_manager,self).__init__()
		self.dialog=Ui_MainWindow()
		self.dialog.setupUi(self)
		print self.dialog.pushButton_3
		self.dialog.pushButton_3.clicked.connect(self.addDownload)

	def addDownload(self):
		global urlname
		global urlsize
		global urlstatus
		global urltype
		global model
		global idx
		url=str(self.dialog.lineEdit.text())
		print url
		file_name = url.split('/')[-1]
		response=urllib2.urlopen(url)
		f=open(file_name,'wb')
		f.write(response.read())

class Main(QtGui.QMainWindow):
	def __init__(self):
		super(Main,self).__init__()
		self.newd=download_manager()
		self.newd.show()

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	MainWindow = Main()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	sys.exit(app.exec_())
