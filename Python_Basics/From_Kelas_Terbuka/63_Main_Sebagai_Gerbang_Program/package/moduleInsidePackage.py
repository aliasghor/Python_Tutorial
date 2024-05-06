def findCommonNumbers(data_list: list, num: int) -> int:
    """A function to count how many numbers that is showed inside of a list"""
    count = 0

    for i in data_list:
        if i == num:
            count += 1

    return count