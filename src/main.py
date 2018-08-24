import os
import sys
import pygame
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QGridLayout
from PyQt5.QtCore import Qt


class ButtonWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.layout = QGridLayout()
        self.init_ui()

    def init_ui(self) -> None:
        buzzer_button = QPushButton('')
        buzzer_button.clicked.connect(self.on_click_buzz)
        buzzer_button.setStyleSheet('QPushButton{background-color: red;'
                                    '            border-radius: 50%;'
                                    '            height: 100px;'
                                    '            width: 100px;'
                                    '            max-width: 100px;}\n'
                                    'QPushButton:hover {border: 5px solid darkred}'
                                    'QPushButton:pressed {background-color: darkred}')
        self.layout.setAlignment(buzzer_button, Qt.AlignCenter)
        self.layout.addWidget(buzzer_button, 0, 0, 1, 1)
        self.setLayout(self.layout)

    @staticmethod
    def on_click_buzz() -> None:
        pygame.mixer.init()
        pygame.mixer.music.load(resource_path('./audio/buzz.wav'))
        pygame.mixer.music.play()


class PrimaryWindow(QMainWindow):
    def __init__(self, app: QMainWindow) -> None:
        super().__init__()
        self.app = app
        self.init_ui()

    def init_ui(self) -> None:
        self.setWindowTitle('Bzzz')
        button = ButtonWidget()
        self.setCentralWidget(button)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    Main = PrimaryWindow(App)
    Main.show()
    sys.exit(App.exec_())
