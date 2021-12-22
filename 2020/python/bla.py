# import only system from os 
from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 

import msvcrt
        
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

print("SARAH")
clear()

loop = 'y'
x = 5
y = 5
print(('\n' * y)+ (' ' * x) + 'o' )

while loop == 'y':
    result = msvcrt.getch()
    # print(result)
    if result == b'l':
        x += 1

    elif result == b'k':
        if x > 0:
            x -= 1
        
    elif result == b'p':
        if y > 0:
            y -= 1

    elif result == b',':
        y += 1
        
    elif result == b'n':
        loop = 'n'
    
    clear()
    print(('\n' * y)+ (' ' * x) + 'o' )