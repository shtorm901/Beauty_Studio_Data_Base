from PySide6 import QtWidgets, QtCore, QtGui
from src.client.api.session import Session
from src.client.main_widgets.authorization_menu import AuthorizationMenu
from src.client.main_widgets.user_profile import UserProfile
from server import start_server
import multiprocessing



class MainWindow(QtWidgets.QMainWindow):
    session: Session = Session()

    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.start_server()
        self.__init_ui()
        self.__setting_ui()

        self.show()
    
    def __init_ui(self) -> None:
        self.central_widget = QtWidgets.QWidget(self)
        self.main_h_layout = QtWidgets.QHBoxLayout()
        self.user_profile = UserProfile(self)
        self.authorization_menu = AuthorizationMenu(self)
    
    def start_server(self) -> None:
        self.server_process = multiprocessing.Process(target=start_server)
        self.server_process.start()
    
    def __setting_ui(self) -> None:
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.main_h_layout)
        self.setWindowTitle('Main window')
        self.main_h_layout.setContentsMargins(0, 0, 0, 0)
        self.main_h_layout.addWidget(self.authorization_menu)
        self.main_h_layout.addWidget(self.user_profile)
                
        self.user_profile.hide()

    def authorization(self) -> None:
        self.authorization_menu.hide()
        self.user_profile.show()
        self.user_profile.fill_line_edits()

    def leave(self) -> None:
        self.authorization_menu.show()
        self.user_profile.hide()
        self.session.leave()
                
    def show_message(self, text: str, error: bool = False, parent=None) -> None:
        message_box = QtWidgets.QMessageBox(parent=self if not parent else parent)
        message_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        message_box.setWindowTitle('Error' if error else 'Information')
        message_box.setText(text)
        message_box.setIcon(QtWidgets.QMessageBox.Icon.Critical if error else QtWidgets.QMessageBox.Icon.Information)
        message_box.exec_()

    def close_func(self) -> None:
        self.server_process.terminate()
        self.close()
        exit()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.close_func()