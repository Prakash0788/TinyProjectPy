import folium
import numpy as np

# Create the map
m = folium.Map(location=[0, 0], zoom_start=2)

# Add random circle markers
for _ in range(30):
    folium.CircleMarker(
        location=[
            np.random.uniform(-60, 60),
            np.random.uniform(-180, 180)
        ],
        radius=4,
        color="blue",
        fill=True,
        fill_opacity=0.7
    ).add_to(m)

# Save map to HTML
m.save("map.html")
