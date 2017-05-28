file_set = {2015, 2017, 2019}

file_list = [2015, 2017, 2017]

file_list = set(file_list)

print(file_list)

print(type(file_set))
print(type(file_list))

file_list = list(file_list)

print(type(file_list))

file_dict = {
    "last year": 2016,
    "this year": 2017,
    "next year": 2018
}

print(type(file_dict))

print(file_dict)

print(file_dict["this year"])