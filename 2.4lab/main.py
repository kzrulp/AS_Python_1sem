а)
def capitalize_words(text, separator=' '):
    parts = text.split(separator)
    result = []

    for word in parts:
        result.append(word.capitalize())

    return separator.join(result)

б)
def filter_elements(list1, list2, filter_function=None):
    result = []

    for x in list1:
        if filter_function is None or filter_function(x):
            result.append(x)

    for x in list2:
        if filter_function is None or filter_function(x):
            result.append(x)

    return result

в)
def merge_dictionaries(*dicts):
    result = {}

    for d in dicts:
        for key in d:
            result[key] = d[key]

    return result


г)
def unique_keys(*dicts):
    result = {}

    for i in range(len(dicts)):
        for key in dicts[i]:
            count = 0

            for j in range(len(dicts)):
                if key in dicts[j]:
                    count += 1

            if count == 1:
                result[key] = dicts[i][key]

    return result
