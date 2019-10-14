<<<<<<< HEAD
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_user_interface()

    def init_user_interface(self):

        save_action = QAction(QIcon('../img/save.png'), 'Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.setStatusTip('Save')

        edit_action = QAction(QIcon('../img/edit.png'), 'Edit', self)
        edit_action.setShortcut('Ctrl+E')
        edit_action.setStatusTip('Edit')

        print_action = QAction(QIcon('../img/print.png'), 'Print', self)
        print_action.setShortcut('Ctrl+P')
        print_action.setStatusTip('Print')

        exit_action = QAction(QIcon('../img/exit.png'), 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit Application')
        exit_action.triggered.connect(qApp.quit)  # 마우스 클릭 시 생성되는 시그널 -> quit() 메소드에 연결

        self.statusBar()

        self.toolbar = self.addToolBar('Save')
        self.toolbar.addAction(save_action)

        self.toolbar = self.addToolBar('Edit')
        self.toolbar.addAction(edit_action)

        self.toolbar = self.addToolBar('Print')
        self.toolbar.addAction(print_action)

        self.toolbar = self.addToolBar('Exit')  # 
        self.toolbar.addAction(exit_action)

        self.setWindowTitle('Toolbar')
        self.setGeometry(300, 300, 300, 300)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
=======
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_user_interface()

    def init_user_interface(self):

        save_action = QAction(QIcon('../img/save.png'), 'Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.setStatusTip('Save')

        edit_action = QAction(QIcon('../img/edit.png'), 'Edit', self)
        edit_action.setShortcut('Ctrl+E')
        edit_action.setStatusTip('Edit')

        print_action = QAction(QIcon('../img/print.png'), 'Print', self)
        print_action.setShortcut('Ctrl+P')
        print_action.setStatusTip('Print')

        exit_action = QAction(QIcon('../img/exit.png'), 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit Application')
        exit_action.triggered.connect(qApp.quit)  # 마우스 클릭 시 생성되는 시그널 -> quit() 메소드에 연결

        self.statusBar()

        self.toolbar = self.addToolBar('Save')
        self.toolbar.addAction(save_action)

        self.toolbar = self.addToolBar('Edit')
        self.toolbar.addAction(edit_action)

        self.toolbar = self.addToolBar('Print')
        self.toolbar.addAction(print_action)

        self.toolbar = self.addToolBar('Exit')  # 
        self.toolbar.addAction(exit_action)

        self.setWindowTitle('Toolbar')
        self.setGeometry(300, 300, 300, 300)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
>>>>>>> 40dba21a340598117f263c9a82de31d364836cdb
