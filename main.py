from PyQt5.QtWidgets import *
from statistics import mean
from PyQt5 import (QtCore)
from PyQt5 import QtGui

from designer_python import Ui_MainWindow
from PyQt5.QtCore import QProcess
import sys
import re
from fitness import *

progress_re = re.compile("Total complete: (\d+)%")


class Stream(QtCore.QObject):
    """Redirects console output to text widget."""
    newText = QtCore.pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))


def simple_percent_parser(output):
    """
    Matches lines using the progress_re regex,
    returning a single integer for the % progress.
    """
    m = progress_re.search(output)
    if m:
        pc_complete = m.group(1)
        return int(pc_complete)

class GeneticAlgorithm():
    def __init__(self):
        super(). __init__()
        self.mutation_val = 0.1  # float(input(f"Set Mutation Probablity: "))

    def mutation(self, ind, m):
        for k, v in enumerate(ind):
            if random.random() < m:
                ind[k] = random.randint(0, 6)
        return ind

    def crossover_singlepoint(self, ind1, ind2):
        # print(f"111111")
        p = random.randint(0, len(ind1))
        self.c1 = ind1[0: p] + ind2[p:]
        self.c2 = ind2[0: p] + ind1[p:]
        return self.c1, self.c2

    def crossover_multipoint(self, ind1, ind2):
        # print(f"222222")
        p3 = random.randint(0, len(ind1))
        p4 = random.randint(0, len(ind1) - 1)
        c1 = ind1[p3: p4] + ind2[p3:p4]
        c2 = ind2[p4: p3] + ind1[p4:p3]
        return c1, c2

if __name__ == '__main__':
 class gui(QMainWindow):
    def __init__(self):
        super(). __init__()
        self.dispatcher = {'0': self.crossover_singlepoint, '1': self.crossover_multipoint}
        self.p = None
        self.GA = GeneticAlgorithm()
        self.crossover_type = '0'
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.ui.lineEdit_2.setText("0")
        self.ui.lineEdit.setText("0")
        self.G = int(self.ui.lineEdit_2.text()) # input(int(f"umber of generations"))  # number of generations 200
        self.N = int(self.ui.lineEdit.text())  # input(int(f"number of individuals in population"))  # number of individuals in population 100
        self.c2 = list()
        self.c1 = list()
        self.ui.pushButton.clicked.connect(self.save_text)

        sys.stdout = Stream(newText=self.onUpdateText)
        self.ui.pushButton_2.clicked.connect(self.start_program)
        #self.ui.pushButton_2.clicked.connect(lambda: self.ui.textBrowser_2.appendPlainText(str(self.start_program())))

        self.ui.radioButton.toggled.connect(self.singlecross)
        self.ui.radioButton_2.clicked.connect(self.multicross)
        self.ui.pushButton_3.clicked.connect(self.display_text)
        self.ui.radioButton.setChecked(True)
        self.ui.radioButton_5.setChecked(True)
        self.ui.checkBox.setChecked(True)
        self.ui.radioButton_9.setChecked(True)
        self.display_text()
        self.ui.lineEdit_3.setText('N/A')

    def onUpdateText(self, text):
        """Write console output to text widget."""
        cursor = self.ui.textBrowser_2.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.ui.textBrowser_2.setTextCursor(cursor)
        self.ui.textBrowser_2.ensureCursorVisible()

    def crossover_singlepoint(self, ind1, ind2):
        p = random.randint(0, len(ind1))
        self.c1 = ind1[0: p] + ind2[p:]
        self.c2 = ind2[0: p] + ind1[p:]
        #print("Single")
        return self.c1, self.c2

    def crossover_multipoint(self, ind1, ind2):
        p3 = random.randint(0, len(ind1))
        p4 = random.randint(0, len(ind1) - 1)
        c1 = ind1[p3: p4] + ind2[p3:p4]
        c2 = ind2[p4: p3] + ind1[p4:p3]
        #print("multi")
        return c1, c2

    def print(self):
        #self.ui.textBrowser_2.appendPlainText(self.ui.lineEdit_2.text())
        print(self.crossover_type)

    def singlecross(self):
        self.crossover_type = '0'
        return self.crossover_type

    def multicross(self):
        self.crossover_type = '1'
        return self.crossover_type

    def output_terminal_written(self, text):
        self.ui.textBrowser_2.appendPlainText(text)

    def save_text(self):
        with open('fitness.py','w') as f:
              my_text = self.ui.lineEdit_5.toPlainText()
              f.write(my_text)

    def display_text(self):
        with open('fitness.py','r') as f:
            self.ui.lineEdit_5.setPlainText(f.read())

    def message(self, s):
        self.ui.textBrowser_2.appendPlainText(s)

    def start_program(self):
        if self.p is None:  # No process running.
            self.message("Executing process", )
            self.p = QtCore.QProcess(self)  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.ui.lineEdit_2.setText(self.ui.lineEdit_2.text())
            self.G = int(self.ui.lineEdit_2.text())
            self.ui.lineEdit.setText(self.ui.lineEdit.text())
            self.N = int(self.ui.lineEdit.text())
            self.p.start(self.function())


    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        # Extract progress if it is in the data.
        progress = self.function(stderr)
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

    def function(self):
        G = self.G
        N = self.N
        pop = list()

        # init pop
        for i in range(N):
            pop.append(generate_individual())
        # genetic algorithm loop
        for i in range(G):
            f_vals = list()  # a place for fitness values of each individual
            for ind in pop:
                f_vals.append(fitness(ind))  # compute fitness for all in the population
            newpop = list()  # the NEXT generation...
            bfitpop = max(f_vals)
            while len(newpop) < N:  # keep doing this until we have N number of inds in newpop
                idx = random.choices(range(0, len(pop)), k=16)  # -> randomly selects 16 inds
                val = [f_vals[p] for p in idx]  # -> grabs the fitness values for selected idx
                p1 = pop[idx[val.index(max(val))]]
                # do it again
                # burada aynı idx geliyor olmasın? üstteki listeden iki tane en iyi seçmeyi deneyelim
                idx.pop(val.index(max(val)))  # remove max
                val.pop(val.index(max(val)))
                p2 = pop[idx[val.index(max(val))]]
                m = self.GA.mutation_val
                # children
                c1, c2 = self.dispatcher[self.crossover_type](p1, p2)
                c1 = self.GA.mutation(c1, m)
                c2 = self.GA.mutation(c2, m)
                newpop.append(c1)
                newpop.append(c2)
            pop = newpop
            print("mean: " + str(mean(f_vals)) + ", best: " + str(bfitpop))

            #print(self.ui.textBrowser_2.appendPlainText,"mean: " + str(mean(f_vals)) + ", best: " + str(bfitpop))

if __name__ == '__main__':
 app = QApplication(sys.argv)
 window = gui()
 window.show()
 sys.exit(app.exec_())