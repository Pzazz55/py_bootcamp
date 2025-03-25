'''
There are 3 ways of doing this -
- Simply tracking time elapsed
- Using the 'timeit' module
- Special %%timeit "magic" for Jupyter Notebooks
'''

def func_one(n):
    return [str(num) for num in range(n)]

def func_two(n):
    return list(map(str, range(n)))

print(func_one(10))
print(func_two(10))

#APPROACH#1
import time

print("APPROACH#1")
#GRAB THE CURRENT TIME BEFORE RUNNING THE CODE
start_time = time.time()
#RUN THE CODE
result = func_one(10000)
#GRAB THE CURRENT TIME AFTER RUNNING THE CODE
end_time = time.time()
#ELAPSE TIME
elapsed_time = end_time - start_time
print("The difference using 'time' for func_one is : ", elapsed_time)

#GRAB THE CURRENT TIME BEFORE RUNNING THE CODE
start_time = time.time()
#RUN THE CODE
result = func_two(10000)
#GRAB THE CURRENT TIME AFTER RUNNING THE CODE
end_time = time.time()
#ELAPSE TIME
elapsed_time = end_time - start_time
print("The difference using 'time' for func_two is : ", elapsed_time)


#APPROACH#2
import timeit

print("APPROACH#2")
stmt_one = '''
func_one(100)
'''
setup_one = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

time_fun_one = timeit.timeit(stmt_one, setup_one, number=1000000)
print("The difference using 'timeit' for func_one is : ", time_fun_one)

stmt_two = '''
func_two(100)
'''
setup_two = '''
def func_two(n):
    return [str(num) for num in range(n)]
'''
time_fun_two = timeit.timeit(stmt_two, setup_two, number=1000000)
print("The difference using 'timeit' for func_two is : ", time_fun_two)