import sys
from PyQt5.QtWidgets import (QWidget, QSlider, QApplication,
    QHBoxLayout, QVBoxLayout, QLineEdit,QPushButton)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import (QObject, Qt, pyqtSignal)
from PyQt5.QtGui import QPainter, QFont, QColor, QPen
import numpy as np


_counts_of_image = 3
_len_recognizeble_vector = 15

_recognizable_image_first = np.array([1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, 1])

_recognizable_image_second = np.array([1, -1, -1, 1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, -1])

_recognizable_image_third = np.array([1, 1, 1, -1, -1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1])

_recognizable_image_vectors = np.array([[_recognizable_image_first],[_recognizable_image_second],[_recognizable_image_third]])


if __name__ == '__main__':




    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle('Textbox example @pythonspot.com')

    # Create textbox
    textbox1 = QLineEdit(w)
    textbox1.move(20, 20)
    textbox1.resize(100, 40)

    # Create textbox
    textbox2 = QLineEdit(w)
    textbox2.move(20, 60)
    textbox2.resize(100, 40)

    # Create textbox
    textbox3 = QLineEdit(w)
    textbox3.move(20, 100)
    textbox3.resize(100, 40)

    # Create textbox
    textbox4 = QLineEdit(w)
    textbox4.move(20, 140)
    textbox4.resize(100, 40)

    # Create textbox
    textbox5 = QLineEdit(w)
    textbox5.move(20, 180)
    textbox5.resize(100, 40)

    # Create textbox
    textbox6 = QLineEdit(w)
    textbox6.move(120, 20)
    textbox6.resize(100, 40)

    # Create textbox
    textbox7 = QLineEdit(w)
    textbox7.move(120, 60)
    textbox7.resize(100, 40)

    # Create textbox
    textbox8 = QLineEdit(w)
    textbox8.move(120, 100)
    textbox8.resize(100, 40)

    # Create textbox
    textbox9 = QLineEdit(w)
    textbox9.move(120, 140)
    textbox9.resize(100, 40)

    # Create textbox
    textbox10 = QLineEdit(w)
    textbox10.move(120, 180)
    textbox10.resize(100, 40)

    # Create textbox
    textbox11 = QLineEdit(w)
    textbox11.move(220, 20)
    textbox11.resize(100, 40)

    # Create textbox
    textbox12 = QLineEdit(w)
    textbox12.move(220, 60)
    textbox12.resize(100, 40)

    # Create textbox
    textbox13 = QLineEdit(w)
    textbox13.move(220, 100)
    textbox13.resize(100, 40)

    # Create textbox
    textbox14 = QLineEdit(w)
    textbox14.move(220, 140)
    textbox14.resize(100, 40)

    # Create textbox
    textbox15 = QLineEdit(w)
    textbox15.move(220, 180)
    textbox15.resize(100, 40)

    # Set window size.
    w.resize(400, 400)

    # Create a button in the window
    button = QPushButton('Click me', w)
    button.move(150, 300)



    textbox_container = []

    textbox_container.append(textbox1)
    textbox_container.append(textbox2)
    textbox_container.append(textbox3)
    textbox_container.append(textbox4)
    textbox_container.append(textbox5)
    textbox_container.append(textbox6)
    textbox_container.append(textbox7)
    textbox_container.append(textbox8)
    textbox_container.append(textbox9)
    textbox_container.append(textbox10)
    textbox_container.append(textbox11)
    textbox_container.append(textbox12)
    textbox_container.append(textbox13)
    textbox_container.append(textbox14)
    textbox_container.append(textbox15)




    def making_up_mx_weight(skit=_recognizable_image_vectors):
        weight_matrix = np.zeros((15, 15))
        for element in (skit):
            weight_matrix += element * element.T
        np.fill_diagonal(weight_matrix, 0)
        return weight_matrix


    def get_output_net(predicted_set):
        net_values = []
        weight_matrix = making_up_mx_weight()
        for i in range(_len_recognizeble_vector):
            net_temp_per_index = 0
            for j in range(_len_recognizeble_vector):
                if (i == j):
                    continue
                else:
                    net_temp_per_index += weight_matrix[i][j] * predicted_set[j]
            net_values.append(net_temp_per_index)

        return np.array(net_values)


    def activate_net_values(net_predicted_set, f_net_previous):
        f_net_set = []
        net_values = get_output_net(net_predicted_set)
        for i in range(_len_recognizeble_vector):
            if net_values[i] > 0:
                f_net_set.append(1)
            elif net_values[i] == 0:
                f_net_set.append(f_net_previous[i])
            elif net_values[i] < 0:
                f_net_set.append(-1)
            else:
                print('What_s wrong')
        return np.array(f_net_set)


    _changed_image_first = np.array([-1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1, -1, -1])  #### ------------CHANGE
    start_vector =  _changed_image_first.tolist()

    f_net = _recognizable_image_first
    f_net_previous = _changed_image_first
    counter = 0
    OUTPUT_RESULT = 0



    while True:
        counter += 1
        print(counter)


        net_previous = get_output_net(_changed_image_first)
        _changed_image_first = net_previous

        f_net = activate_net_values(net_previous, f_net)

        if ((f_net == f_net_previous).all()): #######-------------    CHANGE
            print('ура')
            OUTPUT_RESULT = f_net.tolist()
            break
        else:
            f_net_previous = f_net
            continue



    for i in range (_len_recognizeble_vector):
        if (start_vector[i] == 1):
            textbox_container[i].setText('####\n####')
        else:
            textbox_container[i].setText('')


    @pyqtSlot()
    def on_click():
        for i in range(_len_recognizeble_vector):
            if(OUTPUT_RESULT[i] == 1):
                textbox_container[i].setText('####\n####')
            else:
                textbox_container[i].setText('')



    # connect the signals to the slots
    button.clicked.connect(on_click)

    w.show()
    app.exec_()
