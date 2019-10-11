from tkinter import filedialog as fd
from tkinter.ttk import *
import tkinter as tk
import csv
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import math					

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
#global xValues
#global yValues

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
    
#-------------------------------------------------------------- team 3
"""
def basic_stats():
    n=len(x)					
    print("count of data is: ",n)					
    sum_x1=sum(x1)					
    sum_y=sum(y)					
                                            
    #sum of x1*y					
    x1y = [x1[i]*y[i] for i in range(len(x1))]					
    #print(x1y)					
    sum_x1y=sum(x1y)					
    #print("sum of x1*y: ",sum_x1y)					
                                            
    #n* sum of x1 y					
    nx1y=n*sum_x1y					
    #print(nx1y)					
                                            
    #sum of x1* sum of y					
    Ex1Ey=sum_x1*sum_y					
    #print(Ex1Ey)					
                                            
    #sum of sqaures of x1					
    SS_x1 = sum(map(lambda i : i * i, x1)) 					
    #print ("The sum of squares of list is : " + str(SS_x1)) 					
    #n* sum of x1^2					
    nSSx1=n*SS_x1					
    #print(nSSx1)					
                                            
                                            
    #(sum of x1)^2					
        S_x1=sum_x1*sum_x1					
    #print(S_x1)					
                                            
    #print("sum of sum_x1: ", sum_x1)					
    #print("sum of sum_y: ", sum_y)					
                                            
    n=len(x1)					
    print("count of data: ",n)					
                                            
    mean_x1 = sum(x1) / len(x1)					
    mean_y = sum(y) / len(y) 					
                                            
    print("Mean of x1 is : " + str(mean_x1)) 					
    print("Mean of y is : " + str(mean_y)) 					
                                            
    #calculating cross deviation 					
    SS_x1y = nx1y-Ex1Ey					
    #print(SS_x1y)					
    SS_x1x1 = nSSx1-S_x1					
    #print(SS_x1x1)					
                                            
    m=SS_x1y/SS_x1x1					
    print("X Variable 1: ",m)					
                                            
    #m*sum of x1					
    mEx1=m*sum_x1					
    #print(mEx1)					
                                            
    nmrtr=sum_y-mEx1 #nmrtr=numerator					
    #print(nmrtr)					
                                            
    c=nmrtr/n					
    print("Intercept: ",c)					
                                            
    #so the regression line for x1 and y is					
                                            
                                            
    print("Best fit line:")					
    print("y = "+str(m)+"x1"+str(c))					
                                            
    #testing of regression equation					
    #x = float(input("Enter a value to calculate: "))					
    #print("y = "+str(m*x+c))					
                                            
                                            
                                                    
                                    
#correlation coefficient					
					
def correlationCoefficient(X, Y, n) : 					
	sum_X = 0				
	sum_Y = 0				
	sum_XY = 0				
	squareSum_X = 0				
	squareSum_Y = 0				
					
					
	i = 0				
	while i < n : 				
		# sum of elements of array X. 			
		sum_X = sum_X + X[i] 			
					
		# sum of elements of array Y. 			
		sum_Y = sum_Y + Y[i] 			
					
		# sum of X[i] * Y[i]. 			
		sum_XY = sum_XY + X[i] * Y[i] 			
					
		# sum of square of array elements. 			
		squareSum_X = squareSum_X + X[i] * X[i] 			
		squareSum_Y = squareSum_Y + Y[i] * Y[i] 			
					
		i = i + 1			
					
	# use formula for calculating correlation coefficient. 				
	corr = (float)(n * sum_XY - sum_X * sum_Y)/(float)(math.sqrt((n * squareSum_X - sum_X * sum_X)* (n * squareSum_Y - sum_Y * sum_Y))) 				
	return corr 				
					
# Driver function 					
X = x1					
Y = y					
					
# Find the size of array. 					
n = len(X) 					
					
# Function call to correlationCoefficient. 					
print ('Correlation Coefficient between x1 & y is ','{0:.6f}'.format(correlationCoefficient(X, Y, n))) 					
var_x1  = sum(pow(x-mean_x1,2) for x in x1) / len(x1)					
print("variance of x1 is : " + str(var_x1))					
					
std_x1  = math.sqrt(var_x1)					
print("SD of x1 is : " + str(std_x1)) 					
var_y  = sum(pow(x-mean_y,2) for x in y) / len(y)					
std_y  = math.sqrt(var_y)					
print("SD of y is : " + str(std_y)) 					
					
#covariance(x1, y)					

#x1 bar and y bar
x1_bar=	sum_x1/n
y_bar=	sum_y/n

#print(x1_bar)	
#print(y_bar)	

x1x_bar = [x1[i]-x1_bar for i in range(len(x1))]
#print(x1x_bar)
sum_x1x_bar=sum(x1x_bar)
#print(sum_x1x_bar)

yy_bar=[y[i]-y_bar for i in range(len(y))]
#print(yy_bar)
sum_yy_bar=sum(yy_bar)
#print(sum_yy_bar)

z = [x1x_bar[i]*yy_bar[i] for i in range(len(x1x_bar))]
#print(z)
sum_z=sum(z)
#print(sum_z)

cov=sum_z/n
print("coveriance between x1 & y is: ",cov)

"""

# team4
global N
class LinearRegression:

    global N
    @staticmethod
    def get_cofactor(arr, temp, p, q, n):
        i = 0
        j = 0

        for row in range(n):
            for col in range(n):
                if row != p and col != q:
                    temp[i][j] = arr[row][col]
                    j += 1

                    if j == n-1:
                        j = 0
                        i += 1

    def get_det(self, arr, n):
        D = 0

        if n == 1:
            return arr[0][0]

        temp = []
        for i in range(N):
            temp.append([])
            for j in range(N):
                temp[i].append([])

        sign = 1

        for f in range(n):
            self.get_cofactor(arr, temp, 0, f, n)
            D += sign * arr[0][f] * self.get_det(temp, n-1)
            sign = -sign

        return D

    def get_adjoint(self, arr, adj):
        if N == 1:
            adj[0][0] = 1
            return

        temp = []
        for i in range(N):
            temp.append([])
            for j in range(N):
                temp[i].append([])

        for i in range(N):
            for j in range(N):
                self.get_cofactor(arr, temp, i, j, N)

                sign = 1 if ((i + j) % 2 == 0) else -1

                # adj[p][q] = sign * get_matrix_determinant(tmp)
                adj[j][i] = sign * self.get_det(temp, N-1)

    def get_matrix_inverse(self, arr, inverse):
        # determinant = get_matrix_determinant(m)

        determinant = self.get_det(arr, N)
        # special case for 2x2 matrix:
        # if len(arr) == 2:
        #    return [[arr[1][1]/determinant, -1*arr[0][1]/determinant],
        #            [-1*arr[1][0]/determinant, arr[0][0]/determinant]]
        # find matrix of co-factors

        adj = []
        for i in range(N):
            adj.append([])
            for j in range(N):
                adj[i].append([])

        self.get_adjoint(arr, adj)

        for i in range(N):
            for j in range(N):
                inverse[i][j] = adj[i][j] / float(determinant)

#---------------------------------------------------------------------
linear = LinearRegression()
global result 
def non_Linear_Regression():
    global dataValues
    global result
    global N
    # dataValues = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120'], ['7.50', '44.31', '60.80', '148.97', '225.50', '262.64', '289.06', '451.53', '439.62', '698.88', '748.24', '896.46', '1038.78', '1214.04', '1377.08', '1579.86', '1763.14', '1993.92', '2196.96', '2456.22', '2678.54', '2966.76', '3207.88', '3525.54', '3784.98', '4132.56', '4409.84', '4787.82', '5082.46', '5491.32', '5802.84', '6243.06', '6570.98', '7043.04', '7386.88', '7891.26', '8250.54', '8787.72', '9161.96', '9732.42', '10121.14', '10725.36', '11128.08', '11766.54', '12182.78', '12855.96', '13285.24', '13993.62', '14435.46', '15179.52', '15633.44', '16413.66', '16879.18', '17696.04', '18172.68', '19026.66', '19513.94', '20405.52', '20902.96', '21832.62', '22339.74', '23307.96', '23824.28', '24831.54', '25356.58', '26403.36', '26936.64', '28023.42', '28564.46', '29691.72', '30240.04', '31408.26', '31963.38', '33173.04', '33734.48', '34986.06', '35553.34', '36847.32', '37419.96', '38756.82', '39334.34', '40714.56', '41296.48', '42720.54', '43306.38', '44774.76', '45364.04', '46877.22', '47469.46', '49027.92', '49622.64', '51226.86', '51823.58', '53474.04', '54072.28', '55769.46', '56368.74', '58113.12', '58712.96', '60505.02', '61104.94', '62945.16', '63544.68', '65433.54', '66032.18', '67970.16', '68567.44', '70555.02', '71150.46', '73188.12', '73781.24', '75869.46', '76459.78', '78599.04', '79186.08', '81376.86', '81960.14', '84202.92', '84781.96', '87077.22']]
    # x = '0, 1, 2, 3, 4'
    # y = '1, 1.8, 3.3, 4.5, 6.3'
    # y = '-4, -1, 4, 11, 20'

    # x = '1, 2, 3, 4'
    # y = '6, 11, 18, 27'

    # x = '1, 2, 3, 4, 5, 6'
    # y = '1200, 900, 600, 200, 110, 50'

    # x = '71, 68, 73, 69, 67, 65, 66, 67'
    # y = '69, 72, 70, 70, 68, 67, 68, 64'

    # x = '-1, 0, 1, 2'
    # y = '2, 5, 3, 0'

    # x = '1, 2, 3, 4, 5, 6, 7, 8, 9'
    # y = '2, 6, 7, 8, 10, 11, 11, 10, 9'

    # x = '1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937'
    # y = '352, 356, 357, 358, 360, 361, 361, 360, 359'

    # y = '1, 1.8, 1.3, 2.5, 6.3'

    # x = '1, 2, 3, 4, 5, 6, 7, 8, 9, 10'
    # y = '7.5, 44.31, 60.8, 148.97, 222.5, 262.64, 289.06, 451.53, 439.62, 698.88'
    """ commented to test
    x = '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, ' \
        '31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, ' \
        '59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, ' \
        '87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, ' \
        '112, 113, 114, 115, 116, 117, 118, 119, 120 '
    y = '7.50, 44.31, 60.80, 148.97, 225.50, 262.64, 289.06, 451.53, 439.62, 698.88, 748.24, 896.46, 1038.78, 1214.04, '\
        '1377.08, 1579.86, 1763.14, 1993.92, 2196.96, 2456.22, 2678.54, 2966.76, 3207.88, 3525.54, 3784.98, 4132.56, ' \
        '4409.84, 4787.82, 5082.46, 5491.32, 5802.84, 6243.06, 6570.98, 7043.04, 7386.88, 7891.26, 8250.54, 8787.72, ' \
        '9161.96, 9732.42, 10121.14, 10725.36, 11128.08, 11766.54, 12182.78, 12855.96, 13285.24, 13993.62, 14435.46, ' \
        '15179.52, 15633.44, 16413.66, 16879.18, 17696.04, 18172.68, 19026.66, 19513.94 ,20405.52, 20902.96, 21832.62, ' \
        '22339.74, 23307.96, 23824.28, 24831.54, 25356.58, 26403.36, 26936.64, 28023.42, 28564.46, 29691.72, 30240.04, ' \
        '31408.26, 31963.38, 33173.04, 33734.48, 34986.06, 35553.34, 36847.32, 37419.96, 38756.82, 39334.34, 40714.56, ' \
        '41296.48, 42720.54, 43306.38, 44774.76, 45364.04, 46877.22, 47469.46, 49027.92, 49622.64, 51226.86, 51823.58, ' \
        '53474.04, 54072.28, 55769.46, 56368.74, 58113.12, 58712.96, 60505.02, 61104.94, 62945.16, 63544.68, 65433.54, ' \
        '66032.18, 67970.16, 68567.44, 70555.02, 71150.46, 73188.12, 73781.24, 75869.46, 76459.78, 78599.04, 79186.08, ' \
        '81376.86, 81960.14, 84202.92, 84781.96, 87077.22 '
    """
    degree_of_x: int = int(number_chosen.get()) # str to int 

    independentInputArray = dataValues[0]
    dependentInputArray = dataValues[1]

    sigma_X = []
    sigma_XY = []

    x_count = 1
    while x_count <= degree_of_x * 2:
        temp = 0
        for x in independentInputArray:
            temp = temp + pow(float(x), x_count)

        sigma_X.append(temp)
        x_count += 1

    y_count = 0
    while y_count <= degree_of_x:
        temp = 0
        number_of_x = 0
        for y in dependentInputArray:
            temp = temp + float(y) * (pow(float(independentInputArray[number_of_x]), y_count))
            number_of_x = number_of_x + 1

        sigma_XY.append(temp)
        y_count += 1

    arr = []

    sigma_X.insert(0, float(len(independentInputArray)))

    for i in range(degree_of_x + 1):
        temp = []
        for j in range(degree_of_x + 1):
            temp.append(sigma_X[j + i])
        arr.append(temp)

    N = degree_of_x + 1
    adj = []
    inverse = []

    for i in range(N):
        adj.append([])
        inverse.append([])
        for j in range(N):
            adj[i].append([])
            inverse[i].append([])

    sigma_XY_Transpose = []
    for i in range(N):
        sigma_XY_Transpose.append([])
        for j in range(1):
            sigma_XY_Transpose[i].append(0)

    for i in range(N):
        sigma_XY_Transpose[i][0] = sigma_XY[i]

    print('\n Transpose of different sigma xy \n')
    for transpose in sigma_XY_Transpose:
        print(transpose)
    print('\n')

    print('\n Array after finding and putting x and y values in equations \n')
    for a in arr:
        print(a)
    print('\n')

    linear.get_adjoint(arr, adj)
    print('\n Array Adjoint \n')
    for adjoint in adj:
        print(adjoint)
    print('\n')

    linear.get_matrix_inverse(arr, inverse)

    print('\n Inverse of Array after finding x and y values \n')
    for inv in inverse:
        print(inv)
    print('\n')

    result = []
    for i in range(N):
        result.append([])
        for j in range(1):
            result[i].append(0)

    for i in range(len(inverse)):
        for j in range(len(sigma_XY_Transpose[0])):
            for k in range(len(sigma_XY_Transpose)):
                result[i][j] += inverse[i][k] * sigma_XY_Transpose[k][j]
    """
    variable_count = 0
    for res in result:
        print('printing \u03B2', variable_count, ' = ', res)
        variable_count += 1
    """
    variable_count = 0
    result_str = ''
    for res in result:
        result_str = result_str  + '\u03B2'+str(variable_count)+ ' = ' +str(res)+ ' '
        variable_count += 1

    #b = ttk.Label(root ,text=' Regression').grid(column=0, row=2)
    a = tk.Label(root ,text='Polynomial Regression of degree = '+ number_chosen.get() +' \u03B2  coefficients are :').grid(column=0, row=1)
    b = tk.Label(root ,text= result_str).grid(column=0, row=2)
    #b.destroy()

#ttk.Label(root, text="Choose a number:").grid(column=1, row=2)
number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 3, 4)
number_chosen.grid(column=1, row=2)
number_chosen.current(0)

btn = Button(mighty, text='Polynomial Regression', command=lambda: non_Linear_Regression())
btn.grid(column=0, row=2)
