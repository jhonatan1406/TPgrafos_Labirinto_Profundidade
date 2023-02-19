class Graph:
    def __init__(self, node_count: int=0, edge_count: int = 0, adj_list: list[list[int]] = []) -> None:
        self.node_count = node_count
        self.edge_count = edge_count
        self.adj_list = adj_list
        if adj_list == []:
            for _ in range(self.node_count):
                self.adj_list.append([])

    def add_directed_edge(self, u: int, v: int):
        if u < 0 or u >= len(self.adj_list) or v < 0 or v >= len(self.adj_list):
            print(f"Node u={u} or v={v} is out of allowed range (0, {self.node_count - 1})")
        self.adj_list[u].append(v)
        self.edge_count += 1

    def add_undirected_edge(self, u: int, v: int):
        self.add_directed_edge(u, v)
        self.add_directed_edge(v, u)

    def degree_out(self, u: int) -> int:
        return len(self.adj_list[u])

    def degree_in(self, u: int) -> int:
        degree = 0
        for i in range(len(self.adj_list)):
            if u in self.adj_list[i]:
                degree += 1
        return degree

    def highest_degree_out(self) -> int:
        max_degree_out = 0
        highest_degree_node = 0
        for u in range(self.node_count):
            degree_out_node_u = self.degree_out(u)
            if max_degree_out < degree_out_node_u:
                max_degree_out = degree_out_node_u
                highest_degree_node = u
        return highest_degree_node

    def highest_degree_in(self) -> int:
        max_degree_in = 0
        highest_degree_node = 0
        for u in range(self.node_count):
            degree_in_node_u = self.degree_in(u)
            if max_degree_in < degree_in_node_u:
                max_degree_in = degree_in_node_u
                highest_degree_node = u
        return highest_degree_node

    def density(self):
        return self.edge_count / (self.node_count * (self.node_count - 1))

    def complete(self):
        return self.density() == 1

    def regular(self):
        degree = len(self.adj_list[0])
        for u in range(1, len(self.adj_list)):
            if len(self.adj_list[u]) != degree:
                return False
        return True

    def complement(self):
        g2 = Graph(self.node_count, adj_list=[])
        for u in range(len(self.adj_list)):
            for v in range(self.node_count):
                if v not in self.adj_list[u] and v != u:
                    g2.add_undirected_edge(u, v)
        return g2

    def subgraph(self, g2):
        if g2.node_count > self.node_count or g2.edge_count > self.edge_count:
            return False
        for u in range(len(g2.adj_list)):
            for v in g2.adj_list[u]:
                if v not in self.adj_list[u]:
                    return False
        return True

    def bfs(self, s):
        desc = []
        for _ in range(self.node_count):
            desc.append(0)
        Q = [s]
        R = [s]
        desc[s] = 1
        while len(Q) != 0:
            u = Q.pop(0)
            for v in self.adj_list[u]:
                if desc[v] == 0:
                    Q.append(v)
                    R.append(v)
                    desc[v] = 1
        return R

    def connected(self):
        return len(self.bfs(0)) == self.node_count

    def unvisited_neighbor(self, u, desc):
        # Verifica se ha vizinho de u nao visitado
        for v in self.adj_list[u]:
            if desc[v] == 0:
                return v
        return -1

    def dfs(self, s):
        desc = []
        for _ in range(self.node_count):
            desc.append(0)
        S = [s]
        R = [s]
        desc[s] = 1
        while len(S) != 0:
            u = S[-1]
            v = self.unvisited_neighbor(u, desc)
            if v != -1:
                S.append(v)
                R.append(v)
                desc[v] = 1
            else:
                S.pop()
        return R

    def dfs_rec_aux(self, u, desc, R):
        desc[u] = 1
        R.append(u)
        for v in self.adj_list[u]:
            if desc[v] == 0:
                self.dfs_rec_aux(v, desc, R)

    def dfs_rec(self, s):
        desc = [0 for _ in range(self.node_count)]
        R = []
        self.dfs_rec_aux(s, desc, R)
        return R

    def dfs_end(self, s:int, e:int)-> list:
        desc = []
        Q = [s]
        for _ in range(len(self.adj_list)):
            desc.append(0)
        desc[s] = 1
        while len(Q) != 0:
            u = Q[-1]
            desempilhar = True
            for v in self.adj_list[u]:
                if desc[v] == 0:
                    desempilhar = False
                    Q.append(v)
                    desc[v] = 1
                    break
            if e in Q:
                break
            elif desempilhar:
                Q.pop()
        return Q

    def is_neighbor(self, u, v):
        """Returns True iif. u and v are neighbors in the graph"""
        pass

    def to_adj_matrix(self):
        """Returns the adj_matrix representation of the graph"""
        pass

    def is_valid_walk(self, walk: list[int]):
        """Returns True iif. walk (passeio) only uses valid edges to traverse the graph"""
        pass

    def is_valid_path(self, path: list[int]):
        """Returns True iif. path (caminho) is valid (i.e. does not repeat neither edges nor nodes)"""
        pass

    def is_closed(self, walk: list[int]):
        """Returns True iif. walk (passeio) starts and ends at the same node"""
        pass

    def degree_in_more_than(self, min_degree):
        """Returns the set of nodes that have the in degree larger than max_degree"""
        pass

    def degree_out_more_than(self, min_degree):
        """Returns the set of nodes that have the out degree larger than max_degree"""
        pass

    def nodes_having_in_degree(self, in_degree):
        """Returns the number of nodes having the given in_degree"""
        pass

    def nodes_having_out_degree(self, out_degree):
        """Returns the number of nodes having the given out_degree"""
        pass

    def diff_min_max_in_degree(self):
        """Returns the difference between the maximum and minimum in degree"""
        pass

    def diff_min_max_out_degree(self):
        """Returns the difference between the maximum and minimum out degree"""
        pass

    def is_directed(self):
        """Returns True if graph is directed, and False otherwise"""
        pass

    def remove_directed_edge(self, u, v):
        """Removes edge from u to v (and NOT from v to u)"""
        pass

    def remove_undirected_edge(self, u, v):
        """Removes both edges from u to v and from v to u"""
        pass

    def add_node(self):
        """Adds a new node (with no neighbors)"""
        pass

    def remove_node(self, u):
        """Remove node u (also remove any edge from/to it) - nodes from u+1 and on should be updated accordingly"""
        pass

    # ...
