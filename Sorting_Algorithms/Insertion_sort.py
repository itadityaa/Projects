import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def insertion_sort(arr):
    """
    Perform insertion sort on the given array and return a list of arrays representing each step of the sorting process.

    Parameters:
    arr (array_like): The input array to be sorted.

    Returns:
    list: A list of arrays representing each step of the sorting process.
    """
    sorted_arr = [arr.copy()]
    n = len(arr)
    number_of_operations = 0  
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            number_of_operations += 1  
            sorted_arr.append(arr.copy()) 
        arr[j + 1] = key
    return sorted_arr, number_of_operations

def plot_sorting(arr):
    """
    Plot the sorting process of the given array using insertion sort.

    Parameters:
    arr (array_like): The input array to be sorted.
    """
    sorted_arr, _ = insertion_sort(arr)
    fig, ax = plt.subplots()
    ax.set_title('Insertion Sort Visualization')
    bar_rects = ax.bar(range(len(arr)), arr, color='lightblue')
    
    def update_fig(idx):
        arr = sorted_arr[idx]
        for i, rect in enumerate(bar_rects):
            rect.set_height(arr[i])
        ax.set_xlabel(f'Operation: {idx + 1}/{len(sorted_arr)}')
    
    anim = animation.FuncAnimation(fig, func=update_fig,
                                   frames=len(sorted_arr),
                                   interval=250, repeat=False)
    plt.show()

# Example usage
arr = np.random.randint(1, 100, size=10)
plot_sorting(arr)
print(f'Original array: {arr}')
print(f'Sorted array: {insertion_sort(arr)[0][-1]}')
print(f'Number of operations: {insertion_sort(arr)[1]}')