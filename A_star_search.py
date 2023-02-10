import heapq


class AStarSearch:
    def __init__(self, start, goal, graph):
        self.start = start
        self.goal = goal
        self.graph = graph
        self.visited = set()
        self.priority_queue = []
        self.came_from = {}
        self.cost_so_far = {}
        self.heuristic = {}

    def heuristic_estimate(self, current, goal):
        # Here you can implement any heuristic function you want.
        # For example, you can use the Euclidean distance.
        return ((current[0] - goal[0]) ** 2 + (current[1] - goal[1]) ** 2) ** 0.5

    def a_star_search(self):
        heapq.heappush(self.priority_queue, (0, self.start))
        self.came_from[self.start] = None
        self.cost_so_far[self.start] = 0
        self.heuristic[self.start] = self.heuristic_estimate(
            self.start, self.goal)

        while self.priority_queue:
            current_cost, current_node = heapq.heappop(self.priority_queue)
            if current_node == self.goal:
                break
            if current_node in self.visited:
                continue
            self.visited.add(current_node)
            for neighbor in self.graph.neighbors(current_node):
                new_cost = self.cost_so_far[current_node] + \
                    self.graph.cost(current_node, neighbor)
                if neighbor not in self.cost_so_far or new_cost < self.cost_so_far[neighbor]:
                    self.cost_so_far[neighbor] = new_cost
                    priority = new_cost + \
                        self.heuristic_estimate(neighbor, self.goal)
                    heapq.heappush(self.priority_queue, (priority, neighbor))
                    self.came_from[neighbor] = current_node
                    self.heuristic[neighbor] = priority

        return self.came_from, self.cost_so_far

    def get_path(self):
        came_from, cost_so_far = self.a_star_search()
        current = self.goal
        path = [current]
        while current != self.start:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path
