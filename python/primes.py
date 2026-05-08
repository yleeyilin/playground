def sieve_of_eratosthenes(n):
    """
    our goal here is to find all the primes, up to and inclusive of n 
    """
    is_prime = [True for _ in range(n+1)]
    p = 2 
    while p ** 2 < n:
        if (is_prime[p]):
            # Note: starts from p^2 not 2p because anyth smaller has been marked by smaller primes
            #       therefore, more efficient. 
            for i in range(p*p, n+1, p): 
                is_prime[i] = False
        p += 1
    res = list(p for p in is_prime if is_prime[p])
    return res 

def smallest_prime_factor(n): 
    """
    our goal here is to find the smallest prime number that divides it

    note: this is a variation of sieve of eratosthenes 
    ref: https://codeforces.com/blog/entry/140773
    """
    prime_factor = [i for i in range(n+1)]
    p = 2 
    while p ** 2 < n:
        if (prime_factor[p] == p): # is prime 
            for i in range(p*p, n+1, p): 
                if (prime_factor[i] == i): # no smaller prime has reached it 
                    prime_factor[i] = p
        p += 1
    return prime_factor 