"""
절대적 배치(absolute positioning)
  - 위젯의 위치, 크기를 픽셀(pixel) 단위로 설정하여 배치
  - 창의 크기를 조절해도 위젯의 위치, 크기는 변하지 않음
  - 플랫폼에 따라 다르게 보일 수 있음
  - 폰트 변경 시 레이아웃이 변경될 수 있음
  - 레이아웃을 변경할 경우 완전히 새로 고쳐야 함
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_user_interface()

    def init_user_interface(self):
        label1 = QLabel('Label1', self)
        label1.move(20, 20)  # move(x, y) 메소드를 이용하여 위젯 위치 지정(x좌표, y좌표)
        label2 = QLabel('Label2', self)
        label2.move(20, 60)

        btn1 = QPushButton('Button1', self)
        btn1.move(80, 13)
        btn2 = QPushButton('Button2', self)
        btn2.move(80, 53)

        self.setWindowTitle('절대적 배치(Absolute Positioning)')
        self.setGeometry(300, 300, 400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
