# time to cook
import copy

# TO DO LIST
# consider if # given equations > # variables
# add support for infinite/no solutions

# matrix operation functions
"""def remove_column(matrix, index): # finished, seems to work
    for i in range(0, len(matrix)):
        matrix[i].pop(index)
    return matrix"""

def det(matrix): # finished, in-depth debugging TBD
    PDC = copy.deepcopy(matrix)

    # base case
    length = len(matrix)
    if length == 2:
        return delist(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])
    if length == 1:
        return delist(matrix[0])
    
    # otherwise - FINALLY
    output = 0 
    for i in range(0, length):
        output += matrix[0][i] * det(minor(matrix, (0, i))) * ((-1)**i)
        matrix = copy.deepcopy(PDC)
    return delist(output)


def inverse(matrix): # issue with det sometimes outputting a list
    output = copy.deepcopy(matrix)
    odet = det(matrix)
    for i in range(len(output)):
        for j in range(len(output)):
            #print(det(minor(matrix, (i, j))))
            #print(((-1)**(i+j)))
            #print(((-1)**(i+j)) * det(minor(matrix, (i, j)))[0])
            output[i][j] = ((-1)**(i+j)) * det(minor(matrix, (i, j)))#[0] #* output[i][j] check this is how you find the inverse
    #print(output)

    new_output = copy.deepcopy(output)
    for i in range(len(output)):
        for j in range(len(output)):
            """p = -1
            try:
                int(output[i][j])
                p = output[i][j]
            except:
                print(output[i][j])
                print(output)
                p = output[i][j][0]"""
            new_output[j][i] = output[i][j]/odet #output[i][j]/odet # i swear to skibidi if this brekas bc of pointers im actually going to shsdass
    return new_output

def apply(matrix, vector):
    output = []
    for row in matrix:
        value = 0
        for i in range(len(row)):
            value += row[i] * vector[i]
        output.append(value)
    return output

def minor(matrix, position):
    output = copy.deepcopy(matrix)
    output.pop(position[0])
    for i in range(0, len(output)):
        output[i].pop(position[1])
    return output

def delist(thing):
    while True:
        try:
            float(thing)
            return thing
        except:
            thing = thing[0]

#"""
# input section
variables = input("please input your variables with one space between each (i.e., a b, x y z) \n").split(" ") # note: potential issue if same variable issued twice

mform = []
constants = []
while True:
    mline = []
    raw = input("please type in an equation with all variables on the left and constants on the right, or 'finish' if you wish to finish entering equations. The constant cannot be negative, and please include a coefficient of 1 if necessary \n")
    if raw == "finish":
        break

    line = list(raw)
    for i in range(line.count(" ")):
        line.remove(" ")
    
    for variable in variables:
        value = 0
        if variable in line:
            posicion = line.index(variable)
            for i in range(1, 10000):
                if posicion - i >= 0 and line[posicion - i].isdigit(): 
                    value += (10**(i-1)) * int(line[posicion - i])
                    #print(line[posicion - i])
                elif line[posicion - i] == "-":
                    value *= -1
                    break
                else: 
                    break
            value = 1 if value == 0 else value
        else: # if it isn't in the equation
            value = 0
        mline.append(value)
    # constant
    value = 0
    posicion = len(line)
    for i in range(1, 10000):
            if posicion - i >= 0 and line[posicion - i].isdigit(): 
                value += (10**(i-1)) * int(line[posicion - i])
            else: 
                break
    constants.append(value)
    mform.append(mline)

    print("line: " + str(line))
    #print("mline: " + str(mline))
    print("constant: " + str(constants))
    print("mform: " + str(mform))
#"""

"""
variables = ["a", "b", "c"]
mform = [[2, 13, -2], [1, 1, 1], [0, 1,0]]
constants = [22, 6, 2]
#"""
"""
variables = ["a", "b"]
mform = [[5, 5], [5, 0]]
constants = [35,10]
#"""
# solving section
# check for infinite/no answers
if det(mform) == 0 or len(mform) < len(variables):
    print("unfortuantely, there are either no or infinite solutions. Good luck!")

# main solving
solution = apply(inverse(mform), constants)
output_str = []
for i in range(len(solution)):
    output_str.append("{}: {}".format(str(variables[i]), str(solution[i])))
    output_str.append("\n")
print("solutions: ")
print("".join(output_str))
