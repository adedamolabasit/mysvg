def pop(list):
    def get_last(my_list):
        return my_list[-1]
    list.remove(get_last(list))
    return  list

def outerFunction(text):
    def innerFunction():
        print(text)
    return innerFunction

def nth_power(exponent):
    def power(base):
        return  pow(base,exponent)



