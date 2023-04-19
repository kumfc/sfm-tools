########
sfm = None
debug = True
########

from PySide import QtGui


def MessageBoxInfo(text, window):
    msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Information, "Info", text, QtGui.QMessageBox.NoButton, window)
    msgBox.addButton("&Continue", QtGui.QMessageBox.RejectRole)
    if msgBox.exec_() == QtGui.QMessageBox.AcceptRole:
        pass


def MessageBoxError(text, window):
    msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Critical, "Error", text, QtGui.QMessageBox.NoButton, window)
    msgBox.addButton("&Continue", QtGui.QMessageBox.RejectRole)
    if msgBox.exec_() == QtGui.QMessageBox.AcceptRole:
        pass


class Log():
    @staticmethod
    def info(msg):
        sfm.Msg('[Python] [*] ' + str(msg) + '\n')

    @staticmethod
    def debug(msg):
        if debug:
            sfm.Msg('[Python] [DEBUG] ' + str(msg) + '\n')