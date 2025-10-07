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
         my_label = qtw.QLabel("Type something into the box below")
         my_label.setFont(qtg.QFont("Helvetica", 18))
         self.layout().addWidget(my_label)

         #create an text box
         my_text= qtw.QTextEdit(self, 
                               lineWrapMode= qtw.QTextEdit.FixedColumnWidth,
                               #html= "<h1> Big Header </h1>", #You can even set text with the syntax of html code
                               #plainText= "This is real text",
                               acceptRichText= True, #This atribute is to accept text in bold, cursive, crossed or even with color. If we set to False, all the rich text is become to plain text.
                               lineWrapColumnOrWidth= 50, #This atribute is to indicate how far the line is
                               placeholderText="Hello World!!!", #This is the text will apear when the widget is created
                               readOnly=False #This is to become editable the text if we don't want the text is modified we could change to True
                               )
         
         #my_spin= qtw.QDoubleSpinBox(self, value=10, maximum=100, minimum=0, singleStep=5.50, prefix="#", suffix=" Order") #Spin Box with decimals
         
         #Change the font size in my spin
         #my_spin.setFont(qtg.QFont("Helvetica", 14))
         
         #Put combobox on the screen
         self.layout().addWidget(my_text)

         #Create a button
         my_button = qtw.QPushButton("Press me!", clicked= lambda: press_it())
         self.layout().addWidget(my_button)

         
         self.show()

         def press_it():
            #Add name to label
            my_label.setText(f"You typed {my_text.toPlainText()}") #You can set currentText, currentData, currentIndex
            my_text.setPlainText("You pressed the button!!") #This text appear when the user clicked the button in the text box
            

app= qtw.QApplication([])
mw= MainWindow()

#Run the app
app.exec_()