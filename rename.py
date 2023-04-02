import pathlib
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile

class Rename:
          def __init__(self) :
             qfile_rename = QFile("rename.ui")
             qfile_rename.open(QFile.ReadOnly)
             qfile_rename.close()   
             self.ui = QUiLoader().load(qfile_rename)
             self.ui.RUNButton.clicked.connect(self.rename_photos)
             
             
          def rename_photos(self):
               checkbox = self.ui.checkBox.isChecked()
               filename = self.ui.FilenametextEdit.toPlainText()
               path = pathlib.Path('.') / "photos"
               for folder in path.iterdir():
                   if folder.is_dir():
                        counter  = 1
                        for file in folder.iterdir():
                             if file.is_file():
                                  if checkbox == True:
                                        new_file = folder.name + "_" + str(counter) + file.suffix
                                        file.rename(path / folder.name / new_file)
                                        counter += 1
                                  else:
                                       new_file = filename + "_" + str(counter) + file.suffix
                                       file.rename(path / folder.name / new_file)
                                       counter += 1
                                   
                                 
app = QApplication([])
stats = Rename()
stats.ui.show()
app.exec_()