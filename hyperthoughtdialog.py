# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/mjackson/Workspace4/EasyBake/hyperthoughtdialog.ui',
# licensing of '/Users/mjackson/Workspace4/EasyBake/hyperthoughtdialog.ui' applies.
#
# Created: Mon Jun 21 13:12:38 2021
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_HyperthoughtDialog(object):
    def setupUi(self, HyperthoughtDialog):
        HyperthoughtDialog.setObjectName("HyperthoughtDialog")
        HyperthoughtDialog.resize(736, 481)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HyperthoughtDialog.sizePolicy().hasHeightForWidth())
        HyperthoughtDialog.setSizePolicy(sizePolicy)
        HyperthoughtDialog.setWindowTitle("")
        HyperthoughtDialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(HyperthoughtDialog)
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(HyperthoughtDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.parentDirectoryButton = QtWidgets.QToolButton(self.frame)
        self.parentDirectoryButton.setStatusTip("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/arrow-top@2x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.parentDirectoryButton.setIcon(icon)
        self.parentDirectoryButton.setIconSize(QtCore.QSize(16, 16))
        self.parentDirectoryButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.parentDirectoryButton.setObjectName("parentDirectoryButton")
        self.horizontalLayout_2.addWidget(self.parentDirectoryButton)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.directoryLabel = QtWidgets.QLabel(self.frame)
        self.directoryLabel.setObjectName("directoryLabel")
        self.horizontalLayout.addWidget(self.directoryLabel)
        spacerItem = QtWidgets.QSpacerItem(569, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.newFolderButton = QtWidgets.QToolButton(self.frame)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/resources/folder@2x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newFolderButton.setIcon(icon1)
        self.newFolderButton.setIconSize(QtCore.QSize(16, 16))
        self.newFolderButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.newFolderButton.setObjectName("newFolderButton")
        self.horizontalLayout.addWidget(self.newFolderButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.frame, 2, 0, 1, 12)
        self.locationLineEdit = QtWidgets.QLineEdit(HyperthoughtDialog)
        self.locationLineEdit.setObjectName("locationLineEdit")
        self.gridLayout.addWidget(self.locationLineEdit, 4, 1, 1, 11)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(HyperthoughtDialog)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.ht_server_url = QtWidgets.QLabel(HyperthoughtDialog)
        self.ht_server_url.setObjectName("ht_server_url")
        self.horizontalLayout_3.addWidget(self.ht_server_url)
        self.label_3 = QtWidgets.QLabel(HyperthoughtDialog)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.ht_username = QtWidgets.QLabel(HyperthoughtDialog)
        self.ht_username.setObjectName("ht_username")
        self.horizontalLayout_3.addWidget(self.ht_username)
        self.label_2 = QtWidgets.QLabel(HyperthoughtDialog)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.token_expiration = QtWidgets.QLabel(HyperthoughtDialog)
        self.token_expiration.setObjectName("token_expiration")
        self.horizontalLayout_3.addWidget(self.token_expiration)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 12)
        self.apiKeyLineEdit = QtWidgets.QLineEdit(HyperthoughtDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apiKeyLineEdit.sizePolicy().hasHeightForWidth())
        self.apiKeyLineEdit.setSizePolicy(sizePolicy)
        self.apiKeyLineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.apiKeyLineEdit.setObjectName("apiKeyLineEdit")
        self.gridLayout.addWidget(self.apiKeyLineEdit, 0, 2, 1, 9)
        self.apiKeyLabel = QtWidgets.QLabel(HyperthoughtDialog)
        self.apiKeyLabel.setObjectName("apiKeyLabel")
        self.gridLayout.addWidget(self.apiKeyLabel, 0, 0, 1, 2)
        self.apiKeyButton = QtWidgets.QPushButton(HyperthoughtDialog)
        self.apiKeyButton.setObjectName("apiKeyButton")
        self.gridLayout.addWidget(self.apiKeyButton, 0, 11, 1, 1)
        self.locationLabel = QtWidgets.QLabel(HyperthoughtDialog)
        self.locationLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.locationLabel.setObjectName("locationLabel")
        self.gridLayout.addWidget(self.locationLabel, 4, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(HyperthoughtDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 5, 10, 1, 2)
        self.listView = DeselectableListView(HyperthoughtDialog)
        self.listView.setAlternatingRowColors(True)
        self.listView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.listView.setUniformItemSizes(True)
        self.listView.setSelectionRectVisible(True)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 3, 0, 1, 12)
        spacerItem1 = QtWidgets.QSpacerItem(380, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 10)

        self.retranslateUi(HyperthoughtDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), HyperthoughtDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), HyperthoughtDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HyperthoughtDialog)

    def retranslateUi(self, HyperthoughtDialog):
        self.parentDirectoryButton.setToolTip(QtWidgets.QApplication.translate("HyperthoughtDialog", "Move Up a Directory", None, -1))
        self.parentDirectoryButton.setText(QtWidgets.QApplication.translate("HyperthoughtDialog", "Up", None, -1))
        self.directoryLabel.setText(QtWidgets.QApplication.translate("HyperthoughtDialog", "/", None, -1))
        self.newFolderButton.setToolTip(QtWidgets.QApplication.translate("HyperthoughtDialog", "Create Remote Folder", None, -1))
        self.newFolderButton.setText(QtWidgets.QApplication.translate("HyperthoughtDialog", "New Remote Folder", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("HyperthoughtDialog", "Server:", None, -1))
        self.ht_server_url.setText(QtWidgets.QApplication.translate("HyperthoughtDialog", "Not Autheticated", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("HyperthoughtDialog", "User:", None, -1))
        self.ht_username.setText(QtWidgets.QApplication.translate("HyperthoughtDialog", "Not Autheticated", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("HyperthoughtDialog", "Expires:", None, -1))
        self.token_expiration.setText(QtWidgets.QApplication.translate("HyperthoughtDialog", "Not Autheticated", None, -1))
        self.apiKeyLabel.setText(QtWidgets.QApplication.translate("HyperthoughtDialog", "Hyperthought API Key:", None, -1))
        self.apiKeyButton.setText(QtWidgets.QApplication.translate("HyperthoughtDialog", "Authenticate", None, -1))
        self.locationLabel.setText(QtWidgets.QApplication.translate("HyperthoughtDialog", "Folder:", None, -1))

from ht_widgets.deselectable_list_view import DeselectableListView
import resources_rc
