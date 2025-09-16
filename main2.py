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

        # ====== Load data =======
        df = pd.read_excel("OLD_DF.xlsx")

        df["EXPIRY"] = pd.to_datetime(df["EXPIRY"], errors='coerce')
        df["EXPIRY"] = df["EXPIRY"].dt.strftime("%d%b%y").str.upper()
        df["EXPIRY"] = df["EXPIRY"].fillna("")
        if "VALUE" not in df.columns:
            df["VALUE"] = (df["QUANTITY"] * df["RATE"] * -1).astype(int)
        self.df = df

        # ==== Group by key: one card per unique combination ====
        key_cols = ["BROKER_ID", "SHEET", "STRATEGY", "SYMBOL", "EXPIRY"]
        self.groups = {
            key: sub.reset_index(drop=True)
            for key, sub in df.groupby(key_cols, dropna=False)
        }

        # ==== Build all cards once, cache them ====
        self.cards_cache = {}
        for key, sub in self.groups.items():
            c = Card()
            c.set_data(sub)
            self.cards_cache[key] = c

        # ==== Fill filter combos ====
        self._fill_combo(self.ui.broker_box,   df["BROKER_ID"])
        self._fill_combo(self.ui.sheet_box,    df["SHEET"])
        self._fill_combo(self.ui.strategy_box, df["STRATEGY"])
        self._fill_combo(self.ui.symbol_box,   df["SYMBOL"])
        self._fill_combo(self.ui.expiry_box,   df["EXPIRY"])

        # ==== Wire filters to realtime refresh ===
        for cb in (
            self.ui.broker_box,
            self.ui.sheet_box,
            self.ui.strategy_box,
            self.ui.symbol_box,
            self.ui.expiry_box,
        ):
            cb.currentTextChanged.connect(self.apply_filters)

        # ==== Initial render =====
        self.apply_filters()

    # ------------------------------------------------------------------
    def _fill_combo(self, combo, series):
        """fill a combo with 'All' + unique values from a column."""
        combo.blockSignals(True)
        combo.clear()
        combo.addItem("All")
        vals = sorted(map(str, pd.Series(series).dropna().unique()))
        combo.addItems(vals)  # <-- addItems (not addItem)
        combo.blockSignals(False)

    def _clear_cards_area(self):
        """Remove all widgets from the cards layout (keep cached cards)."""
        lay = self.ui.cardsLayout
        while lay.count():
            item = lay.takeAt(0)
            w = item.widget()
            if w is not None:
                w.hide()
            # we don't delete the widget; we only remove from layout

    def apply_filters(self, *_):
        """Realtime multi-column AND filter for cards."""
        b = self.ui.broker_box.currentText()
        s = self.ui.sheet_box.currentText()
        t = self.ui.strategy_box.currentText()
        y = self.ui.symbol_box.currentText()
        e = self.ui.expiry_box.currentText()

        # Normalize "All"/empty -> None
        b = None if b in (None, "", "All") else b
        s = None if s in (None, "", "All") else s
        t = None if t in (None, "", "All") else t
        y = None if y in (None, "", "All") else y
        e = None if e in (None, "", "All") else e

        self._clear_cards_area()  # <-- correct method name

        # key = (BROKER_ID, SHEET, STRATEGY, SYMBOL, EXPIRY)
        for (bro, sheet, strat, sym, expi), sub in self.groups.items():  # <-- items()
            if b and str(bro)   != b:   continue
            if s and str(sheet) != s:   continue
            if t and str(strat) != t:   continue
            if y and str(sym)   != y:   continue
            if e and str(expi)  != e:   continue

            card = self.cards_cache[(bro, sheet, strat, sym, expi)]
            card.show()
            self.ui.cardsLayout.addWidget(card)


        self.ui.cardsLayout.addStretch(1)


# ----------------------------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = StrategyWin()
    w.show()
    sys.exit(app.exec())

