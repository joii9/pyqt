import PyQt5.QtWidgets as qtw


class MainWindow(qtw.QWidget):
     def __init__(self):
         super().__init__()
         
         #Add title
         self.setWindowTitle("Hello world")

         #Set a Vertical layout
         self.setLayout(qtw.QVBoxLayout()) #If we want a Horizontal Layout we need to exchange QVBoxLayout to QHBoxLayout

         #Create a Label
         my_label= qtw.QLabel("Joel Carbajal Muñoz")
         self.layout().addWidget(my_label)

         self.show()

app= qtw.QApplication([])
mw= MainWindow()

#Run the app
app.exec_()