# https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/python

def even_or_odd(number):
    
    # Compare the Modulo of the input to 2 
    # If no remainder (0) then set return to 'Even'
    # Else set return to 'Odd'
    
    if number % 2 == 0:
        x = "Even"
    else:
        x = "Odd"
        
    return x