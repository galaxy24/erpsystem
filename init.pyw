from mainUI import MainWindow
import sys
import public
from login import LoginWindow
from PyQt5 import QtWidgets
from student import StudentManager
from calculator import CalculatorManager
from zuohuo import ZuohuoManager
from tuozhong import TuozhongManager
from finance import FinanceManager
from total import TotalManager

if __name__ == "__main__":
    argv = sys.argv
    FILEPATH = argv[0]
    #QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    app.addLibraryPath(".")

    public.studentManager = StudentManager()
    public.calculatorManager = CalculatorManager()
    public.zuohuoManager = ZuohuoManager()
    public.tuozhongManager = TuozhongManager()
    public.financeManager = FinanceManager()
    public.totalManager = TotalManager()

    # public.mainDialog = LoginWindow()
    public.mainDialog = MainWindow()
    public.mainDialog.show()

    sys.exit(app.exec_())