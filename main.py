import sys
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtCore import QSortFilterProxyModel, Qt
from table_ui import Ui_MainWindow

#============================================================================#

class PandasModel(QAbstractTableModel):
    def __init__(self, df):
        super().__init__()
        self.df = df 

    def rowCount(self, parent=None):
        return self.df.shape[0]

    def columnCount(self, parent=None):
        return self.df.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.DisplayRole:
            value = self.df.iat[index.row(), index.column()]
            return "" if pd.isna(value) else str(value)
        return None


    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return str(self.df.columns[section])
        else:
            return str(section)

#============================================================================#

class MultiColFilterProxy(QSortFilterProxyModel):
    def __init__(self):
        super().__init__()
        self.filters = {}

    def setFilterForColumn(self, col, text):
        if text:
            self.filters[col] = text.lower()
        else:
            self.filters.pop(col, None)
        self.invalidateFilter()

    def filterAcceptsRow(self, source_row, source_parent):
        model = self.sourceModel()
        for col, needle in self.filters.items():
            idx = model.index(source_row, col, source_parent)
            val = model.data(idx, Qt.DisplayRole)
            hay = "" if val is None else str(val).lower()
            if not hay.startswith(needle):
                return False
        return True

#============================================================================#

class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        df = pd.read_excel("OLD_DF.xlsx")
        df["VALUE"] = (df["QUANTITY"] * df["RATE"] * -1).astype(int)

        key = ["BROKER_ID", "SHEET", "STRATEGY"]
        model = PandasModel(df)

        self.proxy = MultiColFilterProxy()
        self.proxy.setSourceModel(model)

        self.ui.tableView.setModel(self.proxy)
        self.ui.tableView.setSortingEnabled(True)

        # these are the columns in OLD_DF
        # BROKER_ID	SHEET	STRATEGY	EXCHANGE	INSTRUMENT	SYMBOL	
        # EXPIRY	STRIKE	OPT_TYPE	QUANTITY

        #================================ FILTERS ==================================#

        self.ui.broker.setEditable(True)
        self.ui.broker.lineEdit().setPlaceholderText("BROKER_ID")
        self.ui.broker.addItem("")
        self.ui.broker.addItems(df["BROKER_ID"].astype(str).unique().tolist())

        self.ui.broker.currentTextChanged.connect(
            lambda text: self.proxy.setFilterForColumn(0, text)
        )

        self.ui.sheet.setEditable(True)
        self.ui.sheet.lineEdit().setPlaceholderText("SHEET")
        self.ui.sheet.addItem("")
        self.ui.sheet.addItems(df["SHEET"].astype(str).unique().tolist())

        self.ui.sheet.currentTextChanged.connect(
            lambda text: self.proxy.setFilterForColumn(1, text)
        )

        self.ui.strategy.setEditable(True)
        self.ui.strategy.lineEdit().setPlaceholderText("STRATEGY")
        self.ui.strategy.addItem("")
        self.ui.strategy.addItems(df["STRATEGY"].astype(str).unique().tolist())

        self.ui.strategy.currentTextChanged.connect(
            lambda text: self.proxy.setFilterForColumn(2, text)
        )

        self.ui.exchange.setEditable(True)
        self.ui.exchange.lineEdit().setPlaceholderText("EXCHANGE")
        self.ui.exchange.addItem("")
        self.ui.exchange.addItems(df["EXCHANGE"].astype(str).unique().tolist())

        self.ui.exchange.currentTextChanged.connect(
            lambda text: self.proxy.setFilterForColumn(3, text)
        )

        self.ui.instrument.setEditable(True)
        self.ui.instrument.lineEdit().setPlaceholderText("INSTRUMENT")
        self.ui.instrument.addItem("")
        self.ui.instrument.addItems(df["INSTRUMENT"].astype(str).unique().tolist())

        self.ui.instrument.currentTextChanged.connect(
            lambda text: self.proxy.setFilterForColumn(4, text)
        )

        self.ui.symbol.setEditable(True)
        self.ui.symbol.lineEdit().setPlaceholderText("SYMBOL")
        self.ui.symbol.addItem("")
        self.ui.symbol.addItems(df["SYMBOL"].astype(str).unique().tolist())

        self.ui.symbol.currentTextChanged.connect(
            lambda text: self.proxy.setFilterForColumn(5, text)
        )

        self.ui.expiry.setEditable(True)
        self.ui.expiry.lineEdit().setPlaceholderText("EXPIRY")
        self.ui.expiry.addItem("")
        self.ui.expiry.addItems(df["EXPIRY"].astype(str).unique().tolist())

        self.ui.expiry.currentTextChanged.connect(
            lambda text: self.proxy.setFilterForColumn(6, text)
        )

        self.ui.strike.setEditable(True)
        self.ui.strike.lineEdit().setPlaceholderText("STRIKE")
        self.ui.strike.addItem("")
        self.ui.strike.addItems(df["STRIKE"].astype(str).unique().tolist())

        self.ui.strike.currentTextChanged.connect(
            lambda text: self.proxy.setFilterForColumn(7, text)
        )

        self.ui.opt_type.setEditable(True)
        self.ui.opt_type.lineEdit().setPlaceholderText("OPT_TYPE")
        self.ui.opt_type.addItem("")
        self.ui.opt_type.addItems(df["OPT_TYPE"].astype(str).unique().tolist())

        self.ui.opt_type.currentTextChanged.connect(
            lambda text: self.proxy.setFilterForColumn(8, text)
        )

        self.ui.quantity.setEditable(True)
        self.ui.quantity.lineEdit().setPlaceholderText("QUANTITY")
        self.ui.quantity.addItem("")
        self.ui.quantity.addItems(df["QUANTITY"].astype(str).unique().tolist())

        self.ui.quantity.currentTextChanged.connect(
            lambda text: self.proxy.setFilterForColumn(9, text)
        )

        #================================ FILTERS END ==================================#








def set_dark_theme(app: QApplication):
    app.setStyle("Fusion")
    dark = QPalette()
    dark.setColor(QPalette.Window, QColor(53, 53, 53))
    dark.setColor(QPalette.WindowText, QColor(220, 220, 220))
    dark.setColor(QPalette.Base, QColor(35, 35, 35))
    dark.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark.setColor(QPalette.ToolTipBase, QColor(220, 220, 220))
    dark.setColor(QPalette.ToolTipText, QColor(220, 220, 220))
    dark.setColor(QPalette.Text, QColor(220, 220, 220))
    dark.setColor(QPalette.Button, QColor(53, 53, 53))
    dark.setColor(QPalette.ButtonText, QColor(220, 220, 220))
    dark.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
    app.setPalette(dark)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    set_dark_theme(app)   # <-- activate dark theme here
    w = MainWin()
    w.show()
    sys.exit(app.exec())




