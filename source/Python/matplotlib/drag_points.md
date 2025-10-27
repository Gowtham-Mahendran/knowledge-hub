## import library and draw a figure 

```bash
import matplotlib.pyplot as plt

# Create figure and axes
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Initial point
x, y = [5], [5]
point, = ax.plot(x, y, "o", markersize=10, color="red")
```

Register a flag to know the status of dragging

```bash
dragging = False 
```


Define the events

```bash
def on_press(event):
    global dragging
    if event.inaxes != ax: 
        return
    if abs(event.xdata - x[0]) < 0.3 and abs(event.ydata - y[0]) < 0.3:
        dragging = True

def on_release(event):
    global dragging
    dragging = False

def on_motion(event):
    if not dragging or event.inaxes != ax:
        return
    x[0], y[0] = event.xdata, event.ydata
    point.set_data(x, y)
    fig.canvas.draw_idle()
```

Connect these events

```bash
fig.canvas.mpl_connect("button_press_event", on_press)
fig.canvas.mpl_connect("button_release_event", on_release)
fig.canvas.mpl_connect("motion_notify_event", on_motion)
```

Show figure

```bash
plt.title("Drag the red point")
plt.show()
```