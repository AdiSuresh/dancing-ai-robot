# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Home_Screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from importlib.resources import path
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import os
import Copy_File
import Compare_Dance

class Home_Screen(QWidget):
    def upload_video(self):
        # exec(open("Copy_File.py").read())
        # os.system('python Copy_File.py')
        # runpy.run_path(path_name='Copy_File.py')

        # let's just run the function instead
        # Copy_File.App()
        os.system('python Catch_Pose.py')

    
    def record_dance(self):
        # Call capture_pose
		
        # Capture_Pose.App()
        os.system('python Capture_Pose.py')

        # os.system('python pose_est\pose_est\capture_pose.py')
        # runpy.run_path(path_name='pose_est\pose_est\main.py')

        # capture_pose.App()
		

    def compare_dance(self):
        Compare_Dance.App()
        # os.system('python Compare_Dance.py')

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Dance Evaluator')

        # To set up the logo
        logo = QIcon()
        logo.addPixmap(QPixmap('assets/logo.png'), QIcon.Selected, QIcon.On)
        self.setWindowIcon(logo)

        layout = QGridLayout()

        Image_Label = QLabel()
        pixmap = QPixmap('assets/Dance.jpg')
        Image_Label.setPixmap(pixmap)
        Image_Label.resize(pixmap.width(), pixmap.height())

        layout.addWidget(Image_Label, 0, 0, 1, 3)

        Upload_video = QPushButton('Upload Video File to Estimate')
        # Upload Video File to Estimate
        Upload_video.clicked.connect(self.upload_video)
        layout.addWidget(Upload_video, 1, 0)
        
        Record_Dance = QPushButton('Record your Dance Moves to Score')
        # Record your Dance Moves to Score
        Record_Dance.clicked.connect(self.record_dance)
        layout.addWidget(Record_Dance, 1, 1)
        

        Compare_Dance = QPushButton('Comparing Dance Moves')
        # Comparing Dance Moves
        Compare_Dance.clicked.connect(self.compare_dance)
        layout.addWidget(Compare_Dance, 1 , 2)

        self.setLayout(layout)
        
        # To fix the width and height
        self.setMaximumSize(self.width(), self.height())

        self.show()



if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = Home_Screen()
    sys.exit(app.exec_())