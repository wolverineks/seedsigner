import timeit


class A:
    def get_dict(self):
        return {"a": 1, "b": 2}


def get_dict():
    return {"a": 1, "b": 2}


# instantiate once, call method 1e6 times
a = A()
method_time = timeit.timeit(a.get_dict, number=1_000_000)

# call function 1e6 times
func_time = timeit.timeit(get_dict, number=1_000_000)

# include instantiation cost separately
instantiate_time = timeit.timeit(lambda: A(), number=1_000_000)

print(f"method: {method_time:.3f}s")
print(f"function: {func_time:.3f}s")
print(f"instantiate: {instantiate_time:.3f}s")
