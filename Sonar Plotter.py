#Sonar Plotter

from matplotlib import pyplot as plt

plotfile = open("SONAR_Experiment-Results", 'r')
plotfile = plotfile.read()

x_axis = ""

y_axis = ""

data = []

number_list = ['1','2','3','4','5','6','7','8','9','0','.']
letter_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',
               'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y',
               'Z']
    

plot_list = list(plotfile.split("\n"))


for i in range(len(plot_list)):
    txt = plot_list[i]
    data.append(txt)
    i += 4

x = data

for i in range(len(x)):
    val = x[i]
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

print(y_axis)
print(x_axis)

plt.plot(x_axis,y_axis,'o')
plt.show()
