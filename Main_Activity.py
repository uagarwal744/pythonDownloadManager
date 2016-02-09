import urllib2
import urllib
import timeit
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
		self.dialog.pushButton_3.clicked.connect(self.addDownload)
		self.dialog.pushButton_16.clicked.connect(self.addDownload2)

	def addDownload(self):
		start=timeit.default_timer()
		global urlname
		global urlsize
		global urlstatus
		global urltype
		global model
		global idx
		url=str(self.dialog.lineEdit.text())
		urlname = url.split('/')[-1]
		response=urllib2.urlopen(url)
		self.meta=response.info()
		urlsize=int(self.meta.getheaders('Content-Length')[0])
		if 1000<urlsize<1000000:
			urlsize=str(urlsize/1000.0) + " KB"
		elif 1000000<urlsize<10**9:
			urlsize=str(1.0*urlsize/10**6) + " MB"
		else:
			urlsize=str(1.0*urlsize/10**9) + " GB"
		self.dialog.label_15.setText(urlsize)
		self.dialog.label_7.setText(urlname)
		f=open(urlname,'wb')
		f.write(response.read())
		stop=timeit.default_timer()
		speed=float(urlsize.split(' ')[0])/(stop-start)
		speed=str(speed) + " " + urlsize.split(' ')[-1] + "/s"
		self.dialog.label_13.setText("100 %")
		self.dialog.label_8.setText(speed)
		self.dialog.label_9.setText(str(stop-start) + " s")

	def addDownload2(self):
		start=timeit.default_timer()
		global urlname
		global urlsize
		global urlstatus
		global urltype
		global model
		global idx
		url=str(self.dialog.lineEdit_6.text())
		urlname = url.split('/')[-1]
		response=urllib2.urlopen(url)
		self.meta=response.info()
		urlsize=int(self.meta.getheaders('Content-Length')[0])
		if 1000<urlsize<1000000:
			urlsize=str(urlsize/1000.0) + " KB"
		elif 1000000<urlsize<10**9:
			urlsize=str(1.0*urlsize/10**6) + " MB"
		else:
			urlsize=str(1.0*urlsize/10**9) + " GB"
		self.dialog.label_17.setText(urlsize)
		self.dialog.label_68.setText(urlname)
		f=open(urlname,'wb')
		f.write(response.read())
		stop=timeit.default_timer()
		speed=float(urlsize.split(' ')[0])/(stop-start)
		speed=str(speed) + " " + urlsize.split(' ')[-1] + "/s"
		self.dialog.label_67.setText("100 %")
		self.dialog.label_69.setText(speed)
		self.dialog.label_70.setText(str(stop-start))

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
