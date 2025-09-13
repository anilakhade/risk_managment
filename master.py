# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'master.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.strategy_btn = QPushButton(self.frame)
        self.strategy_btn.setObjectName(u"strategy_btn")

        self.horizontalLayout.addWidget(self.strategy_btn)

        self.net_btn = QPushButton(self.frame)
        self.net_btn.setObjectName(u"net_btn")

        self.horizontalLayout.addWidget(self.net_btn)

        self.horizontalSpacer = QSpacerItem(592, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, -1)
        self.watch_frame = QFrame(self.frame_2)
        self.watch_frame.setObjectName(u"watch_frame")
        self.watch_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.watch_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.watch_frame)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 0)
        self.watch_table = QTableView(self.watch_frame)
        self.watch_table.setObjectName(u"watch_table")

        self.verticalLayout_2.addWidget(self.watch_table)


        self.horizontalLayout_2.addWidget(self.watch_frame)

        self.folio_frame = QFrame(self.frame_2)
        self.folio_frame.setObjectName(u"folio_frame")
        self.folio_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.folio_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.folio_frame)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, -1)
        self.folio_table = QTableView(self.folio_frame)
        self.folio_table.setObjectName(u"folio_table")

        self.verticalLayout.addWidget(self.folio_table)


        self.horizontalLayout_2.addWidget(self.folio_frame)


        self.verticalLayout_3.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.strategy_btn.setText(QCoreApplication.translate("MainWindow", u"Strategy", None))
        self.net_btn.setText(QCoreApplication.translate("MainWindow", u"Net Position", None))
    # retranslateUi

