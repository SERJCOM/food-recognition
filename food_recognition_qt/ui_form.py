# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(474, 435)
        self.eval_button = QPushButton(Widget)
        self.eval_button.setObjectName(u"eval_button")
        self.eval_button.setGeometry(QRect(20, 380, 161, 26))
        self.result_btn = QLabel(Widget)
        self.result_btn.setObjectName(u"result_btn")
        self.result_btn.setGeometry(QRect(80, 340, 201, 18))
        font = QFont()
        font.setPointSize(15)
        self.result_btn.setFont(font)
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 340, 68, 18))
        self.label_2.setFont(font)
        self.browse_btn = QPushButton(Widget)
        self.browse_btn.setObjectName(u"browse_btn")
        self.browse_btn.setGeometry(QRect(230, 380, 161, 26))
        self.image = QLabel(Widget)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(30, 20, 401, 291))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.eval_button.setText(QCoreApplication.translate("Widget", u"Eval", None))
        self.result_btn.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"result:", None))
        self.browse_btn.setText(QCoreApplication.translate("Widget", u"Browse", None))
        self.image.setText("")
    # retranslateUi

