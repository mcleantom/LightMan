from light_man import Beam, EOrientation, Point, Room, plot_room


def main():
    room = Room(
        width=10,
        height=5,
        beams=[
            Beam(position=Point(x=5, y=0), orientation=EOrientation.HORIZONTAL, width=1),
            Beam(position=Point(x=0, y=2), orientation=EOrientation.VERTICAL, width=1),
        ],
    )
    plot_room(room)


if __name__ == "__main__":
    main()
