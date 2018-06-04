"""
Hamilton Evans

CSCI 0200 Programming Assingment 1

Did not work with anyone.

Sample Output:

deduce (["(A and C) or not D","(B or C) and (D or  A)","(not C and B) or (not D and not B)"])

A C D B : 
---------
T T F F 
T F F T


14 hours
"""


import itertools as iter


def caps (string):
    """
    Function that returns the variables in the strings (the capital letters)
    """
    
    arrayCap = []
    
    letters = list (string)
    
    for letter in letters:
        if (letter.isupper ()): # only adding capital ltters to arrayCap
            
            if letter in arrayCap:
                continue
            
            else:
                arrayCap.append (letter)
                
        else:
            continue
        
    return arrayCap



def generateTruthList (columns):
    """
    Function that returns all of the possible combinations
    of true and false given the number of variables.
    Has 2^columns variables in array. 
    """
    
    temp = []
    result = []
    
    combinations = list (iter.product ([True, False], repeat = columns)) # returning arrays with each iteration of
                                                                            # true and false given number of columns
    for element in combinations:
        for i in element:
            temp.append (i)
    
    for value in temp: # for printing later
        if (value == True):
            result.append ('T')
            
        else:
            result.append ('F')
    
    return result






def evaluateString (string, truthList, dictLets, capsTot):
    """
    Function that returns true or false values for
    each combination from the truthList, given the string.
    Using the dictionary of the letters, it orders the variables correctly for each string.
    """
    letters = caps (string)
    tempString = string
    resultArray = []
    
    for i in range (len (truthList)):
        if truthList[i] == "T":
            truthList[i] = "True"
            
        elif truthList[i] == "F":
            truthList[i] = "False"
    
    
    
    for x in range ((len (truthList)) // len (capsTot)):
        temp1 = []
        for z in range (len (letters)):
            important = dictLets [letters [z]] # which letter is used for each position in truthList
            type = ((x * len(capsTot)) + important) # index in truthList
            temp = tempString.replace (letters[z], truthList[type])  # Replacing variables with True or False to be evaluated
            tempString = temp
        
        for q in range (len (capsTot)): # even if less vars in string than total, will return given truthlist for all vars
            temp1.append (truthList [x * len (capsTot) + q])
        
        
        result = eval (tempString) 
        
        if result == True:
            resultArray.append (temp1)
            
        tempString = string
 
    return resultArray

        

def makeBoard (capsTot, finalArray):
    """
    Formats the printing of the final board.
    Prints all of the variables, a line of "-",
    then the true/false combinations for the variables that
    make all of the strings true
    """
    
    columns = len (capsTot)
    print ('\n')
    
    for i in range (columns):  # printing top line
        if (i == (columns) - 1): 
            print (capsTot [i], end =  " :")
            
        else:
            print (capsTot [i], end = ' ')
    
    print (" ")
    print("-" * (len (capsTot) * 3 - 2))
                   
    for element in finalArray:
        for i in range (columns): # for printing asthetic
            if (element [i] == "True"):
                element [i] = "T"
            elif (element [i] == "False"):
                element [i] = "F"
            print (element [i], end = ' ')
        print ("")
        
        
            
    
def deduce (arrayStrings):
    """
    Takes all of the above functions and combines them,
    producing a truth table with the correct evaluated strings of true and false
    for every string from the starting array.
    """
    capsTot = []
    result = []
    dictLets = {}
    final = []
    first = []
    x = 0
    
    print ("A")
    for string in arrayStrings: # making capsTot
        c = caps (string)
        
        for element in c: 
            if element in capsTot: # making capsTot- a list of all off the variables in the strings in the order they are given
                continue
        
            else:
                capsTot.append (element)
                
    lengthCapsTot = len(capsTot)
    truthList = generateTruthList (lengthCapsTot) # making one master truthList for the total number of variables
    
    for string in arrayStrings: # needed a separate loop because need capsTot and the truthList, found in/after the last one
        letters = caps (string) # figuring out how many variables are in a certain string
        
        for let in letters: 
            for i in range (lengthCapsTot):
                if (let == capsTot [i]):
                    dictLets [let] = i # making a dictionary of all of the letters in order 
        
        temporary = evaluateString (string, truthList, dictLets, capsTot)
        result.append (temporary) # result is an array of arrays with true/false values that work for each individual string
        dictLets = {}
    
    if (len (arrayStrings) != 0): # making sure there is a string inputted
        first = result [0] # only checking for the first string- must be true in first string to be true overall
        
    else:
        x = 1 # if no string inputed
        print ("Input a String!")
    
    for i in range (len (first)):  # for each true/false statement that was successful in the first string it compares with all of the other strings
        for element in result:   # if also true in every other string, appends to final array
            if (first [i] in element): 
                if (element == result [-1]): # if in the last array and still there, must be true for all
                    final.append (first [i])
 
                continue
            else:
                break
    
    if (x == 0):
        makeBoard (capsTot, final) #make board with final array!

        
        