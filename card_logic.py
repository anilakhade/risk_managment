from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from card import Ui_card
from main import PandasModel


class Card(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_card()
        self.ui.setupUi(self)

        self._df_subset = None
        self._table_ready = False

        # start hidden
        self.ui.tableView.setVisible(False)

        try:
            self.ui.show_button.clicked.disconnect()
        except TypeError:
            pass
        self.ui.show_button.clicked.connect(self._toggle)

    def set_data(self, df_subset):
        self._df_subset = df_subset

        self.ui.broker_label.setText(str(df_subset["BROKER_ID"].iloc[0]))
        self.ui.symbol_label.setText(str(df_subset["SYMBOL"].iloc[0]))
        self.ui.strategy_label.setText(str(df_subset["STRATEGY"].iloc[0]))
        self.ui.value_label.setText(f"Value: {df_subset['VALUE'].sum():,.0f}")

    def _fit_table_height(self):
        tv = self.ui.tableView
        tv.resizeRowsToContents()
        header_h = tv.horizontalHeader().height()
        rows = tv.model().rowCount()
        rows_h = sum(tv.rowHeight(r) for r in range(rows))
        margin = 2 * tv.frameWidth()
        tv.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        tv.setFixedHeight(header_h + rows_h + margin)

    def _toggle(self):
        vis = self.ui.tableView.isVisible()
        if not vis and not self._table_ready and self._df_subset is not None:
            model = PandasModel(self._df_subset.reset_index(drop=True))
            self.ui.tableView.setModel(model)
            self.ui.tableView.setSortingEnabled(True)
            self._fit_table_height()   # <--- expand height
            self._table_ready = True

        if not vis:
            self._fit_table_height()   # ensure correct height when re-shown

        self.ui.tableView.setVisible(not vis)
        self.ui.show_button.setText("Hide" if not vis else "Show more")

