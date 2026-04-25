import streamlit as st
from collections import deque

st.title("🧭 Smart Navigation (BFS & DFS)")

def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append(path + [neighbor])

    return None

def dfs(graph, start, goal, path=[]):
    path = path + [start]

    if start == goal:
        return path

    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = dfs(graph, neighbor, goal, path)
            if new_path:
                return new_path

    return None

st.write("Enter graph (example: A:B,C)")

input_data = st.text_area("Graph Input", "A:B,C\nB:D\nC:D\nD:F\nF:")

start = st.text_input("Start Node", "A")
goal = st.text_input("Goal Node", "F")

if st.button("Find Path"):
    lines = input_data.split("\n")
    graph = {}

    for line in lines:
        if ":" in line:
            node, neigh = line.split(":")
            if neigh.strip() == "":
                graph[node.strip()] = []
            else:
                graph[node.strip()] = [n.strip() for n in neigh.split(",")]

    bfs_path = bfs(graph, start, goal)
    dfs_path = dfs(graph, start, goal)

    if bfs_path:
        st.success("BFS Path: " + " → ".join(bfs_path))
    else:
        st.error("No BFS path found")

    if dfs_path:
        st.info("DFS Path: " + " → ".join(dfs_path))
    else:
        st.error("No DFS path found")