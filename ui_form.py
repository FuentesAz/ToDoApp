# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(791, 508)
        Main.setMaximumSize(QSize(940, 600))
        self.WCentral = QWidget(Main)
        self.WCentral.setObjectName(u"WCentral")
        self.gridLayout_2 = QGridLayout(self.WCentral)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Nav = QGridLayout()
        self.Nav.setObjectName(u"Nav")
        self.NavDelete = QPushButton(self.WCentral)
        self.NavDelete.setObjectName(u"NavDelete")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.NavDelete.setIcon(icon)

        self.Nav.addWidget(self.NavDelete, 0, 1, 1, 1)

        self.NavEdit = QPushButton(self.WCentral)
        self.NavEdit.setObjectName(u"NavEdit")
        self.NavEdit.setStyleSheet(u"QPushButton:disabled {\n"
"                background-color: white;  /* Color de fondo cuando est\u00e1 deshabilitado */\n"
"                color: black;\n"
"}\n"
"")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MailMessageNew))
        self.NavEdit.setIcon(icon1)
        self.NavEdit.setIconSize(QSize(16, 16))

        self.Nav.addWidget(self.NavEdit, 0, 0, 1, 1)

        self.NavSave = QPushButton(self.WCentral)
        self.NavSave.setObjectName(u"NavSave")
        self.NavSave.setStyleSheet(u"QPushButton::disabled {\n"
"                background-color: white;  /* Color de fondo cuando est\u00e1 deshabilitado */\n"
"                color: black;\n"
"            }\n"
"")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.NavSave.setIcon(icon2)

        self.Nav.addWidget(self.NavSave, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.Nav, 1, 0, 1, 1)

        self.widget = QWidget(self.WCentral)
        self.widget.setObjectName(u"widget")

        self.gridLayout_2.addWidget(self.widget, 4, 0, 1, 1)

        self.WForm = QGridLayout()
        self.WForm.setObjectName(u"WForm")
        self.Form = QGridLayout()
        self.Form.setObjectName(u"Form")
        self.FAdd = QPushButton(self.WCentral)
        self.FAdd.setObjectName(u"FAdd")
        self.FAdd.setMinimumSize(QSize(0, 35))
        self.FAdd.setMaximumSize(QSize(1200, 500))
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.FAdd.setIcon(icon3)
        self.FAdd.setIconSize(QSize(16, 16))
        self.FAdd.setCheckable(False)

        self.Form.addWidget(self.FAdd, 7, 1, 1, 1)

        self.FNLable = QLineEdit(self.WCentral)
        self.FNLable.setObjectName(u"FNLable")
        self.FNLable.setMinimumSize(QSize(0, 30))

        self.Form.addWidget(self.FNLable, 1, 1, 1, 1)

        self.FName = QLabel(self.WCentral)
        self.FName.setObjectName(u"FName")

        self.Form.addWidget(self.FName, 0, 1, 1, 1)

        self.FDText = QPlainTextEdit(self.WCentral)
        self.FDText.setObjectName(u"FDText")

        self.Form.addWidget(self.FDText, 6, 1, 1, 1)

        self.FDesc = QLabel(self.WCentral)
        self.FDesc.setObjectName(u"FDesc")

        self.Form.addWidget(self.FDesc, 5, 1, 1, 1)

        self.FPriority = QLabel(self.WCentral)
        self.FPriority.setObjectName(u"FPriority")

        self.Form.addWidget(self.FPriority, 2, 1, 1, 1)

        self.FOptions = QComboBox(self.WCentral)
        self.FOptions.addItem("")
        self.FOptions.addItem("")
        self.FOptions.addItem("")
        self.FOptions.addItem("")
        self.FOptions.setObjectName(u"FOptions")
        self.FOptions.setMinimumSize(QSize(0, 35))
        self.FOptions.setStyleSheet(u"QComboBox::item {\n"
"                height: 300px;\n"
"}")
        self.FOptions.setEditable(False)
        self.FOptions.setIconSize(QSize(50, 50))

        self.Form.addWidget(self.FOptions, 4, 1, 1, 1)


        self.WForm.addLayout(self.Form, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(10, 10, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.WForm.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.WForm, 2, 1, 1, 1)

        self.Table = QTableWidget(self.WCentral)
        if (self.Table.columnCount() < 3):
            self.Table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.Table.setObjectName(u"Table")
        self.Table.setRowCount(0)
        self.Table.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_2.addWidget(self.Table, 2, 0, 1, 1)

        Main.setCentralWidget(self.WCentral)
        self.menubar = QMenuBar(Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 791, 21))
        Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Main)
        self.statusbar.setObjectName(u"statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Main", None))
        self.NavDelete.setText(QCoreApplication.translate("Main", u"Eliminar", None))
        self.NavEdit.setText(QCoreApplication.translate("Main", u"Editar", None))
        self.NavSave.setText(QCoreApplication.translate("Main", u"Guardar", None))
        self.FAdd.setText(QCoreApplication.translate("Main", u"Agregar", None))
        self.FName.setText(QCoreApplication.translate("Main", u"Nombre:", None))
        self.FDText.setPlaceholderText("")
        self.FDesc.setText(QCoreApplication.translate("Main", u"Descripci\u00f3n:", None))
        self.FPriority.setText(QCoreApplication.translate("Main", u"Prioridad:", None))
        self.FOptions.setItemText(0, QCoreApplication.translate("Main", u"Baja", None))
        self.FOptions.setItemText(1, QCoreApplication.translate("Main", u"Moderada", None))
        self.FOptions.setItemText(2, QCoreApplication.translate("Main", u"Alta", None))
        self.FOptions.setItemText(3, QCoreApplication.translate("Main", u"Urgente", None))

        ___qtablewidgetitem = self.Table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Main", u"Tareas", None));
        ___qtablewidgetitem1 = self.Table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Main", u"Prioridad", None));
        ___qtablewidgetitem2 = self.Table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Main", u"Descripci\u00f3n", None));
    # retranslateUi

