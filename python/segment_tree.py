import math

nums = [-1,0,3,6]
x = math.ceil(math.log(len(nums), 2))
expected_len = (2 ** x) * 2 - 1 

segment_arr = [float('inf') for _ in range(expected_len)]

def create_segment_tree(segment_arr, low, high, pos):
    if low == high:
        segment_arr[pos] = nums[low]
        return
    mid = low + (high - low) // 2 
    create_segment_tree(segment_arr, low, mid, 2 * pos + 1) # left child 
    create_segment_tree(segment_arr, mid + 1, high, 2 * pos + 2) # right child 
    segment_arr[pos] = min(segment_arr[2 * pos + 1], segment_arr[2 * pos + 2])

def find_minimum(segment_arr, left, right, low, high, pos):
    if left <= low and high <= right:
        # means total overlap
        return segment_arr[pos]
    if right < low or left > high:
        # means no overlap
        return float('inf')
    # otherwise, means partial overlap 
    mid = low + (high - low) // 2 
    val_1 = find_minimum(segment_arr, left, right, low, mid, 2 * pos + 1)
    val_2 = find_minimum(segment_arr, left, right, mid+1, high, 2 * pos + 2)
    return min(val_1, val_2)

if __name__ == "__main__":
    # print(math.ceil(math.log(4,2)))
    # print(math.ceil(math.log(5,2)))
    # print(math.ceil(math.log(8,2)))
    print(segment_arr)
    create_segment_tree(segment_arr, 0, 3, 0)
    print(segment_arr)

    # suppose we want to query min over [1,3] inclusive
    print(find_minimum(segment_arr, 1, 3, 0, 3, 0))
    print(find_minimum(segment_arr, 2, 3, 0, 3, 0))