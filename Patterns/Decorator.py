import functools


def nsum_bed(n):
    assert(n >= 0), 'n must be >= 0'
    if n in known_sum:
        return known_sum[n]
    res = n + nsum(n-1)
    known_sum[n] = res
    return res


def memoize(fn):
    known = dict()
    @functools.wraps(fn)
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]


@memoize
def nsum(n):
    '''Returns the sum of the first n numbers'''
    assert(n >= 0), 'n must be >= 0'
    return 0 if n == 0 else n + nsum(n-1)


@memoize
def fibonacci(n):
    '''Returns the nth number of the Fibonacci sequence'''
    assert(n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n-1) + fibonacci(n-2)
    return memoizer


if __name__ == '__main__':
    from timeit import Timer
    measure = [{'exec': 'fibonacci(100)', 'import': 'fibonacci',
                'func': fibonacci}, {'exec': 'nsum(200)', 'import': 'nsum',
                                     'func': nsum}]
    for m in measure:
        t = Timer('{}'.format(m['exec']),
                  'from __main__import  {} '.format(m['import']))
        print('name: {}, doc: {}, executing: {}, time:{}'.format(
            m['func'].__name__, m['func'].__doc__, m['exec'], t.timeit()))
