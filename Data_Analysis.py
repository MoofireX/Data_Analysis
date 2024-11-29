# Data_Analysis
import pandas as pd
from matplotlib import pyplot as plt
import sys


def plot(file, read_or_write, plot_style):
    
    number_list = ['1','2','3','4','5','6','7','8','9','0','.']
    letter_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',
               'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y',
               'Z']

    x_axis = ""

    y_axis = ""

    data = []

    file = open(file, read_or_write)
    file = file.read()

    plot_list = list(file.split("\n"))


    for i in range(len(plot_list)):
        txt = plot_list[i]
        data.append(txt)
        i += 4

    z = data

    for i in range(len(z)):
        val = z[i]
        for char in val:
            if char in number_list:
                y_axis += char
            elif char in letter_list:
                x_axis += char
        y_axis += " "
        x_axis += " "

    val = 0

    y_axis = y_axis.split(" ")
    
    for val in y_axis:
        if val == " ":
            y_axis.remove(val)
    for val in y_axis:
        if val == "":
            y_axis.remove(val)

    val = 0

    x_axis = x_axis.split(" ")

    for val in x_axis:
        if val == " ":
            x_axis.remove(val)
    for val in x_axis:
        if val == "":
            x_axis.remove(val)

    val = 0
    
    for val in x_axis:
        if val == " ":
            x_axis.remove(val)
    for val in y_axis:
        if val == " ":
            y_axis.remove(val)

    x_axis = x_axis[:len(data)]
    y_axis = y_axis[:len(data)]

    plt.plot(x_axis,y_axis,plot_style)
    plt.show()

def x_data(file,read_or_write):
    number_list = ['1','2','3','4','5','6','7','8','9','0','.']
    letter_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',
               'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y',
               'Z']

    x_axis = ""

    y_axis = ""

    data = []

    file = open(file, read_or_write)
    file = file.read()

    plot_list = list(file.split("\n"))


    for i in range(len(plot_list)):
        txt = plot_list[i]
        data.append(txt)
        i += 4

    z = data

    for i in range(len(z)):
        val = z[i]
        for char in val:
            if char in number_list:
                y_axis += char
            elif char in letter_list:
                x_axis += char
        y_axis += " "
        x_axis += " "

    val = 0

    x_axis = x_axis.split(" ")

    for val in x_axis:
        if val == " ":
            x_axis.remove(val)
    for val in x_axis:
        if val == "":
            x_axis.remove(val)

    val = 0
    
    for val in x_axis:
        if val == " ":
            x_axis.remove(val)

    x_axis = x_axis[:len(data)]

    print(x_axis)

    return x_axis
    

def y_data(file,read_or_write):

    number_list = ['1','2','3','4','5','6','7','8','9','0','.']
    letter_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',
               'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y',
               'Z']

    x_axis = ""

    y_axis = ""

    data = []

    file = open(file, read_or_write)
    file = file.read()

    plot_list = list(file.split("\n"))


    for i in range(len(plot_list)):
        txt = plot_list[i]
        data.append(txt)
        i += 4

    z = data

    for i in range(len(z)):
        val = z[i]
        for char in val:
            if char in number_list:
                y_axis += char
            elif char in letter_list:
                x_axis += char
        y_axis += " "
        x_axis += " "

    val = 0

    y_axis = y_axis.split(" ")
    
    for val in y_axis:
        if val == " ":
            y_axis.remove(val)
    for val in y_axis:
        if val == "":
            y_axis.remove(val)


    val = 0
    
    for val in y_axis:
        if val == " ":
            y_axis.remove(val)

    y_axis = y_axis[:len(data)]

    print(y_axis)

    return y_axis


def plot_frame(frame=None, keys=None, values=None,plot_style = 'o'):

    if keys is None and values is None:
        frame_keys = frame.keys()

        x = list(frame_keys)

        y = []

        for val in frame:
            y.append(list(frame[val]))

        print(y)

        plt.plot(x,y,plot_style)
        plt.show()

    if frame is None:
        
        if len(keys) != len(values):
            print("The length of the tuple keys should be equal to the length of the tuple values.", "(", len(keys), ")", "!=" , "(",len(values),")")
            print("Please fix this error and run the code again.")

            sys.exit()    

        indx = 0

        frame_dict = {}
    
        while indx < len(keys):
        
            frame_dict[keys[indx]] = [values[indx]]

            indx += 1

        frame = pd.DataFrame(frame_dict)    

        x = keys
        y = values

        plt.plot(x,y,plot_style)
        plt.show()


def print_frame(keys, values):

    if len(keys) != len(values):
        print("The length of the tuple keys should be equal to the length of the tuple values.", "(", len(keys), ")", "!=" , "(",len(values),")")
        print("Please fix this error and run the code again.")

        sys.exit()    

    indx = 0

    frame_dict = {}
    
    while indx < len(keys):
        
        frame_dict[keys[indx]] = [values[indx]]

        indx += 1

    frame = pd.DataFrame(frame_dict)
    print(frame)
