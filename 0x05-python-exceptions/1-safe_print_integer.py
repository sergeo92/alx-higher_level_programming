def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except ValueError:
        return False
    return True


if __name__ == '__main__':
    print(safe_print_integer("5"))
