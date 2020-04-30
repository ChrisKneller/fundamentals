import random
import time
import csv
from mergesort import mergesort

def generate_list(length: int, max_multiplier: int = 10) -> list:
    '''
    Return a list of input size with randomly generated values between 0 and the size * max_multiplier.

    E.g. if the input size is 100 and the max_multiplier is 10, the values will be between 0 and 100*10=1000
    '''
    return [random.randint(0,length*max_multiplier) for _ in range(length)]

sorting_algorithms = {
    'builtin': sorted,
    'mergesort': mergesort,
}

def test_sort_algos(
    output_file: str = 'csv/sorting_comparison.csv', 
    write_method: str = 'a',
    num_lists: int = 50,
    spacing: int = 10,
    sorting_algorithms=sorting_algorithms):

    '''
    Randomly generate lists of different sizes with random values and apply different sorting algorithms to them, recording performance.

    Data is written to the specified output_file in the format '10,0.00001,mergesort' where 10 is the number of items, 0.00001 is
    the time in seconds to run the algorithm, and mergesort is the name of the sorting algorithm used.
    '''

    with open(output_file, write_method, newline='') as file:
        
        writer = csv.writer(file)
       
        if write_method == 'w':
            writer.writerow(['num_items', 'time(s)', 'algorithm'])
        
        for i in range(num_lists):

            gen_list = generate_list(i*spacing)

            for name,sort in sorting_algorithms.items():
                
                start = time.perf_counter()
                new_list = sort(gen_list)
                end = time.perf_counter()
                assert new_list == sorted(gen_list), f"Result is not sorted. Your {name} algorithm failed."
                time_taken = end-start
                writer.writerow([len(new_list), time_taken, name])


            