from src.network_manager import NetworkManager
from src.model_logic import PCenterSolver
from src.visualizer import MapVisualizer

def main():
    # Initialize network manager and load map data
    manager = NetworkManager("Coaldale, Alberta, Canada")
    graph = manager.load_graph()
    
    # Select random sample points and calculate distance matrix
    sample_nodes, distances = manager.get_sample_distances(sample_size=30, seed=42)

    # Solve p-center problem to locate facilities
    # p_count = # of Hospitals
    solver = PCenterSolver(sample_nodes, distances, p_count=2)
    hospitals, max_dist = solver.solve()

    # Print optimization status and facility locations
    print(f"\nStatus: Optimal")
    print(f"Maximized Equity Distance: {max_dist:.3f} meters")
    for i, h in enumerate(hospitals, 1):
        print(f"Hospital {i} Location (Node ID): {h}")

    # Generate and save spatial visualization
    viz = MapVisualizer(graph)
    viz.save_map(hospitals, filename="hospital_map.png")

if __name__ == "__main__":
    main()