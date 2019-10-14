import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application')
        self.move(500, 500)  # 화면에서 창이 띄워지는 위치
        self.resize(400, 200)  # 위젯의 가로 세로 크기
        self.show()  # 위젯을 화면에 나타냄


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex_window = MyApp()
    sys.exit(app.exec())
