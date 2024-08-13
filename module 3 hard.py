data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def sum(*args):
    s = 0
    for arg in args:
        if isinstance(arg, (list, tuple, set)):
            s += sum(*arg)
        elif isinstance(arg, dict):
            s += sum(*arg.items())
        elif isinstance(arg, str):
            s += len(arg)
        elif isinstance(arg, (int, float)):
            s += arg
    return s
print (sum(data_structure))