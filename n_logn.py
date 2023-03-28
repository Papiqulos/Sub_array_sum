import sys
import numpy as np
import timeit


# Divide and Conquer O(nlogn) πολυπλοκότητα
def max_subarray_nlogn(arr, low, high):

    if low == high - 1:
        return low, high, arr[low]
    else:
        mid = (low + high) // 2
        left_start, left_end, left_max = max_subarray_nlogn(arr, low, mid)
        right_start, right_end, right_max = max_subarray_nlogn(arr, mid, high)
        bound_1, bound_2, max_sum = max_crossing_subarray(arr, low, mid, high)
        if left_max > right_max and left_max > max_sum:
            return left_start, left_end, left_max
        elif right_max > left_max and right_max > max_sum:
            return right_start, right_end, right_max
        else:
            return bound_1, bound_2-1, max_sum


def max_crossing_subarray(arr, low, mid, high):

    sum_left = float('-inf')
    sum_temp = 0
    cross_start = mid
    for i in range(mid - 1, low - 1, -1):
        sum_temp = sum_temp + arr[i]
        if sum_temp > sum_left:
            sum_left = sum_temp
            cross_start = i

    sum_right = float('-inf')
    sum_temp = 0
    cross_end = mid + 1
    for i in range(mid, high):
        sum_temp = sum_temp + arr[i]
        if sum_temp > sum_right:
            sum_right = sum_temp
            cross_end = i + 1
    return cross_start, cross_end, sum_left + sum_right


if __name__ == '__main__':
    # sys.setrecursionlimit(5000) # Μπορεί να χρειαστεί σε άλλα συστήματα
    try:
        n1, n2 = [int(x) for x in input("Δώστε δύο μεγέθη για τους πίνακες (χωρισμένα με ενα space: ").split(' ')]
        # Φτιάχνουμε πρώτα τa array με seed το ΑΜ
        AM = 123456

        np.random.seed(AM)
        # n1 = 8 ** 6  # Μέγεθος ώστε ο αλγόριθμος να τελειώνει σε περίπου 1 δευτερόλεπτο
        arr1 = np.random.randint(-100, 100, n1)
        # print(f"array with {n1} elements: {arr1}")

        t0 = timeit.default_timer()
        bound1_1, bound1_2, sub_sum1 = max_subarray_nlogn(arr1, 0, n1)
        print(f"Maximum sub-array sum with {n1} elements: {sub_sum1}")
        print(f"Indexes of sub-array start:{bound1_1} end:{bound1_2}")
        t1 = timeit.default_timer() - t0
        print(f"Execution time: {t1}")

        np.random.seed(AM)
        # n2 = 8 ** 7  # Μέγεθος ώστε ο αλγόριθμος να τελειώνει σε χρόνο τάξης δευτερολέπτων
        arr2 = np.random.randint(-100, 100, n2)
        # print(f"array with {n2} elements: {arr2}")

        t0 = timeit.default_timer()
        bound2_1, bound2_2, sub_sum2 = max_subarray_nlogn(arr2, 0, n2)
        print(f"Maximum sub-array sum with {n2} elements: {sub_sum2}")
        print(f"Indexes of sub-array start:{bound2_1},end:{bound2_2}")
        t1 = timeit.default_timer() - t0
        print(f"Execution time: {t1}")
    except KeyboardInterrupt:
        quit()
