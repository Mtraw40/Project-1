import sys
import os
from PyQt6.QtGui import QCloseEvent
from PyQt6.QtWidgets import QApplication, QMainWindow
from app import Ui_widget
from logic import VotingLogic


def clear_files() -> None:
    """
    Clears the files 'votes.txt' and 'vote_tally.txt' for new votes
    """
    try:
        os.remove("votes.txt")
    except FileNotFoundError:
        pass
    try:
        os.remove("vote_tally.txt")
    except FileNotFoundError:
        pass


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_widget()
        self.ui.setupUi(self)
        self.logic = VotingLogic(self.ui)
        self.closeEvent = self.logic.close_application
        clear_files()

    def closeEvent(self, event: QCloseEvent) -> None:
        """
        cleanup the application  when the application is closed.
        """
        self.logic.close_application(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
