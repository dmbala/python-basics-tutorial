def print_helloname(name = "friend"):
    '''This function returns the string hello name'''
    local_string = "hello " + name
    return local_string

var = print_helloname()
print(var)
var = print_helloname("Joe")
print(var)


