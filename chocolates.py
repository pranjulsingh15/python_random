def chocolate_count(child_time, A, B, C):
    count = 0
    while count < C:
        count = 0
        count = sum([child_time[-1] // i for i in child_time])
        child_time.append(A * (child_time[-1]) + B)
    else:
        return child_time[-2]


if __name__ == "__main__":
    X, A, B, C = list(map(int, input().split(" ")))
    child_time = [X]
    time = chocolate_count(child_time, A, B, C)
    print("Minimum time required is ", time)