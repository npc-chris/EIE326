# coords_manager.py

points = []  # this will be a list of tuples


def add_point(x: float, y: float):
    pt = (x, y)      # tuple
    points.append(pt)


def list_points():
    for p in points:
        print(p)


def bounding_box():
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    return (min(xs), min(ys)), (max(xs), max(ys))  # two tuples


def main():
    # rudimentary CLI loop...
    pass


if __name__ == '__main__':
    main()
