def apply_all_func(int_list, *functions):
    results = {}
    for fun_name in functions:
        results[fun_name.__name__] = fun_name(int_list)
    return results


print(apply_all_func([6, 20, 15, 9], max, min), end='')
print(apply_all_func([6, 20, 15, 9], len, sum, sorted), end='')
print(apply_all_func([6, 20, 15, 9],  enumerate, bool, frozenset))
