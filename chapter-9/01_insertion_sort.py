from random import randint

def insertion_sort(array):
    """
    Sort the array using the Insertion sort algorithm
    
    Parameters:
    - array: The array to be sorted
    
    Returns: Nothing. The array is sorted in-place.
    """
    keep_sorting = True
    
    # Tää ei todellakaan oikea tapa, mutta se toimii
    # Sattuu päähän
    while keep_sorting:
        sorts = 0
        for i in range(len(array)):
          
            if i > 0:
                if array[i] < array[i-1]:
                    array[i],array[i-1] = array[i-1],array[i]
                    sorts += 1
            
        if sorts == 0:
            break



	

array = [randint(0,100) for _ in range(20)]
sorted_array = sorted(array)
insertion_sort(array)
print(array, " array")
print(sorted_array, " sorted")

print(array == sorted_array)