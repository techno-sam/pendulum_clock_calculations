import math
import matplotlib.pyplot as plt
from values import *

def inertia(mass: float, radius: float) -> float: # mass in grams, radius in meters
    return mass * radius*radius

i_body = inertia(m_body, r_body)

i_nuts = [inertia(m_single_nut, r_nut) for r_nut in r_nuts]

i_total = i_body + sum(i_nuts)

# weighted mass
m_r = ((m_body*r_body) + (sum(r_nuts)*m_single_nut))

def theta(t: float) -> float:
    i_total_over_mr_g = i_total / (m_r * g)
    mr_g_over_i_total = (m_r * g) / i_total
    return i_total_over_mr_g * math.cos(math.sqrt(mr_g_over_i_total)*t)

def calc_period() -> float:
    i_total_over_mr_g = i_total / (m_r * g)
    return 2 * math.pi * math.sqrt(i_total_over_mr_g)

if __name__ == "__main__":
    f = theta  # math.sin

    t_min = -1
    t_max = 1

    t_step = 0.001

    x_pts, y_pts = [], []

    t = t_min

    while t < t_max:
        x_pts.append(t)
        y_pts.append(f(t)*100)
        t += t_step

    # print(y_pts)
    print()
    min_pt = min(y_pts)
    print(f"{min_pt=} (count: {y_pts.count(min_pt)})")

    start_idx = -1
    indexes = []
    if y_pts.count(min_pt) != 2: # attempt simpler method
        print("Approximating indexes")
        for i, pt in enumerate(y_pts):
            if abs(pt - min_pt) < 0.00000000001:
                indexes.append(i)
    else:
        print("Using accurate indexes")
        while True:
            try:
                indexes.append(y_pts.index(min_pt, start_idx + 1))
            except ValueError:
                break
            start_idx = indexes[-1]

    print(f"{indexes=}")

    times = [x_pts[i] for i in indexes]

    print(f"{times=}")

    if len(indexes) == 2:
        print("Analyzing period")
        period = times[1] - times[0]
        print(f"{period=} s")
    else:
        print("Count not 2, unable to analyze period. Maybe adjust timing parameters?")

    print("Formulaic period:", calc_period(), "s")

    plt.plot(x_pts, y_pts)
    plt.title("Inertial")
    plt.xlabel("Time (s)")
    plt.ylabel("Angle")
    #plt.savefig("inertial.png")
    plt.show()
