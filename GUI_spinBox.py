import PyQt5.QtWidgets as qtw #Importing QtWidgets
import PyQt5.QtGui as qtg #Importing QtGui


class MainWindow(qtw.QWidget):
     def __init__(self):
         super().__init__()
         
         #Add title
         self.setWindowTitle("Hello world!")

         #Set a Vertical layout
         self.setLayout(qtw.QVBoxLayout()) #If we want a Horizontal Layout we need to exchange QVBoxLayout to QHBoxLayout

         #Create a Label
         my_label = qtw.QLabel("Pick something from the list")
         my_label.setFont(qtg.QFont("Helvetica", 18)) #Change the font size of label. For that I need to import PyQt5.QtGui
         self.layout().addWidget(my_label)

         #create an spin box
         my_spin= qtw.QSpinBox(self, 
                               value=10, 
                               maximum=100, 
                               minimum=0, 
                               singleStep=5, 
                               prefix="Your order is #", 
                               suffix=" Order")
         
         #my_spin= qtw.QDoubleSpinBox(self, value=10, maximum=100, minimum=0, singleStep=5.50, prefix="#", suffix=" Order") #Spin Box with decimals
         
         #Change the font size in my spin
         my_spin.setFont(qtg.QFont("Helvetica", 14))
         
         #Put combobox on the screen
         self.layout().addWidget(my_spin)

         #Create a button
         my_button = qtw.QPushButton("Press me!", clicked= lambda: press_it())
         self.layout().addWidget(my_button)

         
         self.show()

         def press_it():
            #Add name to label
            my_label.setText(f"You picked {my_spin.value()}") #You can set currentText, currentData, currentIndex
            

app= qtw.QApplication([])
mw= MainWindow()

#Run the app
app.exec_()