import time
import concurrent.futures

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def calculate_factorials_with_threadpoolexecutor(numbers):
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(factorial, number) for number in numbers]
        for f in concurrent.futures.as_completed(results):
            print(f.result())
    end = time.perf_counter()
    print("Time taken with ThreadPoolExecutor: ", end - start)

def calculate_factorials_with_processpoolexecutor(numbers):
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(factorial, number) for number in numbers]
        for f in concurrent.futures.as_completed(results):
            print(f.result())
    end = time.perf_counter()
    print("Time taken with ProcessPoolExecutor: ", end - start)

if __name__ == '__main__':
    numbers = [10, 20, 30, 40, 50]

    start = time.perf_counter()
    calculate_factorials_with_threadpoolexecutor(numbers)
    end = time.perf_counter()
    thread_time = end - start

    start = time.perf_counter()
    calculate_factorials_with_processpoolexecutor(numbers)
    end = time.perf_counter()
    process_time = end - start

    if thread_time < process_time:
        print("ThreadPoolExecutor was faster.")
    else:
        print("ProcessPoolExecutor was faster.")