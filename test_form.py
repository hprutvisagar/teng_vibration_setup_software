<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>main_widget</class>
 <widget class="QWidget" name="main_widget">
  <property name="windowModality">
   <enum>Qt::WindowModality::ApplicationModal</enum>
  </property>
  <property name="enabled">
   <bool>true</bool>
  </property>
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1339</width>
    <height>915</height>
   </rect>
  </property>
  <property name="sizePolicy">
   <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
    <horstretch>0</horstretch>
    <verstretch>0</verstretch>
   </sizepolicy>
  </property>
  <property name="windowTitle">
   <string>Frequency tunable triboelectric test and measurement setup</string>
  </property>
  <layout class="QGridLayout" name="gridLayout_7" rowstretch="0,0,0,0" columnstretch="3,0,0,0,0,10,10,10">
   <item row="0" column="5" rowspan="4" colspan="3">
    <layout class="QVBoxLayout" name="right_box" stretch="10,10,2">
     <item>
      <widget class="QGroupBox" name="scope_box">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="font">
        <font>
         <family>Times New Roman</family>
         <pointsize>10</pointsize>
         <bold>true</bold>
        </font>
       </property>
       <property name="title">
        <string>Oscilloscope data</string>
       </property>
       <property name="flat">
        <bool>false</bool>
       </property>
       <property name="checkable">
        <bool>false</bool>
       </property>
       <layout class="QGridLayout" name="gridLayout_16">
        <property name="spacing">
         <number>0</number>
        </property>
        <item row="0" column="0">
         <layout class="QGridLayout" name="gridLayout_4">
          <item row="0" column="0">
           <widget class="QCheckBox" name="scope_channel1">
            <property name="sizePolicy">
             <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="font">
             <font>
              <family>Times New Roman</family>
              <pointsize>10</pointsize>
              <bold>false</bold>
             </font>
            </property>
            <property name="text">
             <string>Channel 1</string>
            </property>
           </widget>
          </item>
          <item row="0" column="1">
           <widget class="QCheckBox" name="scope_channel2">
            <property name="sizePolicy">
             <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="font">
             <font>
              <family>Times New Roman</family>
              <pointsize>10</pointsize>
              <bold>false</bold>
             </font>
            </property>
            <property name="text">
             <string>Channel 2</string>
            </property>
           </widget>
          </item>
          <item row="0" column="2">
           <widget class="QCheckBox" name="scope_channel3">
            <property name="sizePolicy">
             <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="font">
             <font>
              <family>Times New Roman</family>
              <pointsize>10</pointsize>
              <bold>false</bold>
             </font>
            </property>
            <property name="text">
             <string>Channel 3</string>
            </property>
           </widget>
          </item>
          <item row="0" column="3">
           <widget class="QCheckBox" name="scope_channel4">
            <property name="sizePolicy">
             <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="font">
             <font>
              <family>Times New Roman</family>
              <pointsize>10</pointsize>
              <bold>false</bold>
             </font>
            </property>
            <property name="text">
             <string>Channel 4</string>
            </property>
           </widget>
          </item>
          <item row="2" column="0" colspan="2">
           <widget class="QPushButton" name="scope_fetch_button">
            <property name="sizePolicy">
             <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="font">
             <font>
              <family>Times New Roman</family>
              <pointsize>10</pointsize>
              <bold>false</bold>
             </font>
            </property>
            <property name="text">
             <string>FETCH DATA</string>
            </property>
           </widget>
          </item>
          <item row="2" column="2" colspan="2">
           <widget class="QPushButton" name="scope_data_save_button">
            <property name="sizePolicy">
             <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="font">
             <font>
              <family>Times New Roman</family>
              <pointsize>10</pointsize>
              <bold>false</bold>
             </font>
            </property>
            <property name="text">
             <string>SAVE</string>
            </property>
           </widget>
          </item>
          <item row="1" column="0" colspan="4">
           <widget class="QGraphicsView" name="scope_graphics_view">
            <property name="sizePolicy">
             <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="font">
             <font>
              <family>Times New Roman</family>
              <pointsize>6</pointsize>
              <bold>false</bold>
             </font>
            </property>
           </widget>
          </item>
         </layout>
        </item>
       </layout>
      </widget>
     </item>
     <item>
      <widget class="QGroupBox" name="accel_box">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="font">
        <font>
         <family>Times New Roman</family>
         <pointsize>10</pointsize>
         <bold>true</bold>
        </font>
       </property>
       <property name="title">
        <string>Accelerometer data</string>
       </property>
       <layout class="QGridLayout" name="gridLayout_8">
        <item row="1" column="0">
         <layout class="QGridLayout" name="gridLayout_5" rowstretch="10,1">
          <item row="0" column="0" colspan="3">
           <widget class="QGraphicsView" name="accel_graph">
            <property name="sizePolicy">
             <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="font">
             <font>
              <family>Times New Roman</family>
              <pointsize>8</pointsize>
              <bold>false</bold>
             </font>
            </property>
           </widget>
          </item>
          <item row="1" column="2">
           <widget class="QPushButton" name="accel_save_button">
            <property name="sizePolicy">
             <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="font">
             <font>
              <family>Times New Roman</family>
              <pointsize>10</pointsize>
              <bold>false</bold>
             </font>
            </property>
            <property name="text">
             <string>SAVE</string>
            </property>
           </widget>
          </item>
          <item row="1" column="0">
           <widget class="QPushButton" name="accel_fetch_button">
            <property name="sizePolicy">
             <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="font">
             <font>
              <family>Times New Roman</family>
              <pointsize>10</pointsize>
              <bold>false</bold>
             </font>
            </property>
            <property name="text">
             <string>CONNECT</string>
            </property>
           </widget>
          </item>
          <item row="1" column="1">
           <widget class="QPushButton" name="accel_disconnect_button">
            <property name="sizePolicy">
             <sizepolicy hsizetype="Minimum" vsizetype="Expanding">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="font">
             <font>
              <family>Times New Roman</family>
              <pointsize>10</pointsize>
              <bold>false</bold>
             </font>
            </property>
            <property name="text">
             <string>DISCONNECT</string>
            </property>
           </widget>
          </item>
         </layout>
        </item>
       </layout>
      </widget>
     </item>
     <item>
      <widget class="QGroupBox" name="output">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="styleSheet">
        <string notr="true"/>
       </property>
       <property name="title">
        <string>Messages</string>
       </property>
       <layout class="QGridLayout" name="gridLayout_15">
        <item row="1" column="0">
         <widget class="QTextEdit" name="output_message">
          <property name="sizePolicy">
           <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
            <horstretch>0</horstretch>
            <verstretch>0</verstretch>
           </sizepolicy>
          </property>
          <property name="styleSheet">
           <string notr="true">color: rgb(42, 42, 42);</string>
          </property>
          <property name="readOnly">
           <bool>true</bool>
          </property>
          <property name="html">
           <string>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;meta charset=&quot;utf-8&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
hr { height: 1px; border-width: 0; }
li.unchecked::marker { content: &quot;\2610&quot;; }
li.checked::marker { content: &quot;\2612&quot;; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
          </property>
          <property name="acceptRichText">
           <bool>true</bool>
          </property>
         </widget>
        </item>
       </layout>
      </widget>
     </item>
    </layout>
   </item>
   <item row="0" column="0" rowspan="4">
    <layout class="QVBoxLayout" name="left_box" stretch="5,6,1">
     <item>
      <widget class="QGroupBox" name="con_box">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>0</width>
         <height>30</height>
        </size>
       </property>
       <property name="font">
        <font>
         <family>Times New Roman</family>
         <pointsize>10</pointsize>
         <bold>true</bold>
        </font>
       </property>
       <property name="title">
        <string>Connected devices</string>
       </property>
       <layout class="QGridLayout" name="gridLayout_9">
        <item row="0" column="0">
         <layout class="QVBoxLayout" name="verticalLayout">
          <property name="spacing">
           <number>5</number>
          </property>
          <property name="topMargin">
           <number>5</number>
          </property>
          <item>
           <widget class="QPushButton" name="identify_res_button">
            <property name="sizePolicy">
             <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="font">
             <font>
              <family>Times New Roman</family>
              <pointsize>10</pointsize>
              <bold>false</bold>
             </font>
            </property>
            <property name="text">
             <string>IDENTIFY CONNECTED DEVICE</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QTableWidget" name="connected_devices_table">
            <property name="sizePolicy">
             <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="minimumSize">
             <size>
              <width>0</width>
              <height>20</height>
             </size>
            </property>
            <property name="font">
             <font>
              <family>Times New Roman</family>
              <pointsize>10</pointsize>
              <bold>false</bold>
             </font>
            </property>
           </widget>
          </item>
         </layout>
        </item>
       </layout>
      </widget>
     </item>
     <item>
      <widget class="QGroupBox" name="config_box">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="font">
        <font>
         <family>Times New Roman</family>
         <pointsize>10</pointsize>
         <bold>true</bold>
        </font>
       </property>
       <property name="title">
        <string>Configurations</string>
       </property>
       <layout class="QGridLayout" name="gridLayout_10">
        <item row="1" column="0">
         <widget class="QGroupBox" name="fun_config_box">
          <property name="sizePolicy">
           <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
            <horstretch>0</horstretch>
            <verstretch>0</verstretch>
           </sizepolicy>
          </property>
          <property name="font">
           <font>
            <family>Times New Roman</family>
            <pointsize>10</pointsize>
            <bold>false</bold>
           </font>
          </property>
          <property name="title">
           <string>Function Generator</string>
          </property>
          <layout class="QGridLayout" name="gridLayout_12">
           <item row="0" column="0">
            <layout class="QGridLayout" name="gridLayout">
             <property name="horizontalSpacing">
              <number>0</number>
             </property>
             <item row="0" column="0" colspan="3">
              <layout class="QHBoxLayout" name="horizontalLayout">
               <item>
                <widget class="QLabel" name="fun_id_label">
                 <property name="text">
                  <string>DEVICE ID</string>
                 </property>
                </widget>
               </item>
               <item>
                <widget class="QLineEdit" name="fun_id_input">
                 <property name="sizePolicy">
                  <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                   <horstretch>0</horstretch>
                   <verstretch>0</verstretch>
                  </sizepolicy>
                 </property>
                </widget>
               </item>
              </layout>
             </item>
             <item row="1" column="0" colspan="3">
              <layout class="QHBoxLayout" name="horizontalLayout_2">
               <item>
                <widget class="QLabel" name="waveform_type_label">
                 <property name="sizePolicy">
                  <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                   <horstretch>0</horstretch>
                   <verstretch>0</verstretch>
                  </sizepolicy>
                 </property>
                 <property name="font">
                  <font>
                   <family>Times New Roman</family>
                   <pointsize>10</pointsize>
                   <bold>false</bold>
                  </font>
                 </property>
                 <property name="text">
                  <string>WAVEFORM TYPE</string>
                 </property>
                </widget>
               </item>
               <item>
                <widget class="QComboBox" name="fun_config_waveform_input">
                 <property name="sizePolicy">
                  <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                   <horstretch>0</horstretch>
                   <verstretch>0</verstretch>
                  </sizepolicy>
                 </property>
                 <property name="font">
                  <font>
                   <family>Times New Roman</family>
                   <pointsize>10</pointsize>
                   <bold>false</bold>
                  </font>
                 </property>
                 <property name="editable">
                  <bool>false</bool>
                 </property>
                 <property name="currentText">
                  <string/>
                 </property>
                 <property name="currentIndex">
                  <number>-1</number>
                 </property>
                 <property name="placeholderText">
                  <string>Please select waveform</string>
                 </property>
                 <item>
                  <property name="text">
                   <string>Sine</string>
                  </property>
                 </item>
                 <item>
                  <property name="text">
                   <string>Triangular</string>
                  </property>
                 </item>
                 <item>
                  <property name="text">
                   <string>Square</string>
                  </property>
                 </item>
                </widget>
               </item>
              </layout>
             </item>
             <item row="2" column="0">
              <layout class="QHBoxLayout" name="horizontalLayout_3">
               <item>
                <widget class="QLabel" name="freq_input_label">
                 <property name="sizePolicy">
                  <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                   <horstretch>0</horstretch>
                   <verstretch>0</verstretch>
                  </sizepolicy>
                 </property>
                 <property name="font">
                  <font>
                   <family>Times New Roman</family>
                   <pointsize>10</pointsize>
                   <bold>false</bold>
                  </font>
                 </property>
                 <property name="text">
                  <string>FREQ</string>
                 </property>
                </widget>
               </item>
               <item>
                <widget class="QLineEdit" name="fun_config_freq_input">
                 <property name="sizePolicy">
                  <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                   <horstretch>0</horstretch>
                   <verstretch>0</verstretch>
                  </sizepolicy>
                 </property>
                 <property name="font">
                  <font>
                   <family>Times New Roman</family>
                   <pointsize>10</pointsize>
                   <bold>false</bold>
                  </font>
                 </property>
                </widget>
               </item>
              </layout>
             </item>
             <item row="2" column="1" colspan="2">
              <layout class="QHBoxLayout" name="horizontalLayout_4">
               <item>
                <widget class="QLabel" name="vpp_label">
                 <property name="sizePolicy">
                  <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                   <horstretch>0</horstretch>
                   <verstretch>0</verstretch>
                  </sizepolicy>
                 </property>
                 <property name="font">
                  <font>
                   <family>Times New Roman</family>
                   <pointsize>10</pointsize>
                   <bold>false</bold>
                  </font>
                 </property>
                 <property name="text">
                  <string>Vpp</string>
                 </property>
                </widget>
               </item>
               <item>
                <widget class="QLineEdit" name="fun_config_vpp_input">
                 <property name="sizePolicy">
                  <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                   <horstretch>0</horstretch>
                   <verstretch>0</verstretch>
                  </sizepolicy>
                 </property>
                 <property name="font">
                  <font>
                   <family>Times New Roman</family>
                   <pointsize>10</pointsize>
                   <bold>false</bold>
                  </font>
                 </property>
                 <property name="inputMethodHints">
                  <set>Qt::InputMethodHint::ImhDigitsOnly</set>
                 </property>
                </widget>
               </item>
              </layout>
             </item>
             <item row="3" column="0" colspan="2">
              <widget class="QPushButton" name="fun_save_button">
               <property name="sizePolicy">
                <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                 <horstretch>0</horstretch>
                 <verstretch>0</verstretch>
                </sizepolicy>
               </property>
               <property name="font">
                <font>
                 <family>Times New Roman</family>
                 <pointsize>10</pointsize>
                 <bold>false</bold>
                </font>
               </property>
               <property name="text">
                <string>SAVE</string>
               </property>
              </widget>
             </item>
             <item row="3" column="2">
              <widget class="QPushButton" name="fun_config_send_button">
               <property name="sizePolicy">
                <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                 <horstretch>0</horstretch>
                 <verstretch>0</verstretch>
                </sizepolicy>
               </property>
               <property name="font">
                <font>
                 <family>Times New Roman</family>
                 <pointsize>10</pointsize>
                 <bold>false</bold>
                </font>
               </property>
               <property name="text">
                <string>SEND</string>
               </property>
              </widget>
             </item>
            </layout>
           </item>
          </layout>
         </widget>
        </item>
        <item row="3" column="0">
         <widget class="QGroupBox" name="scope_config_box">
          <property name="font">
           <font>
            <family>Times New Roman</family>
            <pointsize>10</pointsize>
            <bold>false</bold>
           </font>
          </property>
          <property name="title">
           <string>Oscilloscope</string>
          </property>
          <layout class="QGridLayout" name="gridLayout_13">
           <item row="0" column="0">
            <layout class="QGridLayout" name="gridLayout_2">
             <item row="1" column="0">
              <layout class="QHBoxLayout" name="horizontalLayout_6">
               <item>
                <widget class="QLabel" name="scope_xrange_label">
                 <property name="sizePolicy">
                  <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                   <horstretch>0</horstretch>
                   <verstretch>0</verstretch>
                  </sizepolicy>
                 </property>
                 <property name="font">
                  <font>
                   <family>Times New Roman</family>
                   <pointsize>10</pointsize>
                   <bold>false</bold>
                  </font>
                 </property>
                 <property name="text">
                  <string>X RANGE</string>
                 </property>
                </widget>
               </item>
               <item>
                <widget class="QLineEdit" name="scope_config_xrange_input">
                 <property name="sizePolicy">
                  <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                   <horstretch>0</horstretch>
                   <verstretch>0</verstretch>
                  </sizepolicy>
                 </property>
                 <property name="font">
                  <font>
                   <family>Times New Roman</family>
                   <pointsize>10</pointsize>
                   <bold>false</bold>
                  </font>
                 </property>
                </widget>
               </item>
              </layout>
             </item>
             <item row="1" column="1">
              <layout class="QHBoxLayout" name="horizontalLayout_7">
               <item>
                <widget class="QLabel" name="scope_yrange_label">
                 <property name="sizePolicy">
                  <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                   <horstretch>0</horstretch>
                   <verstretch>0</verstretch>
                  </sizepolicy>
                 </property>
                 <property name="font">
                  <font>
                   <family>Times New Roman</family>
                   <pointsize>10</pointsize>
                   <bold>false</bold>
                  </font>
                 </property>
                 <property name="text">
                  <string>Y RANGE</string>
                 </property>
                </widget>
               </item>
               <item>
                <widget class="QLineEdit" name="scope_config_yrange_input">
                 <property name="sizePolicy">
                  <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                   <horstretch>0</horstretch>
                   <verstretch>0</verstretch>
                  </sizepolicy>
                 </property>
                 <property name="font">
                  <font>
                   <family>Times New Roman</family>
                   <pointsize>10</pointsize>
                   <bold>false</bold>
                  </font>
                 </property>
                </widget>
               </item>
              </layout>
             </item>
             <item row="0" column="0" colspan="2">
              <layout class="QHBoxLayout" name="horizontalLayout_5">
               <item>
                <widget class="QLabel" name="scope_id_label">
                 <property name="sizePolicy">
                  <sizepolicy hsizetype="Preferred" vsizetype="Minimum">
                   <horstretch>0</horstretch>
                   <verstretch>0</verstretch>
                  </sizepolicy>
                 </property>
                 <property name="minimumSize">
                  <size>
                   <width>0</width>
                   <height>0</height>
                  </size>
                 </property>
                 <property name="text">
                  <string>DEVICE ID</string>
                 </property>
                </widget>
               </item>
               <item>
                <widget class="QLineEdit" name="scope_config_id_input">
                 <property name="sizePolicy">
                  <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                   <horstretch>0</horstretch>
                   <verstretch>0</verstretch>
                  </sizepolicy>
                 </property>
                </widget>
               </item>
              </layout>
             </item>
             <item row="2" column="0" colspan="2">
              <layout class="QHBoxLayout" name="horizontalLayout_8">
               <item>
                <widget class="QLabel" name="scope_trigger_label">
                 <property name="sizePolicy">
                  <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                   <horstretch>0</horstretch>
                   <verstretch>0</verstretch>
                  </sizepolicy>
                 </property>
                 <property name="font">
                  <font>
                   <family>Times New Roman</family>
                   <pointsize>10</pointsize>
                   <bold>false</bold>
                  </font>
                 </property>
                 <property name="text">
                  <string>TRIGGER POS</string>
                 </property>
                </widget>
               </item>
               <item>
                <widget class="QLineEdit" name="scope_config_trigger_input">
                 <property name="sizePolicy">
                  <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                   <horstretch>0</horstretch>
                   <verstretch>0</verstretch>
                  </sizepolicy>
                 </property>
                 <property name="font">
                  <font>
                   <family>Times New Roman</family>
                   <pointsize>10</pointsize>
                   <bold>false</bold>
                  </font>
                 </property>
                </widget>
               </item>
              </layout>
             </item>
             <item row="3" column="0" colspan="2">
              <widget class="QPushButton" name="scope_config_save_button">
               <property name="sizePolicy">
                <sizepolicy hsizetype="Minimum" vsizetype="Preferred">
                 <horstretch>0</horstretch>
                 <verstretch>0</verstretch>
                </sizepolicy>
               </property>
               <property name="font">
                <font>
                 <family>Times New Roman</family>
                 <pointsize>10</pointsize>
                 <bold>false</bold>
                </font>
               </property>
               <property name="text">
                <string>SAVE</string>
               </property>
              </widget>
             </item>
            </layout>
           </item>
          </layout>
         </widget>
        </item>
        <item row="4" column="0">
         <widget class="QGroupBox" name="accel_config_box">
          <property name="font">
           <font>
            <family>Times New Roman</family>
            <pointsize>10</pointsize>
            <bold>false</bold>
           </font>
          </property>
          <property name="title">
           <string>Accelerometer</string>
          </property>
          <layout class="QGridLayout" name="gridLayout_11">
           <item row="0" column="0">
            <layout class="QGridLayout" name="gridLayout_3" rowstretch="1,1">
             <item row="0" column="1">
              <layout class="QHBoxLayout" name="horizontalLayout_10">
               <item>
                <widget class="QLabel" name="com_baud_rate_label">
                 <property name="sizePolicy">
                  <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                   <horstretch>0</horstretch>
                   <verstretch>0</verstretch>
                  </sizepolicy>
                 </property>
                 <property name="text">
                  <string>BAUD RATE</string>
                 </property>
                </widget>
               </item>
               <item>
                <widget class="QComboBox" name="com_baud_rate_input">
                 <property name="sizePolicy">
                  <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                   <horstretch>0</horstretch>
                   <verstretch>0</verstretch>
                  </sizepolicy>
                 </property>
                 <item>
                  <property name="text">
                   <string>115200</string>
                  </property>
                 </item>
                 <item>
                  <property name="text">
                   <string>57600</string>
                  </property>
                 </item>
                 <item>
                  <property name="text">
                   <string>38400</string>
                  </property>
                 </item>
                 <item>
                  <property name="text">
                   <string>19200</string>
                  </property>
                 </item>
                 <item>
                  <property name="text">
                   <string>9600</string>
                  </property>
                 </item>
                 <item>
                  <property name="text">
                   <string>4800</string>
                  </property>
                 </item>
                </widget>
               </item>
              </layout>
             </item>
             <item row="1" column="0" colspan="2">
              <widget class="QPushButton" name="accel_config_save_button">
               <property name="sizePolicy">
                <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
                 <horstretch>0</horstretch>
                 <verstretch>0</verstretch>
                </sizepolicy>
               </property>
               <property name="text">
                <string>SAVE</string>
               </property>
              </widget>
             </item>
             <item row="0" column="0">
              <layout class="QHBoxLayout" name="horizontalLayout_9">
               <item>
                <widget class="QLabel" name="accel_com_label">
                 <property name="sizePolicy">
                  <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                   <horstretch>0</horstretch>
                   <verstretch>0</verstretch>
                  </sizepolicy>
                 </property>
                 <property name="font">
                  <font>
                   <family>Times New Roman</family>
                   <pointsize>10</pointsize>
                   <bold>false</bold>
                  </font>
                 </property>
                 <property name="text">
                  <string>COM PORT</string>
                 </property>
                </widget>
               </item>
               <item>
                <widget class="QLineEdit" name="accel_config_com_input">
                 <property name="sizePolicy">
                  <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                   <horstretch>0</horstretch>
                   <verstretch>0</verstretch>
                  </sizepolicy>
                 </property>
                 <property name="font">
                  <font>
                   <family>Times New Roman</family>
                   <pointsize>14</pointsize>
                   <bold>false</bold>
                  </font>
                 </property>
                </widget>
               </item>
              </layout>
             </item>
            </layout>
           </item>
          </layout>
         </widget>
        </item>
       </layout>
      </widget>
     </item>
     <item>
      <widget class="QGroupBox" name="information_box">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="font">
        <font>
         <family>Times New Roman</family>
         <pointsize>12</pointsize>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(197, 197, 197);</string>
       </property>
       <property name="title">
        <string/>
       </property>
       <property name="alignment">
        <set>Qt::AlignmentFlag::AlignCenter</set>
       </property>
       <layout class="QGridLayout" name="gridLayout_6" rowstretch="3,2,1">
        <item row="0" column="0" colspan="2">
         <widget class="QLabel" name="project_name">
          <property name="sizePolicy">
           <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
            <horstretch>0</horstretch>
            <verstretch>0</verstretch>
           </sizepolicy>
          </property>
          <property name="font">
           <font>
            <family>Times New Roman</family>
            <pointsize>16</pointsize>
            <bold>true</bold>
           </font>
          </property>
          <property name="text">
           <string>Frequency tunable Triboelectric Energy Harvester</string>
          </property>
          <property name="alignment">
           <set>Qt::AlignmentFlag::AlignCenter</set>
          </property>
         </widget>
        </item>
        <item row="1" column="0" colspan="2">
         <widget class="QLabel" name="author">
          <property name="font">
           <font>
            <family>Times New Roman</family>
            <pointsize>12</pointsize>
            <bold>true</bold>
           </font>
          </property>
          <property name="text">
           <string>Dr. Sagar Hosangadi Prutvi, Post Doc Researcher @ LivMatS cluster</string>
          </property>
          <property name="alignment">
           <set>Qt::AlignmentFlag::AlignHCenter|Qt::AlignmentFlag::AlignTop</set>
          </property>
         </widget>
        </item>
        <item row="2" column="0">
         <widget class="QGraphicsView" name="imtek_logo">
          <property name="sizePolicy">
           <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
            <horstretch>0</horstretch>
            <verstretch>0</verstretch>
           </sizepolicy>
          </property>
          <property name="minimumSize">
           <size>
            <width>0</width>
            <height>30</height>
           </size>
          </property>
         </widget>
        </item>
        <item row="2" column="1">
         <widget class="QGraphicsView" name="logo_space">
          <property name="sizePolicy">
           <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
            <horstretch>0</horstretch>
            <verstretch>0</verstretch>
           </sizepolicy>
          </property>
          <property name="minimumSize">
           <size>
            <width>0</width>
            <height>30</height>
           </size>
          </property>
         </widget>
        </item>
       </layout>
      </widget>
     </item>
    </layout>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
