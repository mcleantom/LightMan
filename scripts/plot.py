from light_man import Room, find_optimal_positions_of_lights
import shapely


def main():
    room = Room(
        dimensions=shapely.geometry.box(0, 0, 20, 15),
        beams=[
            shapely.geometry.box(4.5, 0, 6, 5),
            shapely.geometry.box(3, 0, 4, 4),
            shapely.geometry.box(0, 2, 10, 3),
            shapely.geometry.box(0, 12, 20, 14),
            shapely.geometry.box(8, 6, 12, 8)
        ],
    )
    lights = find_optimal_positions_of_lights(room, 3, 4); 
    ##plot_room(room, lights = [])


if __name__ == "__main__":
    main()
