# Algorithm: Dutch National Flag (DNF)

## 1. Definition
The Dutch National Flag algorithm is a linear-time partitioning algorithm that sorts an array containing three distinct values. Named after Edsger Dijkstra and inspired by the three colors of the Dutch flag (red, white, blue).

## 2. Core Concepts
- **Three-Way Partitioning**: Divides array into three sections
- **Invariant Maintenance**: Maintains sections for values less than, equal to, and greater than the pivot
- **In-Place Sorting**: Performs sorting without extra space

## 3. How It Works
- Maintain three pointers: low, mid, and high
- Divide array into four regions:
    - [0 to low-1]: Values less than pivot
    - [low to mid-1]: Values equal to pivot
    - [mid to high]: Unprocessed values
    - [high+1 to end]: Values greater than pivot

## 4. Key Operations
- **Initialize**: Set low = mid = 0, high = array length - 1
- **Process**: While mid ≤ high:
    - If current element < pivot: swap with low region
    - If current element = pivot: move to next
    - If current element > pivot: swap with high region

## 5. Time Complexity
- **Time**: O(n) - single pass through array
- **Space**: O(1) - in-place sorting
- **Comparisons**: Maximum of n comparisons
- **Swaps**: Maximum of n swaps

## 6. Implementation Strategies
- **Single Pivot**: Traditional implementation with one pivot value
- **Multiple Pivots**: Extended version for more than three partitions
- **Stability**: Can be modified for stable sorting

## 7. When to Use
- **Three-Value Sorting**: When array contains exactly three distinct values
- **Partition Problems**: As a subroutine in quicksort
- **Color Sorting**: For problems involving color arrangement

## 8. Limitations
- **Fixed Values**: Only works efficiently for three distinct values
- **Element Distribution**: Performance affected by initial distribution
- **Stability**: Basic implementation is not stable

## 9. Example Code
```python
def dutch_national_flag(arr):
    low = mid = 0
    high = len(arr) - 1
    pivot = 1  # Usually the middle value (1 in case of 0,1,2)

    while mid <= high:
        if arr[mid] < pivot:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] > pivot:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
        else:
            mid += 1
    
    return arr
```