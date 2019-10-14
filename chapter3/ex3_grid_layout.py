"""
그리드 레이아웃(Grid Layout) -> 표(Tabel)와 비슷
  - 가장 일반적인 레이아웃 클래스
  - 위젯의 공간을 행, 열로 구분
  - QGridLayout 클래스 사용
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QTextEdit, QLabel


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_user_interface()

    def init_user_interface(self):
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('Title:'), 0, 0)  # gird.addWidget() 2번째, 3번째 파라미터가 행과 열 위치를 의미
        grid.addWidget(QLabel('Author:'), 1, 0)
        grid.addWidget(QLabel('Review:'), 2, 0)
        # grid.addWidget(QLabel('Comments:'), 3, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1)
        # grid.addWidget(QLineEdit(), 3, 1)

        self.setWindowTitle('QGridLayout')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    exit(app.exec_())
