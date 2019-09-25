import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.init_user_interface()

    def init_user_interface(self):
        self.setWindowTitle('Centering')
        self.resize(500, 350)
        self.center()
        self.show()

    def center(self):
        q_rectangle = self.frameGeometry()  # frameGeometry() 메소드를 통해 창의 위치 정보를 가져옴
        # print(q_rectangle) # PyQt5.QtCore.QRect() 반환

        center_point = QDesktopWidget().availableGeometry().center()  # 사용하는 모니터의 중심(Center) 위치를 파악
        # print(center_point) # PyQt5.QtCore.QPoint() 반환

        q_rectangle.moveCenter(center_point)  # 바로 앞에서 가져온 정보(cp)를 기반으로 창의 위치를 화면 중심으로 이동
        self.move(q_rectangle.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
