# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Fri Jul 11 02:09:53 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 600)
        MainWindow.setMinimumSize(QtCore.QSize(700, 600))
        MainWindow.setMaximumSize(QtCore.QSize(700, 600))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(682, 582))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.actorTab = QtGui.QWidget()
        self.actorTab.setObjectName("actorTab")
        self.verticalLayout = QtGui.QVBoxLayout(self.actorTab)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtGui.QGroupBox(self.actorTab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.buscarANombreLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.buscarANombreLineEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.buscarANombreLineEdit.setObjectName("buscarANombreLineEdit")
        self.horizontalLayout_5.addWidget(self.buscarANombreLineEdit)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.buscarAPeliculaComboBox = QtGui.QComboBox(self.groupBox_2)
        self.buscarAPeliculaComboBox.setMinimumSize(QtCore.QSize(150, 0))
        self.buscarAPeliculaComboBox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.buscarAPeliculaComboBox.setObjectName("buscarAPeliculaComboBox")
        self.horizontalLayout_5.addWidget(self.buscarAPeliculaComboBox)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.widget = QtGui.QWidget(self.actorTab)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_3 = QtGui.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.actoresTreeView = QtGui.QTreeView(self.widget_3)
        self.actoresTreeView.setMinimumSize(QtCore.QSize(0, 0))
        self.actoresTreeView.setProperty("cursor", QtCore.Qt.PointingHandCursor)
        self.actoresTreeView.setFrameShadow(QtGui.QFrame.Sunken)
        self.actoresTreeView.setEditTriggers(QtGui.QAbstractItemView.AnyKeyPressed)
        self.actoresTreeView.setTabKeyNavigation(True)
        self.actoresTreeView.setAlternatingRowColors(True)
        self.actoresTreeView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.actoresTreeView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.actoresTreeView.setTextElideMode(QtCore.Qt.ElideRight)
        self.actoresTreeView.setIndentation(0)
        self.actoresTreeView.setRootIsDecorated(False)
        self.actoresTreeView.setSortingEnabled(True)
        self.actoresTreeView.setAnimated(True)
        self.actoresTreeView.setWordWrap(True)
        self.actoresTreeView.setObjectName("actoresTreeView")
        self.actoresTreeView.header().setCascadingSectionResizes(False)
        self.actoresTreeView.header().setDefaultSectionSize(110)
        self.actoresTreeView.header().setSortIndicatorShown(True)
        self.actoresTreeView.header().setStretchLastSection(True)
        self.horizontalLayout_4.addWidget(self.actoresTreeView)
        self.horizontalLayout_3.addWidget(self.widget_3)
        self.widget_4 = QtGui.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.actorImagenLabel = QtGui.QLabel(self.widget_4)
        self.actorImagenLabel.setMinimumSize(QtCore.QSize(200, 240))
        self.actorImagenLabel.setMaximumSize(QtCore.QSize(200, 240))
        self.actorImagenLabel.setText("")
        self.actorImagenLabel.setScaledContents(True)
        self.actorImagenLabel.setObjectName("actorImagenLabel")
        self.verticalLayout_2.addWidget(self.actorImagenLabel)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_3.addWidget(self.widget_4)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.actorTab)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 49))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 49))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtGui.QSpacerItem(306, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.nuevoAButton = QtGui.QPushButton(self.widget_2)
        self.nuevoAButton.setObjectName("nuevoAButton")
        self.horizontalLayout_2.addWidget(self.nuevoAButton)
        self.editarAButton = QtGui.QPushButton(self.widget_2)
        self.editarAButton.setObjectName("editarAButton")
        self.horizontalLayout_2.addWidget(self.editarAButton)
        self.borrarAButton = QtGui.QPushButton(self.widget_2)
        self.borrarAButton.setObjectName("borrarAButton")
        self.horizontalLayout_2.addWidget(self.borrarAButton)
        self.verticalLayout.addWidget(self.widget_2)
        self.tabWidget.addTab(self.actorTab, "")
        self.peliculaTab = QtGui.QWidget()
        self.peliculaTab.setObjectName("peliculaTab")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.peliculaTab)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_3 = QtGui.QGroupBox(self.peliculaTab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.buscarPNombreLineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.buscarPNombreLineEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.buscarPNombreLineEdit.setObjectName("buscarPNombreLineEdit")
        self.horizontalLayout_6.addWidget(self.buscarPNombreLineEdit)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.buscarPActorComboBox = QtGui.QComboBox(self.groupBox_3)
        self.buscarPActorComboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.buscarPActorComboBox.setObjectName("buscarPActorComboBox")
        self.horizontalLayout_6.addWidget(self.buscarPActorComboBox)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.widget_5 = QtGui.QWidget(self.peliculaTab)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.widget_5)
        self.horizontalLayout_8.setContentsMargins(0, -1, -1, 9)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.widget_8 = QtGui.QWidget(self.widget_5)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.widget_8)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.peliculasTableView = QtGui.QTableView(self.widget_8)
        self.peliculasTableView.setMinimumSize(QtCore.QSize(0, 0))
        self.peliculasTableView.setProperty("cursor", QtCore.Qt.PointingHandCursor)
        self.peliculasTableView.setEditTriggers(QtGui.QAbstractItemView.AnyKeyPressed)
        self.peliculasTableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.peliculasTableView.setObjectName("peliculasTableView")
        self.horizontalLayout_9.addWidget(self.peliculasTableView)
        self.horizontalLayout_8.addWidget(self.widget_8)
        self.widget_9 = QtGui.QWidget(self.widget_5)
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget_9)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.peliculaImagenLabel = QtGui.QLabel(self.widget_9)
        self.peliculaImagenLabel.setMinimumSize(QtCore.QSize(200, 240))
        self.peliculaImagenLabel.setMaximumSize(QtCore.QSize(200, 240))
        self.peliculaImagenLabel.setText("")
        self.peliculaImagenLabel.setObjectName("peliculaImagenLabel")
        self.verticalLayout_4.addWidget(self.peliculaImagenLabel)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.horizontalLayout_8.addWidget(self.widget_9)
        self.verticalLayout_5.addWidget(self.widget_5)
        self.groupBox = QtGui.QGroupBox(self.peliculaTab)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 80))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 9)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.tramaPLabel = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(10)
        font.setItalic(True)
        self.tramaPLabel.setFont(font)
        self.tramaPLabel.setText("")
        self.tramaPLabel.setWordWrap(True)
        self.tramaPLabel.setObjectName("tramaPLabel")
        self.horizontalLayout_11.addWidget(self.tramaPLabel)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.widget_10 = QtGui.QWidget(self.peliculaTab)
        self.widget_10.setMinimumSize(QtCore.QSize(0, 49))
        self.widget_10.setMaximumSize(QtCore.QSize(16777215, 49))
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.widget_10)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem5 = QtGui.QSpacerItem(306, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.nuevoPButton = QtGui.QPushButton(self.widget_10)
        self.nuevoPButton.setObjectName("nuevoPButton")
        self.horizontalLayout_10.addWidget(self.nuevoPButton)
        self.editarPButton = QtGui.QPushButton(self.widget_10)
        self.editarPButton.setObjectName("editarPButton")
        self.horizontalLayout_10.addWidget(self.editarPButton)
        self.pushButton_9 = QtGui.QPushButton(self.widget_10)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_10.addWidget(self.pushButton_9)
        self.verticalLayout_5.addWidget(self.widget_10)
        self.tabWidget.addTab(self.peliculaTab, "")
        self.verticalLayout_3.addWidget(self.tabWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.buscarANombreLineEdit)
        MainWindow.setTabOrder(self.buscarANombreLineEdit, self.buscarAPeliculaComboBox)
        MainWindow.setTabOrder(self.buscarAPeliculaComboBox, self.actoresTreeView)
        MainWindow.setTabOrder(self.actoresTreeView, self.nuevoAButton)
        MainWindow.setTabOrder(self.nuevoAButton, self.editarAButton)
        MainWindow.setTabOrder(self.editarAButton, self.borrarAButton)
        MainWindow.setTabOrder(self.borrarAButton, self.buscarPNombreLineEdit)
        MainWindow.setTabOrder(self.buscarPNombreLineEdit, self.buscarPActorComboBox)
        MainWindow.setTabOrder(self.buscarPActorComboBox, self.peliculasTableView)
        MainWindow.setTabOrder(self.peliculasTableView, self.nuevoPButton)
        MainWindow.setTabOrder(self.nuevoPButton, self.editarPButton)
        MainWindow.setTabOrder(self.editarPButton, self.pushButton_9)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Séptimo Arte", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Buscar actor por:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Película:", None, QtGui.QApplication.UnicodeUTF8))
        self.nuevoAButton.setText(QtGui.QApplication.translate("MainWindow", "&Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.editarAButton.setText(QtGui.QApplication.translate("MainWindow", "&Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.borrarAButton.setText(QtGui.QApplication.translate("MainWindow", "&Borrar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.actorTab), QtGui.QApplication.translate("MainWindow", "&Actores", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Buscar película por:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Actor:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Trama:", None, QtGui.QApplication.UnicodeUTF8))
        self.nuevoPButton.setText(QtGui.QApplication.translate("MainWindow", "&Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.editarPButton.setText(QtGui.QApplication.translate("MainWindow", "&Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_9.setText(QtGui.QApplication.translate("MainWindow", "&Borrar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.peliculaTab), QtGui.QApplication.translate("MainWindow", "&Películas", None, QtGui.QApplication.UnicodeUTF8))

