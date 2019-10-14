import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_user_interface()

    def init_user_interface(self):

        exit_action = QAction(QIcon('../img/exit.png'), 'Exit', self)  # icon 이미지 및 'Exit' 표시
        exit_action.setShortcut('Ctrl + Q')  # 단축키(Short Cut) 설정
        exit_action.setStatusTip('Exit Application')  # setStatusTip() 메소드를 통해 Menu에 마우스 커서를 올렸을 때 상태바 표시
        exit_action.triggered.connect(qApp.quit)  # 생성된 시그널이 QApplication 위젯의 quit() 메소드에 연결 -> Application 종료

        self.statusBar()

        menubar = self.menuBar()  # 메뉴바 생성
        menubar.setNativeMenuBar(False)
        file_menu = menubar.addMenu('&File')  # 메뉴바에 'File' 탭 생성, &는 단축키 사용이 가능하도록 해줌 'F' 앞에 있기 때문에 'Alt + F' 단축키 사용 가능
        file_menu.addAction(exit_action)  # 'File' 탭에  exit_action 연결(추가)

        self.setWindowTitle('Menubar')
        self.setGeometry(300, 300, 300, 300)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
