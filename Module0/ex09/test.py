from ft_package import count_in_list


def main():
    """main"""
    print(count_in_list(["toto", "tata", "toto"], "toto"))
    print(count_in_list(["toto", "tata", "toto"], "tutu"))


if __name__ == "__main__":
    main()
