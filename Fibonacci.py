# Function to generate Fibonacci sequence up to a limit upto 100
def generate_fibonacci(limit):

    fib_seq = [0, 1]


    while True:

        next_term = fib_seq[-1] + fib_seq[-2]


        if next_term > limit:
            break


        fib_seq.append(next_term)

    return fib_seq



fibonacci_sequence = generate_fibonacci(100)


print("Fibonacci sequence up to 100:", fibonacci_sequence)

