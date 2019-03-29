#                ©Daniil Samoylov               #
#                   @volyomaS                   #

#                                               #
#   this module could help you to calculate     #
#   some your physics lab related things        #
#                                               #


def get_data(data):
    for i in range(len(data)):
        data[i] = float(data[i])
    return data


def get_dict_data(data):
    if type(data) != list:
        return
    for i in range(len(data)):
        data[i] = float(data[i])
    dict_ = {}
    for i in range(len(data)):
        if data[i] in dict_:
            dict_[data[i]] += 1
        else:
            dict_[data[i]] = 1
    return dict_


def print_dict_data(dict_):
    for i in sorted(dict_.keys()):
        if i != 1.8:
            print(i, '*' * dict_[i])
        else:
            print(i, ' *' * dict_[i])


def average(data):
    return sum(data)/len(data)


def dispersion(data):
    data_new = [(i - average(data)) ** 2 for i in data]
    return (sum(data_new) / len(data)) ** 0.5


def standard_deviation(data):
    data_new = [(i - average(data)) ** 2 for i in data]
    return (sum(data_new) / (len(data) * (len(data) - 1))) ** 0.5


def random_error(data, k_Student):
    return standard_deviation(data) * k_Student


def absolute_error(instrument_error, computational_error, random_error):
    return (instrument_error ** 2 + computational_error ** 2 + random_error ** 2) ** 0.5
