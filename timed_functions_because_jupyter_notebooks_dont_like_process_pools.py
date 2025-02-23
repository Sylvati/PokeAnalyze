import time
def execute_task(permutation):
    time.sleep(3)  # Simulate 3-second execution
    #print(f"Done: {permutation}")
    return f"Executed: {permutation}"


import itertools
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
#import timed_functions_because_jupyter_notebooks_dont_like_process_pools as lmao

# Simulated execution function (replace with your actual function)


def main():
    items = [1, 2, 3, 4, 5, 6]  
    permutations = list(itertools.permutations(items, 4))
    print(len(permutations))

    

    with ThreadPoolExecutor() as executor:
        #futures = [executor.submit(execute_task, perm) for perm in permutations]
        results = executor.map(execute_task, permutations)

    for r in results:
        print(r)

if __name__ == "__main__":
    main()
