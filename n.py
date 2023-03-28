import numpy as np
import timeit


# Kadane's Algorithm O(n) πολυπλοκότητα
def max_subarray_n(arr, n):
    max_sum = 0
    current_sum = 0

    bound_1 = 0
    bound_2 = 0
    current_start = 0

    for i in range(n):
        current_sum = current_sum + arr[i]
        current_end = i
        if current_sum < 0:
            current_sum = 0
            current_start = current_end + 1

        if max_sum < current_sum:
            max_sum = current_sum
            bound_1 = current_start
            bound_2 = current_end

    return max_sum, bound_1, bound_2


if __name__ == '__main__':

    try:

        n1, n2 = [int(x) for x in input("Δώστε δύο μεγέθη για τους πίνακες (χωρισμένα με ενα space: ").split(' ')]

        # Φτιάχνουμε πρώτα τa array με seed το ΑΜ
        AM = 1083738

        np.random.seed(AM)
        # n1 = 2 * 9 ** 7  # Μέγεθος ώστε ο αλγόριθμος να τελειώνει σε περίπου 1 δευτερόλεπτο
        arr1 = np.random.randint(-100, 100, n1)
        # print(f"array with {n1} elements: {arr1}")

        t0 = timeit.default_timer()
        sub_sum1, bound1_1, bound1_2 = max_subarray_n(arr1, n1)
        print(f"Maximum sub-array sum with {n1} elements: {sub_sum1}")
        print(f"Indexes of sub-array start:{bound1_1} end:{bound1_2}")
        t1 = timeit.default_timer() - t0
        print(f"Execution time: {t1}")

        np.random.seed(AM)
        # n2 = 4 * 9 ** 7  # Μέγεθος ώστε ο αλγόριθμος να τελειώνει σε χρόνο τάξης δευτερολέπτων
        arr2 = np.random.randint(-100, 100, n2)
        # print(f"array with {n2} elements: {arr2}")

        t0 = timeit.default_timer()
        sub_sum2, bound2_1, bound2_2 = max_subarray_n(arr2, n2)
        print(f"Maximum sub-array sum with {n2} elements: {sub_sum2}")
        print(f"Indexes of sub-array start:{bound2_1},end:{bound2_2}")
        t1 = timeit.default_timer() - t0
        print(f"Execution time: {t1}")

    except KeyboardInterrupt:
        quit()
