import matplotlib.pyplot as plt


def test_colors():
    x = range(10)
    y = [1]*10
    fig, ax = plt.subplots(1)
    for i in x:
        ax.scatter(x[i],y[i], s=100)


test_colors()

plt.style.use("YII_1")

test_colors()

plt.show()
