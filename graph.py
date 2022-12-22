'''
assignment: programming assignment 5 - graph.py
author: Lucais Sanderson
date: June 2, 2022
file: graph.py creates a Graph ADT. it implements both BFS and 
DFS.
input: can make graph ADT object. from there vertices and 
edges can be formed. They then can be traversed by either 
BFS or DFS. 
output: prints the tile board in terminal. 
'''


from random import choice

class Vertex:

    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        # initializes queue, stack and result 
        self.q = []
        self.s = []
        self.result = []

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def breadth_first_search(self, s):
        # base case: once the result contains 
        # the same number of element as the number of 
        # vertices, return the result.
        if len(self.result) == len(self.getVertices()):
            return self.result
        # recursive case:
        else:
            # if current vid not in queue,
            # enqueue
            if s not in self.q:
                self.q.append(s)
            # iterate the vid's connections
            for i in self.vertList[s].getConnections():
                # enqueue each one that isn't already present
                if i.id not in self.q and i.id not in self.result:
                    self.q.append(i.id)
            # dequeue and append front queue item
            self.result.append(self.q.pop(0))
            # if the queue is empty call function with None
            if len(self.q) == 0:
                return self.breadth_first_search(None)
            # else: recall function with current front of 
            # queue.
            else:
                return self.breadth_first_search(self.q[0])
    def depth_first_search(self):
        return self.DFS(1)

    def DFS(self, vid, path=[]):
        # base case:
        # if the path contains same number as vertices 
        # return the path
        if len(path) == len(self.getVertices()):
            print(path)
            return path
        # recursive case
        else:
            # if id not visited :
            if vid not in path:
                # push into stack and append value
                self.s.append(vid)
                path.append(vid)
            # searches current node's connections and checks if 
            # it's in the path already
            invalid = [i.id for i in self.vertList[vid].getConnections() if i in path]
            # if the all connections are visited
            if len(invalid) == len(self.vertList[vid].getConnections()):
                # recall function with top of stack 
                return self.DFS(self.s.pop(len(self.s)-1), path)
            elif len(invalid) == 0:
                # if no neighbors have been visited,
                # pick a path from the neighbor nodes 
                return self.DFS(choice([i.id for i in self.vertList[vid].getConnections()]), path)
            else:
                # if only a few neighbors haven't been visited,
                # visit one of those nodes.
                return self.DFS(choice([i.id for i in self.vertList[vid].getConnections() if i not in path]), path)
                
            

if __name__ == '__main__':
    g = Graph()
    for i in range(1,7):
        g.addVertex(i)
        
    g.addEdge(1,2)
    g.addEdge(1,5)
    g.addEdge(5,2)
    g.addEdge(5,4)
    g.addEdge(4,3)
    g.addEdge(3,2)
    g.addEdge(4,6)
    
    for v in g:
        print(v)
    #print(g.getVertex(0) in g)
    #assert (g.getVertex(0) in g) == True
    #assert (g.getVertex(6) in g) == False
        '''
    print(g.getVertex(0))
    assert str(g.getVertex(0)) == '0 connectedTo: [1, 5]'
    print(g.getVertex(5))
    assert str(g.getVertex(5)) == '5 connectedTo: [4, 2]'
    '''
    path = g.breadth_first_search(0)
    print('BFS traversal by discovery time (preordering): ', path)
    #assert path == [0, 1, 5, 2, 4, 3]
    
    path = g.depth_first_search()
    print('DFS traversal by discovery time (preordering): ', path)
    #assert path == [0, 1, 2, 3, 4, 5]
    

    