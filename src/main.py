from textnode import *


def main():
    my_object = TextNode("Here is my text", TextType.BOLD, "www.test.com")
    print(repr(my_object))


if __name__ == "__main__":
    main()
