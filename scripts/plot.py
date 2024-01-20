from light_man import Beam, Point, Rectangle, Room, plot_room


def main():
    room = Room(
        dimensions=Rectangle(p1=Point(x=0, y=0), p2=Point(x=10, y=5)),
        beams=[
            Beam(dimensions=Rectangle(p1=Point(x=5, y=0), p2=Point(x=6, y=5))),
            Beam(dimensions=Rectangle(p1=Point(x=0, y=2), p2=Point(x=10, y=3))),
        ],
    )
    plot_room(room, lights=[])


if __name__ == "__main__":
    main()
