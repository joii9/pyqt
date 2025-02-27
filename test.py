import PyQt5.QtWidgets as qtw


class MainWindow(qtw.QWidget):
     def __init__(self):
         super().__init__()
         #Add title
         self.setWindowTitle("Hello world")

         self.show()

app= qtw.QApplication([])
mw= MainWindow()

#Run the app
app.exec_()