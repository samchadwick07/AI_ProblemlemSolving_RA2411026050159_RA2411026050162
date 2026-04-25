# AI Problem Solving Assignment

## Student Details
- **Name:** Your Name
- **Register Number:** Your Register Number

## Project Overview
This project implements two Artificial Intelligence problem-solving techniques using Python and Streamlit for interactive visualization.

### Problems Implemented:
1. Map Coloring Problem (CSP)
2. Smart Navigation System (BFS & DFS)

---

## Problem 5: Map Coloring (CSP)

### Description
The Map Coloring problem involves assigning colors to regions on a map such that no two adjacent regions share the same color.

### Objective
- Assign colors to each region
- Ensure adjacent regions have different colors
- Use a limited number of colors (Red, Green, Blue)

### Algorithm Used
- Constraint Satisfaction Problem (CSP)
- Backtracking approach

### Input Format
```
A:B,C
B:A,C,D
C:A,B,D
D:B,C
```

### Output Example
```
A → Red
B → Green
C → Blue
D → Red
```

---

## Problem 8: Smart Navigation (BFS & DFS)

### Description
This problem finds a path between two nodes in a graph using search algorithms.

### Objective
- Find path from start node to goal node
- Compare BFS and DFS approaches

### Algorithms Used
- Breadth-First Search (BFS)
- Depth-First Search (DFS)

### Input Format
```
A:B,C
B:D
C:D
D:F
F:
```
Start Node: A | Goal Node: F

### Output Example
```
BFS Path: A → B → D → F
DFS Path: A → C → D → F
```

---

## Technologies Used
- Python
- Streamlit

## How to Run

```bash
pip install streamlit
streamlit run Problem5_MapColoring/map_coloring_app.py
streamlit run Problem8_Navigation/navigation_app.py
```

## Project Structure
```
AI_ProblemSolving_<RegisterNumber>/
├── Problem5_MapColoring/
│   └── map_coloring_app.py
├── Problem8_Navigation/
│   └── navigation_app.py
└── README.md
```

## GitHub Repository
(Add your link here)
