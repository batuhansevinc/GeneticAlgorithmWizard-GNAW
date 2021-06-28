import functools
import time
import random
from PyQt5.QtWidgets import *
from statistics import mean
from PyQt5 import (QtCore)
from PyQt5 import QtGui
from concurrent import futures
from designer_python import Ui_MainWindow
from fitness import *
import sys


val = 1
thread_pool_executor = futures.ThreadPoolExecutor(max_workers=1)

def tk_after(target):
    @functools.wraps(target)
    def wrapper(self, *args, **kwargs):
        args = (self,) + args
        self.after(0, target, *args, **kwargs)
    return wrapper

def submit_to_pool_executor(executor):
    '''Decorates a method to be sumbited to the passed in executor'''
    def decorator(target):
        @functools.wraps(target)
        def wrapper(*args, **kwargs):
            result = executor.submit(target, *args, **kwargs)
            result.add_done_callback(executor_done_call_back)
            return result
        return wrapper
    return decorator

def executor_done_call_back(future):
    exception = future.exception()
    if exception:
        raise exception

class Stream(QtCore.QObject):
    """Redirects console output to text widget."""
    newText = QtCore.pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))

if __name__ == '__main__':
 class gui(QMainWindow, QtCore.QObject):

    finished = QtCore.pyqtSignal()

    def __init__(self):
        super(). __init__()
        self.setWindowIcon(QtGui.QIcon('logo.ico'))
        self.selection_type = '0'
        self.dispatcher = {'0': self.crossover_singlepoint, '1': self.crossover_multipoint, '2': self.crossover_uniform}
        self.dispatcher2 = {'0': self.selRandom, '1': self.selTournament, '2': self.selRank, '3': self.selRoulette}
        self.p = None
        self.crossover_type = '0'
        self.pop = list()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.ui.lineEdit_2.setText("10")
        self.ui.lineEdit.setText("10")
        self.ui.lineEdit_4.setText("10")
        self.mutation_val = float(self.ui.lineEdit_4.text())  # float(input(f"Set Mutation Probablity: "))
        self.NumOfGen = int(self.ui.lineEdit_2.text()) # input(int(f"umber of generations"))  # number of generations 200
        self.NumOfPop = int(self.ui.lineEdit.text())  # input(int(f"number of individuals in population"))  # number of individuals in population 100
        self.c2 = list()
        self.c1 = list()
        self.ui.pushButton.clicked.connect(self.save_text)
        sys.stdout = Stream(newText=self.onUpdateText)
        self.ui.pushButton_2.clicked.connect(self.start_program)
        self.ui.radioButton.clicked.connect(self.singlecross)
        self.ui.radioButton_2.clicked.connect(self.multicross)
        self.ui.radioButton_3.clicked.connect(self.uniformcross)
        self.ui.pushButton_3.clicked.connect(self.display_text)
        self.ui.radioButton_5.clicked.connect(self.randomsel)
        self.ui.radioButton_4.clicked.connect(self.tournamentsel)
        self.ui.radioButton_6.clicked.connect(self.ranksel)
        self.ui.radioButton_7.clicked.connect(self.roulettesel)
        self.ui.pushButton_4.clicked.connect(self.changeFitlbl)
        self.ui.textBrowser_2.setPlaceholderText("OUTPUT")
        self.ui.radioButton.setChecked(True)
        self.ui.radioButton_5.setChecked(True)
        self.display_text()
        self.ui.lineEdit_3.setText("0")
        self.thread = QtCore.QThread(self)
        self.moveToThread(self.thread)
        self.finished.connect(self.handleFinished)
        self.thread.started.connect(self.function)
        self.thansign = '0'

    def changeFitlbl(self):

        global val
        val += 1

        if val % 2 == 0:
            self.ui.pushButton_4.setText("<")
            self.thansign = '1'
            return val


        if val % 2 == 1:
            self.ui.pushButton_4.setText(">")
            self.thansign = '0'
            return val



    def mutation(self, ind, m):
        for k, v in enumerate(ind):
            if random.random() < m:
                ind[k] = random.randint(0, 6)
        return ind

    def onUpdateText(self, text):
        """Write console output to text widget."""
        cursor = self.ui.textBrowser_2.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.ui.textBrowser_2.setTextCursor(cursor)
        self.ui.textBrowser_2.ensureCursorVisible()

    def crossover_singlepoint(self, ind1, ind2):
        p = random.randint(0, len(ind1))
        c1 = ind1[0: p] + ind2[p:]
        c2 = ind2[0: p] + ind1[p:]
        #print("Single")
        return c1, c2

    def crossover_multipoint(self, ind1, ind2):
        p1 = random.randint(0, len(ind1))
        p2 = random.randint(p1+1, len(ind1))
        c1 = ind1[0: p1] + ind2[p1+1: p2] + ind1[p2+1: ]
        c2 = ind1[0: p2] + ind2[p2+1: p1] + ind1[p1+1: ]
        # print("Single")
        return c1, c2

    def crossover_uniform(self, ind1, ind2):
        size = min(len(ind1), len(ind2))
        for i in range(size):
            if random.random() < random.random():
                ind1[i], ind2[i] = ind2[i], ind1[i]
        return ind1, ind2

    def selRandom(self,pop):
        return random.choices(range(0, len(pop)), k=16)

    def selTournament(self, pop):
        parents = random.choices(pop, k=16)
        parents = sorted(parents, key=lambda agent: agent.fitness, reverse=True)
        return parents[0], parents[1]

    def selRank(self, pop):
        return random.choices(range(0, len(pop)), k=16)

    def selRoulette(self, pop):
        return random.choices(range(0, len(pop)), k=16)

    def generate_individual(self):
        return [random.randint(0, 6) for i in range(0, 243)]

    def singlecross(self):
        self.crossover_type = '0'
        return self.crossover_type

    def multicross(self):
        self.crossover_type = '1'
        return self.crossover_type

    def uniformcross(self):
        self.crossover_type = '2'
        return self.crossover_type

    def randomsel(self):
        self.selection_type = '0'

        return self.selection_type

    def tournamentsel(self):
        self.selection_type = '1'

        return self.selection_type

    def ranksel(self):
        self.selection_type = '2'

        return self.selection_type

    def roulettesel(self):
        self.selection_type = '3'

        return self.selection_type

    def save_text(self):
        with open('fitness.py','w') as f:
            my_text = self.ui.lineEdit_5.toPlainText()
            f.write(my_text)
            self.ui.label_9.setText("Last saved on: "+ time.strftime('%X'))


    def display_text(self):
        with open('fitness.py','r') as f:
            self.ui.lineEdit_5.setPlainText(f.read())

    def message(self, s):
        self.ui.textBrowser_2.appendPlainText(s)

    def start_program(self):
        self.ui.pushButton_2.setEnabled(False)
        self.ui.radioButton.setEnabled(False)
        self.ui.radioButton_2.setEnabled(False)
        self.ui.radioButton_3.setEnabled(False)
        self.ui.radioButton_4.setEnabled(False)
        self.ui.radioButton_5.setEnabled(False)
        self.ui.radioButton_6.setEnabled(False)
        self.ui.radioButton_7.setEnabled(False)
        self.thread.start()
        print("Process Started...")

    def handleFinished(self):
        self.thread.quit()
        self.thread.wait()
        self.ui.pushButton_2.setEnabled(True)
        self.ui.radioButton.setEnabled(True)
        self.ui.radioButton_2.setEnabled(True)
        self.ui.radioButton_3.setEnabled(True)
        self.ui.radioButton_4.setEnabled(True)
        self.ui.radioButton_5.setEnabled(True)
        self.ui.radioButton_6.setEnabled(True)
        self.ui.radioButton_7.setEnabled(True)
        print("Process Finished.")

    @submit_to_pool_executor(thread_pool_executor)
    def function(self):
        self.NumOfGen = int(self.ui.lineEdit_2.text())
        self.NumOfPop = int(self.ui.lineEdit.text())
        self.mutation_val = float(self.ui.lineEdit_4.text()) / 100
        pop = self.pop
        NumOfGen = self.NumOfGen
        NumOfPop = self.NumOfPop
        thansign = self.thansign

        # init pop
        for i in range(NumOfPop):
            pop.append(self.generate_individual())
        # genetic algorithm loop
        for i in range(NumOfGen):
            f_vals = list()  # a place for fitness values of each individual
            for ind in pop:
                f_vals.append(fitness(ind))  # compute fitness for all in the population
            newpop = list()  # the NEXT generation...
            bfitpop = max(f_vals)
            while len(newpop) < NumOfPop:  # keep doing this until we have N number of inds in newpop
                idx = self.dispatcher2[self.selection_type](pop)#random.choices(range(0, len(pop)), k=16)  # -> randomly selects 16 inds
                val = [f_vals[p] for p in idx]  # -> grabs the fitness values for selected idx
                p1 = pop[idx[val.index(max(val))]]
                # do it again
                # burada aynı idx geliyor olmasın? üstteki listeden iki tane en iyi seçmeyi deneyelim
                idx.pop(val.index(max(val)))  # remove max
                val.pop(val.index(max(val)))
                p2 = pop[idx[val.index(max(val))]]
                m = self.mutation_val
                # children
                c1, c2 = self.dispatcher[self.crossover_type](p1, p2)
                c1 = self.mutation(c1, m)
                c2 = self.mutation(c2, m)
                newpop.append(c1)
                newpop.append(c2)
            pop = newpop
            print(str(mean(f_vals)) + ", best: " + str(bfitpop))
            if bfitpop >= float(self.ui.lineEdit_3.text()) and thansign == '0' :
             print("Succesfully reached the fitness limit  :  " + str(bfitpop))
             break
            if bfitpop <= float(self.ui.lineEdit_3.text()) and thansign == '1' :
             print("Succesfully reached the fitness limit  :  " + str(bfitpop))
             break


        self.finished.emit()

if __name__ == '__main__':
 app = QApplication(sys.argv)
 window = gui()
 window.show()
 sys.exit(app.exec_())