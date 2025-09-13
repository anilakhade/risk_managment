# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'table.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFrame, QHBoxLayout, QHeaderView, QMainWindow,
    QPushButton, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1201, 661)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.filter_frame = QFrame(self.centralwidget)
        self.filter_frame.setObjectName(u"filter_frame")
        self.filter_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.filter_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.filter_frame)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.broker = QComboBox(self.filter_frame)
        self.broker.setObjectName(u"broker")
        self.broker.setEditable(False)

        self.horizontalLayout.addWidget(self.broker)

        self.sheet = QComboBox(self.filter_frame)
        self.sheet.setObjectName(u"sheet")

        self.horizontalLayout.addWidget(self.sheet)

        self.strategy = QComboBox(self.filter_frame)
        self.strategy.setObjectName(u"strategy")

        self.horizontalLayout.addWidget(self.strategy)

        self.exchange = QComboBox(self.filter_frame)
        self.exchange.setObjectName(u"exchange")

        self.horizontalLayout.addWidget(self.exchange)

        self.instrument = QComboBox(self.filter_frame)
        self.instrument.setObjectName(u"instrument")

        self.horizontalLayout.addWidget(self.instrument)

        self.symbol = QComboBox(self.filter_frame)
        self.symbol.setObjectName(u"symbol")

        self.horizontalLayout.addWidget(self.symbol)

        self.expiry = QComboBox(self.filter_frame)
        self.expiry.setObjectName(u"expiry")

        self.horizontalLayout.addWidget(self.expiry)

        self.strike = QComboBox(self.filter_frame)
        self.strike.setObjectName(u"strike")

        self.horizontalLayout.addWidget(self.strike)

        self.opt_type = QComboBox(self.filter_frame)
        self.opt_type.setObjectName(u"opt_type")

        self.horizontalLayout.addWidget(self.opt_type)

        self.quantity = QComboBox(self.filter_frame)
        self.quantity.setObjectName(u"quantity")

        self.horizontalLayout.addWidget(self.quantity)

        self.openCardBtn = QPushButton(self.filter_frame)
        self.openCardBtn.setObjectName(u"openCardBtn")

        self.horizontalLayout.addWidget(self.openCardBtn)


        self.verticalLayout_2.addWidget(self.filter_frame)

        self.table_frame = QFrame(self.centralwidget)
        self.table_frame.setObjectName(u"table_frame")
        self.table_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.table_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.table_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tableView = QTableView(self.table_frame)
        self.tableView.setObjectName(u"tableView")
        font = QFont()
        font.setFamilies([u"RobotoMono Nerd Font [GOOG]"])
        font.setPointSize(12)
        font.setBold(True)
        self.tableView.setFont(font)
        self.tableView.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableView.setSortingEnabled(True)
        self.tableView.setWordWrap(False)
        self.tableView.verticalHeader().setProperty(u"showSortIndicator", True)

        self.verticalLayout.addWidget(self.tableView)


        self.verticalLayout_2.addWidget(self.table_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.broker.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BROKER_ID", None))
        self.sheet.setPlaceholderText(QCoreApplication.translate("MainWindow", u"SHEET", None))
        self.strategy.setPlaceholderText(QCoreApplication.translate("MainWindow", u"STRATEGY", None))
        self.exchange.setPlaceholderText(QCoreApplication.translate("MainWindow", u"EXCHANGE", None))
        self.instrument.setPlaceholderText(QCoreApplication.translate("MainWindow", u"INSTRUMENT", None))
        self.symbol.setPlaceholderText(QCoreApplication.translate("MainWindow", u"SYMBOL", None))
        self.expiry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"EXPIRY", None))
        self.strike.setPlaceholderText(QCoreApplication.translate("MainWindow", u"STRIKE", None))
        self.opt_type.setPlaceholderText(QCoreApplication.translate("MainWindow", u"OPT_TYPE", None))
        self.quantity.setPlaceholderText(QCoreApplication.translate("MainWindow", u"QUANTITY", None))
        self.openCardBtn.setText(QCoreApplication.translate("MainWindow", u"CARD", None))
    # retranslateUi

