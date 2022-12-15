import networkx as nx
import numpy as np
class VNS:
    def __init__(self, A):
        self.A = A
        self.G = nx.from_numpy_matrix(A)
        self.B = nx.modularity_matrix(self.G)
        # init data structures


    def init_data_structures(self):
        # init all the dictionary and other data structures

    def check_modularity_change(self, node, community):
        # calculates the change of modularity when a node changes community

    def init_solution(self):
        # initial solution, should be set to LPAm+ algorithm

    def shaking(self, nodes_indicator):
        # shake by no
        if nodes_indicator:
            # shake by selecting a percentage of nodes
            # and applying a random transformation
        else:
            # shake by selecting a percentage of communities
            # and applying a random transformation


    def local_search(self, bi_indicator):
        # get all nodes
        node_list = [n for n in G]
        # BEST IMPROVEMENT
        if bi_indicator:
            best_improvement = None
            # go through the list until empty
            while node_list.len > 0:
                for node in node_list:
                # check if node could be moved with improvement
                # if not, remove from list
                # else, compare it with the best improvement found
                if best_improvement is not None:
                    # move the node and reset the best improvement
                    # update node list
                    best_improvement = None


        # FIRST IMPROVEMENT
        else:
        # go through the list until empty
        while node_list.len > 0:
            for node in node_list:
                # check if node could be moved with improvement
                # if not, remove from list
                # else, move the node and update node list



    def solve(self, n_iterations, seed, bi_indicator, nodes_indicator_p):
        # set seed
        np.random.default_rng(seed)
        best_sol = self.initial_solution()
        for iteration in range(n_iterations):
            nodes_indicator = True if np.random() > nodes_indicator_p else False
            x_prim = self.shaking(nodes_indicator)
            x_sec = self.local_search(x_prim, bi_indicator)
            if x_sec.modularity > best_sol.modularity:
                # move x_sec into best
                best_sol = x_sec

