# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'card.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

class Ui_card(object):
    def setupUi(self, card):
        if not card.objectName():
            card.setObjectName(u"card")
        card.resize(559, 423)
        self.verticalLayout = QVBoxLayout(card)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(card)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.put_sold = QLabel(self.frame)
        self.put_sold.setObjectName(u"put_sold")

        self.gridLayout.addWidget(self.put_sold, 1, 5, 1, 1)

        self.booked_label = QLabel(self.frame)
        self.booked_label.setObjectName(u"booked_label")

        self.gridLayout.addWidget(self.booked_label, 1, 1, 1, 1)

        self.call_sold = QLabel(self.frame)
        self.call_sold.setObjectName(u"call_sold")

        self.gridLayout.addWidget(self.call_sold, 1, 3, 1, 1)

        self.call_buy = QLabel(self.frame)
        self.call_buy.setObjectName(u"call_buy")

        self.gridLayout.addWidget(self.call_buy, 1, 4, 1, 1)

        self.net_lable = QLabel(self.frame)
        self.net_lable.setObjectName(u"net_lable")

        self.gridLayout.addWidget(self.net_lable, 1, 2, 1, 1)

        self.broker_label = QLabel(self.frame)
        self.broker_label.setObjectName(u"broker_label")

        self.gridLayout.addWidget(self.broker_label, 0, 0, 1, 1)

        self.symbol_label = QLabel(self.frame)
        self.symbol_label.setObjectName(u"symbol_label")

        self.gridLayout.addWidget(self.symbol_label, 0, 2, 1, 1)

        self.value_label = QLabel(self.frame)
        self.value_label.setObjectName(u"value_label")

        self.gridLayout.addWidget(self.value_label, 1, 0, 1, 1)

        self.strategy_label = QLabel(self.frame)
        self.strategy_label.setObjectName(u"strategy_label")

        self.gridLayout.addWidget(self.strategy_label, 0, 1, 1, 1)

        self.margin_label = QLabel(self.frame)
        self.margin_label.setObjectName(u"margin_label")

        self.gridLayout.addWidget(self.margin_label, 0, 4, 1, 1)

        self.interst_label = QLabel(self.frame)
        self.interst_label.setObjectName(u"interst_label")

        self.gridLayout.addWidget(self.interst_label, 0, 5, 1, 1)

        self.put_buy = QLabel(self.frame)
        self.put_buy.setObjectName(u"put_buy")

        self.gridLayout.addWidget(self.put_buy, 2, 0, 1, 1)

        self.exposure = QLabel(self.frame)
        self.exposure.setObjectName(u"exposure")

        self.gridLayout.addWidget(self.exposure, 2, 1, 1, 1)

        self.show_button = QPushButton(self.frame)
        self.show_button.setObjectName(u"show_button")

        self.gridLayout.addWidget(self.show_button, 2, 5, 1, 1)

        self.expiry_label = QLabel(self.frame)
        self.expiry_label.setObjectName(u"expiry_label")

        self.gridLayout.addWidget(self.expiry_label, 0, 3, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.tableView = QTableView(card)
        self.tableView.setObjectName(u"tableView")
        font = QFont()
        font.setFamilies([u"RobotoMono Nerd Font [GOOG]"])
        font.setPointSize(12)
        font.setBold(True)
        self.tableView.setFont(font)
        self.tableView.setAutoFillBackground(True)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableView.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.tableView.setShowGrid(True)
        self.tableView.setSortingEnabled(True)
        self.tableView.setWordWrap(False)

        self.verticalLayout.addWidget(self.tableView)


        self.retranslateUi(card)
        self.show_button.clicked.connect(self.tableView.show)

        QMetaObject.connectSlotsByName(card)
    # setupUi

    def retranslateUi(self, card):
        card.setWindowTitle(QCoreApplication.translate("card", u"Form", None))
        self.put_sold.setText("")
        self.booked_label.setText("")
        self.call_sold.setText("")
        self.call_buy.setText("")
        self.net_lable.setText("")
        self.broker_label.setText("")
        self.symbol_label.setText("")
        self.value_label.setText("")
        self.strategy_label.setText("")
        self.margin_label.setText("")
        self.interst_label.setText("")
        self.put_buy.setText("")
        self.exposure.setText("")
        self.show_button.setText(QCoreApplication.translate("card", u"show more", None))
        self.expiry_label.setText("")
    # retranslateUi

