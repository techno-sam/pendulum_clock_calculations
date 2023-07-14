import math
import matplotlib.pyplot as plt
from values import *

def theta(t: float) -> float:
    r_over_g = r_total_avg / g
    sqrt_g_over_r = math.sqrt(g / r_total_avg)
    return r_over_g * math.cos(sqrt_g_over_r*t)

def calc_period() -> float:
    sqrt_r_over_g = math.sqrt(r_total_avg / g)
    return 2 * math.pi * sqrt_r_over_g


if __name__ == "__main__":
    f = theta#math.sin

    t_min = -1
    t_max = 1

    t_step = 0.01

    x_pts, y_pts = [], []

    t = t_min

    while t < t_max:
        x_pts.append(t)
        y_pts.append(f(t)*100)
        t += t_step

    print(y_pts)
    print()
    min_pt = min(y_pts)
    print(f"{min_pt=} (count: {y_pts.count(min_pt)})")

    start_idx = -1
    indexes = []
    while True:
        try:
            indexes.append(y_pts.index(min_pt, start_idx+1))
        except ValueError:
            break
        start_idx = indexes[-1]

    print(f"{indexes=}")

    times = [x_pts[i] for i in indexes]

    print(f"{times=}")

    if y_pts.count(min_pt) == 2:
        print("Analyzing period")
        period = times[1] - times[0]
        print(f"{period=} s")
    else:
        print("Count not 2, unable to analyze period. Maybe adjust timing parameters?")

    print("Formulaic period:", calc_period(), "s")

    plt.plot(x_pts, y_pts)
    plt.title("Simple")
    plt.xlabel("Time (s)")
    plt.ylabel("Angle")
    plt.show()
