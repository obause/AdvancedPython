def function1():
    return "{} {}".format("Hello", "World")


def function2():
    return f'{"Hello"} {"World"}'


def main():
    function1()
    function2()


if __name__ == "__main__":
    main()

# Syntax tree anzeigen: python -m ast syntax_tree.py
