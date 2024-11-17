def is_golden_number(n):
#     # function implementation ...
    if n < 0 or n > 1000 : 
        return False 
    
    for a in range(1, n):
        b = n - a
        if (a * b) % 1000 == 0:
            return True
        
    return False #boolen
    # fuel and maximium dont work properly and decrypt not finished 

#print(is_golden_number(65)) 
#print(is_golden_number(70)) 
#print(is_golden_number(73)) 
        
