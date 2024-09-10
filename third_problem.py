#I choose merge method to sort list, because it's have O(n log n) time which make it fast

def merge(left_list:list, right_list:list)->list:  
    result_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)
    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:

            if left_list[left_list_index] <= right_list[right_list_index]:
                result_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                result_list.append(right_list[right_list_index])
                right_list_index += 1

        elif left_list_index == left_list_length:
            result_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            result_list.append(left_list[left_list_index])
            left_list_index += 1
    return result_list

def sort_by_merge(unsorted_list:list)->list:  
    length = len(unsorted_list)
    if length <= 1:
        return unsorted_list
    half = length // 2
    left_list = sort_by_merge(unsorted_list[:half])
    right_list = sort_by_merge(unsorted_list[half:])
    return merge(left_list, right_list)

def main():
    test_list = [30, 10, 176, 3, 15, 94, 39, 189, 259, 300]  
    test_list = sort_by_merge(test_list)  

if __name__ == '__main__':
    main()
