import concurrent.futures
import time


def run_sleep(sec):
    print(f'Running sleep for {sec} seconds...')
    time.sleep(sec)


if __name__ == '__main__':
    start_time = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        seconds = [5, 4, 3, 2, 1]
        results = executor.map(run_sleep, seconds)

    end_time = time.perf_counter()
    print(f'Completed the process in {round(end_time - start_time, 2)} seconds')
