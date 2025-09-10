from PySide6.QtWidgets import QWidget
from card import Ui_card   # generated from card.ui
from main import PandasModel   # reuse your existing model

class Card(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_card()
        self.ui.setupUi(self)

        self._df_subset = None
        self._table_ready = False

        # start with table hidden
        self.ui.tableView.setVisible(False)

        # rewire button
        try:
            self.ui.show_button.clicked.disconnect()
        except TypeError:
            pass
        self.ui.show_button.clicked.connect(self._toggle)

    def set_data(self, df_subset):
        """Fill labels with data from one subset of your DataFrame"""
        self._df_subset = df_subset

        # Set summary labels (use first row or aggregated info)
        self.ui.broker_label.setText(str(df_subset["BROKER_ID"].iloc[0]))
        self.ui.symbol_label.setText(str(df_subset["SYMBOL"].iloc[0]))
        self.ui.strategy_label.setText(str(df_subset["STRATEGY"].iloc[0]))
        self.ui.value_label.setText(f"Value: {df_subset['VALUE'].sum():,.0f}")

    def _toggle(self):
        vis = self.ui.tableView.isVisible()
        if not vis and not self._table_ready and self._df_subset is not None:
            # Create model from this subset
            model = PandasModel(self._df_subset.reset_index(drop=True))
            self.ui.tableView.setModel(model)
            self.ui.tableView.setSortingEnabled(True)
            self._table_ready = True

        # toggle visibility
        self.ui.tableView.setVisible(not vis)
        self.ui.show_button.setText("Hide" if not vis else "Show more")

            

