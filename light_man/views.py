from typing import List

import matplotlib.pyplot as plt

from light_man import Point, Room

__all__ = ["plot_room"]


def plot_room(room: Room, lights: List[Point]):
    fig, ax = plt.subplots()
    width = room.geometry.width
    height = room.geometry.height
    ax.plot([0, width, width, 0, 0], [0, 0, height, height, 0], color="black")

    for beam in room.beams:
        rect = plt.Rectangle(
            (beam.geometry.p1.x, beam.geometry.p1.y),
            beam.geometry.p2.x - beam.geometry.p1.x,
            beam.geometry.p2.y - beam.geometry.p1.y,
            linewidth=1,
            edgecolor="r",
            facecolor="none",
            linestyle="dashed",
            label=f"Beam {beam.geometry.p1.x, beam.geometry.p1.y} to {beam.geometry.p2.x, beam.geometry.p2.y}",
        )
        ax.add_patch(rect)

    light_xs = [light.x for light in lights]
    light_ys = [light.y for light in lights]
    ax.scatter(light_xs, light_ys, color="blue", label="Lights")

    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect("equal", "box")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    plt.show()
