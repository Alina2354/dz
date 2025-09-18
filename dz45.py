from functools import wraps

def convert_args(*arg_types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            if len(args) != len(arg_types):
                raise ValueError("Number of arguments does not match number of types")

            converted_args = []
            for arg, arg_type in zip(args, arg_types):
                try:
                    converted_arg = arg_type(arg)
                    converted_args.append(converted_arg)
                except ValueError:
                    raise ValueError(f"Could not convert argument '{arg}' to type '{arg_type.__name__}'")
                except TypeError:
                    raise TypeError(f"Could not convert argument '{arg}' to type '{arg_type.__name__}'")


            return func(*converted_args)

        return wrapper
    return decorator


if __name__ == '__main__':
    @convert_args(int, float)
    def calc(a, b):
        print(f"Тип a: {type(a)}, Тип b: {type(b)}")
        return a + b

    print(calc("2", "3.5"))

    @convert_args(str, str, int)
    def greet(name, greeting, repeat):
        return (greeting + " " + name + "! ") * repeat

    print(greet("Alice", "Hello", "2"))

    try:
        print(calc("2", "abc"))
    except ValueError as e:
        print(f"Error: {e}")

