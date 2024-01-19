import matplotlib.pyplot as plt

from light_man import EOrientation, Room

__all__ = ["plot_room"]


def plot_room(room: Room):
    fig, ax = plt.subplots()

    ax.plot([0, room.width, room.width, 0, 0], [0, 0, room.height, room.height, 0], color="black")

    for beam in room.beams:
        if beam.orientation == EOrientation.HORIZONTAL:
            rect = plt.Rectangle(
                (beam.position.x, beam.position.y),
                beam.width,
                room.height,
                linewidth=1,
                edgecolor="r",
                facecolor="none",
                linestyle="dashed",
                label=f"Beam {beam.orientation.name} at ({beam.position.x}, {beam.position.y})",
            )
        else:
            rect = plt.Rectangle(
                (beam.position.x, beam.position.y - beam.width),
                room.width,
                beam.width,
                linewidth=1,
                edgecolor="r",
                facecolor="none",
                linestyle="dashed",
                label=f"Beam {beam.orientation.name} at ({beam.position.x}, {beam.position.y})",
            )

        ax.add_patch(rect)

    ax.set_xlim(0, room.width)
    ax.set_ylim(0, room.height)
    ax.set_aspect("equal", "box")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    plt.show()
