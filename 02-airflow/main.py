def main():
    test(name = 'ayush', age = 52)

def test(**kwargs):
    print(type(kwargs))
    print(kwargs['name'])
    print(kwargs['age'])
    print(kwargs)


if __name__ == "__main__":
    main()
