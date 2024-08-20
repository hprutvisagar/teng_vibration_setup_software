# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGraphicsView,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1920, 1080)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        self.con_box = QGroupBox(Widget)
        self.con_box.setObjectName(u"con_box")
        self.con_box.setGeometry(QRect(30, 20, 541, 451))
        self.widget = QWidget(self.con_box)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(21, 41, 491, 381))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.identify_res_button = QPushButton(self.widget)
        self.identify_res_button.setObjectName(u"identify_res_button")

        self.verticalLayout.addWidget(self.identify_res_button)

        self.connected_devices_table = QTableWidget(self.widget)
        self.connected_devices_table.setObjectName(u"connected_devices_table")

        self.verticalLayout.addWidget(self.connected_devices_table)

        self.config_box = QGroupBox(Widget)
        self.config_box.setObjectName(u"config_box")
        self.config_box.setGeometry(QRect(630, 20, 1241, 451))
        self.fun_config_box = QGroupBox(self.config_box)
        self.fun_config_box.setObjectName(u"fun_config_box")
        self.fun_config_box.setGeometry(QRect(60, 30, 1091, 121))
        self.fun_save_button = QPushButton(self.fun_config_box)
        self.fun_save_button.setObjectName(u"fun_save_button")
        self.fun_save_button.setGeometry(QRect(519, 64, 75, 24))
        self.pushButton_2 = QPushButton(self.fun_config_box)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(600, 64, 75, 24))
        self.widget1 = QWidget(self.fun_config_box)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(518, 31, 259, 24))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.vpp_label = QLabel(self.widget1)
        self.vpp_label.setObjectName(u"vpp_label")

        self.horizontalLayout.addWidget(self.vpp_label)

        self.vpp_input = QLineEdit(self.widget1)
        self.vpp_input.setObjectName(u"vpp_input")
        self.vpp_input.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)

        self.horizontalLayout.addWidget(self.vpp_input)

        self.widget2 = QWidget(self.fun_config_box)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(22, 31, 210, 24))
        self.horizontalLayout_2 = QHBoxLayout(self.widget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.waveform_type_label = QLabel(self.widget2)
        self.waveform_type_label.setObjectName(u"waveform_type_label")

        self.horizontalLayout_2.addWidget(self.waveform_type_label)

        self.waveform_input = QComboBox(self.widget2)
        self.waveform_input.addItem("")
        self.waveform_input.addItem("")
        self.waveform_input.addItem("")
        self.waveform_input.setObjectName(u"waveform_input")
        self.waveform_input.setEditable(False)

        self.horizontalLayout_2.addWidget(self.waveform_input)

        self.widget3 = QWidget(self.fun_config_box)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(22, 68, 196, 24))
        self.horizontalLayout_3 = QHBoxLayout(self.widget3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.freq_input_label = QLabel(self.widget3)
        self.freq_input_label.setObjectName(u"freq_input_label")

        self.horizontalLayout_3.addWidget(self.freq_input_label)

        self.freq_input = QLineEdit(self.widget3)
        self.freq_input.setObjectName(u"freq_input")

        self.horizontalLayout_3.addWidget(self.freq_input)

        self.scope_config_box = QGroupBox(self.config_box)
        self.scope_config_box.setObjectName(u"scope_config_box")
        self.scope_config_box.setGeometry(QRect(60, 160, 1091, 151))
        self.scope_save_button = QPushButton(self.scope_config_box)
        self.scope_save_button.setObjectName(u"scope_save_button")
        self.scope_save_button.setGeometry(QRect(531, 98, 75, 24))
        self.widget4 = QWidget(self.scope_config_box)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setGeometry(QRect(19, 34, 168, 24))
        self.horizontalLayout_4 = QHBoxLayout(self.widget4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scope_xmin_label = QLabel(self.widget4)
        self.scope_xmin_label.setObjectName(u"scope_xmin_label")

        self.horizontalLayout_4.addWidget(self.scope_xmin_label)

        self.scope_xmin_input = QLineEdit(self.widget4)
        self.scope_xmin_input.setObjectName(u"scope_xmin_input")

        self.horizontalLayout_4.addWidget(self.scope_xmin_input)

        self.widget5 = QWidget(self.scope_config_box)
        self.widget5.setObjectName(u"widget5")
        self.widget5.setGeometry(QRect(19, 66, 177, 24))
        self.horizontalLayout_5 = QHBoxLayout(self.widget5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scope_yrange_label = QLabel(self.widget5)
        self.scope_yrange_label.setObjectName(u"scope_yrange_label")

        self.horizontalLayout_5.addWidget(self.scope_yrange_label)

        self.scope_yrange_input = QLineEdit(self.widget5)
        self.scope_yrange_input.setObjectName(u"scope_yrange_input")

        self.horizontalLayout_5.addWidget(self.scope_yrange_input)

        self.widget6 = QWidget(self.scope_config_box)
        self.widget6.setObjectName(u"widget6")
        self.widget6.setGeometry(QRect(531, 34, 170, 24))
        self.horizontalLayout_6 = QHBoxLayout(self.widget6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scope_xmax_label = QLabel(self.widget6)
        self.scope_xmax_label.setObjectName(u"scope_xmax_label")

        self.horizontalLayout_6.addWidget(self.scope_xmax_label)

        self.scope_xmax_input = QLineEdit(self.widget6)
        self.scope_xmax_input.setObjectName(u"scope_xmax_input")

        self.horizontalLayout_6.addWidget(self.scope_xmax_input)

        self.widget7 = QWidget(self.scope_config_box)
        self.widget7.setObjectName(u"widget7")
        self.widget7.setGeometry(QRect(531, 66, 208, 24))
        self.horizontalLayout_7 = QHBoxLayout(self.widget7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.scope_trigger_label = QLabel(self.widget7)
        self.scope_trigger_label.setObjectName(u"scope_trigger_label")

        self.horizontalLayout_7.addWidget(self.scope_trigger_label)

        self.scope_trigger_input = QLineEdit(self.widget7)
        self.scope_trigger_input.setObjectName(u"scope_trigger_input")

        self.horizontalLayout_7.addWidget(self.scope_trigger_input)

        self.accel_config_box = QGroupBox(self.config_box)
        self.accel_config_box.setObjectName(u"accel_config_box")
        self.accel_config_box.setGeometry(QRect(60, 350, 1091, 71))
        self.widget8 = QWidget(self.accel_config_box)
        self.widget8.setObjectName(u"widget8")
        self.widget8.setGeometry(QRect(20, 20, 281, 41))
        self.horizontalLayout_8 = QHBoxLayout(self.widget8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.accel_com_label = QLabel(self.widget8)
        self.accel_com_label.setObjectName(u"accel_com_label")

        self.horizontalLayout_8.addWidget(self.accel_com_label)

        self.accel_com_input = QLineEdit(self.widget8)
        self.accel_com_input.setObjectName(u"accel_com_input")

        self.horizontalLayout_8.addWidget(self.accel_com_input)

        self.widget9 = QWidget(self.accel_config_box)
        self.widget9.setObjectName(u"widget9")
        self.widget9.setGeometry(QRect(530, 20, 221, 41))
        self.horizontalLayout_9 = QHBoxLayout(self.widget9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget9)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_9.addWidget(self.pushButton)

        self.accel_com_status_label = QLabel(self.widget9)
        self.accel_com_status_label.setObjectName(u"accel_com_status_label")

        self.horizontalLayout_9.addWidget(self.accel_com_status_label)

        self.scope_box = QGroupBox(Widget)
        self.scope_box.setObjectName(u"scope_box")
        self.scope_box.setGeometry(QRect(630, 500, 1241, 421))
        self.widget10 = QWidget(self.scope_box)
        self.widget10.setObjectName(u"widget10")
        self.widget10.setGeometry(QRect(61, 31, 1091, 361))
        self.gridLayout = QGridLayout(self.widget10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.scope_channel3 = QCheckBox(self.widget10)
        self.scope_channel3.setObjectName(u"scope_channel3")

        self.gridLayout.addWidget(self.scope_channel3, 0, 2, 1, 1)

        self.scope_channel2 = QCheckBox(self.widget10)
        self.scope_channel2.setObjectName(u"scope_channel2")

        self.gridLayout.addWidget(self.scope_channel2, 0, 1, 1, 1)

        self.graphicsView = QGraphicsView(self.widget10)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 4)

        self.scope_channel1 = QCheckBox(self.widget10)
        self.scope_channel1.setObjectName(u"scope_channel1")

        self.gridLayout.addWidget(self.scope_channel1, 0, 0, 1, 1)

        self.scope_channel4 = QCheckBox(self.widget10)
        self.scope_channel4.setObjectName(u"scope_channel4")

        self.gridLayout.addWidget(self.scope_channel4, 0, 3, 1, 1)

        self.scope__fetch = QPushButton(self.widget10)
        self.scope__fetch.setObjectName(u"scope__fetch")

        self.gridLayout.addWidget(self.scope__fetch, 2, 0, 1, 2)

        self.scope_save_waveform_data = QPushButton(self.widget10)
        self.scope_save_waveform_data.setObjectName(u"scope_save_waveform_data")

        self.gridLayout.addWidget(self.scope_save_waveform_data, 2, 2, 1, 2)

        self.accel_box = QGroupBox(Widget)
        self.accel_box.setObjectName(u"accel_box")
        self.accel_box.setGeometry(QRect(30, 500, 541, 426))
        self.accel_graph = QGraphicsView(self.accel_box)
        self.accel_graph.setObjectName(u"accel_graph")
        self.accel_graph.setGeometry(QRect(20, 26, 491, 192))
        self.accel_fft = QGraphicsView(self.accel_box)
        self.accel_fft.setObjectName(u"accel_fft")
        self.accel_fft.setGeometry(QRect(20, 245, 491, 161))

        self.retranslateUi(Widget)

        self.waveform_input.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.con_box.setTitle(QCoreApplication.translate("Widget", u"Connected devices", None))
        self.identify_res_button.setText(QCoreApplication.translate("Widget", u"Identify connected devices", None))
        self.config_box.setTitle(QCoreApplication.translate("Widget", u"Configurations", None))
        self.fun_config_box.setTitle(QCoreApplication.translate("Widget", u"Function Generator", None))
        self.fun_save_button.setText(QCoreApplication.translate("Widget", u"save", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"Generate", None))
        self.vpp_label.setText(QCoreApplication.translate("Widget", u"Voltage(peak-to-peak)", None))
        self.waveform_type_label.setText(QCoreApplication.translate("Widget", u"Waveform", None))
        self.waveform_input.setItemText(0, QCoreApplication.translate("Widget", u"Sine", None))
        self.waveform_input.setItemText(1, QCoreApplication.translate("Widget", u"Triangular", None))
        self.waveform_input.setItemText(2, QCoreApplication.translate("Widget", u"Square", None))

        self.waveform_input.setCurrentText("")
        self.waveform_input.setPlaceholderText(QCoreApplication.translate("Widget", u"Please select waveform", None))
        self.freq_input_label.setText(QCoreApplication.translate("Widget", u"Frequency", None))
        self.scope_config_box.setTitle(QCoreApplication.translate("Widget", u"Oscilloscope", None))
        self.scope_save_button.setText(QCoreApplication.translate("Widget", u"Save", None))
        self.scope_xmin_label.setText(QCoreApplication.translate("Widget", u"xmin", None))
        self.scope_yrange_label.setText(QCoreApplication.translate("Widget", u"yrange", None))
        self.scope_xmax_label.setText(QCoreApplication.translate("Widget", u"xmax", None))
        self.scope_trigger_label.setText(QCoreApplication.translate("Widget", u"Trigger value", None))
        self.accel_config_box.setTitle(QCoreApplication.translate("Widget", u"Accelerometer", None))
        self.accel_com_label.setText(QCoreApplication.translate("Widget", u"COM", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Check status", None))
        self.accel_com_status_label.setText(QCoreApplication.translate("Widget", u"Available!", None))
        self.scope_box.setTitle(QCoreApplication.translate("Widget", u"Oscilloscope data", None))
        self.scope_channel3.setText(QCoreApplication.translate("Widget", u"Channel 3", None))
        self.scope_channel2.setText(QCoreApplication.translate("Widget", u"Channel 2", None))
        self.scope_channel1.setText(QCoreApplication.translate("Widget", u"Channel 1", None))
        self.scope_channel4.setText(QCoreApplication.translate("Widget", u"Channel 4", None))
        self.scope__fetch.setText(QCoreApplication.translate("Widget", u"Fetch", None))
        self.scope_save_waveform_data.setText(QCoreApplication.translate("Widget", u"Save waveform", None))
        self.accel_box.setTitle(QCoreApplication.translate("Widget", u"Accelerometer data", None))
    # retranslateUi

