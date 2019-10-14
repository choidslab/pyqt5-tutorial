"""
QRadioButton
  - 라디오 버튼 기능 제공
  - 라디오 버튼은 일반적으로 사용자가 여러개의 항목 중 하나의 옵션을 선택하도록 할 때 사용
  - 라디오 버튼은 기본적으로 autoExclusive로 설정 -> 하나의 항목을 선택하면 다른 항목의 선택은 모두 해제
  - 만약, 라디오 버튼 여러개를 선택하도록 하고 싶으면 setAutoExclusive() 메소드에 False 값 입력
  - 체크박스와 동일하게 버튼이 선택되면 상태가 변하여 toggled() 시그널이 발생
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.init_user_interface()

    def init_user_interface(self):
        r_btn1 = QRadioButton('First Button', self)
        r_btn1.move(50, 50)
        r_btn1.setChecked(True)

        r_btn2 = QRadioButton('Second Button', self)
        r_btn2.move(50, 70)

        r_btn3 = QRadioButton('Third Button', self)
        r_btn3.move(50, 90)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Radio Button')
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
