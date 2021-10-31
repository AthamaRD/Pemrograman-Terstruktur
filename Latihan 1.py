def isPythagoras(A, B, C):
    if(A**2 + B**2 == C**2 ): return True
    else : return False

print('A = 3, B = 4, C = 5', ' --> ' ,isPythagoras(3,4,5))
print('A = 5, B = 9, C = 12', ' --> ' ,isPythagoras(5,9,12))
print('A = 8, B = 6, C = 10', ' --> ' ,isPythagoras(8,6,10))
print('A = 7, B = 8, C = 11', ' --> ' ,isPythagoras(7,8,11))