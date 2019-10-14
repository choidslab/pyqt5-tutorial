"""
QLabel
  - 텍스트 또는 이미지 라벨을 만들 때 사용
  - 라벨은 수평방향으로 왼쪽 정렬, 수직방향으로 가운데 정렬이 default(setAlignment() 메소드를 통해 정렬 위치 수정 가능)
"""


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_user_interface()

    def init_user_interface(self):
        label1 = QLabel('First Label', self)
        label1.setAlignment(Qt.AlignCenter)

        label2 = QLabel('Second Label', self)
        label2.setAlignment(Qt.AlignVCenter)

        font1 = label1.font()  # font 객체 생성
        font1.setPointSize(20)  # font 설정

        font2 = label2.font()
        font2.setFamily('Times New Roman')  # font 종류
        font2.setBold(True)  # bold

        label1.setFont(font1)  # label 객체에 font 객체를 전달
        label2.setFont(font2)

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)

        self.setLayout(layout)
        self.setWindowTitle('QLabel')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
