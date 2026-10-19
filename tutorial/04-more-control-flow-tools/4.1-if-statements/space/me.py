x = int(input("Please enter an integer: ")) # apply comp to x variable 

def run_my_input(y: int | None):
    if y < 0:
        y = 0
        return 'Negative changed to zero'
    elif y == 0: # else if  
        return 'Zero' 
    elif y == 1:
        return 'Single' 
    else:
        return 'More'

# print(run_my_input(x))
