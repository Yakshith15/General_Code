def count_substring(string, sub_string):
    position = 0
    count = 0
    
    while string.find(sub_string, position) != -1:
        count += 1
        position = string.find(sub_string, position) + 1
    
    return count
