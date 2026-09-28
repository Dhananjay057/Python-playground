import time

def sum_of_all_nums(num):
    total=0
    for i in range(1,num+1):
        total= total+i
    return total

start = time.perf_counter()
print(sum_of_all_nums(10000))
end = time.perf_counter()
print(f"Time taken: {end - start}")

def sum_of_all_nums2(num):
    list = [num for num in range(1,num+1)]
    return sum(list)

start = time.perf_counter()
print(sum_of_all_nums2(10000))
end = time.perf_counter()
print(f"Time taken: {end - start}")

def sum_of_all_nums3(num):
    list = {num for num in range(1,num+1)}
    return sum(list)

start = time.perf_counter()
print(sum_of_all_nums3(100))
end = time.perf_counter()
print(f"Time taken: {end - start}")

def sum_of_all_nums4(num):
    list = (num for num in range(1,num+1))
    return sum(list)

start = time.perf_counter()
print(sum_of_all_nums4(10000))
end = time.perf_counter()
print(f"Time taken: {end - start}")     

def sum_of_all_nums5(num):
    return num*(num+1)//2

start = time.perf_counter()
print(sum_of_all_nums5(10000))
end = time.perf_counter()
print(f"Time taken: {end - start}") 