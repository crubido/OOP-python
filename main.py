from point import Point, ePoint, Segment


def main():
    p1 = Point(4, 2)
    p2 = Point(6, 6)
    s1 = Segment(p1, p2)
    print(s1.length())


if __name__ == "__main__":
    main()
