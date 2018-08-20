import sys
from pygame import mixer
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QGridLayout


class ButtonWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.layout = QGridLayout()
        self.init_ui()

    def init_ui(self) -> None:
        buzzer_button = QPushButton('Bzzz')
        buzzer_button.clicked.connect(self.on_click_buzz)
        self.layout.addWidget(buzzer_button, 0, 0, 1, 1)
        self.setLayout(self.layout)

    @staticmethod
    def on_click_buzz() -> None:
        mixer.init()
        sound = mixer.Sound('buzz.wav')
        sound.play()


class PrimaryWindow(QMainWindow):
    def __init__(self, app: QMainWindow) -> None:
        super().__init__()
        self.app = app
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Bzzz')
        button = ButtonWidget()
        self.setCentralWidget(button)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    Main = PrimaryWindow(App)
    Main.show()
    sys.exit(App.exec_())
