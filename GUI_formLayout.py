import PyQt5.QtWidgets as qtw #Importing QtWidgets
import PyQt5.QtGui as qtg #Importing QtGui


class MainWindow(qtw.QWidget):
     def __init__(self):
         super().__init__()
         
         #Add title
         self.setWindowTitle("Hello world!")

         #Set a Vertical layout
         form_layout = qtw.QFormLayout()
         self.setLayout(form_layout)
         
         #Add stuff/widgets
         label_1=qtw.QLabel("This is a cool label row")
         label_1.setFont(qtg.QFont("Helvetica", 24))

         f_name= qtw.QLineEdit(self)
         l_name= qtw.QLineEdit(self)

         #Add row to app
         form_layout.addRow(label_1)
         form_layout.addRow("First Name", f_name)
         form_layout.addRow("Last Name", l_name)
         form_layout.addRow(qtw.QPushButton("Press Me!", clicked= lambda: press_it()))

         
         self.show()

         def press_it():
            #Add name to label
            label_1.setText(f"You clicked the button {f_name.text()} {l_name.text()}!") #You can set currentText, currentData, currentIndex
            
            

app= qtw.QApplication([])
mw= MainWindow()

#Run the app
app.exec_()