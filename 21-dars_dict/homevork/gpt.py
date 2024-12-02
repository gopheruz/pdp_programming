import math

# Example 2D matrix
matrix = [[0 for _ in range(10)] for _ in range(10)]

matrix[5][5] = 4

def compute_euclidean_distance(point1, point2):
    """Compute the Euclidean distance between two points."""
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))

def find_nearest_neighbors(matrix):
    """Find the nearest neighbor for each point in the matrix."""
    neighbors = []
    for i in range(len(matrix)):  # Loop through each point
        point1 = matrix[i]
        min_distance = float('inf')
        nearest_neighbor = -1
        for j in range(len(matrix)):  # Compare to all other points
            if i != j:  # Skip self
                point2 = matrix[j]
                distance = compute_euclidean_distance(point1, point2)
                if distance < min_distance:
                    min_distance = distance
                    nearest_neighbor = j
        neighbors.append((i, nearest_neighbor, min_distance))
    return neighbors

nearest_neighbors = find_nearest_neighbors(matrix)

print(nearest_neighbors)