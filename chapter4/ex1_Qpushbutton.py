"""
QPushButton
  - GUI에 표시되는 버튼을 생성하는 클래스

* 자주 사용되는 메소드
  - setCheckable(): True 설정 시, 클릭 상태와 클리하지 않은 상태를 구분
  - toggle(): 상태 변경
  - setIcon(): 아이콘 표시
  - setEnabled(): False 설정 시, 버튼 사용 X
  - isChecked(): 버튼 선택 여부 반환
  - setText(): 버튼에 표시될 텍스트 설정
  - text(): 버튼에 표시된 텍스트 반환

* 자주 사용되는 시그널
  - clicked(): 버튼 클릭 시 발생
  - pressed(): 버튼이 눌려있을 때 발생
  - released(): 버튼을 눌렀다 뗄 때 발생
  - toggled(): 버튼 상태가 바뀔 때 발생
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_user_interface()

    def init_user_interface(self):
        btn1 = QPushButton('&Button1', self)  # 버튼 객체 생성
        btn1.setCheckable(True)  # 클릭 되거나 클리되지 않은 상태 유지
        btn1.toggle()  # 버튼 상태 변경

        btn2 = QPushButton(self)
        btn2.setText('Button&2')  # &를 넣어주면 shortcut 설정 (Alt+b)

        btn3 = QPushButton('&Button3', self)
        btn3.setEnabled(False)  # False인 경우 버튼 비활성화

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
