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
import pickle
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn import tree
import numpy as np
from sklearn.externals import joblib
import train
# from skimage.measure import structural_similarity as compare_mse
from PIL import Image

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
        # arr = pickle.load(open("data.sav", 'rb'))
        # x = arr[0]
        # y = arr[1]
        # self.xt = arr[2]
        # self.yt = arr[3]
        # self.clf = tree.DecisionTreeClassifier()
        # self.clf = self.clf.fit(x, y)
        self.clf = joblib.load("finalized_model.sav")

        # This function should add one paragraph at a time to the document including a delete character

    #This function takes in a string and has espeak say it
    def say(self, n):
        if comp:
            os.system("espeak '" + n + "'")
            print(chr(27) + "[2J")
        else:
            voice.Speak(n)

    # Start the video recording here
    def startAction(self):
        newLetter = " "

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
            # Draw the newLetter
            cv2.putText(image, newLetter.upper(), (490, 195),
                        cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 200, 0), 5)
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
                subIm = cv2.flip(subIm, 1)

                img = Image.fromarray(subIm)
                # self.letter += self.imageToLetter(subIm)
                img = img.convert("L")
                basewidth = 50
                wpercent = (basewidth / float(img.size[0]))
                hsize = int((float(img.size[1]) * float(wpercent)))
                img = img.resize((basewidth, hsize), Image.ANTIALIAS)
                img = np.asarray(img, dtype=np.uint8).reshape(1, -1)
                # new = self.xt[0]
                # tot = ssim(self.xt[0].reshape(50, 50), img[0].reshape(50, 50))
                # for i in self.xt:
                #     # err = np.linalg.norm(i - img)
                #     s = ssim(i.reshape(50, 50), img[0].reshape(50, 50))
                #     if s > tot:
                #         tot = s
                #         new = i


                # TODO: images suck
                # err = np.argmin([compare_mse(img[0], i) for i in self.xt])
                # new = self.xt[err]
                # test = self.clf.predict(new.reshape(1, -1))
                # print(err)
                test = self.clf.predict(img)
                for i in test:
                    # print(chr(np.argmax(i) + ord('A')))
                    newLetter = i
                    self.letter += i

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
        self.say(self.letter)


###########
def main():
    app = QApplication(sys.argv)
    start = mainWindow()

    ### This pops up a weird extra window. Avoid because life is hard
    ##start.show()

    sys.exit(app.exec_())


###########################
if (__name__ == "__main__"):
    main()
