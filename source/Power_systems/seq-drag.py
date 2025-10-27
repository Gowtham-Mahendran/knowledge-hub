import cmath
import math
import matplotlib.pyplot as plt
import numpy as np

def phase_deg(z):
    return math.degrees(cmath.phase(z)) % 360

def compute_sequence(Ea,Eb,Ec):
    a = complex(-0.5,0.866)
    Eao = (Ea + Eb + Ec)/3
    Ea1 = (Ea + (a*Eb) + (a*a*Ec))/3
    Ea2 = (Ea + (a*a*Eb) + (a*Ec))/3

    Ebo = Eao
    Eco = Eao
    Eb1 = a*a*Ea1
    Eb2 = a*Ea2
    Ec1 = a*Ea1
    Ec2 = a*a*Ea2

    return {
        "Ea": Ea, "Eb" : Eb, "Ec": Ec,
        "Eao": Eao, "Ea1": Ea1, "Ea2": Ea2,
        "Ebo": Eao, "Eb1": Eb1, "Eb2": Eb2,
        "Eco": Eao, "Ec1": Ec1, "Ec2": Ec2         
    }

def draw_original_vectors(ax_cart,Ea,Eb,Ec):

    phasors = {"Ea": Ea, "Eb": Eb, "Ec": Ec}
    colors = {"Ea": "red", "Eb": "orange", "Ec": "blue"}

    q = ax_cart.quiver(
        [0, 0, 0], [0, 0, 0],
        [phasors[k].real for k in ["Ea","Eb","Ec"]],
        [phasors[k].imag for k in ["Ea","Eb","Ec"]],
        angles='xy', scale_units='xy', scale=1,
        color=[colors[k] for k in ["Ea","Eb","Ec"]]
    )

    tip_markers = {}
    for k in ["Ea","Eb","Ec"]:
        (pt,) = ax_cart.plot(
            phasors[k].real, phasors[k].imag,
            "o", alpha=0.6, ms=6, color=colors[k], picker=7
        )
        tip_markers[k] = pt

    return q, tip_markers

def cartesian_plane(Ea,Eb,Ec):
    fig = plt.figure(figsize=(6, 6))
    ax_cart = fig.subplots()

    limit = max(abs(Ea.real),abs(Eb.real),abs(Ec.real),abs(Ea.imag),abs(Eb.imag),abs(Ec.imag)) * 1.25

    ticks_frequency = int(math.ceil(limit / 5 / 10) * 10)

    ax_cart.set(xlim=(-(limit), limit), ylim=(-(limit), limit), aspect='equal')

    ax_cart.spines['bottom'].set_position('zero')
    ax_cart.spines['left'].set_position('zero')
    ax_cart.spines['top'].set_visible(False)
    ax_cart.spines['right'].set_visible(False)

    ax_cart.set_xlabel('$x$', size=14, labelpad=-24, x=1.02)
    ax_cart.set_ylabel('$y$', size=14, labelpad=-21, y=1.02, rotation=0)
    
    plt.text(0.49, 0.49, r"$O$", ha='right', va='top', transform=ax_cart.transAxes, fontsize=14)

    x_ticks = np.arange(-(limit), limit, ticks_frequency)
    y_ticks = np.arange(-(limit), limit, ticks_frequency)
    ax_cart.set_xticks(x_ticks[x_ticks != 0])
    ax_cart.set_yticks(y_ticks[y_ticks != 0])

    ax_cart.grid(which='major', color='grey', linewidth=1, linestyle='-', alpha=0.2)

    return fig, ax_cart

def draw_sequence_components(ax_cart,seq):
    Ea_seq = [seq["Ea1"], seq["Ea2"], seq["Eao"]]
    Eb_seq = [seq["Eb1"], seq["Eb2"], seq["Ebo"]]
    Ec_seq = [seq["Ec1"], seq["Ec2"], seq["Eco"]]

    seq_comp = [Ea_seq, Eb_seq, Ec_seq]
    seq_quivers = []

    for comp in seq_comp:
        origin = 0+0j
        for x in comp:
            q = ax_cart.quiver(origin.real, origin.imag, x.real, x.imag, angles='xy', scale_units='xy', scale=1, width=0.003)
            seq_quivers.append(q)
            origin += x
    return seq_quivers

def on_pick(event):
    for k, artist in tip_markers.items():
        if event.artist is artist:
            dragging_key["key"] = k
            break

def on_drag(event):
    k = dragging_key["key"]
    if k is None or event.inaxes is not ax_cart:
        return
    if event.xdata is None or event.ydata is None:
        return
    phasors[k] = complex(event.xdata, event.ydata)
    tip_markers[k].set_data([phasors[k].real], [phasors[k].imag])

    U = [phasors["Ea"].real, phasors["Eb"].real, phasors["Ec"].real]
    V = [phasors["Ea"].imag, phasors["Eb"].imag, phasors["Ec"].imag]
    q_main.set_UVC(U, V)

    seq = compute_sequence(phasors["Ea"], phasors["Eb"], phasors["Ec"])

    for q in seq_quivers:
        q.remove()
    seq_quivers.clear()

    seq_quivers.extend(draw_sequence_components(ax_cart, seq))
    
    fig.canvas.draw_idle()

def on_release(event):
    dragging_key["key"] = None


Ea = complex(60,0)
Eb = complex(45,-75)
Ec = complex(-21,120)

fig, ax_cart = cartesian_plane(Ea,Eb,Ec)
q_main, tip_markers = draw_original_vectors(ax_cart,Ea,Eb,Ec)
seq = compute_sequence(Ea,Eb,Ec)
seq_quivers = draw_sequence_components(ax_cart,seq)

phasors = {"Ea": Ea, "Eb": Eb, "Ec": Ec} 
dragging_key = {"key": None} 

pick = fig.canvas.mpl_connect("pick_event", on_pick)
drag = fig.canvas.mpl_connect("motion_notify_event", on_drag)
release = fig.canvas.mpl_connect("button_release_event", on_release)

plt.show()