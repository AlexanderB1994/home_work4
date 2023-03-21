# 1
def get_sum_from_parameters(*args, **kwargs):
    total = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            total += arg
    for value in kwargs.values():
        if isinstance(value, (int, float)):
            total += value
    return total


print(get_sum_from_parameters(2, 4, "abc", param_1=2))
print(get_sum_from_parameters(2, 4, "abc", param_1=2, param_2="abc", param_3=2.5))


# 2
def get_sum_from_parameters(*args, **kwargs):
    total = 0
    parameters = list(args) + list(kwargs.values())
    for parameter in parameters:
        if isinstance(parameter, (int, float)):
            total += parameter
        elif isinstance(parameter, (list, tuple, set)):
            total += get_sum_from_parameters(*parameter)
    return total


print(get_sum_from_parameters(1, 1, 1, "abc", "12", [1, 1, "cad"]))
print(get_sum_from_parameters(1, 1, 1, "abc", "12", [1, 1, [1, 1], "cad"]))
print(get_sum_from_parameters(1, 1, 1, "abc", "12", [1, 1, [1, 1, {1, 2.5}], "cad"]))
