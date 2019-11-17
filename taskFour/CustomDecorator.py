import time


def time_it(func):
    highest_time_taken = 0

    def inner():
        nonlocal highest_time_taken

        start = time.time()
        resp = func()  # actual function getting called over here
        end = time.time()

        if highest_time_taken < (end - start):
            highest_time_taken = (end - start)

        print('Start time: ' + str(start * 1000) + " ms")
        print('End time: ' + str(end * 1000) + " ms")
        print('Time Taken: ' + str((end - start) * 1000) + " ms")
        print('Highest Time Taken: ' + str(highest_time_taken * 1000) + " ms")

        return resp

    return inner


@time_it
def my_test_function():
    print('-'*50)
    a = 0
    for i in range(1, 10):
        a = i

    return a


@time_it
def my_test_function2():
    print('-' * 50)
    a = 0
    for i in range(1, 100000):
        a = i

    return a


@time_it
def my_test_function3():
    print('-' * 50)
    a = 0
    for i in range(1, 100000000):
        a = i

    return a


# works
# print(time_it(my_test_function))

print("Output: " + str(my_test_function()))
print("Output: " + str(my_test_function2()))
print("Output: " + str(my_test_function3()))
