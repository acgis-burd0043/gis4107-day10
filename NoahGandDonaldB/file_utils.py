
# ------------------------------------------------------------------------------

def main():
    pass

def get_file_content(file_name):
    """Dump the contents of demo test file as a string"""
    try:
        with open(file_name) as in_file:
            file_contents = in_file.read().replace('\n', '')
        return file_contents

    except IOError:
        return '{} does not exist'.format(file_name)


def write_to_file(file_name, content):
    pass



if __name__ == '__main__':
    main()