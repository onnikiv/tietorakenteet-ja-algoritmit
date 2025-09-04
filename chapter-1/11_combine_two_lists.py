
def combine_lists(list1, list2):
    output_list = []
    
    for i in list1:
        output_list.append(i)
    
    for i in list2:
        output_list.append(i)

    output_list.sort()
    return output_list
    
