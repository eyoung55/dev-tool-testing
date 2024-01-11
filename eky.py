import numpy as np

a = np.linspace(0, 1)
b = 5
c = "some string"

print(c)

d = 5 + 5

more_wrong_lines = (
    5 + np.cos(100.0) + np.sin(100.0) + np.sqrt(np.array([100.0, 200.0, 300.00]))
)

aa = "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh" + str(
    8743764734834834733437438478
)


another_bad_thing = 5 + np.array([100, 100, 100, 100, 100, 100, 100, 100, 100])
