import urllib2
import urllib
from PyQt4 import QtGui,QtCore
from download_manager import Ui_MainWindow

urllib2.install_opener(
    urllib2.build_opener(
        urllib2.ProxyHandler({'http': '10.3.100.207:8080'})
    )
)


class download_manager(QtGui.QDialog):
	def __init__(self):
		self.dialog=Ui_MainWindow()
		self.dialog.setupUi(self)
		self.dialog.pushButton_3.clicked.connect(self.addDownload)
	print "Clickme"
	def addDownload(self):
		print "Click"
		global urlname
		global urlsize
		global urlstatus
		global urltype
		global model
		global idx
		self.url=str(self.dialog.lineEdit.text())
		print self.url
		self.u=urllib.urlretrieve(self.url,"python.png")
class Main(QtGui.QMainWindow):
	def __init__(self):
		super(Main,self).__init__()
		self.newd=download_manager()
		newd.show()
		print "Work"

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

