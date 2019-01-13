"""
https://github.com/fatih/color/blob/master/color.go<Paste>
"""
version = "0.1.1"
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


formats = {
    "bright": 1,
    "bold": 1,
    "dim": 2,
    "italic": 3,
    "underlined": 4,
    "blink": 5,
    "reverse": 7,
}


def get_color_func(color):
    def fn(text, format=None):
        if isinstance(format, str):
            format = formats[format]
        assert format in list(range(1, 9))

        code = get_color_code(color)
        if not code:
            raise Exception("color {} not support".format(color))
        if format:
            return "\033[{};{}m{}\033[0m".format(format, code, text)
        else:
            return "\033[{}m{}\033[0m".format(format, code, text)

    return fn


for name in __all__:
    locals()[name] = get_color_func(name.upper())
