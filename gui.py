from PyQt5.QtWidgets import *
from statistics import mean
from PyQt5 import (QtCore, QtGui)
import random
from designer_python import Ui_MainWindow
from PyQt5.QtCore import QProcess
import sys
import re
from main import *



crossover_type = '0'


mutation_val = 0.1  # float(input(f"Set Mutation Probablity: "))

progress_re = re.compile("Total complete: (\d+)%")




def simple_percent_parser(output):
    """
    Matches lines using the progress_re regex,
    returning a single integer for the % progress.
    """
    m = progress_re.search(output)
    if m:
        pc_complete = m.group(1)
        return int(pc_complete)



if __name__ == '__main__':
 class gui(QMainWindow) :


    def __init__(self):
        super(). __init__()

        self.p = None



        #loadUi("untitled.ui", self)

        self.ui = Ui_MainWindow()
        self.strt = bam()
        self.ui.setupUi(self)

        self.progress = QProgressBar()
        self.progress.setRange(0, 100)

        self.ui.pushButton.clicked.connect(self.save_text)
        self.ui.pushButton_2.clicked.connect(self.start_program)
        self.ui.radioButton.toggled.connect(self.singlecross)
        self.ui.radioButton_2.toggled.connect(self.multicross)




    def save_text(self):

        with open('fitness.py','w') as f:
              my_text = self.ui.lineEdit_5.toPlainText()
              f.write(my_text)


    def message(self, s):

        self.ui.textBrowser_2.appendPlainText(s)







    def start_program(self):
        if self.p is None:  # No process running.


            self.message("Executing process")
            self.p = QtCore.QProcess(self)  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start("python3", ['main.py'])
















    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        # Extract progress if it is in the data.
        progress = simple_percent_parser(stderr)
        if progress:
            self.progress.setValue(progress)
        self.message(stderr)

    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.message(stdout)

    def handle_state(self, state):
        states = {
            QProcess.NotRunning: 'Not running',
            QProcess.Starting: 'Starting',
            QProcess.Running: 'Running',
        }


        state_name = states[state]
        self.message(f"State changed: {state_name}")





    def process_finished(self):
        self.message("Process finished.")
        self.p = None

    def multicross(self):


        self.crossover_type = "1"

    def singlecross(self):


        crossover_type = '0'



    def mutation(ind, m):
         for k, v in enumerate(ind):
             if random.random() < m:
                 ind[k] = random.randint(0, 6)
         return ind


    def crossover_singlepoint(ind1, ind2):
         # print(f"111111")

         p = random.randint(0, len(ind1))
         c1 = ind1[0: p] + ind2[p:]
         c2 = ind2[0: p] + ind1[p:]
         return c1, c2


    def crossover_multipoint(ind1, ind2):
         # print(f"222222")
         p3 = random.randint(0, len(ind1))
         p4 = random.randint(0, len(ind1) - 1)
         c1 = ind1[p3: p4] + ind2[p3:p4]
         c2 = ind2[p4: p3] + ind1[p4:p3]
         return c1, c2













 app = QApplication([])

 window = gui()
 window.show()
 app.exec_()

