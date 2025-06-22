import folium
from folium import Map, Marker, PolyLine
import osmnx as ox
import networkx as nx

def visualize_routes_real_roads(locations, routes, filename="real_road_routes.html"):
    if not routes or not routes[0]:
        print("No route to visualize.")
        return

    print("Fetching OSM road network...")
    center_lat = sum(lat for lat, _ in locations) / len(locations)
    center_lon = sum(lon for _, lon in locations) / len(locations)
    G = ox.graph_from_point((center_lat, center_lon), dist=7000, network_type='drive')

    print("Mapping points to OSM road nodes...")
    node_ids = [ox.distance.nearest_nodes(G, lon, lat) for lat, lon in locations]

    m = Map(location=locations[0], zoom_start=13)
    route_color = 'red'

    for i, route in enumerate(routes):
        full_path_coords = []
        for j in range(len(route) - 1):
            u = node_ids[route[j]]
            v = node_ids[route[j + 1]]
            try:
                path = nx.shortest_path(G, u, v, weight='length')
                coords = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in path]
                full_path_coords.extend(coords)
            except:
                print(f" Could not find path from {route[j]} to {route[j+1]}")

        
        PolyLine(full_path_coords, color=route_color, weight=3.5, opacity=1).add_to(m)

        
        for j, idx in enumerate(route):
            label = "Start" if j == 0 else str(j)
            Marker(
                locations[idx],
                popup=f"{label}: Point {idx}",
                tooltip=label,
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(m)

    m.save(filename)
    print(f" Road-following map saved to {filename}")
