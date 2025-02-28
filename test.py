import PyQt5.QtWidgets as qtw #Importing QtWidgets
import PyQt5.QtGui as qtg #Importing QtGui


class MainWindow(qtw.QWidget):
     def __init__(self):
         super().__init__()
         
         #Add title
         self.setWindowTitle("Welcome window")

         #Set a Vertical layout
         self.setLayout(qtw.QVBoxLayout()) #If we want a Horizontal Layout we need to exchange QVBoxLayout to QHBoxLayout

         #Create a Label
         my_label= qtw.QLabel("Hello! What's your name?")
         
         #Change the font size of label. For that I need to import PyQt5.QtGui
         my_label.setFont(qtg.QFont("Helvetica", 18))
         self.layout().addWidget(my_label)

         #create an entry box
         my_entry = qtw.QLineEdit()
         my_entry.setObjectName("name_field")
         my_entry.setText("")
         self.layout().addWidget(my_entry)

         #Create a button
         my_button = qtw.QPushButton("Press me!", clicked= lambda: press_it())
         self.layout().addWidget(my_button)

         
         self.show()

         def press_it():
            #Add name to label
            my_label.setText(f"Hello {my_entry.text()}")
            #Clear the entry box
            my_entry.setText("")

app= qtw.QApplication([])
mw= MainWindow()

#Run the app
app.exec_()