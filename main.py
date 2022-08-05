from writter import executor, info_decorator


@info_decorator
def main():
    executor(filename='result')


if __name__ == '__main__':
    main()
