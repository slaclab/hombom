from pydm import Display
from PyQt5 import QtGui
import numpy as np

class HomBom(Display):

    def __init__(self, parent=None, args=None, pixmapname='HOM_Sketches_Cryomodule.png'):
        super(HomBom, self).__init__(parent=parent, args=args)

    def ui_filename(self):
        return 'hombom.ui'

    def absPV(self, PV):
        return np.abs(PV)

    #def resizeImageWithQT(pixmapname, dest):
    #    #https://stackoverflow.com/questions/21802868/python-how-to-resize-raster-image-with-pyqt
    #    pixmap = QtGui.QPixmap(pixmapname)
    #    pixmap_resized = pixmap.scaled(720, 405, QtCore.Qt.KeepAspectRatio)
    #    if not os.path.exists(os.path.dirname(dest)): os.makedirs(os.path.dirname(dest))
    #    pixmap_resized.save(dest)


    #def updatePower(self):
    #    button = self.ui.devPanelLisa

#intelclass = HomBom



#class Example(Display):
#
#    def __init__(self, parent=None, args=None):
#        super(Example, self).__init__(parent=parent, args=args)
#        self.ui.testButton.clicked.connect(lambda:self.updateOutput("Button Pushed"))
#        self.ui.testCheckBox.stateChanged.connect(self.buttonToggled)
#
#    def ui_filename(self):
#        return 'example.ui'
#
#    def updateOutput(self, output):
#        print(output)
#        self.ui.outputBox.setText(output)
#
#    def buttonToggled(self):
#        self.ui.outputBox.setText("Checkbox is " + ("checked"
#                                  if self.ui.testCheckBox.isChecked()
#                                  else "not checked"))
#
