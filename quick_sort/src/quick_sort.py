
class QuickSort:
    def sort(items):
        if len(items) > 1:

            pivot_index = len(items) // 2
            print(pivot_index)
            smaller = []
            larger = []
            for i, val in enumerate(items):
                if i != pivot_index:
                    if val < items[pivot_index]:
                        smaller.append(val)
                    else:
                        larger.append(val)
            QuickSort.sort(smaller)
            QuickSort.sort(larger)
            items[:] = smaller + [items[pivot_index]] + larger
