import PyQt5.QtWidgets as qtw #Importing QtWidgets
import PyQt5.QtGui as qtg #Importing QtGui




class MainWindow(qtw.QWidget):
     def __init__(self):
         super().__init__()
         
         #Add title
         self.setWindowTitle("Hello world")

         #Set a Vertical layout
         self.setLayout(qtw.QVBoxLayout()) #If we want a Horizontal Layout we need to exchange QVBoxLayout to QHBoxLayout

         #Create a Label
         my_label= qtw.QLabel("Joel Carbajal Muñoz")
         
         #Change the font size of label. For that I need to import PyQt5.QtGui
         my_label.setFont(qtg.QFont("Helvetica", 18))

         self.layout().addWidget(my_label)
         
         self.show()

app= qtw.QApplication([])
mw= MainWindow()

#Run the app
app.exec_()