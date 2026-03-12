import pulp
# Point to the data and logic
from src.model_logic import solve_p_center
from src.town_data import super_nodes, distance_matrix, hospitals_to_place

if __name__ == "__main__":
    # Run the solver
    result, facilities, max_dist = solve_p_center(super_nodes, distance_matrix, hospitals_to_place)

    # Reults of Solver
    print(f"Solver Status: {pulp.LpStatus[result.status]}")
    print(f"Maximized Equity Distance: {pulp.value(max_dist)}")
    
    for node in super_nodes:
        if pulp.value(facilities[node]) == 1:
            print(f"Optimal Hospital Location: {node}")