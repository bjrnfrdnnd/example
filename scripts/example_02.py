import sys

import pkg_resources

from example.example import print_hi

EXAMPLE_DATA_FILE_NAME = pkg_resources.resource_filename('example', 'data/example_data')

def main(argv):
    print_hi('example')
    print(EXAMPLE_DATA_FILE_NAME)

if __name__ == '__main__':
    sys.exit(main(sys.argv))