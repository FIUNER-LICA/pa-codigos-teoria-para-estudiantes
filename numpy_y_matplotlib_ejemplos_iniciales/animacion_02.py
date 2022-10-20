import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure(figsize=(7,2), dpi=100)
ax = plt.subplot()

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

line1, = ax.plot(X, C, marker="o", markevery=[-1],
markeredgecolor="white")
line2, = ax.plot(X, S, marker="o", markevery=[-1],
markeredgecolor="white")

def update(frame, *fargs):
    line1.set_data(X[:frame], C[:frame])
    line2.set_data(X[:frame], S[:frame])
    print('fargs:', fargs, '  -  frame:', frame)
    
    if frame in range(0, 50, 10):
       plt.savefig(f"animation-frame_{frame}.png", dpi=300)

ani = animation.FuncAnimation(fig, update, interval=10, fargs=(1,2,3), frames=100)

plt.show()