import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.init_user_interface()

    def init_user_interface(self):

        """
        - QLabel 클래스를 이용하여 3개의 라벨 생성
        - 라벨 이름은 각각 Red, Green, Blue로 설정
        """
        lbl_red = QLabel('Red')
        lbl_green = QLabel('Green')
        lbl_blue = QLabel('Blue')

        """
        - setStyleSheet() 메소드를 이용하여 폰트 색깔, 경계선(Border) 색상/두께/종류, 배경색상 등을 설정할 수 있음
        """
        lbl_red.setStyleSheet("color: red;"
                              "border-style: solid;"
                              "border-width: 2px;"
                              "border-color: #FA8072;"
                              "border-radius: 3px")

        lbl_green.setStyleSheet("color: green;"
                                "background-color: #7FFFD4;")

        lbl_blue.setStyleSheet("color: blue;"
                               "background-color: #87CEFA;"
                               "border-style: dashed;"
                               "border-width: 3px;"
                               "border-color: #1E90FF")

        """
        - QVBoxLayout()을 이용하여 라벨 위젯을 수직으로 배치(vertical box)
        """
        vbox = QVBoxLayout()
        vbox.addWidget(lbl_red)
        vbox.addWidget(lbl_green)
        vbox.addWidget(lbl_blue)

        self.setLayout(vbox)

        self.setWindowTitle("Stylesheet")
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
