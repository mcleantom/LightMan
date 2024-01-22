import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
from shapely import box, LineString, MultiLineString
import geopandas as gpd
import numpy as np


room = box(0, 0, 1, 1)
light_column = LineString([[0.5, 0], [0.5, 1]])
light_row = LineString([[0, 0.75], [1, 0.75]])
light_row_2 = LineString([[0, 0.25], [1, 0.25]])
light_rows = MultiLineString([light_row, light_row_2])

intersection_points = light_rows.intersection(light_column)

x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
x, y = np.meshgrid(x, y)
illuminance_factor = 1
min_distance = 0.1
illuminance_field = np.zeros_like(x)
for p in intersection_points.geoms:
    x_distance = p.x - x
    y_distance = p.y - y
    distance = np.sqrt(x_distance ** 2 + y_distance**2)
    distance = np.maximum(distance, min_distance)
    illuminance = illuminance_factor / (distance ** 2)
    illuminance_field += illuminance

print(illuminance_field.min())
print(illuminance_field.max())

fig, ax = plt.subplots()
contour = ax.contourf(x, y, np.log10(illuminance_field), cmap="viridis")
gpd.GeoSeries([room]).boundary.plot(ax=ax)
gpd.GeoSeries([light_column, light_rows]).plot(ax=ax)
gpd.GeoSeries([intersection_points]).plot(ax=ax)
plt.show()