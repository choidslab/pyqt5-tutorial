"""
QProgressBar
  - 진행 상태롤 보여주는 위젯
  - setMinimum(), setMaximum() 메소드로 진행 표시줄의 최소, 최대값 설정
  - setRange() 메소드로 한 번에 범위 설정 가능(default: 0~99)
  - 진행 표시줄의 최소값과 최대값을 각각 0으로 설정할 경우 진행 표시줄이 항상 진행 중으로 표시
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QBasicTimer


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.do_action)

        self.timer = QBasicTimer()
        self.step = 0

        self.setWindowTitle('QProgressBar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def timerEvent(self, e):  # 이벤트 핸들러 오버라이딩

        if self.step >= 100:

            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def do_action(self):

        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
