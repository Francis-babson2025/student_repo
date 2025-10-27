def add_them_up(n):

    if n == 1:
        return n
    else:
        return n + add_them_up(n-1)


total = add_them_up(4)
print(total)


'''
add_them_up(4) = 4 + add_them_up(3)
add_them_up(3) =           3  + add_them_up(2)
add_them_up(2) =                     2 + add_them_up(1)

add_them_up(1) = 1
add_them_up(2) = 2 + add_them_up(1) = 2 + 1 = 3
add_them_up(3) = 3 + add_them_up(2) = 3 + 3 = 6
add_them_up(4) = 4 + add_them_up(3) = 4 + 6 = 10                     

'''
