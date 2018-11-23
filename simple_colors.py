version = "0.1.0"
__all__ = ["black", "red", "green", "yellow", "blue", "magenta", "cyan"]


def get_color_code(color):
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36

    WHITE = 97
    RESET = 0

    return locals().get(color.upper())


def get_color_func(color):
    def fn(text):
        code = get_color_code(color)
        if not code:
            raise Exception("color {} not support".format(color))
        return "\033[{}m{}\033[0m".format(code, text)

    return fn


for name in __all__:
    locals()[name] = get_color_func(name.upper())
