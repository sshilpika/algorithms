# Insertion Sort

class InsertionSort:
    def sort(a_list):
        for i in range(1 , len(a_list)):
            key = a_list[i]
            j = i-1
            while j >= 0  and a_list[j] > key :
                a_list[j+1] = a_list[j]
                j -= 1
            a_list[j+1] = key
