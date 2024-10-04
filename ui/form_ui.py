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
        main_widget.setWindowModality(Qt.WindowModality.ApplicationModal)
        main_widget.setEnabled(True)
        main_widget.resize(1259, 744)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_widget.sizePolicy().hasHeightForWidth())
        main_widget.setSizePolicy(sizePolicy)
        self.gridLayout_7 = QGridLayout(main_widget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.right_box = QVBoxLayout()
        self.right_box.setObjectName(u"right_box")
        self.scope_box = QGroupBox(main_widget)
        self.scope_box.setObjectName(u"scope_box")
        sizePolicy.setHeightForWidth(self.scope_box.sizePolicy().hasHeightForWidth())
        self.scope_box.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(10)
        font.setBold(True)
        self.scope_box.setFont(font)
        self.scope_box.setFlat(False)
        self.scope_box.setCheckable(False)
        self.gridLayout_16 = QGridLayout(self.scope_box)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.scope_channel1 = QCheckBox(self.scope_box)
        self.scope_channel1.setObjectName(u"scope_channel1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scope_channel1.sizePolicy().hasHeightForWidth())
        self.scope_channel1.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.scope_channel1.setFont(font1)

        self.gridLayout_4.addWidget(self.scope_channel1, 0, 0, 1, 1)

        self.scope_channel2 = QCheckBox(self.scope_box)
        self.scope_channel2.setObjectName(u"scope_channel2")
        sizePolicy1.setHeightForWidth(self.scope_channel2.sizePolicy().hasHeightForWidth())
        self.scope_channel2.setSizePolicy(sizePolicy1)
        self.scope_channel2.setFont(font1)

        self.gridLayout_4.addWidget(self.scope_channel2, 0, 1, 1, 1)

        self.scope_channel3 = QCheckBox(self.scope_box)
        self.scope_channel3.setObjectName(u"scope_channel3")
        sizePolicy1.setHeightForWidth(self.scope_channel3.sizePolicy().hasHeightForWidth())
        self.scope_channel3.setSizePolicy(sizePolicy1)
        self.scope_channel3.setFont(font1)

        self.gridLayout_4.addWidget(self.scope_channel3, 0, 2, 1, 1)

        self.scope_channel4 = QCheckBox(self.scope_box)
        self.scope_channel4.setObjectName(u"scope_channel4")
        sizePolicy1.setHeightForWidth(self.scope_channel4.sizePolicy().hasHeightForWidth())
        self.scope_channel4.setSizePolicy(sizePolicy1)
        self.scope_channel4.setFont(font1)

        self.gridLayout_4.addWidget(self.scope_channel4, 0, 3, 1, 1)

        self.scope_fetch_button = QPushButton(self.scope_box)
        self.scope_fetch_button.setObjectName(u"scope_fetch_button")
        sizePolicy1.setHeightForWidth(self.scope_fetch_button.sizePolicy().hasHeightForWidth())
        self.scope_fetch_button.setSizePolicy(sizePolicy1)
        self.scope_fetch_button.setFont(font1)

        self.gridLayout_4.addWidget(self.scope_fetch_button, 2, 0, 1, 2)

        self.scope_data_save_button = QPushButton(self.scope_box)
        self.scope_data_save_button.setObjectName(u"scope_data_save_button")
        sizePolicy1.setHeightForWidth(self.scope_data_save_button.sizePolicy().hasHeightForWidth())
        self.scope_data_save_button.setSizePolicy(sizePolicy1)
        self.scope_data_save_button.setFont(font1)

        self.gridLayout_4.addWidget(self.scope_data_save_button, 2, 2, 1, 2)

        self.scope_graphics_view = QGraphicsView(self.scope_box)
        self.scope_graphics_view.setObjectName(u"scope_graphics_view")
        sizePolicy.setHeightForWidth(self.scope_graphics_view.sizePolicy().hasHeightForWidth())
        self.scope_graphics_view.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(6)
        font2.setBold(False)
        self.scope_graphics_view.setFont(font2)

        self.gridLayout_4.addWidget(self.scope_graphics_view, 1, 0, 1, 4)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 1)
        self.gridLayout_4.setColumnStretch(2, 1)
        self.gridLayout_4.setColumnStretch(3, 1)

        self.gridLayout_16.addLayout(self.gridLayout_4, 0, 0, 1, 1)


        self.right_box.addWidget(self.scope_box)

        self.accel_box = QGroupBox(main_widget)
        self.accel_box.setObjectName(u"accel_box")
        sizePolicy.setHeightForWidth(self.accel_box.sizePolicy().hasHeightForWidth())
        self.accel_box.setSizePolicy(sizePolicy)
        self.accel_box.setFont(font)
        self.gridLayout_8 = QGridLayout(self.accel_box)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.accel_graph = QGraphicsView(self.accel_box)
        self.accel_graph.setObjectName(u"accel_graph")
        sizePolicy.setHeightForWidth(self.accel_graph.sizePolicy().hasHeightForWidth())
        self.accel_graph.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(8)
        font3.setBold(False)
        self.accel_graph.setFont(font3)

        self.gridLayout_5.addWidget(self.accel_graph, 0, 0, 1, 3)

        self.accel_save_button = QPushButton(self.accel_box)
        self.accel_save_button.setObjectName(u"accel_save_button")
        sizePolicy.setHeightForWidth(self.accel_save_button.sizePolicy().hasHeightForWidth())
        self.accel_save_button.setSizePolicy(sizePolicy)
        self.accel_save_button.setFont(font1)

        self.gridLayout_5.addWidget(self.accel_save_button, 1, 2, 1, 1)

        self.accel_fetch_button = QPushButton(self.accel_box)
        self.accel_fetch_button.setObjectName(u"accel_fetch_button")
        sizePolicy.setHeightForWidth(self.accel_fetch_button.sizePolicy().hasHeightForWidth())
        self.accel_fetch_button.setSizePolicy(sizePolicy)
        self.accel_fetch_button.setFont(font1)

        self.gridLayout_5.addWidget(self.accel_fetch_button, 1, 0, 1, 1)

        self.accel_disconnect_button = QPushButton(self.accel_box)
        self.accel_disconnect_button.setObjectName(u"accel_disconnect_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.accel_disconnect_button.sizePolicy().hasHeightForWidth())
        self.accel_disconnect_button.setSizePolicy(sizePolicy2)
        self.accel_disconnect_button.setFont(font1)

        self.gridLayout_5.addWidget(self.accel_disconnect_button, 1, 1, 1, 1)

        self.gridLayout_5.setRowStretch(0, 10)
        self.gridLayout_5.setRowStretch(1, 1)
        self.gridLayout_5.setColumnStretch(0, 1)
        self.gridLayout_5.setColumnStretch(1, 1)
        self.gridLayout_5.setColumnStretch(2, 1)

        self.gridLayout_8.addLayout(self.gridLayout_5, 1, 0, 1, 1)


        self.right_box.addWidget(self.accel_box)

        self.output = QGroupBox(main_widget)
        self.output.setObjectName(u"output")
        sizePolicy.setHeightForWidth(self.output.sizePolicy().hasHeightForWidth())
        self.output.setSizePolicy(sizePolicy)
        self.output.setStyleSheet(u"")
        self.gridLayout_15 = QGridLayout(self.output)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.output_message = QTextEdit(self.output)
        self.output_message.setObjectName(u"output_message")
        sizePolicy1.setHeightForWidth(self.output_message.sizePolicy().hasHeightForWidth())
        self.output_message.setSizePolicy(sizePolicy1)
        self.output_message.setStyleSheet(u"color: rgb(42, 42, 42);")
        self.output_message.setReadOnly(True)
        self.output_message.setAcceptRichText(True)

        self.gridLayout_15.addWidget(self.output_message, 0, 0, 2, 1)


        self.right_box.addWidget(self.output)

        self.right_box.setStretch(0, 20)
        self.right_box.setStretch(1, 10)
        self.right_box.setStretch(2, 2)

        self.gridLayout_7.addLayout(self.right_box, 0, 5, 4, 3)

        self.left_box = QVBoxLayout()
        self.left_box.setObjectName(u"left_box")
        self.con_box = QGroupBox(main_widget)
        self.con_box.setObjectName(u"con_box")
        sizePolicy.setHeightForWidth(self.con_box.sizePolicy().hasHeightForWidth())
        self.con_box.setSizePolicy(sizePolicy)
        self.con_box.setMinimumSize(QSize(0, 30))
        self.con_box.setFont(font)
        self.gridLayout_9 = QGridLayout(self.con_box)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 5, -1, -1)
        self.identify_res_button = QPushButton(self.con_box)
        self.identify_res_button.setObjectName(u"identify_res_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.identify_res_button.sizePolicy().hasHeightForWidth())
        self.identify_res_button.setSizePolicy(sizePolicy3)
        self.identify_res_button.setFont(font1)

        self.verticalLayout.addWidget(self.identify_res_button)

        self.connected_devices_table = QTableWidget(self.con_box)
        self.connected_devices_table.setObjectName(u"connected_devices_table")
        sizePolicy.setHeightForWidth(self.connected_devices_table.sizePolicy().hasHeightForWidth())
        self.connected_devices_table.setSizePolicy(sizePolicy)
        self.connected_devices_table.setMinimumSize(QSize(0, 20))
        self.connected_devices_table.setFont(font1)

        self.verticalLayout.addWidget(self.connected_devices_table)


        self.gridLayout_9.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.left_box.addWidget(self.con_box)

        self.config_box = QGroupBox(main_widget)
        self.config_box.setObjectName(u"config_box")
        sizePolicy.setHeightForWidth(self.config_box.sizePolicy().hasHeightForWidth())
        self.config_box.setSizePolicy(sizePolicy)
        self.config_box.setFont(font)
        self.gridLayout_10 = QGridLayout(self.config_box)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.scope_config_box = QGroupBox(self.config_box)
        self.scope_config_box.setObjectName(u"scope_config_box")
        self.scope_config_box.setFont(font1)
        self.gridLayout_13 = QGridLayout(self.scope_config_box)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.scope_xrange_label = QLabel(self.scope_config_box)
        self.scope_xrange_label.setObjectName(u"scope_xrange_label")
        sizePolicy1.setHeightForWidth(self.scope_xrange_label.sizePolicy().hasHeightForWidth())
        self.scope_xrange_label.setSizePolicy(sizePolicy1)
        self.scope_xrange_label.setFont(font1)

        self.horizontalLayout_6.addWidget(self.scope_xrange_label)

        self.scope_config_xrange_input = QLineEdit(self.scope_config_box)
        self.scope_config_xrange_input.setObjectName(u"scope_config_xrange_input")
        sizePolicy1.setHeightForWidth(self.scope_config_xrange_input.sizePolicy().hasHeightForWidth())
        self.scope_config_xrange_input.setSizePolicy(sizePolicy1)
        self.scope_config_xrange_input.setFont(font1)

        self.horizontalLayout_6.addWidget(self.scope_config_xrange_input)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.scope_yrange_label = QLabel(self.scope_config_box)
        self.scope_yrange_label.setObjectName(u"scope_yrange_label")
        sizePolicy1.setHeightForWidth(self.scope_yrange_label.sizePolicy().hasHeightForWidth())
        self.scope_yrange_label.setSizePolicy(sizePolicy1)
        self.scope_yrange_label.setFont(font1)

        self.horizontalLayout_7.addWidget(self.scope_yrange_label)

        self.scope_config_yrange_input = QLineEdit(self.scope_config_box)
        self.scope_config_yrange_input.setObjectName(u"scope_config_yrange_input")
        sizePolicy1.setHeightForWidth(self.scope_config_yrange_input.sizePolicy().hasHeightForWidth())
        self.scope_config_yrange_input.setSizePolicy(sizePolicy1)
        self.scope_config_yrange_input.setFont(font1)

        self.horizontalLayout_7.addWidget(self.scope_config_yrange_input)


        self.gridLayout_2.addLayout(self.horizontalLayout_7, 1, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.scope_id_label = QLabel(self.scope_config_box)
        self.scope_id_label.setObjectName(u"scope_id_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.scope_id_label.sizePolicy().hasHeightForWidth())
        self.scope_id_label.setSizePolicy(sizePolicy4)
        self.scope_id_label.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_5.addWidget(self.scope_id_label)

        self.scope_config_id_input = QLineEdit(self.scope_config_box)
        self.scope_config_id_input.setObjectName(u"scope_config_id_input")
        sizePolicy1.setHeightForWidth(self.scope_config_id_input.sizePolicy().hasHeightForWidth())
        self.scope_config_id_input.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.scope_config_id_input)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.scope_trigger_label = QLabel(self.scope_config_box)
        self.scope_trigger_label.setObjectName(u"scope_trigger_label")
        sizePolicy3.setHeightForWidth(self.scope_trigger_label.sizePolicy().hasHeightForWidth())
        self.scope_trigger_label.setSizePolicy(sizePolicy3)
        self.scope_trigger_label.setFont(font1)

        self.horizontalLayout_8.addWidget(self.scope_trigger_label)

        self.scope_config_trigger_input = QLineEdit(self.scope_config_box)
        self.scope_config_trigger_input.setObjectName(u"scope_config_trigger_input")
        sizePolicy1.setHeightForWidth(self.scope_config_trigger_input.sizePolicy().hasHeightForWidth())
        self.scope_config_trigger_input.setSizePolicy(sizePolicy1)
        self.scope_config_trigger_input.setFont(font1)

        self.horizontalLayout_8.addWidget(self.scope_config_trigger_input)


        self.gridLayout_2.addLayout(self.horizontalLayout_8, 2, 0, 1, 2)

        self.scope_config_save_button = QPushButton(self.scope_config_box)
        self.scope_config_save_button.setObjectName(u"scope_config_save_button")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.scope_config_save_button.sizePolicy().hasHeightForWidth())
        self.scope_config_save_button.setSizePolicy(sizePolicy5)
        self.scope_config_save_button.setFont(font1)

        self.gridLayout_2.addWidget(self.scope_config_save_button, 3, 0, 1, 2)


        self.gridLayout_13.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.scope_config_box, 3, 0, 1, 1)

        self.accel_config_box = QGroupBox(self.config_box)
        self.accel_config_box.setObjectName(u"accel_config_box")
        self.accel_config_box.setFont(font1)
        self.gridLayout_11 = QGridLayout(self.accel_config_box)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.com_baud_rate_label = QLabel(self.accel_config_box)
        self.com_baud_rate_label.setObjectName(u"com_baud_rate_label")
        sizePolicy3.setHeightForWidth(self.com_baud_rate_label.sizePolicy().hasHeightForWidth())
        self.com_baud_rate_label.setSizePolicy(sizePolicy3)

        self.horizontalLayout_10.addWidget(self.com_baud_rate_label)

        self.com_baud_rate_input = QComboBox(self.accel_config_box)
        self.com_baud_rate_input.addItem("")
        self.com_baud_rate_input.addItem("")
        self.com_baud_rate_input.addItem("")
        self.com_baud_rate_input.addItem("")
        self.com_baud_rate_input.addItem("")
        self.com_baud_rate_input.addItem("")
        self.com_baud_rate_input.setObjectName(u"com_baud_rate_input")
        sizePolicy1.setHeightForWidth(self.com_baud_rate_input.sizePolicy().hasHeightForWidth())
        self.com_baud_rate_input.setSizePolicy(sizePolicy1)

        self.horizontalLayout_10.addWidget(self.com_baud_rate_input)


        self.gridLayout_3.addLayout(self.horizontalLayout_10, 0, 1, 1, 1)

        self.accel_config_save_button = QPushButton(self.accel_config_box)
        self.accel_config_save_button.setObjectName(u"accel_config_save_button")
        sizePolicy1.setHeightForWidth(self.accel_config_save_button.sizePolicy().hasHeightForWidth())
        self.accel_config_save_button.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.accel_config_save_button, 1, 0, 1, 2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.accel_com_label = QLabel(self.accel_config_box)
        self.accel_com_label.setObjectName(u"accel_com_label")
        sizePolicy3.setHeightForWidth(self.accel_com_label.sizePolicy().hasHeightForWidth())
        self.accel_com_label.setSizePolicy(sizePolicy3)
        self.accel_com_label.setFont(font1)

        self.horizontalLayout_9.addWidget(self.accel_com_label)

        self.accel_config_com_input = QLineEdit(self.accel_config_box)
        self.accel_config_com_input.setObjectName(u"accel_config_com_input")
        sizePolicy3.setHeightForWidth(self.accel_config_com_input.sizePolicy().hasHeightForWidth())
        self.accel_config_com_input.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setFamilies([u"Times New Roman"])
        font4.setPointSize(14)
        font4.setBold(False)
        self.accel_config_com_input.setFont(font4)

        self.horizontalLayout_9.addWidget(self.accel_config_com_input)


        self.gridLayout_3.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)

        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setRowStretch(1, 1)

        self.gridLayout_11.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.accel_config_box, 4, 0, 1, 1)

        self.fun_config_box = QGroupBox(self.config_box)
        self.fun_config_box.setObjectName(u"fun_config_box")
        sizePolicy3.setHeightForWidth(self.fun_config_box.sizePolicy().hasHeightForWidth())
        self.fun_config_box.setSizePolicy(sizePolicy3)
        self.fun_config_box.setFont(font1)
        self.gridLayout = QGridLayout(self.fun_config_box)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fun_id_label = QLabel(self.fun_config_box)
        self.fun_id_label.setObjectName(u"fun_id_label")

        self.horizontalLayout.addWidget(self.fun_id_label)

        self.fun_id_input = QLineEdit(self.fun_config_box)
        self.fun_id_input.setObjectName(u"fun_id_input")
        sizePolicy1.setHeightForWidth(self.fun_id_input.sizePolicy().hasHeightForWidth())
        self.fun_id_input.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.fun_id_input)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.waveform_type_label = QLabel(self.fun_config_box)
        self.waveform_type_label.setObjectName(u"waveform_type_label")
        sizePolicy3.setHeightForWidth(self.waveform_type_label.sizePolicy().hasHeightForWidth())
        self.waveform_type_label.setSizePolicy(sizePolicy3)
        self.waveform_type_label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.waveform_type_label)

        self.fun_config_waveform_input = QComboBox(self.fun_config_box)
        self.fun_config_waveform_input.addItem("")
        self.fun_config_waveform_input.addItem("")
        self.fun_config_waveform_input.addItem("")
        self.fun_config_waveform_input.setObjectName(u"fun_config_waveform_input")
        sizePolicy1.setHeightForWidth(self.fun_config_waveform_input.sizePolicy().hasHeightForWidth())
        self.fun_config_waveform_input.setSizePolicy(sizePolicy1)
        self.fun_config_waveform_input.setFont(font1)
        self.fun_config_waveform_input.setEditable(False)

        self.horizontalLayout_2.addWidget(self.fun_config_waveform_input)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.freq_input_label = QLabel(self.fun_config_box)
        self.freq_input_label.setObjectName(u"freq_input_label")
        sizePolicy1.setHeightForWidth(self.freq_input_label.sizePolicy().hasHeightForWidth())
        self.freq_input_label.setSizePolicy(sizePolicy1)
        self.freq_input_label.setFont(font1)

        self.horizontalLayout_3.addWidget(self.freq_input_label)

        self.fun_config_freq_input = QLineEdit(self.fun_config_box)
        self.fun_config_freq_input.setObjectName(u"fun_config_freq_input")
        sizePolicy1.setHeightForWidth(self.fun_config_freq_input.sizePolicy().hasHeightForWidth())
        self.fun_config_freq_input.setSizePolicy(sizePolicy1)
        self.fun_config_freq_input.setFont(font1)

        self.horizontalLayout_3.addWidget(self.fun_config_freq_input)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.vpp_label = QLabel(self.fun_config_box)
        self.vpp_label.setObjectName(u"vpp_label")
        sizePolicy1.setHeightForWidth(self.vpp_label.sizePolicy().hasHeightForWidth())
        self.vpp_label.setSizePolicy(sizePolicy1)
        self.vpp_label.setFont(font1)

        self.horizontalLayout_4.addWidget(self.vpp_label)

        self.fun_config_vpp_input = QLineEdit(self.fun_config_box)
        self.fun_config_vpp_input.setObjectName(u"fun_config_vpp_input")
        sizePolicy1.setHeightForWidth(self.fun_config_vpp_input.sizePolicy().hasHeightForWidth())
        self.fun_config_vpp_input.setSizePolicy(sizePolicy1)
        self.fun_config_vpp_input.setFont(font1)
        self.fun_config_vpp_input.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)

        self.horizontalLayout_4.addWidget(self.fun_config_vpp_input)


        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.fun_save_button = QPushButton(self.fun_config_box)
        self.fun_save_button.setObjectName(u"fun_save_button")
        sizePolicy1.setHeightForWidth(self.fun_save_button.sizePolicy().hasHeightForWidth())
        self.fun_save_button.setSizePolicy(sizePolicy1)
        self.fun_save_button.setFont(font1)

        self.horizontalLayout_11.addWidget(self.fun_save_button)

        self.fun_start_button = QPushButton(self.fun_config_box)
        self.fun_start_button.setObjectName(u"fun_start_button")
        sizePolicy1.setHeightForWidth(self.fun_start_button.sizePolicy().hasHeightForWidth())
        self.fun_start_button.setSizePolicy(sizePolicy1)
        self.fun_start_button.setFont(font1)

        self.horizontalLayout_11.addWidget(self.fun_start_button)

        self.fun_stop_button = QPushButton(self.fun_config_box)
        self.fun_stop_button.setObjectName(u"fun_stop_button")

        self.horizontalLayout_11.addWidget(self.fun_stop_button)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 2)
        self.horizontalLayout_11.setStretch(2, 1)

        self.gridLayout.addLayout(self.horizontalLayout_11, 3, 0, 1, 2)


        self.gridLayout_10.addWidget(self.fun_config_box, 0, 0, 3, 1)

        self.gridLayout_10.setRowStretch(0, 4)
        self.gridLayout_10.setRowStretch(1, 4)
        self.gridLayout_10.setRowStretch(2, 2)

        self.left_box.addWidget(self.config_box)

        self.information_box = QGroupBox(main_widget)
        self.information_box.setObjectName(u"information_box")
        sizePolicy1.setHeightForWidth(self.information_box.sizePolicy().hasHeightForWidth())
        self.information_box.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setFamilies([u"Times New Roman"])
        font5.setPointSize(12)
        self.information_box.setFont(font5)
        self.information_box.setStyleSheet(u"background-color: rgb(197, 197, 197);")
        self.information_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_6 = QGridLayout(self.information_box)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.project_name = QLabel(self.information_box)
        self.project_name.setObjectName(u"project_name")
        sizePolicy3.setHeightForWidth(self.project_name.sizePolicy().hasHeightForWidth())
        self.project_name.setSizePolicy(sizePolicy3)
        font6 = QFont()
        font6.setFamilies([u"Times New Roman"])
        font6.setPointSize(16)
        font6.setBold(True)
        self.project_name.setFont(font6)
        self.project_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.project_name, 0, 0, 1, 2)

        self.author = QLabel(self.information_box)
        self.author.setObjectName(u"author")
        font7 = QFont()
        font7.setFamilies([u"Times New Roman"])
        font7.setPointSize(12)
        font7.setBold(True)
        self.author.setFont(font7)
        self.author.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_6.addWidget(self.author, 1, 0, 1, 2)

        self.imtek_logo = QGraphicsView(self.information_box)
        self.imtek_logo.setObjectName(u"imtek_logo")
        sizePolicy1.setHeightForWidth(self.imtek_logo.sizePolicy().hasHeightForWidth())
        self.imtek_logo.setSizePolicy(sizePolicy1)
        self.imtek_logo.setMinimumSize(QSize(0, 30))

        self.gridLayout_6.addWidget(self.imtek_logo, 2, 0, 1, 1)

        self.logo_space = QGraphicsView(self.information_box)
        self.logo_space.setObjectName(u"logo_space")
        sizePolicy1.setHeightForWidth(self.logo_space.sizePolicy().hasHeightForWidth())
        self.logo_space.setSizePolicy(sizePolicy1)
        self.logo_space.setMinimumSize(QSize(0, 30))

        self.gridLayout_6.addWidget(self.logo_space, 2, 1, 1, 1)

        self.gridLayout_6.setRowStretch(0, 3)
        self.gridLayout_6.setRowStretch(1, 2)
        self.gridLayout_6.setRowStretch(2, 1)

        self.left_box.addWidget(self.information_box)

        self.left_box.setStretch(0, 6)
        self.left_box.setStretch(1, 5)
        self.left_box.setStretch(2, 1)

        self.gridLayout_7.addLayout(self.left_box, 0, 0, 4, 1)

        self.gridLayout_7.setColumnStretch(0, 3)
        self.gridLayout_7.setColumnStretch(5, 10)
        self.gridLayout_7.setColumnStretch(6, 10)
        self.gridLayout_7.setColumnStretch(7, 10)

        self.retranslateUi(main_widget)

        self.fun_config_waveform_input.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(main_widget)
    # setupUi

    def retranslateUi(self, main_widget):
        main_widget.setWindowTitle(QCoreApplication.translate("main_widget", u"Frequency tunable triboelectric test and measurement setup", None))
        self.scope_box.setTitle(QCoreApplication.translate("main_widget", u"Oscilloscope data", None))
        self.scope_channel1.setText(QCoreApplication.translate("main_widget", u"Channel 1", None))
        self.scope_channel2.setText(QCoreApplication.translate("main_widget", u"Channel 2", None))
        self.scope_channel3.setText(QCoreApplication.translate("main_widget", u"Channel 3", None))
        self.scope_channel4.setText(QCoreApplication.translate("main_widget", u"Channel 4", None))
        self.scope_fetch_button.setText(QCoreApplication.translate("main_widget", u"FETCH DATA", None))
        self.scope_data_save_button.setText(QCoreApplication.translate("main_widget", u"SAVE", None))
        self.accel_box.setTitle(QCoreApplication.translate("main_widget", u"Accelerometer data", None))
        self.accel_save_button.setText(QCoreApplication.translate("main_widget", u"SAVE", None))
        self.accel_fetch_button.setText(QCoreApplication.translate("main_widget", u"CONNECT", None))
        self.accel_disconnect_button.setText(QCoreApplication.translate("main_widget", u"DISCONNECT", None))
        self.output.setTitle(QCoreApplication.translate("main_widget", u"Messages", None))
        self.output_message.setHtml(QCoreApplication.translate("main_widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.con_box.setTitle(QCoreApplication.translate("main_widget", u"Connected devices", None))
        self.identify_res_button.setText(QCoreApplication.translate("main_widget", u"IDENTIFY CONNECTED DEVICE", None))
        self.config_box.setTitle(QCoreApplication.translate("main_widget", u"Configurations", None))
        self.scope_config_box.setTitle(QCoreApplication.translate("main_widget", u"Oscilloscope", None))
        self.scope_xrange_label.setText(QCoreApplication.translate("main_widget", u"X RANGE", None))
        self.scope_yrange_label.setText(QCoreApplication.translate("main_widget", u"Y RANGE", None))
        self.scope_id_label.setText(QCoreApplication.translate("main_widget", u"DEVICE ID", None))
        self.scope_trigger_label.setText(QCoreApplication.translate("main_widget", u"TRIGGER POS", None))
        self.scope_config_save_button.setText(QCoreApplication.translate("main_widget", u"SAVE", None))
        self.accel_config_box.setTitle(QCoreApplication.translate("main_widget", u"Accelerometer", None))
        self.com_baud_rate_label.setText(QCoreApplication.translate("main_widget", u"BAUD RATE", None))
        self.com_baud_rate_input.setItemText(0, QCoreApplication.translate("main_widget", u"115200", None))
        self.com_baud_rate_input.setItemText(1, QCoreApplication.translate("main_widget", u"57600", None))
        self.com_baud_rate_input.setItemText(2, QCoreApplication.translate("main_widget", u"38400", None))
        self.com_baud_rate_input.setItemText(3, QCoreApplication.translate("main_widget", u"19200", None))
        self.com_baud_rate_input.setItemText(4, QCoreApplication.translate("main_widget", u"9600", None))
        self.com_baud_rate_input.setItemText(5, QCoreApplication.translate("main_widget", u"4800", None))

        self.accel_config_save_button.setText(QCoreApplication.translate("main_widget", u"SAVE", None))
        self.accel_com_label.setText(QCoreApplication.translate("main_widget", u"COM PORT", None))
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
        self.fun_start_button.setText(QCoreApplication.translate("main_widget", u"START", None))
        self.fun_stop_button.setText(QCoreApplication.translate("main_widget", u"STOP", None))
        self.information_box.setTitle("")
        self.project_name.setText(QCoreApplication.translate("main_widget", u"Frequency tunable Triboelectric Energy Harvester", None))
        self.author.setText(QCoreApplication.translate("main_widget", u"Dr. Sagar Hosangadi Prutvi, Post Doc Researcher @ LivMatS cluster", None))
    # retranslateUi

