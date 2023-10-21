# Finds all prime numbers between 1 and number n using Sieve of Eratosthenes
def find_prime(n):
    if isinstance(n, int) and n > 1:
        marked = [True for i in range(n)]
        all_nums = [i for i in range(n)]
        i = 2
        while i * i < n:
            for j in range(i + i ,n, i):
                marked[j] = False
            i += 1
        return [val for val, bool in zip(all_nums, marked) if bool and val not in [0,1]]
    else:
        raise ValueError("n must be larger than 1")

            


