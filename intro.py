import platform
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
def intro():
    os_n = platform.system().upper()
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("X-E-N-O-N")
    label = QLabel(window)
    label.setText(f"     [X] - [E] - [N] - [O] - [N] \n\n-----------S-T-A-R-T-E-D---------\n\n  DEVICE : TERMINAL@{os_n}\n")
    label.setStyleSheet("font-size: 24pt")
    window.setLayout(QVBoxLayout())
    window.layout().addWidget(label)
    window.show()
    sys.exit(app.exec_())

intro()

