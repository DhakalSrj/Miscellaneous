# Suraj Dhakal
# 11/04/2022
# windows using VScode (omega compatible)

#regular expression package import 
import re 

# using regular expression syntax
# the operators '+-*/' are characters with special meaning in Regular expression so need to be escaped with '\' 
rpnOperators = re.compile('[\+\-\*\/]')

#if file exists then open the file to read else print error message 
def openFiletoRead(fileName):
    try:
        file = open(fileName,"r")
        return file
    except IOError :
        print("No such file exists")
        return 0
# Reverse Polish Notation Calculator function
def rpnCalculator(inputfile):
    #iterate through the file 
    for inputLine in inputfile:
        print(inputLine)
        # replacing newline and carriage return using string rstrip() function 
        inputLine =inputLine.rstrip("\n\r")
        #splitting the input lines with spaces 
        expressions = inputLine.split(" ")
        print(expressions)

        #create an empty list for number expression
        emptyList =[]


        #iterate to get the values in the expression. pop two values and use the operator 
        # To perform the operation and put the result back in the list and print the result  

        for expression in expressions:
            if rpnOperators.match(expression):
                value1 = emptyList.pop()
                value2 = emptyList.pop()
            #addition
            if expression == '+':
                emptyList.append(value1 + value2)
            #subtraction 
            elif expression == '-':
                emptyList.append(value2 - value1)
            #multiplication
            elif expression == '*':
                emptyList.append(value1 * value2)
            #division
            elif expression == '/' :
                #check for zero when dividing
                if value1 == 0 :
                    print("Cannot perform the action as denominator is zero")
                    continue
                emptyList.append(value2 /value1)
            # else if append the number 
            elif expression.isdigit():
                emptyList.append(int(expression))
            #else if the expression is not valide print error message 
            else:
                print("invalid Expression")
                break
        # printing the result 
        if len(emptyList) == 1:
             print("The calculated result of the expression is : %f\n" %emptyList[0])
        emptyList.clear

#start of main           
def main():
    # the provided input file name
    File = "input_RPN.txt"
    # open the file
    filehandler = openFiletoRead(File)
    # if file exists then perform the calculation
    if filehandler is not None:
        rpnCalculator(filehandler)

if __name__ == '__main__':
    main()


        









