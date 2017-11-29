from PyQt5 import QtGui, QtCore,QtWidgets
from Ui_MplMainWindow import Ui_MainWindow
class Code_MainWindow(Ui_MainWindow):
	
	def __init__(self, parent = None):
		super(Code_MainWindow, self).__init__(parent)
	
		self.setupUi(self)
		self.btnStart.clicked.connect(self.startPlot)
		self.btnPause.clicked.connect(self.pausePlot)
	def startPlot(self):
		''' begin to plot'''
		self.mplCanvas.startPlot()
		pass
		
	def pausePlot(self):
		''' pause plot '''
		self.mplCanvas.pausePlot()
		pass
		
	def releasePlot(self):
		''' stop and release thread'''
		self.mplCanvas.releasePlot()

	def closeEvent(self,event):
		result = QtGui.QMessageBox.question(self,
				"Confirm Exit...",
				"Are you sure you want to exit ?",
				QtGui.QMessageBox.Yes| QtGui.QMessageBox.No)
		event.ignore()

		if result == QtGui.QMessageBox.Yes:
			self.releasePlot()#release thread's resouce
			event.accept()

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	ui = Code_MainWindow()
	ui.show()
	sys.exit(app.exec_())