def make_averager():
    """calculate the average but only save the counts and total of number instead of exact numbers"""
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return averager


if __name__ == "__main__":
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))
