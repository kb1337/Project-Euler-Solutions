def foo(n):
    my_list = [1]
    for i in range(3, n + 1, 2):
        my_list.append(i ** 2)
        my_list.append(i ** 2 - i + 1)
        my_list.append(i ** 2 - i + 1 - i + 1)
        my_list.append(i ** 2 - i + 1 - i + 1 - i + 1)

    # print(my_list)
    return sum(my_list)


print(foo(1001))
