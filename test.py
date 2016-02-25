# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Tue Feb  9 22:01:24 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Widget(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(750, 394)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 30, 701, 291))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.layoutWidget_3 = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget_3.setGeometry(QtCore.QRect(190, 20, 471, 211))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget_3)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.label_13 = QtGui.QLabel(self.layoutWidget_3)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_3.addWidget(self.label_13)
        self.label_15 = QtGui.QLabel(self.layoutWidget_3)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout_3.addWidget(self.label_15)
        self.label_7 = QtGui.QLabel(self.layoutWidget_3)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_3.addWidget(self.label_7)
        self.label_8 = QtGui.QLabel(self.layoutWidget_3)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_3.addWidget(self.label_8)
        self.label_9 = QtGui.QLabel(self.layoutWidget_3)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_3.addWidget(self.label_9)
        self.label_10 = QtGui.QLabel(self.layoutWidget_3)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_3.addWidget(self.label_10)
        self.label_11 = QtGui.QLabel(self.layoutWidget_3)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_3.addWidget(self.label_11)
        self.layoutWidget_2 = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 20, 141, 211))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.layoutWidget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.label_12 = QtGui.QLabel(self.layoutWidget_2)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_2.addWidget(self.label_12)
        self.label_14 = QtGui.QLabel(self.layoutWidget_2)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_2.addWidget(self.label_14)
        self.label_2 = QtGui.QLabel(self.layoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.layoutWidget_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_5 = QtGui.QLabel(self.layoutWidget_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.layoutWidget_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_4 = QtGui.QLabel(self.layoutWidget_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.layoutWidget = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 240, 451, 41))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.startButton = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setBaseSize(QtCore.QSize(0, 0))
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startButton.setIconSize(QtCore.QSize(16, 16))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.horizontalLayout.addWidget(self.startButton)
        self.pauseButton = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pauseButton.sizePolicy().hasHeightForWidth())
        self.pauseButton.setSizePolicy(sizePolicy)
        self.pauseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pauseButton.setObjectName(_fromUtf8("pauseButton"))
        self.horizontalLayout.addWidget(self.pauseButton)
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_13.setText(_translate("Form", "0 %", None))
        self.label_15.setText(_translate("Form", "0 MB", None))
        self.label_7.setText(_translate("Form", "New File 1", None))
        self.label_8.setText(_translate("Form", "0", None))
        self.label_9.setText(_translate("Form", "0", None))
        self.label_10.setText(_translate("Form", "--", None))
        self.label_11.setText(_translate("Form", "home/downloads", None))
        self.label.setText(_translate("Form", "Download Link", None))
        self.label_12.setText(_translate("Form", "Progress", None))
        self.label_14.setText(_translate("Form", "File Size", None))
        self.label_2.setText(_translate("Form", "File Name", None))
        self.label_3.setText(_translate("Form", "Download Speed", None))
        self.label_5.setText(_translate("Form", "Time Elapsed", None))
        self.label_6.setText(_translate("Form", "Time Remaining", None))
        self.label_4.setText(_translate("Form", "Storage Location", None))
        self.startButton.setText(_translate("Form", "Start", None))
        self.pauseButton.setText(_translate("Form", "Pause/Resume", None))
        self.pushButton_2.setText(_translate("Form", "Cancel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

