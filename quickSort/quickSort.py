def sort(arr):

    if len(arr) < 2:
        return arr

    node = arr[0]

    maior = [i for i in arr[1:] if i >= node]
    menor = [i for i in arr[1:] if i < node]

    

    return sort(menor) + [node] + sort(maior)



print(sort([2,2,6,3,8,1,87]))