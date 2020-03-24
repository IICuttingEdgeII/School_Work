#recursive fibonnaci generator, w/ memoization
def fibonnaci(n, h):
    if n < 1:
        return 0
    elif n <= 2:
        return 1
    if n in h:
        return h[n]
    else:
        h[n] = fibonnaci(n-1, h)+fibonnaci(n-2, h)
        return fibonnaci(n-1, h) + fibonnaci(n-2, h)

print(fibonnaci(999, {}))
