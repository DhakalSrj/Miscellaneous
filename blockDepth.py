#Suraj Dhakal
#11/30/2022
# Windows using vscode(python 18.2)


def openfiletoRead(fileName):
    #open the file to read if there exists a file 
    try:
        file = open(fileName,"r")
        return file
    # if there doesnot exists a file then print an error message 
    except IOError:
        print("No such file exists ")
        return 0
# the function that tracks the nesting depth of the braces of the input file 
def blockDepth(pointertoFile):
    #create a list to keep track of the braces 
    stack = []
    #count to track the block depth
    count_depth = 0
    #iterate over the file
    for line in pointertoFile:
        #remove the newline and the carriage return from the input file using rstrip()
        value = line.rstrip('\n\r')
        #if there are whitespaces strip the line 
        val = value.strip()
        #check if there exists a comment in the line 
        if val.__contains__('//'):
             # get the starting index 
            starting_index = val.find('//')
            if(starting_index == 0 ):
                print(count_depth,value)
                continue
            else:
                val = val.split('//')[0]
        notprinted = True
        # Implement Stack 
        for char in val:
            #check for block comments 
            if char == '*' and len(stack) != 0 and stack[-1] == '*':
                    stack.pop()
            elif char == '*':
                   stack.append('*')
            #if the character is a quote and stak top contains a quote 
            #pop it from the stack
            elif char == '"' and len(stack) != 0 and stack[-1] == '"':
                stack.pop()
            #if the character is a quote push it to the stack
            elif char == '"':
                stack.append('"')
            #if the charcater is a opening brace and not inside a quote 
            #increment ths count 
            #push it to the stack 
            elif char== '{' :
                #if there is a brace inside quotes skip
                if len(stack) != 0 and stack[-1] == '"':
                    continue
                #if there is a brace inside block comment skip
                elif len(stack) != 0  and stack[-1] == '*':
                    continue
                else:
                    count_depth +=1
                    # print the output 
                    print(count_depth,value)
                    #push the brace into the stack
                    stack.append('{')
                    notprinted =False
            #if the charcater is a closing brace and not inside a quote 
            #decrement ths count 
            #pop it from the stack 
            elif char == '}':
                #if there is a brace inside quotes skip
                if len(stack) != 0 and stack[-1] == '"':
                    continue
                #if there is a brace inside block comment skip
                elif len(stack) != 0  and stack[-1] == '*':
                    continue
                else:
                    # print the output 
                    print(count_depth,value)
                    #increment the depth count 
                    count_depth -=1
                    #pop the brace from the stack
                    stack.pop()
                    notprinted =False
        if notprinted:
            print(count_depth,value)
    # if there is no braces remaining then matched else and stack isn't empty 
    # print error message 
    if len(stack) != 0 :
        print("ERROR!!! : expected '}'.\n")     
#start of main           
def main():
    # the input file containig the program
    File = "input.txt"
    # open the file
    filehandler = openfiletoRead(File)
    # if file exists then perform the calculation
    if filehandler is not None:
        blockDepth(filehandler)

if __name__ == '__main__':
    main()


        

