
def average(array):
    # your code goes here
    set_ = set(array)
    sum_ = sum(set_)
    length = len(set_)
    avg = round(sum_/length,3)
    return avg