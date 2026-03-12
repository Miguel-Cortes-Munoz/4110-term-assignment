import osmnx as ox
import networkx as nx
import random
from tqdm import tqdm

class NetworkManager:
    def __init__(self, city_name, network_type="drive"):
        # Store location and network constraints
        self.city_name = city_name
        self.network_type = network_type
        self.graph = None
        self.nodes = []

    def load_graph(self):
        # Download road network from OpenStreetMap
        print(f"--- Loading map for {self.city_name} ---")
        self.graph = ox.graph_from_place(self.city_name, network_type=self.network_type)
        self.nodes = list(self.graph.nodes)
        return self.graph

    def get_sample_distances(self, sample_size=30, seed=None):
        # Sample nodes and calculate travel distances between them
        if seed is not None:
            random.seed(seed)
            
        super_nodes = random.sample(self.nodes, sample_size)
        distance_matrix = {}
        big_m = 999999

        print(f"Calculating shortest paths for {sample_size} sample nodes...")
        
        # Calculate Dijkstra shortest paths for each sample node
        for start_node in tqdm(super_nodes, desc="Pathfinding Progress", unit="node"):
            lengths = nx.single_source_dijkstra_path_length(
                self.graph, 
                start_node, 
                weight='length'
            )
            
            for end_node in super_nodes:
                # Map distances; use penalty for unreachable paths
                dist = lengths.get(end_node, big_m)
                distance_matrix[(start_node, end_node)] = dist
        
        return super_nodes, distance_matrix