
# Main function
def magic(arr):
    sizes = []
    visited = [[False for x in row] for row in arr]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if visited[i][j]:
                continue
            explore_node(i, j, arr, visited, sizes)
    return sorted(sizes)


# traverse all valid nodes and their neighbors, keep track of visited nodes and the currently explored river size
def explore_node(i, j, matrix, visited, sizes):
    current_size = 0
    nodes_to_explore = [[i, j]]
    while len(nodes_to_explore):
        i, j = nodes_to_explore.pop()
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        current_size += 1
        unvisited_neighbors = get_unvisited(i, j, matrix, visited)
        for neighbor in unvisited_neighbors:
            nodes_to_explore.append(neighbor)
    if current_size > 0:
        sizes.append(current_size)


# Helper function for retrieving a specific node unvisited neighbors
def get_unvisited(i, j, matrix, visited):

    unvisited_nodes = []
    if i > 0 and not visited[i - 1][j]:
        unvisited_nodes.append([i - 1, j])
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisited_nodes.append([i + 1, j])
    if j > 0 and not visited[i][j-1]:
        unvisited_nodes.append([i, j - 1])
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisited_nodes.append([i, j + 1])

    return unvisited_nodes


# drivers code
arr1 = [[1, 0, 0, 1],
        [0, 0, 1, 0],
        [1, 0, 1, 0],
        [1, 0, 1, 0]]

arr2 = [[0, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1, 0, 1],
        [1, 1, 1, 0, 0, 0, 0, 0]]

arr3 = [[0, 0, 0, 0, 1],
        [0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0]]

print(magic(arr1))
print(magic(arr2))
print(magic(arr3))
