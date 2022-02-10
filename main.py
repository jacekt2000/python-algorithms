def binary_search(seq, item):
    begin_index = 0
    end_index = len(seq) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = seq[midpoint]
        if midpoint_value == item:
            return midpoint
        elif item < midpoint_value:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1
    return None
seq_a = [2,4,5,6,7,8,9,10,11,12,13,14]
item_a = 8

print(binary_search(seq_a, item_a))
