from collections import Counter

"""NOTE: it is Counter (With cap "C") not counter,
"""

#ONE
'''
a = [1, 1, 2, 3, 4, 4, 5, 5, 6, 6, 6]
print(Counter(a))  
'''


#TWO, Basic op's
'''
a = Counter({1:1, 2:3, 3:2, 5:5})
b = Counter('SPARTANS')
print(a)
print(b)
'''


#THREE
'''
a = Counter({1:2, 3:3, 4:1, 2:2})
print("1's:", a[1])
print("2's:",a[2])
print("3's:",a[3])
'''


#FOUR, Methods of Counter
'''
a = Counter([1,2,3,2,3])
a.update([4,5,6])
print(list((a.elements())))
print(a)
print(a.most_common(3)) #top 3 most common numbers
'''


#FIVE, Some other methods
'''
a = Counter([1,2,3,4,5])
print("Before    : ",a)
a[1] += 3
a[2] += 2
print("After     : ",a)
a.subtract([1,2,3])
print("ThereAfter: ", a)
'''
