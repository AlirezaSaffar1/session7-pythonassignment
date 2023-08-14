def is_sorted(list):
    return list == sorted(list)

user_input = input("give me some random numbers in a list (seprate numbers by using space): ")
list = [int(i) for i in user_input.split()]

if is_sorted(list):
    print("the list is sorted.")
else:
    print("the list is not sorted.")