import matplotlib.pyplot as plt


def midpoint(p1, p2):
    """Return the midpoint between two points."""
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def draw_triangle(points):
    """Draw a triangle from 3 points."""
    x = [points[0][0], points[1][0], points[2][0], points[0][0]]
    y = [points[0][1], points[1][1], points[2][1], points[0][1]]
    plt.plot(x, y)


def sierpinski(points, depth):
    """Recursively draw the Sierpinski triangle."""
    if depth == 0:
        draw_triangle(points)
    else:
        a, b, c = points

        ab = midpoint(a, b)
        bc = midpoint(b, c)
        ca = midpoint(c, a)

        sierpinski([a, ab, ca], depth - 1)
        sierpinski([ab, b, bc], depth - 1)
        sierpinski([ca, bc, c], depth - 1)


def main():
    points = [(0, 0), (1, 0), (0.5, 0.866)]  # roughly equilateral triangle

    plt.figure(figsize=(8, 8))
    sierpinski(points, depth=8)

    plt.axis("equal")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()