import osmnx as ox
import matplotlib.pyplot as plt

class MapVisualizer:
    def __init__(self, graph):
        # Store graph for plotting
        self.graph = graph

    def save_map(self, hospital_nodes, filename="hospital_map.png"):
        # Export map visualization to image file
        print(f"--- Generating {filename} ---")
        
        # Plot road network with hidden intersection nodes
        fig, ax = ox.plot_graph(
            self.graph, 
            node_size=0,
            edge_color='#444444',
            edge_linewidth=0.8,
            edge_alpha=0.2,
            show=False, 
            close=False
        )

        # Plot hospital locations as red markers using coordinates
        for node in hospital_nodes:
            lat = self.graph.nodes[node]['y']
            lon = self.graph.nodes[node]['x']
            ax.scatter(lon, lat, c='red', s=150, edgecolors='white', zorder=5)

        # Configure title and visual theme
        plt.title("Optimal Hospital Placement Per Algorithm", fontsize=15, color='white')
        fig.set_facecolor('black')

        # Save result with high resolution and cropped boundaries
        plt.savefig(filename, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
        plt.close(fig)