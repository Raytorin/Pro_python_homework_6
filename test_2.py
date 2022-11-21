ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}


def unique_numbers(id_number):
    numbers = []
    for i in id_number.values():
        numbers.extend(i)
    numbers = list(set(numbers))
    numbers.sort()
    return numbers


if __name__ == '__main__':
    unique_numbers(ids)
