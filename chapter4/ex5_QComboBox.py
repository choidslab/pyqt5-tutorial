"""
QComboBox
  - 작은 공간을 통해 여러 항목을 선택할 수 있도록 하는 박스
  - 스크롤 형태로 항목 선택
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.init_user_interface()

    def init_user_interface(self):
        self.label = QLabel('Option1', self)
        self.label.move(50, 150)

        combo_box = QComboBox(self)
        combo_box.addItem('Option1')
        combo_box.addItem('Option2')
        combo_box.addItem('Option3')
        combo_box.addItem('Option4')
        combo_box.addItem('Option5')
        combo_box.move(50, 50)

        combo_box.activated[str].connect(self.onActivated)  # 옵션을 선택하면 onActivated() 메소드가 호출되어 텍스트를 전달

        self.setWindowTitle('QComboBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def onActivated(self, text):
        self.label.setText(text)  # 선택된 옵션의 텍스트가 표시
        self.label.adjustSize()  # adjustSize() 메소드를 이용하여 라벨 크기 자동 조절


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
