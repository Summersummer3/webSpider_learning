# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(337, 192)
        self.listView = QtGui.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(0, 0, 271, 192))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.verticalScrollBar = QtGui.QScrollBar(Form)
        self.verticalScrollBar.setGeometry(QtCore.QRect(260, 0, 16, 191))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName(_fromUtf8("verticalScrollBar"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(280, 10, 51, 32))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 72, 20, 20))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 40, 51, 32))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalScrollBar.raise_()
        self.listView.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "PushButton", None))
        self.pushButton_2.setText(_translate("Form", "PushButton", None))
        self.pushButton_3.setText(_translate("Form", "PushButton", None))

