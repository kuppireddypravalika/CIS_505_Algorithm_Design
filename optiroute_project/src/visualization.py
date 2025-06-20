
import folium

def visualize_routes(locations, routes, filename="routes_map.html"):
    m = folium.Map(location=locations[0], zoom_start=12)

    # Add markers for all locations
    for i, loc in enumerate(locations):
        folium.Marker(loc, popup=f"Location {i}").add_to(m)

    colors = ["red", "blue", "green", "purple", "orange", "darkred", "lightred", "beige", "darkblue", "darkgreen", "cadetblue", "darkpurple", "white", "pink", "lightblue", "lightgreen", "gray", "black", "lightgray"]

    for i, route in enumerate(routes):
        route_locations = [locations[node_idx] for node_idx in route]
        folium.PolyLine(route_locations, color=colors[i % len(colors)], weight=2.5, opacity=1).add_to(m)

    m.save(filename)
    print(f"Map saved to {filename}")


