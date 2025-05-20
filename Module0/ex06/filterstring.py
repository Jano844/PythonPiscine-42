

def is_longer_than_n(word, n):
    """If word has more than 4 characters return true"""
    return len(word) > n


if __name__ == "__main__":
    is_longer_than_n("Test", 4)
