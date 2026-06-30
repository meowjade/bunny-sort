def bubble_sort(arr: list) -> None:
    """Sort the array using bubble sort (in-place).

    Args:
        arr: list to be sorted (modified in-place)
    """
    for m in range(len(arr) - 1, 0, -1):
        swapped = False
        for i in range(m):
            j = i + 1
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                swapped = True
        # Already sorted
        if not swapped:
            return

def insertion_sort(arr: list) -> None:
    """Sort the array using insertion sort (in-place).

    Args:
        arr: list to be sorted (modified in-place)
    """
    for i in range(len(arr) - 1):
        j = i + 1
        element = arr[j]
        if element >= arr[i]:
            continue

        # Find insertion index
        for k in range(j):
            if arr[k] <= element:
                continue

            # Found place to insert
            copy = arr[k:j]
            for s in range(len(copy)):
                arr[s+k+1] = copy[s]
            arr[k] = element
            break

def merge_sort(arr: list) -> list:
    """Sort the array using merge sort (out-of-place).

    Args:
        arr: list to be sorted (not modified)

    Returns:
        New sorted list
    """
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    l = 0
    r = 0
    len_l = len(left)
    len_r = len(right)
    while True:
        has_left = l < len_l
        has_right = r < len_r
        if has_left and has_right:
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
            continue
        
        if has_left:
            result += left[l:]
        elif has_right:
            result += right[r:]
        break
    return result

def quick_sort(arr: list) -> list:
    """Sort the array using quick sort (out-of-place).

    Args:
        arr: list to be sorted (not modified)

    Returns:
        New sorted list
    """
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2
    pivot = arr[mid]
    left = []
    right = []
    for i in range(len(arr)):
        if i == mid:
            continue
        x = arr[i]
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)
    return sorted_left + [pivot] + sorted_right

