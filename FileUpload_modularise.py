from tkinter import filedialog as fd
from tkinter.ttk import *
import tkinter as tk
import csv
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile

root = tk.Tk()
#root.geometry('200x100')

root.title('AnalyticsCal')

mighty = ttk.LabelFrame(root, text=' AnalyticsCal Home')
mighty.grid(column=0, row=0, padx=100, pady=50)

global file_name # global path variable
file_name = ''
global dataHeader
global dataValues

def open_file():
    global file_name
    global dataHeader
    global dataValues
    file = askopenfile(mode='r', filetypes=[('CSV Files', '*.csv')])
    if file:
        file_name = file.name
        dataHeader, dataValues = preprocess_csv(file_name)

def preprocess_csv(file_name):  
    csvHeader = [] # Stores header of the csv File
    csvRows = [] # Stores Rest of the rows - values

    # Read CSV file
    csvFileObj = open(file_name) # reads csv file
    readerObj = csv.reader(csvFileObj) # creates a reader object

    # Separate header row and other rows in different lists
    for row in readerObj:
        if readerObj.line_num == 1: # line #1 corresponds to header
            csvHeader = row # store header in a list csvHeader
        else:
            csvRows.append(row) # stores the values in list csvRows
    csvFileObj.close()


    csvList = [] #stores list of column vectors([x1],[x2],[x3]...,[xn],[y])

    # Create list of column vectors
    for i in range(len(csvHeader)):
        csvList.append([row[i] for row in csvRows])

    return csvHeader, csvList

btn = Button(mighty, text='Browse', command=lambda: open_file())
btn.grid(column=0, row=1)

#buttons_frame = ttk.LabelFrame(mighty, text=' Labels in a Frame ')
# buttons_frame.grid(column=1, row=7)        # now col 1
 
# Place labels into the container element
#ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0, sticky=tk.W)
#ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0, sticky=tk.W)
#ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0, sticky=tk.W)


def plot_data():
    fig = Figure(figsize=(100, 100), facecolor='white')
    #--------------------------------------------------------------
    # axis = fig.add_subplot(111) # 1 row, 1 column, only graph
    axis = fig.add_subplot(211) # 2 rows, 1 column, Top graph
    #--------------------------------------------------------------
    xValues = [float(i) for i in dataValues[0]] # convert str list to int list
    yValues = [float(i) for i in dataValues[1]] # convert str list to float list
    axis.plot(xValues, yValues)
    axis.set_xlabel('Horizontal Label')
    axis.set_ylabel('Vertical Label')
    # axis.grid() # default line style
    axis.grid(linestyle='-') # solid grid lines
    root = tk.Tk()
    root.withdraw()
    root.protocol('WM_DELETE_WINDOW', _destroyWindow)
    #--------------------------------------------------------------
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    #--------------------------------------------------------------


    root.update()
    root.deiconify()
    root.mainloop()


btn = Button(mighty, text='Plot', command=lambda: plot_data())
btn.grid(column=1, row=1)

#--------------------------------------------------------------
def _destroyWindow():
    root.quit()
    root.destroy()
#--------------------------------------------------------------



