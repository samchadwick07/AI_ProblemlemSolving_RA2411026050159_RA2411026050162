import streamlit as st

st.title("🗺️ Map Coloring (CSP)")

def is_valid(region, color, assignment, neighbors):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def map_coloring(regions, neighbors, colors, assignment={}):
    if len(assignment) == len(regions):
        return assignment

    unassigned = [r for r in regions if r not in assignment]
    region = unassigned[0]

    for color in colors:
        if is_valid(region, color, assignment, neighbors):
            assignment[region] = color
            result = map_coloring(regions, neighbors, colors, assignment)
            if result:
                return result
            del assignment[region]

    return None

st.write("Enter regions and neighbors (example: A:B,C)")

input_data = st.text_area("Input", "A:B,C\nB:A,C,D\nC:A,B,D\nD:B,C")

colors = ["Red", "Green", "Blue"]

if st.button("Solve"):
    lines = input_data.split("\n")
    neighbors = {}
    regions = []

    for line in lines:
        if ":" in line:
            region, neigh = line.split(":")
            regions.append(region.strip())
            neighbors[region.strip()] = [n.strip() for n in neigh.split(",")]

    solution = map_coloring(regions, neighbors, colors)

    if solution:
        st.success("Solution Found!")
        for r in solution:
            st.write(f"{r} → {solution[r]}")
    else:
        st.error("No solution found")