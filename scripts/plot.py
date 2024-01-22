from light_man import Beam, Point, Rectangle, Room, plot_room, find_optimal_positions_of_lights


def main():
    room = Room(
        dimensions=Rectangle(p1=Point(x=0, y=0), p2=Point(x=20, y=15)),
        beams=[
            Beam(dimensions=Rectangle(p1=Point(x=4.5, y=0), p2=Point(x=6, y=5))),
            Beam(dimensions=Rectangle(p1=Point(x=3, y=0), p2=Point(x=4, y=4))),
            Beam(dimensions=Rectangle(p1=Point(x=0, y=2), p2=Point(x=10, y=3))),
            
            Beam(dimensions=Rectangle(p1=Point(x=0, y=12), p2=Point(x=20, y=14))),
            
            Beam(dimensions=Rectangle(p1=Point(x=8, y=6), p2=Point(x=12, y=8))),
        ],
    )
    lights = find_optimal_positions_of_lights(room, 3, 4); 
    ##plot_room(room, lights = [])


if __name__ == "__main__":
    main()
