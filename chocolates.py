count = 0
def chocolate_count(child_time, A, B, C):
    global count
    while count < C:
        count = 0
        current_count(child_time)
        child_time.append(A * (child_time[-1]) + B)
    else:
        return child_time[-2]


def current_count(child_time):
    global count
    for i in range(0, len(child_time)):
        count = count + (child_time[-1] // child_time[i])


if __name__ == "__main__":
    X, A, B, C = input().split(" ")
    X, A, B, C = int(X), int(A), int(B), int(C)
    child_time = [X]
    time = chocolate_count(child_time, A, B, C)
    print("Minimum time required is ", time)
