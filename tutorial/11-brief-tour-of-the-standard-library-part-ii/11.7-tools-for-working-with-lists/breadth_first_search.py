from collections import deque

graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
starting_node = "A"
is_goal = lambda n: n == "D"
unsearched = deque([starting_node])

def gen_moves(node):
    yield from graph[node]

def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)

print('before', unsearched)
breadth_first_search(unsearched=unsearched)
print('after', unsearched)