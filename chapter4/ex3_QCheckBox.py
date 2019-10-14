"""
QCheckBox
  - QCheckBox 위젯은 on/off 2가지 상태를 갖는 버튼 제공
  - 하나의 텍스트 라벨과 함께 사용됨
  - 체크 박스를 선택하거나 해제할 때 stateChanged() 시그널 발생
  - 따라서 체크 박스 상태가 변할 때 특정 동작을 하도록 시그널과 슬롯을 연결할 수 있음
  - 체크 박스 선택 여부는 isChecked() 메소드를 통해 확인 가능하면 True or False 값 반환
  - setTristate() 메소드는 변경 없음(no change) 상태를 가질 수 있음
  - 3가지 상태를 표시하는 기능은 checkState() 메소드를 통해 가능, 선택/변경 없음/해제
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.init_user_interface()

    def init_user_interface(self):
        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()  # 체크 박스는 default로 체크 되어 있지 않음, 본 예제에서는 체크 상태로 변경하기 위해 toggle() 사용
        cb.stateChanged.connect(self.change_title)  # 체크 상태가 변할 때 발생하는 시그널을 change_title() 메소드에 연결

        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def change_title(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())