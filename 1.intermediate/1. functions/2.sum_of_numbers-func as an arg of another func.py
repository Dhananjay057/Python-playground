""" Higher order function - function as an argument of another function """

import time

def sum_of_all_nums(num):
    total=0
    for i in range(1,num+1):
        total= total+i
    return total

def sum_of_all_nums2(num):
    return sum([num for num in range(1,num+1)])
def sum_of_all_nums3(num):
    return sum({num for num in range(1,num+1)})
def sum_of_all_nums4(num):
    return sum((num for num in range(1,num+1)))
def sum_of_all_nums5(num):
    return num*(num+1)//2


def time_performance(func, num):
    start = time.perf_counter()
    func(num)
    end = time.perf_counter()
    print(f"Time taken: {end - start}")

time_performance(sum_of_all_nums, 100000)
time_performance(sum_of_all_nums2, 100000)     
time_performance(sum_of_all_nums3, 100000)
time_performance(sum_of_all_nums4, 100000)   
time_performance(sum_of_all_nums5, 100000)

# start = time.perf_counter()
# print(sum_of_all_nums(10000))
# end = time.perf_counter()
# print(f"Time taken: {end - start}")

# start = time.perf_counter()
# print(sum_of_all_nums2(10000))
# end = time.perf_counter()
# print(f"Time taken: {end - start}")

# start = time.perf_counter()
# print(sum_of_all_nums3(100))
# end = time.perf_counter()
# print(f"Time taken: {end - start}")

# start = time.perf_counter()
# print(sum_of_all_nums4(10000))
# end = time.perf_counter()
# print(f"Time taken: {end - start}")     

# start = time.perf_counter()
# print(sum_of_all_nums5(10000))
# end = time.perf_counter()
# print(f"Time taken: {end - start}") 