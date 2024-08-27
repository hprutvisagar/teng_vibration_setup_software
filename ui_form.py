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
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_main_widget(object):
    def setupUi(self, main_widget):
        if not main_widget.objectName():
            main_widget.setObjectName(u"main_widget")
        main_widget.setWindowModality(Qt.WindowModality.WindowModal)
        main_widget.setEnabled(True)
        main_widget.resize(1400, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_widget.sizePolicy().hasHeightForWidth())
        main_widget.setSizePolicy(sizePolicy)
        self.information_box = QGroupBox(main_widget)
        self.information_box.setObjectName(u"information_box")
        self.information_box.setGeometry(QRect(20, 720, 541, 71))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.information_box.sizePolicy().hasHeightForWidth())
        self.information_box.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(12)
        self.information_box.setFont(font)
        self.information_box.setStyleSheet(u"background-color: rgb(197, 197, 197);")
        self.information_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget = QWidget(self.information_box)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 541, 71))
        self.gridLayout_6 = QGridLayout(self.widget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.project_name = QLabel(self.widget)
        self.project_name.setObjectName(u"project_name")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.project_name.setFont(font1)
        self.project_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.project_name, 0, 0, 1, 1)

        self.author = QLabel(self.widget)
        self.author.setObjectName(u"author")
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.author.setFont(font2)
        self.author.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_6.addWidget(self.author, 1, 0, 1, 1)

        self.gridLayout_6.setRowStretch(0, 3)
        self.gridLayout_6.setRowStretch(1, 2)
        self.config_box = QGroupBox(main_widget)
        self.config_box.setObjectName(u"config_box")
        self.config_box.setGeometry(QRect(21, 205, 539, 511))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.config_box.sizePolicy().hasHeightForWidth())
        self.config_box.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.config_box.setFont(font3)
        self.accel_config_box = QGroupBox(self.config_box)
        self.accel_config_box.setObjectName(u"accel_config_box")
        self.accel_config_box.setGeometry(QRect(10, 372, 521, 131))
        font4 = QFont()
        font4.setFamilies([u"Times New Roman"])
        font4.setPointSize(10)
        font4.setBold(False)
        self.accel_config_box.setFont(font4)
        self.layoutWidget = QWidget(self.accel_config_box)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 25, 501, 91))
        self.gridLayout_3 = QGridLayout(self.layoutWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.accel_com_label = QLabel(self.layoutWidget)
        self.accel_com_label.setObjectName(u"accel_com_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.accel_com_label.sizePolicy().hasHeightForWidth())
        self.accel_com_label.setSizePolicy(sizePolicy3)
        self.accel_com_label.setFont(font4)

        self.horizontalLayout_9.addWidget(self.accel_com_label)

        self.accel_config_com_input = QLineEdit(self.layoutWidget)
        self.accel_config_com_input.setObjectName(u"accel_config_com_input")
        sizePolicy.setHeightForWidth(self.accel_config_com_input.sizePolicy().hasHeightForWidth())
        self.accel_config_com_input.setSizePolicy(sizePolicy)
        font5 = QFont()
        font5.setFamilies([u"Times New Roman"])
        font5.setPointSize(14)
        font5.setBold(False)
        self.accel_config_com_input.setFont(font5)

        self.horizontalLayout_9.addWidget(self.accel_config_com_input)


        self.gridLayout_3.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.com_baud_rate_label = QLabel(self.layoutWidget)
        self.com_baud_rate_label.setObjectName(u"com_baud_rate_label")
        sizePolicy3.setHeightForWidth(self.com_baud_rate_label.sizePolicy().hasHeightForWidth())
        self.com_baud_rate_label.setSizePolicy(sizePolicy3)

        self.horizontalLayout_10.addWidget(self.com_baud_rate_label)

        self.com_baud_rate_input = QComboBox(self.layoutWidget)
        self.com_baud_rate_input.addItem("")
        self.com_baud_rate_input.addItem("")
        self.com_baud_rate_input.addItem("")
        self.com_baud_rate_input.addItem("")
        self.com_baud_rate_input.addItem("")
        self.com_baud_rate_input.addItem("")
        self.com_baud_rate_input.setObjectName(u"com_baud_rate_input")
        sizePolicy3.setHeightForWidth(self.com_baud_rate_input.sizePolicy().hasHeightForWidth())
        self.com_baud_rate_input.setSizePolicy(sizePolicy3)

        self.horizontalLayout_10.addWidget(self.com_baud_rate_input)


        self.gridLayout_3.addLayout(self.horizontalLayout_10, 0, 1, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.accel_status_check_button = QPushButton(self.layoutWidget)
        self.accel_status_check_button.setObjectName(u"accel_status_check_button")
        sizePolicy2.setHeightForWidth(self.accel_status_check_button.sizePolicy().hasHeightForWidth())
        self.accel_status_check_button.setSizePolicy(sizePolicy2)
        self.accel_status_check_button.setFont(font4)

        self.horizontalLayout_11.addWidget(self.accel_status_check_button)

        self.accel_com_status_label = QLabel(self.layoutWidget)
        self.accel_com_status_label.setObjectName(u"accel_com_status_label")
        sizePolicy.setHeightForWidth(self.accel_com_status_label.sizePolicy().hasHeightForWidth())
        self.accel_com_status_label.setSizePolicy(sizePolicy)
        self.accel_com_status_label.setFont(font4)

        self.horizontalLayout_11.addWidget(self.accel_com_status_label)


        self.gridLayout_3.addLayout(self.horizontalLayout_11, 1, 0, 1, 2)

        self.accel_config_save_button = QPushButton(self.layoutWidget)
        self.accel_config_save_button.setObjectName(u"accel_config_save_button")
        sizePolicy2.setHeightForWidth(self.accel_config_save_button.sizePolicy().hasHeightForWidth())
        self.accel_config_save_button.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.accel_config_save_button, 2, 0, 1, 2)

        self.scope_config_box = QGroupBox(self.config_box)
        self.scope_config_box.setObjectName(u"scope_config_box")
        self.scope_config_box.setGeometry(QRect(10, 197, 521, 171))
        self.scope_config_box.setFont(font4)
        self.layoutWidget1 = QWidget(self.scope_config_box)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(12, 25, 501, 131))
        self.gridLayout_2 = QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.scope_xrange_label = QLabel(self.layoutWidget1)
        self.scope_xrange_label.setObjectName(u"scope_xrange_label")
        sizePolicy.setHeightForWidth(self.scope_xrange_label.sizePolicy().hasHeightForWidth())
        self.scope_xrange_label.setSizePolicy(sizePolicy)
        self.scope_xrange_label.setFont(font4)

        self.horizontalLayout_6.addWidget(self.scope_xrange_label)

        self.scope_config_xrange_input = QLineEdit(self.layoutWidget1)
        self.scope_config_xrange_input.setObjectName(u"scope_config_xrange_input")
        sizePolicy.setHeightForWidth(self.scope_config_xrange_input.sizePolicy().hasHeightForWidth())
        self.scope_config_xrange_input.setSizePolicy(sizePolicy)
        self.scope_config_xrange_input.setFont(font4)

        self.horizontalLayout_6.addWidget(self.scope_config_xrange_input)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.scope_yrange_label = QLabel(self.layoutWidget1)
        self.scope_yrange_label.setObjectName(u"scope_yrange_label")
        sizePolicy.setHeightForWidth(self.scope_yrange_label.sizePolicy().hasHeightForWidth())
        self.scope_yrange_label.setSizePolicy(sizePolicy)
        self.scope_yrange_label.setFont(font4)

        self.horizontalLayout_7.addWidget(self.scope_yrange_label)

        self.scope_config_yrange_input = QLineEdit(self.layoutWidget1)
        self.scope_config_yrange_input.setObjectName(u"scope_config_yrange_input")
        sizePolicy.setHeightForWidth(self.scope_config_yrange_input.sizePolicy().hasHeightForWidth())
        self.scope_config_yrange_input.setSizePolicy(sizePolicy)
        self.scope_config_yrange_input.setFont(font4)

        self.horizontalLayout_7.addWidget(self.scope_config_yrange_input)


        self.gridLayout_2.addLayout(self.horizontalLayout_7, 1, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.scope_id_label = QLabel(self.layoutWidget1)
        self.scope_id_label.setObjectName(u"scope_id_label")
        sizePolicy3.setHeightForWidth(self.scope_id_label.sizePolicy().hasHeightForWidth())
        self.scope_id_label.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.scope_id_label)

        self.scope_config_id_input = QLineEdit(self.layoutWidget1)
        self.scope_config_id_input.setObjectName(u"scope_config_id_input")
        sizePolicy.setHeightForWidth(self.scope_config_id_input.sizePolicy().hasHeightForWidth())
        self.scope_config_id_input.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.scope_config_id_input)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.scope_trigger_label = QLabel(self.layoutWidget1)
        self.scope_trigger_label.setObjectName(u"scope_trigger_label")
        sizePolicy3.setHeightForWidth(self.scope_trigger_label.sizePolicy().hasHeightForWidth())
        self.scope_trigger_label.setSizePolicy(sizePolicy3)
        self.scope_trigger_label.setFont(font4)

        self.horizontalLayout_8.addWidget(self.scope_trigger_label)

        self.scope_config_trigger_input = QLineEdit(self.layoutWidget1)
        self.scope_config_trigger_input.setObjectName(u"scope_config_trigger_input")
        sizePolicy.setHeightForWidth(self.scope_config_trigger_input.sizePolicy().hasHeightForWidth())
        self.scope_config_trigger_input.setSizePolicy(sizePolicy)
        self.scope_config_trigger_input.setFont(font4)

        self.horizontalLayout_8.addWidget(self.scope_config_trigger_input)


        self.gridLayout_2.addLayout(self.horizontalLayout_8, 2, 0, 1, 2)

        self.scope_config_save_button = QPushButton(self.layoutWidget1)
        self.scope_config_save_button.setObjectName(u"scope_config_save_button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.scope_config_save_button.sizePolicy().hasHeightForWidth())
        self.scope_config_save_button.setSizePolicy(sizePolicy4)
        self.scope_config_save_button.setFont(font4)

        self.gridLayout_2.addWidget(self.scope_config_save_button, 3, 0, 1, 2)

        self.fun_config_box = QGroupBox(self.config_box)
        self.fun_config_box.setObjectName(u"fun_config_box")
        self.fun_config_box.setGeometry(QRect(10, 21, 521, 171))
        sizePolicy3.setHeightForWidth(self.fun_config_box.sizePolicy().hasHeightForWidth())
        self.fun_config_box.setSizePolicy(sizePolicy3)
        self.fun_config_box.setFont(font4)
        self.layoutWidget2 = QWidget(self.fun_config_box)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(14, 22, 501, 131))
        self.gridLayout = QGridLayout(self.layoutWidget2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fun_id_label = QLabel(self.layoutWidget2)
        self.fun_id_label.setObjectName(u"fun_id_label")

        self.horizontalLayout.addWidget(self.fun_id_label)

        self.fun_id_input = QLineEdit(self.layoutWidget2)
        self.fun_id_input.setObjectName(u"fun_id_input")
        sizePolicy.setHeightForWidth(self.fun_id_input.sizePolicy().hasHeightForWidth())
        self.fun_id_input.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.fun_id_input)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.waveform_type_label = QLabel(self.layoutWidget2)
        self.waveform_type_label.setObjectName(u"waveform_type_label")
        sizePolicy3.setHeightForWidth(self.waveform_type_label.sizePolicy().hasHeightForWidth())
        self.waveform_type_label.setSizePolicy(sizePolicy3)
        self.waveform_type_label.setFont(font4)

        self.horizontalLayout_2.addWidget(self.waveform_type_label)

        self.fun_config_waveform_input = QComboBox(self.layoutWidget2)
        self.fun_config_waveform_input.addItem("")
        self.fun_config_waveform_input.addItem("")
        self.fun_config_waveform_input.addItem("")
        self.fun_config_waveform_input.setObjectName(u"fun_config_waveform_input")
        sizePolicy.setHeightForWidth(self.fun_config_waveform_input.sizePolicy().hasHeightForWidth())
        self.fun_config_waveform_input.setSizePolicy(sizePolicy)
        self.fun_config_waveform_input.setFont(font4)
        self.fun_config_waveform_input.setEditable(False)

        self.horizontalLayout_2.addWidget(self.fun_config_waveform_input)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.freq_input_label = QLabel(self.layoutWidget2)
        self.freq_input_label.setObjectName(u"freq_input_label")
        sizePolicy.setHeightForWidth(self.freq_input_label.sizePolicy().hasHeightForWidth())
        self.freq_input_label.setSizePolicy(sizePolicy)
        self.freq_input_label.setFont(font4)

        self.horizontalLayout_3.addWidget(self.freq_input_label)

        self.fun_config_freq_input = QLineEdit(self.layoutWidget2)
        self.fun_config_freq_input.setObjectName(u"fun_config_freq_input")
        sizePolicy.setHeightForWidth(self.fun_config_freq_input.sizePolicy().hasHeightForWidth())
        self.fun_config_freq_input.setSizePolicy(sizePolicy)
        self.fun_config_freq_input.setFont(font4)

        self.horizontalLayout_3.addWidget(self.fun_config_freq_input)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.vpp_label = QLabel(self.layoutWidget2)
        self.vpp_label.setObjectName(u"vpp_label")
        sizePolicy.setHeightForWidth(self.vpp_label.sizePolicy().hasHeightForWidth())
        self.vpp_label.setSizePolicy(sizePolicy)
        self.vpp_label.setFont(font4)

        self.horizontalLayout_4.addWidget(self.vpp_label)

        self.fun_config_vpp_input = QLineEdit(self.layoutWidget2)
        self.fun_config_vpp_input.setObjectName(u"fun_config_vpp_input")
        sizePolicy.setHeightForWidth(self.fun_config_vpp_input.sizePolicy().hasHeightForWidth())
        self.fun_config_vpp_input.setSizePolicy(sizePolicy)
        self.fun_config_vpp_input.setFont(font4)
        self.fun_config_vpp_input.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)

        self.horizontalLayout_4.addWidget(self.fun_config_vpp_input)


        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 2)

        self.fun_save_button = QPushButton(self.layoutWidget2)
        self.fun_save_button.setObjectName(u"fun_save_button")
        sizePolicy2.setHeightForWidth(self.fun_save_button.sizePolicy().hasHeightForWidth())
        self.fun_save_button.setSizePolicy(sizePolicy2)
        self.fun_save_button.setFont(font4)

        self.gridLayout.addWidget(self.fun_save_button, 3, 0, 1, 2)

        self.fun_config_send_button = QPushButton(self.layoutWidget2)
        self.fun_config_send_button.setObjectName(u"fun_config_send_button")
        sizePolicy2.setHeightForWidth(self.fun_config_send_button.sizePolicy().hasHeightForWidth())
        self.fun_config_send_button.setSizePolicy(sizePolicy2)
        self.fun_config_send_button.setFont(font4)

        self.gridLayout.addWidget(self.fun_config_send_button, 3, 2, 1, 1)

        self.con_box = QGroupBox(main_widget)
        self.con_box.setObjectName(u"con_box")
        self.con_box.setGeometry(QRect(21, 11, 539, 191))
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.con_box.sizePolicy().hasHeightForWidth())
        self.con_box.setSizePolicy(sizePolicy5)
        self.con_box.setMinimumSize(QSize(0, 30))
        self.con_box.setFont(font3)
        self.layoutWidget3 = QWidget(self.con_box)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(11, 18, 521, 161))
        self.verticalLayout = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.identify_res_button = QPushButton(self.layoutWidget3)
        self.identify_res_button.setObjectName(u"identify_res_button")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.identify_res_button.sizePolicy().hasHeightForWidth())
        self.identify_res_button.setSizePolicy(sizePolicy6)
        self.identify_res_button.setFont(font4)

        self.verticalLayout.addWidget(self.identify_res_button)

        self.connected_devices_table = QTableWidget(self.layoutWidget3)
        self.connected_devices_table.setObjectName(u"connected_devices_table")
        sizePolicy.setHeightForWidth(self.connected_devices_table.sizePolicy().hasHeightForWidth())
        self.connected_devices_table.setSizePolicy(sizePolicy)
        self.connected_devices_table.setMinimumSize(QSize(0, 20))
        self.connected_devices_table.setFont(font4)

        self.verticalLayout.addWidget(self.connected_devices_table)

        self.scope_box = QGroupBox(main_widget)
        self.scope_box.setObjectName(u"scope_box")
        self.scope_box.setGeometry(QRect(570, 10, 821, 391))
        sizePolicy.setHeightForWidth(self.scope_box.sizePolicy().hasHeightForWidth())
        self.scope_box.setSizePolicy(sizePolicy)
        self.scope_box.setFont(font3)
        self.scope_box.setFlat(False)
        self.scope_box.setCheckable(False)
        self.layoutWidget4 = QWidget(self.scope_box)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(10, 30, 801, 341))
        self.gridLayout_4 = QGridLayout(self.layoutWidget4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scope_channel1 = QCheckBox(self.layoutWidget4)
        self.scope_channel1.setObjectName(u"scope_channel1")
        sizePolicy2.setHeightForWidth(self.scope_channel1.sizePolicy().hasHeightForWidth())
        self.scope_channel1.setSizePolicy(sizePolicy2)
        self.scope_channel1.setFont(font4)

        self.gridLayout_4.addWidget(self.scope_channel1, 0, 0, 1, 1)

        self.scope_channel2 = QCheckBox(self.layoutWidget4)
        self.scope_channel2.setObjectName(u"scope_channel2")
        sizePolicy2.setHeightForWidth(self.scope_channel2.sizePolicy().hasHeightForWidth())
        self.scope_channel2.setSizePolicy(sizePolicy2)
        self.scope_channel2.setFont(font4)

        self.gridLayout_4.addWidget(self.scope_channel2, 0, 1, 1, 1)

        self.scope_channel3 = QCheckBox(self.layoutWidget4)
        self.scope_channel3.setObjectName(u"scope_channel3")
        sizePolicy2.setHeightForWidth(self.scope_channel3.sizePolicy().hasHeightForWidth())
        self.scope_channel3.setSizePolicy(sizePolicy2)
        self.scope_channel3.setFont(font4)

        self.gridLayout_4.addWidget(self.scope_channel3, 0, 2, 1, 1)

        self.scope_channel4 = QCheckBox(self.layoutWidget4)
        self.scope_channel4.setObjectName(u"scope_channel4")
        sizePolicy2.setHeightForWidth(self.scope_channel4.sizePolicy().hasHeightForWidth())
        self.scope_channel4.setSizePolicy(sizePolicy2)
        self.scope_channel4.setFont(font4)

        self.gridLayout_4.addWidget(self.scope_channel4, 0, 3, 1, 1)

        self.scope_fetch_button = QPushButton(self.layoutWidget4)
        self.scope_fetch_button.setObjectName(u"scope_fetch_button")
        sizePolicy2.setHeightForWidth(self.scope_fetch_button.sizePolicy().hasHeightForWidth())
        self.scope_fetch_button.setSizePolicy(sizePolicy2)
        self.scope_fetch_button.setFont(font4)

        self.gridLayout_4.addWidget(self.scope_fetch_button, 2, 0, 1, 2)

        self.scope_data_save_button = QPushButton(self.layoutWidget4)
        self.scope_data_save_button.setObjectName(u"scope_data_save_button")
        sizePolicy2.setHeightForWidth(self.scope_data_save_button.sizePolicy().hasHeightForWidth())
        self.scope_data_save_button.setSizePolicy(sizePolicy2)
        self.scope_data_save_button.setFont(font4)

        self.gridLayout_4.addWidget(self.scope_data_save_button, 2, 2, 1, 2)

        self.scope_graphics_view = QGraphicsView(self.layoutWidget4)
        self.scope_graphics_view.setObjectName(u"scope_graphics_view")
        sizePolicy.setHeightForWidth(self.scope_graphics_view.sizePolicy().hasHeightForWidth())
        self.scope_graphics_view.setSizePolicy(sizePolicy)
        self.scope_graphics_view.setFont(font5)

        self.gridLayout_4.addWidget(self.scope_graphics_view, 1, 0, 1, 4)

        self.accel_box = QGroupBox(main_widget)
        self.accel_box.setObjectName(u"accel_box")
        self.accel_box.setGeometry(QRect(570, 410, 821, 271))
        sizePolicy.setHeightForWidth(self.accel_box.sizePolicy().hasHeightForWidth())
        self.accel_box.setSizePolicy(sizePolicy)
        self.accel_box.setFont(font3)
        self.widget1 = QWidget(self.accel_box)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 30, 801, 231))
        self.gridLayout_5 = QGridLayout(self.widget1)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.accel_graph = QGraphicsView(self.widget1)
        self.accel_graph.setObjectName(u"accel_graph")
        font6 = QFont()
        font6.setFamilies([u"Times New Roman"])
        font6.setPointSize(14)
        font6.setBold(True)
        self.accel_graph.setFont(font6)

        self.gridLayout_5.addWidget(self.accel_graph, 0, 0, 1, 3)

        self.accel_fft = QGraphicsView(self.widget1)
        self.accel_fft.setObjectName(u"accel_fft")
        self.accel_fft.setFont(font6)

        self.gridLayout_5.addWidget(self.accel_fft, 1, 0, 1, 3)

        self.accel_fetch_button = QPushButton(self.widget1)
        self.accel_fetch_button.setObjectName(u"accel_fetch_button")
        sizePolicy2.setHeightForWidth(self.accel_fetch_button.sizePolicy().hasHeightForWidth())
        self.accel_fetch_button.setSizePolicy(sizePolicy2)
        self.accel_fetch_button.setFont(font4)

        self.gridLayout_5.addWidget(self.accel_fetch_button, 2, 0, 1, 1)

        self.accel_disconnect_button = QPushButton(self.widget1)
        self.accel_disconnect_button.setObjectName(u"accel_disconnect_button")
        self.accel_disconnect_button.setFont(font4)

        self.gridLayout_5.addWidget(self.accel_disconnect_button, 2, 1, 1, 1)

        self.accel_save_button = QPushButton(self.widget1)
        self.accel_save_button.setObjectName(u"accel_save_button")
        sizePolicy2.setHeightForWidth(self.accel_save_button.sizePolicy().hasHeightForWidth())
        self.accel_save_button.setSizePolicy(sizePolicy2)
        self.accel_save_button.setFont(font4)

        self.gridLayout_5.addWidget(self.accel_save_button, 2, 2, 1, 1)

        self.output = QGroupBox(main_widget)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(570, 690, 821, 101))
        sizePolicy.setHeightForWidth(self.output.sizePolicy().hasHeightForWidth())
        self.output.setSizePolicy(sizePolicy)
        self.output.setStyleSheet(u"")
        self.output_message = QTextEdit(self.output)
        self.output_message.setObjectName(u"output_message")
        self.output_message.setGeometry(QRect(10, 20, 801, 71))
        self.output_message.setStyleSheet(u"color: rgb(42, 42, 42);")
        self.output_message.setReadOnly(True)
        self.output_message.setAcceptRichText(True)

        self.retranslateUi(main_widget)

        self.fun_config_waveform_input.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(main_widget)
    # setupUi

    def retranslateUi(self, main_widget):
        main_widget.setWindowTitle(QCoreApplication.translate("main_widget", u"Frequency tunable triboelectric test and measurement setup", None))
        self.information_box.setTitle("")
        self.project_name.setText(QCoreApplication.translate("main_widget", u"Frequency tunable Triboelectric Energy Harvester", None))
        self.author.setText(QCoreApplication.translate("main_widget", u"Dr. Sagar Hosangadi Prutvi, Post Doc Researcher @ LivMatS cluster", None))
        self.config_box.setTitle(QCoreApplication.translate("main_widget", u"Configurations", None))
        self.accel_config_box.setTitle(QCoreApplication.translate("main_widget", u"Accelerometer", None))
        self.accel_com_label.setText(QCoreApplication.translate("main_widget", u"COM PORT", None))
        self.com_baud_rate_label.setText(QCoreApplication.translate("main_widget", u"BAUD RATE", None))
        self.com_baud_rate_input.setItemText(0, QCoreApplication.translate("main_widget", u"115200", None))
        self.com_baud_rate_input.setItemText(1, QCoreApplication.translate("main_widget", u"57600", None))
        self.com_baud_rate_input.setItemText(2, QCoreApplication.translate("main_widget", u"38400", None))
        self.com_baud_rate_input.setItemText(3, QCoreApplication.translate("main_widget", u"19200", None))
        self.com_baud_rate_input.setItemText(4, QCoreApplication.translate("main_widget", u"9600", None))
        self.com_baud_rate_input.setItemText(5, QCoreApplication.translate("main_widget", u"4800", None))

        self.accel_status_check_button.setText(QCoreApplication.translate("main_widget", u"CHECK STATUS", None))
        self.accel_com_status_label.setText(QCoreApplication.translate("main_widget", u"Available!", None))
        self.accel_config_save_button.setText(QCoreApplication.translate("main_widget", u"SAVE", None))
        self.scope_config_box.setTitle(QCoreApplication.translate("main_widget", u"Oscilloscope", None))
        self.scope_xrange_label.setText(QCoreApplication.translate("main_widget", u"X RANGE", None))
        self.scope_yrange_label.setText(QCoreApplication.translate("main_widget", u"Y RANGE", None))
        self.scope_id_label.setText(QCoreApplication.translate("main_widget", u"DEVICE ID", None))
        self.scope_trigger_label.setText(QCoreApplication.translate("main_widget", u"TRIGGER POS", None))
        self.scope_config_save_button.setText(QCoreApplication.translate("main_widget", u"SAVE", None))
        self.fun_config_box.setTitle(QCoreApplication.translate("main_widget", u"Function Generator", None))
        self.fun_id_label.setText(QCoreApplication.translate("main_widget", u"DEVICE ID", None))
        self.waveform_type_label.setText(QCoreApplication.translate("main_widget", u"WAVEFORM TYPE", None))
        self.fun_config_waveform_input.setItemText(0, QCoreApplication.translate("main_widget", u"Sine", None))
        self.fun_config_waveform_input.setItemText(1, QCoreApplication.translate("main_widget", u"Triangular", None))
        self.fun_config_waveform_input.setItemText(2, QCoreApplication.translate("main_widget", u"Square", None))

        self.fun_config_waveform_input.setCurrentText("")
        self.fun_config_waveform_input.setPlaceholderText(QCoreApplication.translate("main_widget", u"Please select waveform", None))
        self.freq_input_label.setText(QCoreApplication.translate("main_widget", u"FREQ", None))
        self.vpp_label.setText(QCoreApplication.translate("main_widget", u"Vpp", None))
        self.fun_save_button.setText(QCoreApplication.translate("main_widget", u"SAVE", None))
        self.fun_config_send_button.setText(QCoreApplication.translate("main_widget", u"SEND", None))
        self.con_box.setTitle(QCoreApplication.translate("main_widget", u"Connected devices", None))
        self.identify_res_button.setText(QCoreApplication.translate("main_widget", u"IDENTIFY CONNECTED DEVICE", None))
        self.scope_box.setTitle(QCoreApplication.translate("main_widget", u"Oscilloscope data", None))
        self.scope_channel1.setText(QCoreApplication.translate("main_widget", u"Channel 1", None))
        self.scope_channel2.setText(QCoreApplication.translate("main_widget", u"Channel 2", None))
        self.scope_channel3.setText(QCoreApplication.translate("main_widget", u"Channel 3", None))
        self.scope_channel4.setText(QCoreApplication.translate("main_widget", u"Channel 4", None))
        self.scope_fetch_button.setText(QCoreApplication.translate("main_widget", u"FETCH DATA", None))
        self.scope_data_save_button.setText(QCoreApplication.translate("main_widget", u"SAVE", None))
        self.accel_box.setTitle(QCoreApplication.translate("main_widget", u"Accelerometer data", None))
        self.accel_fetch_button.setText(QCoreApplication.translate("main_widget", u"CONNECT", None))
        self.accel_disconnect_button.setText(QCoreApplication.translate("main_widget", u"DISCONNECT", None))
        self.accel_save_button.setText(QCoreApplication.translate("main_widget", u"SAVE", None))
        self.output.setTitle(QCoreApplication.translate("main_widget", u"Messages", None))
        self.output_message.setHtml(QCoreApplication.translate("main_widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

