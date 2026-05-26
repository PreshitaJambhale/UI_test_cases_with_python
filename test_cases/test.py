import math


def find_duplicates(list1):
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    print(list2)

    return list2

find_duplicates([1,2,3,3,2,5,6,3])
"""
def find_count(value):
    list1 = list(value)
    list2 = []
    for i in list1:
        list2.append(list1.count(i))
        print(list2)
        a =1
        count_dict = {list1[a]:list2[a]}
        a+=1

    return count_dict


find_count("harshali")


def remove_duplicates(values):
    list2 = []
    for i in values:
        if i not in list2:
            list2.append(i)

    return list2

print(remove_duplicates([1,2,7,5,3,2,4,2,3]))

 """
def factorial(number):
    multiplier = 1
    list1 = [x - 1 for x in range(2, number + 2)]
    factorial_number = math.prod(list1)
    print(factorial_number)
    return factorial_number
    """
    for i in list1
    while(number >=0):
        num = multiplier*number
        multiplier-=1
        return factorial
"""


print(factorial(5))



