from adjVertex import createAdjVertex
from coordinats import createCoordinatesOfVertex

class Graph:
    def __init__(self):
        self.coordinates = createCoordinatesOfVertex()
        self.adjVertex = createAdjVertex()
