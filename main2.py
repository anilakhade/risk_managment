import sys
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow
from strategy import Ui_MainWindow
from card_logic import Card

class StrategyWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        df = pd.read_excel("OLD_DF.xlsx")
        df["VALUE"] = (df["QUANTITY"] * df["RATE"] * -1).astype(int)

        # group by something meaningful
        for key, df_sub in df.groupby("SYMBOL", dropna=False):
            card = Card()
            card.set_data(df_sub)
            self.ui.cardsLayout.addWidget(card)

        self.ui.cardsLayout.addStretch(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = StrategyWin()
    w.show()
    sys.exit(app.exec())

