#Bubble sort

class BubbleSort:
    def sort(a_list):
        for i in range(len(a_list)-1):
            for j in range(len(a_list)-1-i):
                if(a_list[j] > a_list[j+1]):
                    a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
