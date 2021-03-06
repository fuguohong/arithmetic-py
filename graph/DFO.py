# coding=utf-8

class DFO:
    def __init__(self, graph):
        self._graph = graph
        self._preorder = []
        self._postorder = []
        self._marked = set()
        for v in self._graph.vertexes():
            if v not in self._marked:
                self._search(v)
        del self._marked
        del self._graph

    def _search(self, vertex):
        self._marked.add(vertex)
        self._preorder.append(vertex)
        for v in self._graph.adj(vertex):
            if v not in self._marked:
                self._search(v)
        self._postorder.append(vertex)

    def preorder(self):
        return self._preorder.copy()

    def postorder(self):
        return self._postorder.copy()


# ================= test ===============
if __name__ == '__main__':
    from graph.Digraph import Digraph

    with open('./tinyDG.txt') as f:
        g = Digraph()
        f.readline()
        f.readline()
        for l in f.readlines():
            datas = l.split('  ')
            g.add_edge(int(datas[0]), int(datas[1]))
        c = DFO(g)
        c2 = DFO(g.reverse())
        print(c.postorder())
        print(c2.postorder())
