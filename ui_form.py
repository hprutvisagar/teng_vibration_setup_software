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
        main_widget.resize(1920, 1080)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_widget.sizePolicy().hasHeightForWidth())
        main_widget.setSizePolicy(sizePolicy)
        self.layoutWidget = QWidget(main_widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 10, 541, 1051))
        self.left_vertical_box = QVBoxLayout(self.layoutWidget)
        self.left_vertical_box.setObjectName(u"left_vertical_box")
        self.left_vertical_box.setContentsMargins(0, 0, 0, 0)
        self.con_box = QGroupBox(self.layoutWidget)
        self.con_box.setObjectName(u"con_box")
        sizePolicy.setHeightForWidth(self.con_box.sizePolicy().hasHeightForWidth())
        self.con_box.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        self.con_box.setFont(font)
        self.layoutWidget1 = QWidget(self.con_box)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(22, 35, 491, 301))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.identify_res_button = QPushButton(self.layoutWidget1)
        self.identify_res_button.setObjectName(u"identify_res_button")
        self.identify_res_button.setFont(font)

        self.verticalLayout_2.addWidget(self.identify_res_button)

        self.connected_devices_table = QTableWidget(self.layoutWidget1)
        self.connected_devices_table.setObjectName(u"connected_devices_table")
        self.connected_devices_table.setFont(font)

        self.verticalLayout_2.addWidget(self.connected_devices_table)


        self.left_vertical_box.addWidget(self.con_box)

        self.config_box = QGroupBox(self.layoutWidget)
        self.config_box.setObjectName(u"config_box")
        sizePolicy.setHeightForWidth(self.config_box.sizePolicy().hasHeightForWidth())
        self.config_box.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(16)
        font1.setBold(False)
        self.config_box.setFont(font1)
        self.layoutWidget2 = QWidget(self.config_box)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(19, 30, 491, 561))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 10)
        self.fun_config_box = QGroupBox(self.layoutWidget2)
        self.fun_config_box.setObjectName(u"fun_config_box")
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.fun_config_box.setFont(font2)
        self.layoutWidget3 = QWidget(self.fun_config_box)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(22, 30, 451, 151))
        self.gridLayout_3 = QGridLayout(self.layoutWidget3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.fun_id_label = QLabel(self.layoutWidget3)
        self.fun_id_label.setObjectName(u"fun_id_label")

        self.horizontalLayout_10.addWidget(self.fun_id_label)

        self.fun_id_input = QLineEdit(self.layoutWidget3)
        self.fun_id_input.setObjectName(u"fun_id_input")
        sizePolicy.setHeightForWidth(self.fun_id_input.sizePolicy().hasHeightForWidth())
        self.fun_id_input.setSizePolicy(sizePolicy)

        self.horizontalLayout_10.addWidget(self.fun_id_input)


        self.gridLayout_3.addLayout(self.horizontalLayout_10, 0, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.waveform_type_label = QLabel(self.layoutWidget3)
        self.waveform_type_label.setObjectName(u"waveform_type_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.waveform_type_label.sizePolicy().hasHeightForWidth())
        self.waveform_type_label.setSizePolicy(sizePolicy1)
        self.waveform_type_label.setFont(font2)

        self.horizontalLayout_2.addWidget(self.waveform_type_label)

        self.fun_config_waveform_input = QComboBox(self.layoutWidget3)
        self.fun_config_waveform_input.addItem("")
        self.fun_config_waveform_input.addItem("")
        self.fun_config_waveform_input.addItem("")
        self.fun_config_waveform_input.setObjectName(u"fun_config_waveform_input")
        sizePolicy.setHeightForWidth(self.fun_config_waveform_input.sizePolicy().hasHeightForWidth())
        self.fun_config_waveform_input.setSizePolicy(sizePolicy)
        self.fun_config_waveform_input.setFont(font2)
        self.fun_config_waveform_input.setEditable(False)

        self.horizontalLayout_2.addWidget(self.fun_config_waveform_input)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.freq_input_label = QLabel(self.layoutWidget3)
        self.freq_input_label.setObjectName(u"freq_input_label")
        sizePolicy.setHeightForWidth(self.freq_input_label.sizePolicy().hasHeightForWidth())
        self.freq_input_label.setSizePolicy(sizePolicy)
        self.freq_input_label.setFont(font2)

        self.horizontalLayout_3.addWidget(self.freq_input_label)

        self.fun_config_freq_input = QLineEdit(self.layoutWidget3)
        self.fun_config_freq_input.setObjectName(u"fun_config_freq_input")
        sizePolicy.setHeightForWidth(self.fun_config_freq_input.sizePolicy().hasHeightForWidth())
        self.fun_config_freq_input.setSizePolicy(sizePolicy)
        self.fun_config_freq_input.setFont(font2)

        self.horizontalLayout_3.addWidget(self.fun_config_freq_input)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.vpp_label = QLabel(self.layoutWidget3)
        self.vpp_label.setObjectName(u"vpp_label")
        sizePolicy.setHeightForWidth(self.vpp_label.sizePolicy().hasHeightForWidth())
        self.vpp_label.setSizePolicy(sizePolicy)
        self.vpp_label.setFont(font2)

        self.horizontalLayout.addWidget(self.vpp_label)

        self.fun_config_vpp_input = QLineEdit(self.layoutWidget3)
        self.fun_config_vpp_input.setObjectName(u"fun_config_vpp_input")
        sizePolicy.setHeightForWidth(self.fun_config_vpp_input.sizePolicy().hasHeightForWidth())
        self.fun_config_vpp_input.setSizePolicy(sizePolicy)
        self.fun_config_vpp_input.setFont(font1)
        self.fun_config_vpp_input.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)

        self.horizontalLayout.addWidget(self.fun_config_vpp_input)


        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 1, 1, 1)

        self.fun_save_button = QPushButton(self.layoutWidget3)
        self.fun_save_button.setObjectName(u"fun_save_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.fun_save_button.sizePolicy().hasHeightForWidth())
        self.fun_save_button.setSizePolicy(sizePolicy2)
        self.fun_save_button.setFont(font2)

        self.gridLayout_3.addWidget(self.fun_save_button, 3, 0, 1, 1)

        self.fun_config_send_button = QPushButton(self.layoutWidget3)
        self.fun_config_send_button.setObjectName(u"fun_config_send_button")
        sizePolicy2.setHeightForWidth(self.fun_config_send_button.sizePolicy().hasHeightForWidth())
        self.fun_config_send_button.setSizePolicy(sizePolicy2)
        self.fun_config_send_button.setFont(font2)

        self.gridLayout_3.addWidget(self.fun_config_send_button, 3, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.fun_config_box)

        self.scope_config_box = QGroupBox(self.layoutWidget2)
        self.scope_config_box.setObjectName(u"scope_config_box")
        self.scope_config_box.setFont(font2)
        self.layoutWidget4 = QWidget(self.scope_config_box)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(21, 32, 451, 151))
        self.gridLayout_5 = QGridLayout(self.layoutWidget4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.scope_id_label = QLabel(self.layoutWidget4)
        self.scope_id_label.setObjectName(u"scope_id_label")
        sizePolicy1.setHeightForWidth(self.scope_id_label.sizePolicy().hasHeightForWidth())
        self.scope_id_label.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.scope_id_label)

        self.scope_config_id_input = QLineEdit(self.layoutWidget4)
        self.scope_config_id_input.setObjectName(u"scope_config_id_input")
        sizePolicy.setHeightForWidth(self.scope_config_id_input.sizePolicy().hasHeightForWidth())
        self.scope_config_id_input.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.scope_config_id_input)


        self.gridLayout_5.addLayout(self.horizontalLayout_4, 0, 0, 1, 2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.scope_xrange_label = QLabel(self.layoutWidget4)
        self.scope_xrange_label.setObjectName(u"scope_xrange_label")
        sizePolicy.setHeightForWidth(self.scope_xrange_label.sizePolicy().hasHeightForWidth())
        self.scope_xrange_label.setSizePolicy(sizePolicy)
        self.scope_xrange_label.setFont(font2)

        self.horizontalLayout_5.addWidget(self.scope_xrange_label)

        self.scope_config_xrange_input = QLineEdit(self.layoutWidget4)
        self.scope_config_xrange_input.setObjectName(u"scope_config_xrange_input")
        sizePolicy.setHeightForWidth(self.scope_config_xrange_input.sizePolicy().hasHeightForWidth())
        self.scope_config_xrange_input.setSizePolicy(sizePolicy)
        self.scope_config_xrange_input.setFont(font2)

        self.horizontalLayout_5.addWidget(self.scope_config_xrange_input)


        self.gridLayout_5.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.scope_yrange_label = QLabel(self.layoutWidget4)
        self.scope_yrange_label.setObjectName(u"scope_yrange_label")
        sizePolicy.setHeightForWidth(self.scope_yrange_label.sizePolicy().hasHeightForWidth())
        self.scope_yrange_label.setSizePolicy(sizePolicy)
        self.scope_yrange_label.setFont(font2)

        self.horizontalLayout_7.addWidget(self.scope_yrange_label)

        self.scope_config_yrange_input = QLineEdit(self.layoutWidget4)
        self.scope_config_yrange_input.setObjectName(u"scope_config_yrange_input")
        sizePolicy.setHeightForWidth(self.scope_config_yrange_input.sizePolicy().hasHeightForWidth())
        self.scope_config_yrange_input.setSizePolicy(sizePolicy)
        self.scope_config_yrange_input.setFont(font2)

        self.horizontalLayout_7.addWidget(self.scope_config_yrange_input)


        self.gridLayout_5.addLayout(self.horizontalLayout_7, 1, 1, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.scope_trigger_label = QLabel(self.layoutWidget4)
        self.scope_trigger_label.setObjectName(u"scope_trigger_label")
        sizePolicy1.setHeightForWidth(self.scope_trigger_label.sizePolicy().hasHeightForWidth())
        self.scope_trigger_label.setSizePolicy(sizePolicy1)
        self.scope_trigger_label.setFont(font2)

        self.horizontalLayout_9.addWidget(self.scope_trigger_label)

        self.scope_config_trigger_input = QLineEdit(self.layoutWidget4)
        self.scope_config_trigger_input.setObjectName(u"scope_config_trigger_input")
        sizePolicy.setHeightForWidth(self.scope_config_trigger_input.sizePolicy().hasHeightForWidth())
        self.scope_config_trigger_input.setSizePolicy(sizePolicy)
        self.scope_config_trigger_input.setFont(font1)

        self.horizontalLayout_9.addWidget(self.scope_config_trigger_input)


        self.gridLayout_5.addLayout(self.horizontalLayout_9, 2, 0, 1, 2)

        self.scope_config_save_button = QPushButton(self.layoutWidget4)
        self.scope_config_save_button.setObjectName(u"scope_config_save_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scope_config_save_button.sizePolicy().hasHeightForWidth())
        self.scope_config_save_button.setSizePolicy(sizePolicy3)
        self.scope_config_save_button.setFont(font2)

        self.gridLayout_5.addWidget(self.scope_config_save_button, 3, 0, 1, 2)


        self.verticalLayout_3.addWidget(self.scope_config_box)

        self.accel_config_box = QGroupBox(self.layoutWidget2)
        self.accel_config_box.setObjectName(u"accel_config_box")
        self.accel_config_box.setFont(font2)
        self.layoutWidget5 = QWidget(self.accel_config_box)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(20, 30, 451, 71))
        self.gridLayout_4 = QGridLayout(self.layoutWidget5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.accel_com_label = QLabel(self.layoutWidget5)
        self.accel_com_label.setObjectName(u"accel_com_label")
        sizePolicy1.setHeightForWidth(self.accel_com_label.sizePolicy().hasHeightForWidth())
        self.accel_com_label.setSizePolicy(sizePolicy1)
        self.accel_com_label.setFont(font2)

        self.horizontalLayout_8.addWidget(self.accel_com_label)

        self.accel_config_com_input = QLineEdit(self.layoutWidget5)
        self.accel_config_com_input.setObjectName(u"accel_config_com_input")
        sizePolicy.setHeightForWidth(self.accel_config_com_input.sizePolicy().hasHeightForWidth())
        self.accel_config_com_input.setSizePolicy(sizePolicy)
        self.accel_config_com_input.setFont(font2)

        self.horizontalLayout_8.addWidget(self.accel_config_com_input)

        self.com_baud_rate_label = QLabel(self.layoutWidget5)
        self.com_baud_rate_label.setObjectName(u"com_baud_rate_label")
        sizePolicy1.setHeightForWidth(self.com_baud_rate_label.sizePolicy().hasHeightForWidth())
        self.com_baud_rate_label.setSizePolicy(sizePolicy1)

        self.horizontalLayout_8.addWidget(self.com_baud_rate_label)

        self.com_baud_rate_input = QLineEdit(self.layoutWidget5)
        self.com_baud_rate_input.setObjectName(u"com_baud_rate_input")
        sizePolicy2.setHeightForWidth(self.com_baud_rate_input.sizePolicy().hasHeightForWidth())
        self.com_baud_rate_input.setSizePolicy(sizePolicy2)

        self.horizontalLayout_8.addWidget(self.com_baud_rate_input)


        self.gridLayout_4.addLayout(self.horizontalLayout_8, 0, 0, 1, 3)

        self.accel_status_check_button = QPushButton(self.layoutWidget5)
        self.accel_status_check_button.setObjectName(u"accel_status_check_button")
        sizePolicy2.setHeightForWidth(self.accel_status_check_button.sizePolicy().hasHeightForWidth())
        self.accel_status_check_button.setSizePolicy(sizePolicy2)
        self.accel_status_check_button.setFont(font2)

        self.gridLayout_4.addWidget(self.accel_status_check_button, 1, 0, 1, 1)

        self.accel_com_status_label = QLabel(self.layoutWidget5)
        self.accel_com_status_label.setObjectName(u"accel_com_status_label")
        sizePolicy.setHeightForWidth(self.accel_com_status_label.sizePolicy().hasHeightForWidth())
        self.accel_com_status_label.setSizePolicy(sizePolicy)
        self.accel_com_status_label.setFont(font2)

        self.gridLayout_4.addWidget(self.accel_com_status_label, 1, 1, 1, 1)

        self.accel_config_save_button = QPushButton(self.layoutWidget5)
        self.accel_config_save_button.setObjectName(u"accel_config_save_button")
        sizePolicy2.setHeightForWidth(self.accel_config_save_button.sizePolicy().hasHeightForWidth())
        self.accel_config_save_button.setSizePolicy(sizePolicy2)

        self.gridLayout_4.addWidget(self.accel_config_save_button, 1, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.accel_config_box)

        self.verticalLayout_3.setStretch(0, 4)
        self.verticalLayout_3.setStretch(1, 4)
        self.verticalLayout_3.setStretch(2, 2)

        self.left_vertical_box.addWidget(self.config_box)

        self.information_box = QGroupBox(self.layoutWidget)
        self.information_box.setObjectName(u"information_box")
        sizePolicy.setHeightForWidth(self.information_box.sizePolicy().hasHeightForWidth())
        self.information_box.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(12)
        self.information_box.setFont(font3)
        self.information_box.setStyleSheet(u"background-color: rgb(197, 197, 197);")
        self.information_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.information_box)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.project_name = QLabel(self.information_box)
        self.project_name.setObjectName(u"project_name")
        font4 = QFont()
        font4.setFamilies([u"Times New Roman"])
        font4.setPointSize(16)
        font4.setBold(True)
        self.project_name.setFont(font4)
        self.project_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.project_name)

        self.author = QLabel(self.information_box)
        self.author.setObjectName(u"author")
        self.author.setFont(font3)
        self.author.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout.addWidget(self.author)


        self.left_vertical_box.addWidget(self.information_box)

        self.left_vertical_box.setStretch(0, 350)
        self.left_vertical_box.setStretch(1, 600)
        self.left_vertical_box.setStretch(2, 70)
        self.layoutWidget6 = QWidget(main_widget)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(590, 10, 1311, 1051))
        self.right_vertical_box = QVBoxLayout(self.layoutWidget6)
        self.right_vertical_box.setSpacing(5)
        self.right_vertical_box.setObjectName(u"right_vertical_box")
        self.right_vertical_box.setContentsMargins(5, 0, 5, 0)
        self.scope_box = QGroupBox(self.layoutWidget6)
        self.scope_box.setObjectName(u"scope_box")
        sizePolicy.setHeightForWidth(self.scope_box.sizePolicy().hasHeightForWidth())
        self.scope_box.setSizePolicy(sizePolicy)
        self.scope_box.setFont(font2)
        self.scope_box.setFlat(False)
        self.scope_box.setCheckable(False)
        self.layoutWidget7 = QWidget(self.scope_box)
        self.layoutWidget7.setObjectName(u"layoutWidget7")
        self.layoutWidget7.setGeometry(QRect(21, 31, 1261, 491))
        self.layoutWidget7.setFont(font2)
        self.gridLayout = QGridLayout(self.layoutWidget7)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.scope_channel3 = QCheckBox(self.layoutWidget7)
        self.scope_channel3.setObjectName(u"scope_channel3")
        sizePolicy2.setHeightForWidth(self.scope_channel3.sizePolicy().hasHeightForWidth())
        self.scope_channel3.setSizePolicy(sizePolicy2)
        self.scope_channel3.setFont(font2)

        self.gridLayout.addWidget(self.scope_channel3, 0, 2, 1, 1)

        self.scope_channel2 = QCheckBox(self.layoutWidget7)
        self.scope_channel2.setObjectName(u"scope_channel2")
        sizePolicy2.setHeightForWidth(self.scope_channel2.sizePolicy().hasHeightForWidth())
        self.scope_channel2.setSizePolicy(sizePolicy2)
        self.scope_channel2.setFont(font2)

        self.gridLayout.addWidget(self.scope_channel2, 0, 1, 1, 1)

        self.scope_graphics_view = QGraphicsView(self.layoutWidget7)
        self.scope_graphics_view.setObjectName(u"scope_graphics_view")
        sizePolicy.setHeightForWidth(self.scope_graphics_view.sizePolicy().hasHeightForWidth())
        self.scope_graphics_view.setSizePolicy(sizePolicy)
        self.scope_graphics_view.setFont(font2)

        self.gridLayout.addWidget(self.scope_graphics_view, 1, 0, 1, 4)

        self.scope_channel1 = QCheckBox(self.layoutWidget7)
        self.scope_channel1.setObjectName(u"scope_channel1")
        sizePolicy2.setHeightForWidth(self.scope_channel1.sizePolicy().hasHeightForWidth())
        self.scope_channel1.setSizePolicy(sizePolicy2)
        self.scope_channel1.setFont(font2)

        self.gridLayout.addWidget(self.scope_channel1, 0, 0, 1, 1)

        self.scope_channel4 = QCheckBox(self.layoutWidget7)
        self.scope_channel4.setObjectName(u"scope_channel4")
        sizePolicy2.setHeightForWidth(self.scope_channel4.sizePolicy().hasHeightForWidth())
        self.scope_channel4.setSizePolicy(sizePolicy2)
        self.scope_channel4.setFont(font1)

        self.gridLayout.addWidget(self.scope_channel4, 0, 3, 1, 1)

        self.scope_fetch_button = QPushButton(self.layoutWidget7)
        self.scope_fetch_button.setObjectName(u"scope_fetch_button")
        sizePolicy2.setHeightForWidth(self.scope_fetch_button.sizePolicy().hasHeightForWidth())
        self.scope_fetch_button.setSizePolicy(sizePolicy2)
        self.scope_fetch_button.setFont(font2)

        self.gridLayout.addWidget(self.scope_fetch_button, 2, 0, 1, 2)

        self.scope_data_save_button = QPushButton(self.layoutWidget7)
        self.scope_data_save_button.setObjectName(u"scope_data_save_button")
        sizePolicy2.setHeightForWidth(self.scope_data_save_button.sizePolicy().hasHeightForWidth())
        self.scope_data_save_button.setSizePolicy(sizePolicy2)
        self.scope_data_save_button.setFont(font2)

        self.gridLayout.addWidget(self.scope_data_save_button, 2, 2, 1, 2)


        self.right_vertical_box.addWidget(self.scope_box)

        self.accel_box = QGroupBox(self.layoutWidget6)
        self.accel_box.setObjectName(u"accel_box")
        sizePolicy.setHeightForWidth(self.accel_box.sizePolicy().hasHeightForWidth())
        self.accel_box.setSizePolicy(sizePolicy)
        self.accel_box.setFont(font)
        self.layoutWidget8 = QWidget(self.accel_box)
        self.layoutWidget8.setObjectName(u"layoutWidget8")
        self.layoutWidget8.setGeometry(QRect(20, 30, 1271, 391))
        self.gridLayout_2 = QGridLayout(self.layoutWidget8)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.accel_graph = QGraphicsView(self.layoutWidget8)
        self.accel_graph.setObjectName(u"accel_graph")
        self.accel_graph.setFont(font)

        self.gridLayout_2.addWidget(self.accel_graph, 0, 0, 1, 2)

        self.accel_fft = QGraphicsView(self.layoutWidget8)
        self.accel_fft.setObjectName(u"accel_fft")
        self.accel_fft.setFont(font)

        self.gridLayout_2.addWidget(self.accel_fft, 1, 0, 1, 2)

        self.accel_fetch_button = QPushButton(self.layoutWidget8)
        self.accel_fetch_button.setObjectName(u"accel_fetch_button")
        sizePolicy2.setHeightForWidth(self.accel_fetch_button.sizePolicy().hasHeightForWidth())
        self.accel_fetch_button.setSizePolicy(sizePolicy2)
        self.accel_fetch_button.setFont(font)

        self.gridLayout_2.addWidget(self.accel_fetch_button, 2, 0, 1, 1)

        self.accel_save_button = QPushButton(self.layoutWidget8)
        self.accel_save_button.setObjectName(u"accel_save_button")
        sizePolicy2.setHeightForWidth(self.accel_save_button.sizePolicy().hasHeightForWidth())
        self.accel_save_button.setSizePolicy(sizePolicy2)
        self.accel_save_button.setFont(font)

        self.gridLayout_2.addWidget(self.accel_save_button, 2, 1, 1, 1)


        self.right_vertical_box.addWidget(self.accel_box)

        self.output = QGroupBox(self.layoutWidget6)
        self.output.setObjectName(u"output")
        sizePolicy.setHeightForWidth(self.output.sizePolicy().hasHeightForWidth())
        self.output.setSizePolicy(sizePolicy)
        self.output.setStyleSheet(u"")
        self.output_message = QTextEdit(self.output)
        self.output_message.setObjectName(u"output_message")
        self.output_message.setGeometry(QRect(20, 20, 1271, 50))
        self.output_message.setStyleSheet(u"color: rgb(42, 42, 42);")
        self.output_message.setReadOnly(True)
        self.output_message.setAcceptRichText(True)

        self.right_vertical_box.addWidget(self.output)

        self.right_vertical_box.setStretch(0, 500)
        self.right_vertical_box.setStretch(1, 400)
        self.right_vertical_box.setStretch(2, 87)

        self.retranslateUi(main_widget)

        self.fun_config_waveform_input.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(main_widget)
    # setupUi

    def retranslateUi(self, main_widget):
        main_widget.setWindowTitle(QCoreApplication.translate("main_widget", u"Frequency tunable triboelectric test and measurement setup", None))
        self.con_box.setTitle(QCoreApplication.translate("main_widget", u"Connected devices", None))
        self.identify_res_button.setText(QCoreApplication.translate("main_widget", u"IDENTIFY CONNECTED DEVICES", None))
        self.config_box.setTitle(QCoreApplication.translate("main_widget", u"Configurations", None))
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
        self.scope_config_box.setTitle(QCoreApplication.translate("main_widget", u"Oscilloscope", None))
        self.scope_id_label.setText(QCoreApplication.translate("main_widget", u"DEVICE ID", None))
        self.scope_xrange_label.setText(QCoreApplication.translate("main_widget", u"X RANGE", None))
        self.scope_yrange_label.setText(QCoreApplication.translate("main_widget", u"Y RANGE", None))
        self.scope_trigger_label.setText(QCoreApplication.translate("main_widget", u"TRIGGER POS", None))
        self.scope_config_save_button.setText(QCoreApplication.translate("main_widget", u"SAVE", None))
        self.accel_config_box.setTitle(QCoreApplication.translate("main_widget", u"Accelerometer", None))
        self.accel_com_label.setText(QCoreApplication.translate("main_widget", u"COM PORT", None))
        self.com_baud_rate_label.setText(QCoreApplication.translate("main_widget", u"BAUD RATE", None))
        self.accel_status_check_button.setText(QCoreApplication.translate("main_widget", u"CHECK STATUS", None))
        self.accel_com_status_label.setText(QCoreApplication.translate("main_widget", u"Available!", None))
        self.accel_config_save_button.setText(QCoreApplication.translate("main_widget", u"SAVE", None))
        self.project_name.setText(QCoreApplication.translate("main_widget", u"Frequency tunable Triboelectric Energy Harvester", None))
        self.author.setText(QCoreApplication.translate("main_widget", u"Dr. Sagar Hosangadi Prutvi, Post Doc Researcher @ LivMatS cluster", None))
        self.scope_box.setTitle(QCoreApplication.translate("main_widget", u"Oscilloscope data", None))
        self.scope_channel3.setText(QCoreApplication.translate("main_widget", u"Channel 3", None))
        self.scope_channel2.setText(QCoreApplication.translate("main_widget", u"Channel 2", None))
        self.scope_channel1.setText(QCoreApplication.translate("main_widget", u"Channel 1", None))
        self.scope_channel4.setText(QCoreApplication.translate("main_widget", u"Channel 4", None))
        self.scope_fetch_button.setText(QCoreApplication.translate("main_widget", u"FETCH DATA", None))
        self.scope_data_save_button.setText(QCoreApplication.translate("main_widget", u"SAVE", None))
        self.accel_box.setTitle(QCoreApplication.translate("main_widget", u"Accelerometer data", None))
        self.accel_fetch_button.setText(QCoreApplication.translate("main_widget", u"FETCH DATA", None))
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

