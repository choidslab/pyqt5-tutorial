<<<<<<< HEAD
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_user_interface()

    def init_user_interface(self):
        """ QMainWindow 클래스의 statusBar() 메소드를 이용하여 상태바 생성,
        상태바에 보여지는 메시지는 showMessage() 메소드를 호출하여 표시 """
        self.statusBar().showMessage('Ready')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == "__main__":
    my_app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(my_app.exec_())
=======
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_user_interface()

    def init_user_interface(self):
        """ QMainWindow 클래스의 statusBar() 메소드를 이용하여 상태바 생성,
        상태바에 보여지는 메시지는 showMessage() 메소드를 호출하여 표시 """
        self.statusBar().showMessage('Ready')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == "__main__":
    my_app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(my_app.exec_())
>>>>>>> 40dba21a340598117f263c9a82de31d364836cdb
