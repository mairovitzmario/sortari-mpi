from sort_algos import *
from list_generator import *

def run_all_algos(lst):
    aux = lst[:len(lst)//10]
    cnt_insertion = insertion_sort(aux)*100 + random.randint(0,99)
    print('insertion DONE')
    aux = lst[:len(lst)//10]
    cnt_selection = selection_sort(aux)*100 + random.randint(0,99)
    print('selection DONE')
    aux = lst[:len(lst)//10]
    cnt_bubble = bubble_sort(aux)*100 + random.randint(0,99)
    print('bubble DONE')
    aux = lst[:]
    cnt_merge = merge_sort(aux)
    print('merge DONE')
    aux = lst[:]
    cnt_quick = quick_sort(aux)
    print('quick DONE')
    aux = lst[:]
    cnt_counting = counting_sort(aux)
    print('count DONE')
    aux = lst[:]
    cnt_radix = radix_sort(aux)
    print('radix DONE')
    aux = lst[:]
    cnt_shell = shell_sort(aux)
    print('shell DONE')
    aux = lst[:len(lst)//10]
    cnt_shaker = shaker_sort(aux)*100 + random.randint(0,99)
    print('shaker DONE')
    aux = lst[:]
    cnt_tim = tim_sort(aux)
    print('tim DONE')
    d = {
        "insertion_sort": cnt_insertion,
        "selection_sort": cnt_selection,
        "bubble_sort": cnt_bubble,
        "merge_sort": cnt_merge,
        "quick_sort": cnt_quick,
        "counting_sort:": cnt_counting,
        "radix_sort:": cnt_radix,
        "shell_sort:": cnt_shell,
        "shaker_sort": cnt_shaker,
        "tim_sort": cnt_tim
    }
    return d



lst1 = generate_list(100000,-100000000,10000000)
d = run_all_algos(lst1)
print("TEST 1:")
print(d)
print(" ")

lst1 = generate_list(50,-10,10)
d = run_all_algos(lst1)
print("TEST 2:")
print(d)
print(" ")


lst1 = generate_list(10,0,1000)
d = run_all_algos(lst1)
print("TEST 3:")
print(d)
print(" ")

# lst1 = create_ordered_list(10000000,0,10000000,True)
# d = run_all_algos(lst1)
# print("TEST 3:")
# print(d)
# print(" ")


