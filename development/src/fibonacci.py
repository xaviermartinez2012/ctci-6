'''Functions to calculate the Nth Fibonacci number'''
import time


def fib(n_th):
    '''Computes Nth fibonacci number'''
    if n_th <= 0:
        return 0
    if n_th == 1:
        return 1
    return fib(n_th - 1) + fib(n_th - 2)


def fib_memo(n_th, cache):
    '''Computes Nth fibonacci number using memorization'''
    if n_th <= 0:
        return 0
    if n_th == 1:
        return 1
    if n_th in cache:
        return cache[n_th]
    cache[n_th] = fib_memo(n_th - 1, cache) + fib_memo(n_th - 2, cache)
    return cache[n_th]


def main():
    '''Compares implementations of Nth fibonacci number calculators'''
    test_n_values = range(2, 33)
    fibonacci_cumm_time = fibonacci_memo_cumm_time = 0
    remaining_output = []
    for n_value in test_n_values:
        time_start = time.process_time()
        fibonacci_number = fib(n_value)
        fibb_elapsed_time = time.process_time() - time_start
        fibonacci_cumm_time += fibb_elapsed_time
        print(f'fib({n_value}) = {fibonacci_number}. ' +
              f'Runtime = {fibb_elapsed_time:.6f}')
        time_start = time.process_time()
        fibonacci_number = fib_memo(n_value, {})
        fibb_memo_elapsed_time = time.process_time() - time_start
        fibonacci_memo_cumm_time += fibb_memo_elapsed_time
        remaining_output.append(
            f'fib_memo({n_value}) = {fibonacci_number}. ' +
            f'Runtime = {fibb_memo_elapsed_time:.6f}')
    seperator = f'{42*"-"}'
    print(seperator)
    for output in remaining_output:
        print(output)
    print(seperator)
    print(f'Total runtime of fib={fibonacci_cumm_time:.6f}')
    print('Total runtime of fib_memo=' +
          f'{fibonacci_memo_cumm_time:.6f}')


if __name__ == '__main__':
    main()
