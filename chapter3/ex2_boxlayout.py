"""
박스 레이아웃(Box Layout)
  - QHBoxLayout, QVBoxLayout은 여러 위젯을 수평으로 정렬하는 클래스
  - 수평/수직 박스를 만들어 다른 레이아웃 박스를 넣거나 위젯을 배치할 수 있음
  - 창의 크기를 조절하여도 비율에 맞춰 자동으로 위젯이 위치하게 됨(absolute positioning과 반대)
  - 수평박스(hbox)를 먼저 생성한 뒤, hbox를 수직박스(vbox)에 넣어서 표시하는 경우와 그 반대의 경우 위젯 배치가 다름(순서 중요)
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_user_interface()

    def init_user_interface(self):
        ok_button = QPushButton('OK')
        cancel_button = QPushButton('Cancel')

        hbox = QHBoxLayout()  # 수평 박스 생성
        hbox.addStretch(1)  # addStretch() 메소드를 이용하여 수평 왼쪽에 빈 공간 생성, 메소드 파라미터(stretch factor)로 위치 지정
        hbox.addWidget(ok_button)
        hbox.addWidget(cancel_button)
        hbox.addStretch(1)  # 수평 오른쪽 공간 생성, 수평 양쪽 공간 비율이 1:1

        vbox = QVBoxLayout()  # 수직 박스 생성
        vbox.addStretch(3)  # 버튼의 윗공간 비율
        vbox.addLayout(hbox)  # 수평 박스를 수직박스에 넣어 위치 조정, 위의 addStretch() 메소드에 의해 버튼이 하단에 위치하게 됨
        vbox.addStretch(1)  # 버튼의 아랫공간 비율, 즉 위/아래 공간의 비율이 3:1

        # vbox = QVBoxLayout()  # 수직 박스 생성
        # vbox.addStretch(3)  # 버튼의 윗공간 비율
        # vbox.addWidget(ok_button)
        # vbox.addWidget(cancel_button)
        # vbox.addStretch(1)  # 버튼의 아랫공간 비율, 즉 위/아래 공간의 비율이 3:1
        #
        # hbox = QHBoxLayout()  # 수평 박스 생성
        # hbox.addStretch(1)  # addStretch() 메소드를 이용하여 수평 왼쪽에 빈 공간 생성, 메소드 파라미터(stretch factor)로 위치 지정
        # hbox.addLayout(vbox)
        # hbox.addStretch(1)  # 수평 오른쪽 공간 생성, 수평 양쪽 공간 비율이 1:1

        self.setLayout(vbox)
        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
