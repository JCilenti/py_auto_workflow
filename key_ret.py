from operator import ge


def get_key():
    token_file = open("../token.txt", "r")
    key = token_file.read(39)
    print(key)


if __name__ == "__main__":
    get_key()