import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QShortcut, QKeySequence
from master import Ui_MainWindow
from main2 import StrategyWin
from main import MainWin

def attach_esc_close(win):
    QShortcut(QKeySequence("Escape"), win, win.close)

class MasterWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._strategy_win = None
        self._net_win = None

        self.ui.strategy_btn.clicked.connect(self.open_strategy)
        self.ui.net_btn.clicked.connect(self.open_net)

        self.ui.watch_table.setSortingEnabled(True)
        self.ui.folio_table.setSortingEnabled(True)

    def open_strategy(self):
        if self._strategy_win is None:
            self._strategy_win = StrategyWin()
            attach_esc_close(self._strategy_win)  # ESC closes child
        self._strategy_win.show()
        self._strategy_win.raise_()

    def open_net(self):
        if self._net_win is None:
            self._net_win = MainWin()
            attach_esc_close(self._net_win)       # ESC closes child
        self._net_win.show()
        self._net_win.raise_()

    def closeEvent(self, event):
        # closing master closes children
        for w in (self._strategy_win, self._net_win):
            if w is not None:
                w.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MasterWin()
    w.show()
    sys.exit(app.exec())

