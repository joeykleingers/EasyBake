from PySide2.QtNetwork import QNetworkReply
from PySide2.QtCore import QAbstractTableModel, Qt, QModelIndex
from PySide2.QtGui import QIcon, QColor
from PySide2.QtWidgets import QApplication, QStyle



class TableModelC(QAbstractTableModel):
    def __init__(self,data ,parent=None):
        QAbstractTableModel.__init__(self, parent)
        self.metadataList = []
        visited = {}
        queue = []
        grandParents = {}
        source = ""
        self.hiddenList = []
        self.treeDict = data
        self.requiredList = []


    def rowCount(self, parent=QModelIndex()):
        return len(self.metadataList)

    def columnCount(self, parent=QModelIndex()):
        return 9

    def data(self, index, role):
        if role == Qt.DisplayRole:
            if index.column() == 0:
                return index.row()
            elif index.column() == 1:
                return self.metadataList[index.row()]["Key"]
            elif index.column() == 2:
                if self.metadataList[index.row()]["Value"] == "None":
                    return ""
                return str(self.metadataList[index.row()]["Value"])
            elif index.column() == 3:
                return self.metadataList[index.row()]["Source"]
            #elif index.column() == 4:
            #    return self.metadataList[index.row()][0]
            elif index.column() == 5:
                return str(type(self.metadataList[index.row()]["Value"])).split("'")[1].upper()
        elif role == Qt.CheckStateRole:
            if index.column() == 6:
                return self.metadataList[index.row()]["Required"]
            elif index.column() == 7:
                return self.metadataList[index.row()]["Editable"]

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return
        if orientation == Qt.Horizontal:
            if section == 0:
                return "#^"
            elif section == 1:
                return "HT Name"
            elif section == 2:
                return "HT Value"
            elif section == 3:
                return "Source"
            elif section == 4:
                return "Default Value"
            elif section == 5:
                return "Type"
            elif section == 6:
                return "Require"
            elif section == 7:
                return "Editable"
            elif section == 8:
                return " "
            return None
    def setData(self,index, value, role):
        if role == Qt.EditRole:
            if not index.isValid():
                return False
            if index.column() == 0:
                if int(value) > -1 and int(value) < len(self.metadataList):
                    temp = self.metadataList[int(value)]
                    self.metadataList[int(value)] = self.metadataList[index.row()]
                    self.metadataList[index.row()] = temp
            if index.column() == 1:
                if self.metadataList[index.row()]["Source"] == "Custom Input":

                    self.metadataList[index.row()]["Key"] = value
                    self.dataChanged.emit(index, index)
            elif index.column() == 2:
                treeDict = self.treeDict
                sourcePath = self.metadataList[index.row()]["Source"].split("/")
                for i in range(len(sourcePath)-1):
                    treeDict = treeDict[sourcePath[i]]
                treeDict[sourcePath[-1]] = value
                self.metadataList[index.row()]["Value"] = value
                self.dataChanged.emit(index, index)
            elif index.column() == 8:
                self.metadataList.remove(index.row())

            return True
        elif role == Qt.CheckStateRole:
            if index.column() == 6 or index.column() == 7:
                self.changeChecked(index)
                self.dataChanged.emit(index, index)
            return True

        return False

    def changeChecked(self, index):
        if index.column() == 6:
            if self.metadataList[index.row()]["Required"] == 0:
                self.metadataList[index.row()]["Required"] = 2
                self.requiredList.append(self.metadataList[index.row()]["Key"])
            else:
                self.metadataList[index.row()]["Required"] = 0
                self.requiredList.remove(self.metadataList[index.row()]["Key"])
            print(self.requiredList)
        elif index.column() == 7:
            if self.metadataList[index.row()]["Editable"] == 0:
                self.metadataList[index.row()]["Editable"] = 2
            else:
                self.metadataList[index.row()]["Editable"] = 0

    def flags(self, index):
        if not index.isValid():

            return Qt.ItemIsEnabled
        if index.column() == 2:
            if self.metadataList[index.row()]["Editable"] == 2:
                return Qt.ItemFlags(QAbstractTableModel.flags(self,index) | Qt.ItemIsEditable)
        elif index.column() == 8 or index.column() == 0:
            return Qt.ItemFlags(QAbstractTableModel.flags(self,index) | Qt.ItemIsEditable)
        elif index.column() == 6 or index.column() == 7:
            return Qt.ItemFlags(QAbstractTableModel.flags(self,index) | Qt.ItemIsUserCheckable)
        else:
            if index.data() == "":
                return Qt.ItemFlags(QAbstractTableModel.flags(self,index) | Qt.ItemIsEditable)
            return Qt.ItemIsEnabled

    def addRow(self, dataDict, source, value):
        self.beginInsertRows(self.index(len(self.metadataList),0), len(self.metadataList),len(self.metadataList))
        self.metadataList.append({"Key":value,"Value":dataDict[value],"Source":source+value,"Checked":0,"Required":0,"Editable":0})
        self.endInsertRows()

    def addEmptyRow(self):
        self.beginInsertRows(self.index(len(self.metadataList),0), len(self.metadataList),len(self.metadataList))
        self.metadataList.append({"Key":"","Value":"","Source":"Custom Input","Checked":0,"Required":0,"Editable":0})
        self.endInsertRows()




