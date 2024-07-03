def print_params(a=1, b='строка', c=True):
    # print(a, b, c, d) # Лишний аргумент приведёт к ошибке, невпихуемый
    print(a, b, c)


# print_params()
# print_params(a=1, b='строка')
print_params(b=25, c=[1, 2, 3])
# print_params(c = [1,2,3])
values_list = [1, 'строка', True]
values_dict = {'a': 25, 'b': 30, 'c': 27}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ['fire', 1993]
print_params(*values_list_2, 42)


# def print_params(*params):  # *args, **kwargs  # 1)
#     print(*params)
#
#
# print_params(1, 2, 3, 4, 5, 6, 7)
#
#
# def print_params(a, b, c):  # 2)
#     print(a, b, c)
#
#
# list_ = [1, 2, 3]  # 2.1)
# print_params(list_, 2, 5)
#
# list_ = [1, 2, 3] # 2.2)
# print_params(*list_)  # *
#
# list_ = [1, 2] # 2.3)
# print_params(1, *list_)
#
# dict_ = {'a': 1, 'b': 2, 'c': 3} # 2.4)
# print_params(**dict_)  # **


# def print_params(**kwargs):  # *args, **kwargs # 3
#     print(kwargs)
#
#
# dict_ = {'a': 1, 'b': 2, 'c': 3}
# print_params(**dict_)  # **


# def print_params(**kwargs):  # *args, **kwargs # 4)
#     for key in kwargs:
#         print(key)
#
#
#
# dict_ = {'a': 1, 'b': 2, 'c': 3}
# print_params(**dict_)

# def print_params(**kwargs):  # *args, **kwargs # 5)
#     for key, value in kwargs.items():
#         print(key, value)
#
#
# dict_ = {'a': 1, 'b': 2, 'c': 3}
# print_params(**dict_)


# def print_params(a, b, c):  # 6)
#     print(a, b, c)
#
#
# list_ = [1, 2]
# dict_ = {'c': 9}
# print_params(*list_, **dict_)
