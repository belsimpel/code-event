import hashlib
import sys


def create_hash(string_to_hash):
    """
    This method creates an MD5 hash from the given `string_to_hash`.

    Note: We're not using update() here because in that case, the
    arguments will be concatenated (which is undesired and creates a
    incorrect output).

    :param string_to_hash
    :return:
    """
    return hashlib.md5(string_to_hash).hexdigest()


def is_hash_valid(hash_to_validate):
    return hash_to_validate[0:5] == '00000'


def find_lowest_integer_for_a_valid_hash(private_key):
    for i in range(sys.maxsize):
        string_to_hash = (private_key + str(i)).encode("UTF-8")
        hashed_string = create_hash(string_to_hash)

        if is_hash_valid(hashed_string):
            return i

    return None


if __name__ == "__main__":
    private_key_input = input("What is your private key: ")

    lowest_integer = find_lowest_integer_for_a_valid_hash(private_key_input)

    if lowest_integer is not None:
        print("The lowest positive integer to create a valid hash is: {0}".format(lowest_integer))
    else:
        print("Wasn't able to find a positive integer to create a valid hash from.")