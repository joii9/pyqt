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
         #Change the font size of label. For that I need to import PyQt5.QtGui
         my_label = qtw.QLabel("Pick something from the list")
         my_label.setFont(qtg.QFont("Helvetica", 18))
         self.layout().addWidget(my_label)

         #create an combo box
         #my_combo= qtw.QComboBox(self)
         my_combo= qtw.QComboBox(self, editable=True, insertPolicy= qtw.QComboBox.InsertAtBottom) #To become editable and insert in the widget, InsertAtTop or InsertAtBottom
         #Add items to the combo box
         my_combo.addItem("Pepperoni", 1)
         my_combo.addItem("Cheese", "Something")
         my_combo.addItem("Mushroom", qtw.QWidget)
         my_combo.addItem("Peppers")
         my_combo.addItems(["One", "Two", "Three"]) #Even you can pass a list with a different command addItems instead of addItem
         my_combo.insertItem(2 , "Third thing") #This is the way to insert an item in the combobox in a specific index
         my_combo.insertItems(3 , ["One", "Two", "Third thing"]) #Also you can insert more than one item
         #Put combobox on the screen
         self.layout().addWidget(my_combo)

         #Create a button
         my_button = qtw.QPushButton("Press me!", clicked= lambda: press_it())
         self.layout().addWidget(my_button)

         
         self.show()

         def press_it():
            #Add name to label
            my_label.setText(f"You picked {my_combo.currentText()}") #You can set currentText, currentData, currentIndex
            

app= qtw.QApplication([])
mw= MainWindow()

#Run the app
app.exec_()