<<<<<<< HEAD
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def init_user_interface(self):
        btn = QPushButton('Quit', self)  # 버튼 생성, 첫 번째 파라미터에는 버튼의 이름, 두 번째 파라미터에는 버튼이 위치할 부모 위젯
        btn.move(50, 50)  # 버튼 위치
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)
        """
        PyQt5에서 이벤트 처리는 시그널, 슬롯 메커니즘으로 동작 
        버튼을 클릭하면 clicked 시그널 생성
        instance() 메소드는 현재 인스턴스를 반환
        clicked 시그널은 quit() 메소드에 연결
        이러한 방식으로 Sender와 Receiver, 두 객체 간에 커뮤니케이션이 이루어짐
        본 예제에서 Sender는 Quit 버튼, Receiver는 Application 객체(my_app) 
        """

        self.setWindowTitle('Quit Button')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == "__main__":
    my_app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(my_app.exec_())
=======
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def init_user_interface(self):
        btn = QPushButton('Quit', self)  # 버튼 생성, 첫 번째 파라미터에는 버튼의 이름, 두 번째 파라미터에는 버튼이 위치할 부모 위젯
        btn.move(50, 50)  # 버튼 위치
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)
        """
        PyQt5에서 이벤트 처리는 시그널, 슬롯 메커니즘으로 동작 
        버튼을 클릭하면 clicked 시그널 생성
        instance() 메소드는 현재 인스턴스를 반환
        clicked 시그널은 quit() 메소드에 연결
        이러한 방식으로 Sender와 Receiver, 두 객체 간에 커뮤니케이션이 이루어짐
        본 예제에서 Sender는 Quit 버튼, Receiver는 Application 객체(my_app) 
        """

        self.setWindowTitle('Quit Button')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == "__main__":
    my_app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(my_app.exec_())
>>>>>>> 40dba21a340598117f263c9a82de31d364836cdb
