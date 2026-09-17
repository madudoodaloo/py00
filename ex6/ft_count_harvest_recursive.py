def recursive_print(total: int, curr: int) -> None:
    if (curr > total):
        print("Harvest time!")
        return
    print("Day", curr)
    recursive_print(total, curr + 1)


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    recursive_print(days, 1)
