count = 0


def two_person(a_side, b_side):
    move_a_to_b(a_side[0], a_side[1], a_side, b_side)


def three_person(a_side, b_side):
    move_a_to_b(min(a_side), max(a_side), a_side, b_side)
    move_b_to_a(min(b_side), a_side, b_side)
    move_a_to_b(min(a_side), max(a_side), a_side, b_side)


def four_person_or_more(a_side, b_side):
    move_a_to_b(min(a_side), sorted(a_side)[1], a_side, b_side)
    move_b_to_a(min(b_side), a_side, b_side)
    move_a_to_b(max(a_side), sorted(a_side)[-2], a_side, b_side)
    move_b_to_a(min(b_side), a_side, b_side)


def move_a_to_b(first_num, second_num, a_side, b_side):
    global count
    a_side.remove(first_num)
    a_side.remove(second_num)
    b_side.append(first_num)
    b_side.append(second_num)
    count += max(first_num, second_num)


def move_b_to_a(num, a_side, b_side):
    global count
    b_side.remove(num)
    a_side.append(num)
    count += num


if __name__ == '__main__':
    a_side = list(map(int, input().split(" ")))
    b_side = []

    while len(a_side) != 0:
        if len(a_side) == 1:
            count += a_side.pop()
        elif len(a_side) == 2:
            two_person(a_side, b_side)
        elif len(a_side) == 3:
            three_person(a_side, b_side)
        elif len(a_side) >= 4:
            four_person_or_more(a_side, b_side)
    print(count)
