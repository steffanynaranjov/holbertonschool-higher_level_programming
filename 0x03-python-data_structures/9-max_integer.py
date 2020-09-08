def max_integer(my_list=[]):
    if my_list is not None and len(my_list) > 0:
        max = 0

        for num in my_list:
            if num >= max:
                max = num

        return max
