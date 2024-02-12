def power_of_two(n):

    return n > 0 and (n & (n - 1)) == 0

num = int(input("Enter an integer: "))

result = power_of_two(num)

print("Is the number a power of two?", result)
