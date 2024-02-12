def reverse_integer(k):

    reversed_str = str(k)[::-1]

    if k < 0:
        reversed_str = '-' + reversed_str[:-1]
    return int(reversed_str)


num = int(input("Enter an integer: "))
reversed_num = reverse_integer(num)
print("Reversed integer:", reversed_num)

