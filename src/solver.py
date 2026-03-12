import pulp

class PCenterSolver:
    def __init__(self, nodes, distances, p_count):
        # Initialize solver parameters and variables
        self.nodes = nodes
        self.distances = distances
        self.p_count = p_count
        self.prob = None
        self.y = None
        self.z = None

    def solve(self):
        # Define minimization problem and decision variables
        self.prob = pulp.LpProblem("Hospital_Placement", pulp.LpMinimize)
        self.y = pulp.LpVariable.dicts("Hospital", self.nodes, cat=pulp.LpBinary)
        x = pulp.LpVariable.dicts("Service", (self.nodes, self.nodes), cat=pulp.LpBinary)
        self.z = pulp.LpVariable("MaxDistance", lowBound=0, cat=pulp.LpContinuous)

        # Objective: minimize the maximum distance variable
        self.prob += self.z
        
        # Constraint: total facilities must equal p_count
        self.prob += pulp.lpSum([self.y[j] for j in self.nodes]) == self.p_count

        for i in self.nodes:
            # Constraint: each node assigned to exactly one facility
            self.prob += pulp.lpSum([x[i][j] for j in self.nodes]) == 1
            for j in self.nodes:
                # Constraint: assignment only allowed to existing facilities
                self.prob += x[i][j] <= self.y[j]
            # Constraint: set z as upper bound for all assignment distances
            self.prob += pulp.lpSum([self.distances[i, j] * x[i][j] for j in self.nodes]) <= self.z

        # Execute solver quietly
        self.prob.solve(pulp.PULP_CBC_CMD(msg=0))
        
        # Extract selected node IDs and optimal distance
        hospital_nodes = [n for n in self.nodes if pulp.value(self.y[n]) == 1]
        return hospital_nodes, pulp.value(self.z)