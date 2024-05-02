# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QLabel
from PySide6.QtCore import Slot, Signal, QRect
import PySide6.QtCore as QtCore
from PySide6.QtGui import QPixmap
from food_recognition.recognition import FoodRecognition

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget



class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)


        self.ui.eval_button.connect( QtCore.SIGNAL("clicked()"), lambda: self.EvalButton(self.path))
        self.ui.browse_btn.connect( QtCore.SIGNAL("clicked()"), self.Browse)


        self.ui.result_btn.setText("here will be result")

        self.model = FoodRecognition()

        

    def EvalButton(self, path):
        
        self.ui.image.setPixmap(QPixmap(path[0].path()))
        result = self.model.eval(path[0].path())
        self.ui.result_btn.setText(result[0])


    def Browse(self):
        self.path = QFileDialog.getOpenFileUrl(self, "Open file")
        # print(self.path)


