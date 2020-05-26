# find = lambda argument : return value

#def find(x, y):
#    if x != 0 :
#        return x+y

#same as

find = lambda x, y : x + y if x != 0 else 0

twoDarr = [[1, 2, 3, 4, 5],
           [2, 3, 4, 5, 6],
           [3, 4, 5, 6, 7],
           [4, 5, 6, 7, 8]]

#print(twoDarr[1::2]) # prints 2nd & 4th

# sample = [expression context]
sample = [line[1::2] for line in twoDarr]

# list[first index : end index : step]