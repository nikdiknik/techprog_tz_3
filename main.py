def my_min(arr):
    ans = arr[0]
    for i in arr:
        if ans > i:
            ans = i
    return ans


def my_max(arr):
    ans = arr[0]
    for i in arr:
        if ans < i:
            ans = i
    return ans


def my_sum(arr):
    ans = 0
    for i in arr:
        ans += i
    return ans


def my_product(arr):
    ans = 1
    for i in arr:
        ans *= i
    return ans


def main_func(path):
    with open(path, 'r') as file:
        data = list(map(int, file.read().split()))
    # print(data)
    return [my_min(data), my_max(data), my_sum(data), my_product(data)]


# main_func('data.txt')
