def remove_digits(filename):
    f = open(filename, 'r')
    text = f.read()
    f.close()

    new_text = ''
    for c in text:
        if c < '0' or c > '9':
            new_text = new_text + c

    f = open(filename, 'w')
    f.write(new_text)
    f.close()


def count_symbols(filename):
    f = open(filename, 'r')
    text = f.read()
    f.close()

    return len(text)


def count_lines(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()

    return len(lines)
