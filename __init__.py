from random import shuffle


def shuffle_dict(dictionary):
    keys = list(dictionary.keys())
    shuffle(keys)
    dictionary2 = dict()
    for key in keys:
        dictionary2.update({key: dictionary[key]})
    return dictionary2

