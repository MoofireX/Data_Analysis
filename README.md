# Data_Analysis
Uses matplotlib^ and pandas^ to plot data, give x and y axis values, and plot data frames. More coming soon!*


The matplotlib plotting function* takes a file as an input. The format should be as follows:

#File name (do not include in actual file) = Code

a = 1
b = 2
c = 3
abc = 123


The x_axis and y_axis functions return the x and y axes using the information provided in a file.

The plot_frame function*# takes a data frame's keys (a tuple that the user inputs), its values (another tuple inputted by the user). It converts this into a data frame and then plots it using matplotlib.

The print_frame function does the same thing as the plot_frame function, but it doesn't plot it. It just prints a data frame using keys (tuple) and values (tuple) that are inputted by the user.


*These functions also take a plot_style input, like 'o' for a scatter plot.

^Use pip install (from PyPi) to install matplotlib and pandas: pip install matplotlib + pip install pandas

#All of the values (in the tuple) must be the same length due to how pandas's data frame functions are made.
