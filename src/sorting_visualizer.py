import matplotlib.pyplot as plt 
import random
from matplotlib.patches import Patch



def universal_legend():
    legend_elements = [
        Patch(facecolor='green', label='Sorted'),
        Patch(facecolor='red', label='Comparing'),
        Patch(facecolor='yellow', label='To be Swapped'),
        Patch(facecolor='orange', label='Minimum')
    ]
    plt.legend(handles=legend_elements, loc='upper right', fontsize=8)
    
def visualize(arr, colors, title):
    plt.clf()
    plt.bar(range(len(arr)), arr, color=colors)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title(title)
    universal_legend()
    
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            colors = ['lightblue'] * len(arr)
            colors[j] = 'red'
            colors[j + 1] = 'red'
            
            for k in range(n - i, n):
                colors[k] = 'green'
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            visualize(arr, colors, "Bubble Sort - Sorting in Progress")
            plt.pause(0.000001)
        colors = ['green'] * len(arr)
        visualize(arr, colors, "Bubble Sort - Sorting in Progress")
        plt.pause(0.000001)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        
        min_idx = i
        for j in range(i + 1, n):
            colors = ['lightblue'] * len(arr)
            for k in range(i):
                colors[k] = 'green'
            colors[j] = 'red'
            colors[min_idx] = 'orange'
            colors[i] = 'yellow'
            if arr[j] < arr[min_idx]:
                min_idx = j
            visualize(arr, colors, "Selection Sort - Sorting in Progress")
            plt.pause(0.00001)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        visualize(arr, colors, "Selection Sort - Sorting in Progress")
        plt.pause(0.01)
    visualize(arr, ['green'] * len(arr), "Selection Sort - Sorting in Progress")
    plt.pause(0.01)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    stack = [(0, len(arr) - 1)]
    
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                visualize(arr, ['lightblue'] * len(arr), "Quick Sort - Sorting in Progress")
                plt.pause(0.01)

            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            pivot_idx = i + 1
            visualize(arr, ['lightblue'] * len(arr), "Quick Sort - Sorting in Progress")
            plt.pause(0.01)
            stack.append((low, pivot_idx - 1))
            stack.append((pivot_idx + 1, high))
            

def merge_sort(arr):
    n = len(arr)
    size = 1
    
    while size < n:
        for start in range(0, n, size * 2):
            mid = min(start + size, n)
            end = min(start + size * 2, n)
            merge(arr, start, mid, end)
            visualize(arr, ['lightblue'] * len(arr), "Merge Sort - Sorting in Progress")    
            plt.pause(0.05)
        size *= 2
    

def merge(arr, start, mid, end):
    left = arr[start:mid]
    right = arr[mid:end]
    
    i = 0
    j = 0
    k = start
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

while True:
    plt.ion()
    print("""
╔════════════════════════════════════════════════╗
║     DSA SORTING ALGORITHM VISUALIZER           ║
╚════════════════════════════════════════════════╝

Select a sorting algorithm to visualize:

    1. Bubble Sort
    2. Selection Sort
    3. Merge Sort
    4. Quick Sort
    5. Exit

╚════════════════════════════════════════════════╝
""")
    choice = int(input("╚═➤ Enter your choice (1-5): "))
    if choice == 5:
        print("Exiting the visualizer. Goodbye!")
        break
    x = random.sample(range(1, 51), 50)
    visualize(x, ['lightblue'] * len(x), "Press Enter in console to start sorting")
    plt.pause(0.1)
    input("Press Enter to start sorting...")
    
    if choice == 1:
        bubble_sort(x)
    elif choice == 2:
        selection_sort(x)
    elif choice == 3:
        merge_sort(x)
    elif choice == 4:
        quick_sort(x)
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
    plt.title("Sort completed - Press enter in console to close graph...")
    input("Press enter in console to close graph...")
    plt.close()
    