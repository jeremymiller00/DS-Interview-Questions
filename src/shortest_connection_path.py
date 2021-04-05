"""
You have the entire social graph of Facebook users, with nodes representing users and edges representing
friendships between users. Given the edges of the graph and the number of nodes, write a function to return the
smallest number of friendships in-between two users.

For example, if the graph consists of 5 users A, B, C, D, E, and the friendship edges are:
(A, B), (A, C), (B, D), (D, E) then the function should return 2 for the input A and E.
"""

connections = {
    'a': {'b', 'c'},
    'b': {'a', 'd'},
    'c': {'a'},
    'd': {'b', 'e'},
    'e': {'d'}
}


def shortest_connection_path(node_a, node_b, network):
    steps = 0
    reach = connections.get(node_a)
    while node_b not in reach:
        for n in reach.copy():
            reach.update(network.get(n))
        steps += 1
    return steps


# print(shortest_connection_path('a', 'e', connections))
result = shortest_connection_path('a', 'e', connections)
print(f"Result: {result}")
assert result == 2
