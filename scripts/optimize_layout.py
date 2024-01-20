from light_man import Beam, Point, Rectangle, Room, find_optimal_positions_of_lights


def main():
    room_example = Room(
        dimensions=Rectangle(p1=Point(x=0, y=0), p2=Point(x=10, y=5)),
        beams=[
            Beam(dimensions=Rectangle(p1=Point(x=5, y=0), p2=Point(x=6, y=5))),
            Beam(dimensions=Rectangle(p1=Point(x=0, y=2), p2=Point(x=10, y=3))),
        ],
    )
    n_lights = 4
    optimal_positions = find_optimal_positions_of_lights(room_example, n_lights=n_lights)
    print(optimal_positions)


if __name__ == "__main__":
    main()
