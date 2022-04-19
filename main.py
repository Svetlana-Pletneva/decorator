import time


def parametrized_decor(parameter):
    def logger(old_function):
        def new_function(*args, **kwargs):
            current_time = time.localtime()
            start = time.strftime('%d %m %Y %H:%M:%S', current_time)
            result = old_function(*args, **kwargs)
            print(f''' "{old_function.__name__}" running {start} argument's {args} result ({result})''')
            with open(parameter, "a", encoding="utf-8") as file:
                file.write(f''' "{old_function.__name__}" running {start} argument's {args} result ({result})''')
            return result
        return new_function
    return logger


@parametrized_decor('Decorators')
def add_cook_book(cook_book):
    return cook_book


add_cook_book("recipes.txt")
