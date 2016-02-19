# Merge sort
class MergeSort:
    def sort(a_list):
        #mid element
        if len(a_list) > 1 :
            mid = len(a_list)//2
            left = a_list[0:mid]
            right = a_list[mid:]

            MergeSort.sort(left)
            MergeSort.sort(right)
            l, r = 0,0
            for i in range(len(a_list)):
                lval = left[l] if l < len(left) else None
                rval = right[r] if r < len(right) else None
                if (lval is not None and rval is not None and lval < rval) or rval is None:
                    a_list[i] = lval
                    l+=1
                elif (lval is not None and rval is not None and lval >= rval) or lval is None:
                    a_list[i] = rval
                    r+=1
                else:
                    print('LVAL ',lval,' RVAL ',rval)
                    raise Exception("could not merge, subarray sizes do not match main array")
