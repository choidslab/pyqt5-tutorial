<<<<<<< HEAD
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Icon Tutorial')
        self.setWindowIcon(QIcon('../img/web.png'))
        self.setGeometry(300, 300, 300, 300)  # setresize(), setmove()
        self.show()  # 위젯을 화면에 나타냄


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex_window = MyApp()
    sys.exit(app.exec())
=======
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Icon Tutorial')
        self.setWindowIcon(QIcon('../img/web.png'))
        self.setGeometry(300, 300, 300, 300)  # setresize(), setmove()
        self.show()  # 위젯을 화면에 나타냄


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex_window = MyApp()
    sys.exit(app.exec())
>>>>>>> 40dba21a340598117f263c9a82de31d364836cdb
