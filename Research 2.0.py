#Research program
"""
Program written by Brittany Cain for Karel Casteels
Last update: May 27, 2017

Purpose: Programs a combinetorid model of quantum symmetric matrices
         in order to perform calculations more quickly
         
Users can choose the desired size matrix (nxn) as well as the starting and
ending points. 

Note: the matrix will appear to be one size larger (n+1 x n+1) than your
      desired size this is to allow for starting and ending points. If you
      you would like to be asked less questions while calculating comment out
      the sections inbetween #*** and #***. Use a # at the start of
      each line to do so.
      
      A small portion of this code was taken from 
      https://www.python.org/doc/essays/graphs/  and is noted by ## Thanks...
"""
import numpy as np

# Size of matrix
N= input('Enter the size of desired matrix: ') 
 

"""
nxn dummy matrix
"""
Starting_points = []
Ending_points = []

#Dummy t matrix


t = np.zeros(((N+1),(N+1)))
for row in range (N+1):
    for column in range (0,(N+1)):
        if column == (N) and row <= (N-1):
            Starting_points.append((row)*(N+1) + (column + 1))
            t[row,column] = (row)*(N+1) + (column)+1
        elif row == (N) and column !=N:
            Ending_points.append((row)*(N+1) + (column +1))
            t[row,column] = (row)*(N+1) + (column)+1
        else:
            t[row,column] = (row)*(N+1) + (column)+1
print "[t] =", '\n', t, '\n', '\n'

# t position matrix
tmatrix = np.zeros(((N+1),(N+1)),dtype = object)
for row in range (N+1):
    for column in range (N+1):
        position = [[row,column],1]
        tmatrix[row,column] = position
        

# t inverse position matrix

t_invmatrix = np.zeros(((N+1),(N+1)),dtype = object)
for row in range (N+1):
    for column in range (N+1):
        position = [[row,column],-1]
        t_invmatrix[row,column] = position
        
#***        
showtPositionMatrix = input('Would you like to see the position matrix for t and t inverse? Please enter True or False. ')        
if showtPositionMatrix == True:
    print '\n'
    print "[t] =", '\n', tmatrix, '\n', '\n'    
    print '\n',"[t_inv] =", '\n', t_invmatrix

#***


print '\n', '\n' # Allows a user to select their desired starting point
print "Possible starting points =", Starting_points
start = input('Choose your starting point: ')
print '\n', '\n'

print "Possible ending points =", Ending_points #Allows a user to select their desired ending point
end = input('Choose your ending point: ')  
print '\n'

#creates dictionary that takes a number and gives a location for matrix t

ruDict = {} #dictionary for lower right angles
for j in range (N+1):
    ruDict.update(dict(zip(t[j],tmatrix[j])))


rlDict = {} #dictionary for upper right angles
for j in range (N+1):
    rlDict.update(dict(zip(t[j],t_invmatrix[j])))  
    

"""
Possible Right angles
"""                 
#Upper right angles
upper_angle = []
for row in range (N):
    for column in range (1,N+1):
        upper = [t[row][column],t[row][column - 1],t[row + 1][column - 1]]
        upper_angle.append(upper)
#print upper_angle

#Lower right angles
lower_angle = []
for row in range (N-1):
    for column in range (1,N):
        lower = [t[row][column], t[row + 1][column], t[row + 1][column -1]]
        lower_angle.append(lower)
#print lower_angle

"""
Finding all paths from given start to given finish
"""            
def all_paths(start,end,path=[]):
#Creating flow

    graph = {}
    for j in range (N+1):
        for i in range (N+1):
            if j == 0 and i<= (N-1): #nodes that go down
                graph.update({t[i][j]:[t[(i+1)][j]]})
            elif j!=0 and j!=N and i<=(N-1): #nodes that go both down and left
                graph.update({t[i][j]:[t[i][(j-1)],t[i+1][j]]})
            elif j==N and i<=(N-1):      #starting points (nodes that go only left)
                graph.update({t[i][j]:[t[i][j-1]]})
            else:   #ending points (nodes that only go to themselves)
                graph.update({t[i][j]:[t[i][j]]})
    

        
    path = path + [start]  #Thanks to Python Software Foundation#
    if start == end:
        return [path]
    if not graph.has_key(start):
        return[]
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = all_paths(node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths #End thanks#

#***
printFullPath = input('Would you like to print every full path? Please enter True or False. Note: if N is large this will be very long. ')                                     
if printFullPath == True:
    print '\n'
    print 'paths =', '\n', (all_paths(start,end,path=[]))
print '\n', '\n'                                                                                                       
#***

                                                                                                                                                
"""
Testing for right angles
"""
weight = []
first_weight = []
hello = []
Paths = (all_paths(start,end,path=[]))
for what in range (len(Paths)): 
    pathNum = Paths[what]
    first_weight = []
    for i in range (len(pathNum)-2):
        right_angle = pathNum[i:i+3]
      
        for j in range (len(upper_angle)):
            if right_angle == upper_angle[j]:
                first_weight.append(ruDict[int(right_angle[1])])
            
        for j in range (len(lower_angle)):
            if right_angle == lower_angle[j]:
                first_weight.append(rlDict[int(right_angle[1])])
    
    weight.append(first_weight)
print "weights (right angles of paths) =", '\n', weight,'\n'



"""
Rearranging weights for final solution
"""

preEquation = []
for i in range (len(weight)):
    for j in range (len(weight[i])):
        preEquation.append(weight[i][j])
#print "preEquation =", '\n', preEquation, '\n'


"""
Simplifying weights
"""

position = []
for row in range (N+1):
    for column in range (N+1):
        position.append([row,column])
finEquation = []
for time in position:
    amount = 0
    for i in range (len(preEquation)):
         if time == preEquation[i][0]:
             amount = amount + preEquation[i][1]
    if amount != 0:
        finEquation.append([time,amount])
print "Final Equation =", '\n', finEquation, '\n'

                                                                                                                                                                                                                                                                                                                                                                            
