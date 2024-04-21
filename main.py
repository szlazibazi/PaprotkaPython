import matplotlib.pyplot as plt
import numpy as np

functions = [
    (lambda x, y: (0.0, 0.16 * y), 0.01),
    (lambda x, y: (0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6), 0.85),
    (lambda x, y: (0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6), 0.07),
    (lambda x, y: (-0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44), 0.07)
]

x, y = 0.0, 0.0

max_iterations = 10000
points = []

for _ in range(max_iterations):
    rand = np.random.rand()
    cumulative_prob = 0.0
    chosen_func = None
    for func, prob in functions:
        cumulative_prob += prob
        if rand < cumulative_prob:
            chosen_func = func
            break

    x, y = chosen_func(x, y)

    points.append((x, y))

plt.figure(figsize=(8, 8))
plt.scatter([p[0] for p in points], [p[1] for p in points], s=1, color='green')
plt.title('Fraktal Paproć Barnsleya')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
import matplotlib.pyplot as plt
import numpy as np

functions = [
    (lambda x, y: (0.0, 0.16 * y), 0.01),
    (lambda x, y: (0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6), 0.85),
    (lambda x, y: (0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6), 0.07),
    (lambda x, y: (-0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44), 0.07)
]

x, y = 0.0, 0.0

max_iterations = 10000
points = []

for _ in range(max_iterations):
    rand = np.random.rand()
    cumulative_prob = 0.0
    chosen_func = None
    for func, prob in functions:
        cumulative_prob += prob
        if rand < cumulative_prob:
            chosen_func = func
            break

    x, y = chosen_func(x, y)

    points.append((x, y))

plt.figure(figsize=(8, 8))
plt.scatter([p[0] for p in points], [p[1] for p in points], s=1, color='green')
plt.title('Fraktal Paproć Barnsleya')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()