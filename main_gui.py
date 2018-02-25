#!usr/bin/env python3

# import the needed libraries
import sys
from sys import platform
import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import queue
import os
from docx import Document
from docx.shared import Inches

if platform == "win32":
    import win32com.client as wincl
    voice = wincl.Dispatch("SAPI.SpVoice")

    comp = 0
else:
    comp = 1

##############################
class mainWindow(QMainWindow):

    # initialize the main window
    def __init__(self):
        super().__init__()

        #self.noods = QWidget(webcam)
        self.woohoo = mainWidget()

##########################
class mainWidget(QWidget):


    # function for the controlling GUI
    def __init__(self):
        super().__init__()
        # define a custom signal to be sent from the stop function to start to kill the recording
        self.kill_rec = pyqtSignal()

        # set up the layout(s) and add to the main window
        hLayout1 = QHBoxLayout()

        start = QPushButton("Start Recording")
        start.clicked.connect(self.startAction)

        stop = QPushButton("Stop Recording")
        stop.clicked.connect(self.stopAction)

        write = QPushButton("Save file as: ")
        write.clicked.connect(self.writeAction)

        self.file_name = QLineEdit()


        hLayout1.addWidget(start)
        hLayout1.addWidget(stop)
        hLayout1.addWidget(write)
        self.letter = ""
        hLayout1.addWidget(self.file_name)

        self.setLayout(hLayout1)
        self.show()
        self.doc = Document()

        # This function should add one paragraph at a time to the document including a delete character

    #This function takes in a string and has espeak say it
    def say(self,n):
        if comp:
            os.system("espeak '"+n+"'")
            print(chr(27) + "[2J")
        else:
            voice.Speak(n)
        

    # This function interprets the subImage in order to determine the letter it represents
    def imageToLetter(self, image):
        return "a"

    # Start the video recording here
    def startAction(self):
        # set a flag
        self.play = True

        x1, y1, x2, y2 = 420, 200, 620, 400

        cap = cv2.VideoCapture(0)

        # Set the boundaries of the video
        cap.set(3, 800)
        cap.set(4, 600)

        # Frame counter, creates our one per second count
        frameNumber = 0

        while (self.play):
            # capture frame and flip it
            ret, image = cap.read()
            image = cv2.flip(image, 1)
            # Draw the subImage rectangle
            image = cv2.rectangle(image, (x1, y1), (x2, y2), (255, 200, 0), 3)

            # Display the frame
            cv2.imshow('frame', image)

            # If a q is pressed break from the loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            # Increment our frame counter
            frameNumber = frameNumber + 1

            # Every thirty frames 
            if frameNumber == 30:
                frameNumber = 0
                # Create the subimage
                subIm = image[y1:y2, x1:x2]
                # Interpret the subImage
                newLetter = self.imageToLetter(subIm)
                # Speak the new letter and store it in our current letters array
                self.say(newLetter)
                self.letter += newLetter

        # kill the recording
        cv2.destroyAllWindows()


    # function to stop the recording
    def stopAction(self):
        self.play = False



    # function to write the words to a file with the specified file name
    def writeAction(self):
        name = self.file_name.displayText()
        self.doc.add_paragraph(self.letter)
        self.doc.save(name)


###########
def main():
    app = QApplication(sys.argv)
    start = mainWindow()

    ### This pops up a weird extra window. Avoid because life is hard
    ##start.show()

    sys.exit(app.exec_())


###########################
if(__name__ == "__main__"):
    main()





