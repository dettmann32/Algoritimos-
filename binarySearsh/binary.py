def binarySearsh(arr, value):

    inicio = arr[0]

    final = arr[len(arr) - 1]

    meio = (inicio + final) // 2

    while(final >= inicio):

        if value == arr[meio]:
            return meio 
            break
        
        
            
        if arr[meio] >= value:
            final = meio
            meio = (inicio + final) // 2

        elif arr[meio] < value:

            inicio = meio
            meio = (inicio + final) // 2


array = [1,3,4,6,7,8,9,8]
print(binarySearsh(array, 6))
print(array[binarySearsh(array,6)])