# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/blogin/PycharmProjects/DMT-git/src/ui/ui_proposals.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ProposalsDlg(object):
    def setupUi(self, ProposalsDlg):
        ProposalsDlg.setObjectName("ProposalsDlg")
        ProposalsDlg.resize(786, 428)
        ProposalsDlg.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(ProposalsDlg)
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblMessage = QtWidgets.QLabel(ProposalsDlg)
        self.lblMessage.setText("")
        self.lblMessage.setWordWrap(True)
        self.lblMessage.setObjectName("lblMessage")
        self.verticalLayout.addWidget(self.lblMessage)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(ProposalsDlg)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.propsView = QtWidgets.QTableView(ProposalsDlg)
        self.propsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.propsView.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.propsView.setAlternatingRowColors(True)
        self.propsView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.propsView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.propsView.setShowGrid(True)
        self.propsView.setSortingEnabled(False)
        self.propsView.setObjectName("propsView")
        self.propsView.verticalHeader().setVisible(False)
        self.propsView.verticalHeader().setCascadingSectionResizes(False)
        self.propsView.verticalHeader().setHighlightSections(False)
        self.verticalLayout.addWidget(self.propsView)
        self.buttonBox = QtWidgets.QDialogButtonBox(ProposalsDlg)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ProposalsDlg)
        QtCore.QMetaObject.connectSlotsByName(ProposalsDlg)

    def retranslateUi(self, ProposalsDlg):
        _translate = QtCore.QCoreApplication.translate
        ProposalsDlg.setWindowTitle(_translate("ProposalsDlg", "Dialog"))
        self.pushButton.setText(_translate("ProposalsDlg", "Columns"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProposalsDlg = QtWidgets.QDialog()
    ui = Ui_ProposalsDlg()
    ui.setupUi(ProposalsDlg)
    ProposalsDlg.show()
    sys.exit(app.exec_())

