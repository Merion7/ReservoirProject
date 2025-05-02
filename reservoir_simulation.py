def simulate_flow(permeability, viscosity, pressure):  
    flow_rate = (permeability * pressure) / (viscosity * 1.127)  
    return flow_rate  

print("Simulated Flow Rate:", simulate_flow(500, 2.5, 0.1), "bbl/day")  