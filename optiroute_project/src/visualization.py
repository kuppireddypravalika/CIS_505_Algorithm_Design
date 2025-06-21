import folium
from folium import Map, Marker, PolyLine

def visualize_routes(locations, routes, filename="routes_map.html"):
    if not routes or not routes[0]:
        print("No route to visualize.")
        return

    m = Map(location=locations[0], zoom_start=13)
    colors = ['blue', 'green', 'red', 'purple', 'orange', 'darkred']

    for i, route in enumerate(routes):
        route_locations = [locations[idx] for idx in route]
        PolyLine(route_locations, color=colors[i % len(colors)], weight=2.5, opacity=1).add_to(m)
        for j, idx in enumerate(route):
            Marker(locations[idx], popup=f"{j+1}: Point {idx}").add_to(m)

    m.save(filename)
    print(f"Map saved to {filename}")
