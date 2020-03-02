def main():
    a = list(map(int, input().split()))
    a[:] = a[::-1]
    print(*a)


if __name__ == "__main__":
    main()
