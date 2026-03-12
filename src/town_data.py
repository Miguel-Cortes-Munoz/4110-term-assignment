# Placeholder data to be replaced with OpenStreetMap
super_nodes = ["North_Block", "East_End", "Downtown", "West_Side", "South_Gate"]
hospitals_to_place = 2

distance_matrix = {
    ("North_Block", "North_Block"): 0, ("North_Block", "East_End"): 15, ("North_Block", "Downtown"): 10, ("North_Block", "West_Side"): 20, ("North_Block", "South_Gate"): 30,
    ("East_End", "North_Block"): 15, ("East_End", "East_End"): 0, ("East_End", "Downtown"): 12, ("East_End", "West_Side"): 25, ("East_End", "South_Gate"): 18,
    ("Downtown", "North_Block"): 10, ("Downtown", "East_End"): 12, ("Downtown", "Downtown"): 0, ("Downtown", "West_Side"): 10, ("Downtown", "South_Gate"): 15,
    ("West_Side", "North_Block"): 20, ("West_Side", "East_End"): 25, ("West_Side", "Downtown"): 10, ("West_Side", "West_Side"): 0, ("West_Side", "South_Gate"): 22,
    ("South_Gate", "North_Block"): 30, ("South_Gate", "East_End"): 18, ("South_Gate", "Downtown"): 15, ("South_Gate", "West_Side"): 22, ("South_Gate", "South_Gate"): 0,
}