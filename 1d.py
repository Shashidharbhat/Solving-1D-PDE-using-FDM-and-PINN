import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

alpha=510
length=50
time=0.1
h=1
k=.0005
nodes=int(length/h)
print(nodes)
i=0.0
u = np.zeros(nodes+1)
for index in range(nodes):
     u[index]=u[index]+ 20
     index+=1
     i+=h
 

u[0] =100
u[-1] =100

# Visualizing with a plot

fig, axis = plt.subplots()

pcm = axis.pcolormesh([u], cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(pcm, ax=axis)
axis.set_ylim([-2, 3])
plt.xlabel("Length")
plt.ylabel("Time")
# Simulating

counter = 0

while counter < time :

    w = u.copy()

    for i in range(1, nodes ):

        u[i] =k * alpha * (w[i - 1] - 2 * w[i] + w[i + 1]) / (h ** 2) + w[i]

    counter +=k
    print("t: {:.3f} [s], Average temperature: {:.2f} Celcius".format(counter, np.average(u)))

    # Updating the plot
i=0.0
u = np.zeros(nodes+1)
for index in range(nodes):
     u[index]=u[index]+ 20
     index+=1
     i+=h
 

u[0] =100
u[-1] =100
def update_plot(frame):
    global u
    if frame * k >= time:  # Check if current time exceeds 0.1 seconds
        animation.event_source.stop()  # Stop the animation
    w = u.copy()
    for i in range(1, nodes):
        u[i] = k * alpha * (w[i - 1] - 2 * w[i] + w[i + 1]) / (h ** 2) + w[i]
    pcm.set_array([u])
    axis.set_title(f"Distribution at t: {frame * k:.3f} [s]")

animation = FuncAnimation(fig, update_plot, frames=int(time / k), interval=100, repeat=False)

# Save animation as GIF
animation.save('temperature_distribution1.gif', writer='imagemagick')

plt.show()