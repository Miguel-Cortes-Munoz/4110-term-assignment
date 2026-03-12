import pulp

def solve_p_center(nodes, distances, p_count):
    # Set up the optimization model
    prob = pulp.LpProblem("Hospital_Placement", pulp.LpMinimize)
    
    # Define where hospitals are built
    y = pulp.LpVariable.dicts("Hospital", nodes, cat=pulp.LpBinary)
    
    # Define which neighborhoods they serve
    x = pulp.LpVariable.dicts("Service", (nodes, nodes), cat=pulp.LpBinary)
    
    # Track the longest travel distance
    z = pulp.LpVariable("MaxDistance", lowBound=0, cat=pulp.LpContinuous)
    
    # Goal: minimize that longest distance
    prob += z
    
    # Build exactly p hospitals
    prob += pulp.lpSum([y[j] for j in nodes]) == p_count
    
    for i in nodes:
        # Every area needs a hospital assigned
        prob += pulp.lpSum([x[i][j] for j in nodes]) == 1
        
        for j in nodes:
            # Can't assign an area to a hospital that doesn't exist
            prob += x[i][j] <= y[j]
            
        # Ensure z captures the actual travel time
        prob += pulp.lpSum([distances[i, j] * x[i][j] for j in nodes]) <= z
        
    prob.solve(pulp.PULP_CBC_CMD(msg=0))
    return prob, y, z