string = "heello"
# convert to a list
# for or a while loop
# detect whether the previous item matches the current item
# if it matches then __delitem__
# if it doesn't match do nothing

def convert_to_list():
    # ['h','e','l']
    convert_list = []
    convert_list = list(string)
    return convert_list

def iterate_through_list(converted_list):
    list_range = len(converted_list)
    print(list_range)
    for i in range(list_range):
        print(i)
        try: 
            if converted_list[i-1] == converted_list[i]:
                converted_list.remove(converted_list[i])
                print(converted_list)
        except:
            pass
    return converted_list

converted_list = convert_to_list()

print(iterate_through_list(converted_list))
