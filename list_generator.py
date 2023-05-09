import random

def generate_list(n,mini,maxi):
    lst = []
    for i in range(n):
        lst.append(random.randint(mini,maxi))
    return lst

def create_ordered_list(n, mini, maxi, reverse=False):
    lst = generate_list(n,mini,maxi)
    lst = sorted(lst)
    if reverse == True:
        lst = lst[::-1]
    return lst

def generate_float_list(n):
    lst = []
    for i in range(n):
        lst.append(random.random())
    return lst

if __name__ == '__main__':
    print(max(41100000,233222784))