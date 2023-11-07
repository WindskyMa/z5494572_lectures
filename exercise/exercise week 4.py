'''
in class exercise 1
Write a Python funcion to print the even numbers from a given list, and return the result as a list.
Please test using this list [0,1,2,3,4,5,6,7,8,9,10,20,22,23,25,29,30,31]
'''

test_list = [0,1,2,3,4,5,6,7,8,9,10,20,22,23,25,29,30,31]
def print_even_numbers(lis):
    even_list = []
    for item in lis:
        if item % 2 == 0:
            even_list.append(item)
    return even_list
even_numbers_list = print_even_numbers(test_list)
print(even_numbers_list)



'''
in-class Exercise 2
Please use list comprehension to construct a list from the squares of each element in the
following list
Only if the value of the square is greater than 150.
lst = [2,3,10,14,20,21,25,13,15]
'''

lst = [2,3,10,14,20,21,25,13,15]
new_lst =[item ** 2 for item in lst if item ** 2 > 150]
print(new_lst)

