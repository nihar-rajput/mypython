rows = int(input("enter the # of rows: "))
columns = int(input("enter the # of columns: "))
symbol  = input("enter the symbol to use: ")

for x in range(0,rows):
     for y in range(0,columns):
          print(symbol,end="")
     print()