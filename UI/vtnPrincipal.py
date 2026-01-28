# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtnPrincipal.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_vtnPrincipal(object):
    def setupUi(self, vtnPrincipal):
        if not vtnPrincipal.objectName():
            vtnPrincipal.setObjectName(u"vtnPrincipal")
        vtnPrincipal.resize(800, 600)
        self.centralwidget = QWidget(vtnPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.LBNombre = QLabel(self.centralwidget)
        self.LBNombre.setObjectName(u"LBNombre")
        self.LBNombre.setGeometry(QRect(100, 30, 51, 31))
        self.LBApellido = QLabel(self.centralwidget)
        self.LBApellido.setObjectName(u"LBApellido")
        self.LBApellido.setGeometry(QRect(90, 70, 61, 31))
        self.LBCedula = QLabel(self.centralwidget)
        self.LBCedula.setObjectName(u"LBCedula")
        self.LBCedula.setGeometry(QRect(90, 110, 51, 31))
        self.LBEmail = QLabel(self.centralwidget)
        self.LBEmail.setObjectName(u"LBEmail")
        self.LBEmail.setGeometry(QRect(100, 200, 51, 31))
        self.LBSexo = QLabel(self.centralwidget)
        self.LBSexo.setObjectName(u"LBSexo")
        self.LBSexo.setGeometry(QRect(100, 150, 47, 31))
        self.txtNombre = QLineEdit(self.centralwidget)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setGeometry(QRect(160, 39, 141, 21))
        self.txtNombre.setMaxLength(20)
        self.txtApellido = QLineEdit(self.centralwidget)
        self.txtApellido.setObjectName(u"txtApellido")
        self.txtApellido.setGeometry(QRect(160, 80, 141, 21))
        self.txtApellido.setMaxLength(20)
        self.txtCedula = QLineEdit(self.centralwidget)
        self.txtCedula.setObjectName(u"txtCedula")
        self.txtCedula.setGeometry(QRect(160, 119, 141, 21))
        self.txtCedula.setMaxLength(10)
        self.txtEmail = QLineEdit(self.centralwidget)
        self.txtEmail.setObjectName(u"txtEmail")
        self.txtEmail.setGeometry(QRect(160, 199, 141, 21))
        self.txtEmail.setMaxLength(20)
        self.cbSexo = QComboBox(self.centralwidget)
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.cbSexo.setObjectName(u"cbSexo")
        self.cbSexo.setGeometry(QRect(160, 160, 141, 22))
        self.btGuardar = QPushButton(self.centralwidget)
        self.btGuardar.setObjectName(u"btGuardar")
        self.btGuardar.setGeometry(QRect(100, 260, 141, 31))
        self.btLimpiar = QPushButton(self.centralwidget)
        self.btLimpiar.setObjectName(u"btLimpiar")
        self.btLimpiar.setGeometry(QRect(260, 260, 141, 31))
        vtnPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(vtnPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        vtnPrincipal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(vtnPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        vtnPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(vtnPrincipal)

        QMetaObject.connectSlotsByName(vtnPrincipal)
    # setupUi

    def retranslateUi(self, vtnPrincipal):
        vtnPrincipal.setWindowTitle(QCoreApplication.translate("vtnPrincipal", u"MainWindow", None))
        self.LBNombre.setText(QCoreApplication.translate("vtnPrincipal", u"NOMBRE:", None))
        self.LBApellido.setText(QCoreApplication.translate("vtnPrincipal", u"APELLIDO:", None))
        self.LBCedula.setText(QCoreApplication.translate("vtnPrincipal", u"CEDULA:", None))
        self.LBEmail.setText(QCoreApplication.translate("vtnPrincipal", u"EMAIL:", None))
        self.LBSexo.setText(QCoreApplication.translate("vtnPrincipal", u"SEXO:", None))
        self.cbSexo.setItemText(0, QCoreApplication.translate("vtnPrincipal", u"Seleccionar", None))
        self.cbSexo.setItemText(1, QCoreApplication.translate("vtnPrincipal", u"Masculino", None))
        self.cbSexo.setItemText(2, QCoreApplication.translate("vtnPrincipal", u"Femenino", None))
        self.cbSexo.setItemText(3, QCoreApplication.translate("vtnPrincipal", u"Prefiero no decir ", None))

        self.btGuardar.setText(QCoreApplication.translate("vtnPrincipal", u"GUARDAR ", None))
        self.btLimpiar.setText(QCoreApplication.translate("vtnPrincipal", u"LIMPIAR", None))
    # retranslateUi

