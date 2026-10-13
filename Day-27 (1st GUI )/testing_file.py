def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
print(add(2, 3, 3, 5, 6, 7, 8,))
# def all_aboard(a, *args, **kw):
#     print(a, args, kw)
#
#
# all_aboard(4, 7, 3, 0, x=10, y=64)

