# Made by Evan Quan Oct. 11, 2016
# Converts input number of base 2-36 to output number of base 2-36.
# Gives a comprehensive explanation using Division Algorithm and Positional System.

# Contants
IBASE_MAX = 36
OBASE_MIN = 2
OBASE_MAX = IBASE_MAX

# Main
# Determines what other functions to call and when to call them.
# Parameters: None
# Return values: None
def main():
    # Minimum input base depends on the input number.
    ibase_min = 2
    print("\nBASE CONVERTER\n\nConvert a number from one base to another.\nWorks from base",OBASE_MIN,"up to base",OBASE_MAX,"(0-9,a-z).\n")
    iNum, ibase_min, iNum_original, iList = iNumInput(ibase_min)
    iBase = iBaseInput(iNum_original,ibase_min)
    oBase = oBaseInput()
    oList = [] # Needed to convert Base 10 to Base X
    total = 0 # Sum total in Positional System
    # Deciding what functions to use based on input
    if iBase == 10:
        if oBase != 10:
            print()
            convert10toX(iNum,iBase,oBase,oList,iNum_original)
        else:
            print(iNum_original,"is already base 10.")
    elif iBase != oBase:
        if oBase == 10:
            iNum,oList,total,iList = convertXto10(iNum,iBase,iList,oList,total,iNum_original)
            print("FINAL ANSWER:",iNum_original,"in base",iBase,"converted to base",oBase,"is",str(total) + ".")
        else:
            iNum,oList,total,iList = convertXto10(iNum,iBase,iList,oList,total,iNum_original)
            convert10toX(iNum,iBase,oBase,oList,iNum_original)
    else:
        print(iNum_original,"is already base",str(iBase) + ".")
    repeat()

# Input iNum
# Get input number from user and checks if number is valid
# Parameters: ibase_min
# Return values: iNum, ibase_min, iNum_original, iList
def iNumInput(ibase_min):
    iNum_type_sorted = False
    while not iNum_type_sorted:
        iNum = input("Input number: ").lower() # Defaulted to string
        try:
            if float(iNum) % 1 == 0:
                iNum_type_sorted = True
                iNum = int(float(iNum)) # Turns iNum into integers if all digits
            else:
                print("Input number cannot be a floating point.")
        except ValueError:
            iNum_type_sorted = True
            if "z" in str(iNum):
                ibase_min = 36
            elif "y" in str(iNum):
                ibase_min = 35
            elif "x" in str(iNum):
                ibase_min = 34
            elif "w" in str(iNum):
                ibase_min = 33
            elif "v" in str(iNum):
                ibase_min = 32
            elif "u" in str(iNum):
                ibase_min = 31
            elif "t" in str(iNum):
                ibase_min = 30
            elif "s" in str(iNum):
                ibase_min = 29
            elif "r" in str(iNum):
                ibase_min = 28
            elif "q" in str(iNum):
                ibase_min = 27
            elif "p" in str(iNum):
                ibase_min = 26
            elif "o" in str(iNum):
                ibase_min = 25
            elif "n" in str(iNum):
                ibase_min = 24
            elif "m" in str(iNum):
                ibase_min = 23
            elif "l" in str(iNum):
                ibase_min = 22
            elif "k" in str(iNum):
                ibase_min = 21
            elif "j" in str(iNum):
                ibase_min = 20
            elif "i" in str(iNum):
                ibase_min = 19
            elif "h" in str(iNum):
                ibase_min = 18
            elif "g" in str(iNum):
                ibase_min = 17
            elif "f" in str(iNum):
                ibase_min = 16
            elif "e" in str(iNum):
                ibase_min = 15
            elif "d" in str(iNum):
                ibase_min = 14
            elif "c" in str(iNum):
                ibase_min = 13
            elif "b" in str(iNum):
                ibase_min = 12
            elif "a" in str(iNum):
                ibase_min = 11
            for char in iNum:
                if char not in ("1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"):
                    iNum_type_sorted = False
            if iNum == "":
                iNum_type_sorted = False
            if iNum_type_sorted == False:
                print("Invalid input.")
    iNum_original = iNum
    iList = list(str(iNum)) # Turns iNum into a list of strings if there are letters
    return iNum, ibase_min, iNum_original, iList

# Input Base
# Get input base from user and checks if valid
# Parameters: iNum_original,ibase_min
# Return values: iBase
def iBaseInput(iNum_original,ibase_min):
    iBase_is_int = False # Ensures and converts to int
    while not iBase_is_int:
        iBase = input("Input base: ").lower()
        try:
            if float(iBase) % 1 == 0:
                iBase_is_int = True
                iBase = int(float(iBase))
            else:
                print("Input base cannot be a floating point.")
        except ValueError:
            print("Input base must be an integer.")
        if iBase_is_int:
            if iBase > IBASE_MAX:
                print("Maximum base for %s is %s." % (iNum_original, IBASE_MAX))
                iBase_is_int = False
            elif iBase < ibase_min:
                print("Minimum base for %s is %s." % (iNum_original, ibase_min))
                iBase_is_int = False
    return iBase

# Output Base
# Get output base from user and checks if valid
# Parameters: None
# Return values: oBase
def oBaseInput():
    oBase_is_int = False # Ensures and converts to int
    while not oBase_is_int:
        oBase = input("Output base: ")
        try:
            if float(oBase) % 1 == 0:
                oBase_is_int = True
                oBase = int(float(oBase))
            else:
                print("Output base cannot be a floating point.")
        except ValueError:
            print("Output base must be an integer.")
        if oBase_is_int:
            if oBase > OBASE_MAX:
                print("Maximum base is %s." % OBASE_MAX)
                oBase_is_int = False
            elif oBase < OBASE_MIN:
                print("Minimum base is %s." % OBASE_MIN)
                oBase_is_int = False
    return oBase

# Division Algorithm
# Converts Input Base 10 to Output Base 2-46
# Parameters: iNum,iBase,oBase,iList,oList,iNum_original
# Return values: None
def convert10toX(iNum,iBase,oBase,oList,iNum_original):
    print("Apply Division Algorithm:\nInput number / Output base = Quotient (Q) : Remainder (R)")
    iNum_stored = iNum
    while iNum > 0: # Doing the algorithm
        q = iNum // oBase
        r = iNum % oBase
        print(iNum,"/",oBase,"=",q,":",r)
        iNum = q
        oList.insert(0,r)
    for n,e in enumerate(oList): # Converting numbers to letters if Base > 10
        if e == 10:
            oList[n] = "a"
        elif e == 11:
            oList[n] = "b"
        elif e == 12:
            oList[n] = "c"
        elif e == 13:
            oList[n] = "d"
        elif e == 14:
            oList[n] = "e"
        elif e == 15:
            oList[n] = "f"
        elif e == 16:
            oList[n] = "g"
        elif e == 17:
            oList[n] = "h"
        elif e == 18:
            oList[n] = "i"
        elif e == 19:
            oList[n] = "j"
        elif e == 20:
            oList[n] = "k"
        elif e == 21:
            oList[n] = "l"
        elif e == 22:
            oList[n] = "m"
        elif e == 23:
            oList[n] = "n"
        elif e == 24:
            oList[n] = "o"
        elif e == 25:
            oList[n] = "p"
        elif e == 26:
            oList[n] = "q"
        elif e == 27:
            oList[n] = "r"
        elif e == 28:
            oList[n] = "s"
        elif e == 29:
            oList[n] = "t"
        elif e == 30:
            oList[n] = "u"
        elif e == 31:
            oList[n] = "v"
        elif e == 32:
            oList[n] = "w"
        elif e == 33:
            oList[n] = "x"
        elif e == 34:
            oList[n] = "y"
        elif e == 35:
            oList[n] = "z"
    iNum = ''.join(str(e) for e in oList)
    print("Read the remainder (R) from bottom to top, converting numbers above 9 to their respective letter values.\nEx. 10 = a, 11 = b, 12 = c etc.")
    print(iNum_stored,"in base",oBase,"is",iNum + ".\n") # Output iNum string
    print("FINAL ANSWER:",iNum_original,"in base",iBase,"converted to base",oBase,"is",iNum + ".")

# Positional System
# Converts Input Base 2-16 to Output Base 10
# Parameters: iNum,iBase,iList,oList,total,iNum_original
# Return values: iNum,oList,total,iList
def convertXto10(iNum,iBase,iList,oList,total,iNum_original): 
    print("\nApply Positional System:")
    n = len(str(iNum))
    iStr = ''.join(str(e) for e in iList)
    for n,e in enumerate(iList): # Converts letter elements to integers
        if e in ("a","A"):
            iList[n] = 10
        elif e in ("b","B"):
            iList[n] = 11
        elif e in ("c","C"):
            iList[n] = 12
        elif e in ("d","D"):
            iList[n] = 13
        elif e in ("e","E"):
            iList[n] = 14
        elif e in ("f","F"): # Hexadecimal
            iList[n] = 15
        elif e in ("g","G"):
            iList[n] = 16
        elif e in ("h","H"):
            iList[n] = 17
        elif e in ("i","I"):
            iList[n] = 18
        elif e in ("j","J"):
            iList[n] = 19
        elif e in ("k","K"):
            iList[n] = 20
        elif e in ("l","L"):
            iList[n] = 21
        elif e in ("m","M"):
            iList[n] = 22
        elif e in ("n","N"):
            iList[n] = 23
        elif e in ("o","O"):
            iList[n] = 24
        elif e in ("p","P"):
            iList[n] = 25
        elif e in ("q","Q"):
            iList[n] = 26
        elif e in ("r","R"):
            iList[n] = 27
        elif e in ("s","S"):
            iList[n] = 28
        elif e in ("t","T"):
            iList[n] = 29
        elif e in ("u","U"):
            iList[n] = 30
        elif e in ("v","V"):
            iList[n] = 31
        elif e in ("w","W"):
            iList[n] = 32
        elif e in ("x","X"):
            iList[n] = 33
        elif e in ("y","Y"):
            iList[n] = 34
        elif e in ("z","Z"): # Base 36
            iList[n] = 35
        elif e == "!":
            iList[n] = 36
        elif e == "@":
            iList[n] = 37
        elif e == "#":
            iList[n] = 38
        elif e == "$":
            iList[n] = 39
        elif e == "%":
            iList[n] = 40
        elif e == "^":
            iList[n] = 41
        elif e == "&":
            iList[n] = 42
        elif e == "*":
            iList[n] = 43
        elif e == "(":
            iList[n] = 44
        elif e == ")":
            iList[n] = 45
    iList = [int(i) for i in iList] # Converts all elements of iList to integers
    n = len(iStr)
    while n > 0:
        total += int(iList[len(iList) - n]) * iBase ** (n-1)
        iList = [str(s) for s in iList] # Converts all elements of iList to strings
        print(iList[len(iList) - n],"*",iBase,"^",(n-1),"=",int(iList[len(iList) - n]) * iBase ** (n-1))
        n -= 1
    iNum = int(total)
    print("Sum all products.")
    print(iNum_original,"in base 10 is",str(total) +".\n") # Output must be iNum integer for convert10toX
    return iNum,oList,total,iList
    
# Repeat
# Give user the choice to convert more numbers
# Parameters: None
# Return values: None
def repeat():
    option = input("\nDo you want to convert another number?\n(Yes/No)\n-> ")
    if option in ("y","yes","yes.","yeah","yeah."):
        main()
    elif option in ("n","no","no.","nope","nope."):
        print("Okay. Bye!")
    else:
        print('Choose either "Yes" or "No".')
        repeat()
        
# Start the program
main()
