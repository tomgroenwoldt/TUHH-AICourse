from collections import defaultdict
import csv
from collections import deque


class Wikigraph:
    
    def __init__(self):
        links = open('data/enwiki-2013-small.txt').read().strip().split('\n')
        self.hyperlinks = defaultdict(list)
        for link in links:
            a, b = [int(x) for x in link.split()]
            self.hyperlinks[a].append(b)
        
        self.name_to_id = defaultdict()
        self.id_to_name = defaultdict()
        
        with open('data/enwiki-2013-small-names.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                self.name_to_id[row[1]] = int(row[0])
                self.id_to_name[int(row[0])] = row[1]
    
    def get_id(self, page: str):
        return self.name_to_id[page]
    
    def get_name(self, page_id: int):
        return self.id_to_name[page_id]
    
    def get_links(self, page_id: int):
        return self.hyperlinks[page_id]



def length_of_shortest_path(start_page: str, end_page: str, wikigraph: Wikigraph):
    start_id = wikigraph.get_id(start_page)
    end_id = wikigraph.get_id(end_page)

    q = deque([start_id])
    seen = [start_id]

    parent = {start_id: None}
    while q:
        v = q.pop()
        # check if we are done
        if v == end_id:
            steps = []
            while v:
                steps.append(v)
                v = parent[v]

            # Visualize the resulting path
            for i, s in enumerate(steps[::-1]):
                print(f"Step {i}:")
                print(graph.get_name(s))
            return len(steps)
        for w in wikigraph.get_links(v):
            if w in seen:
                continue
            seen.append(w)
            q.appendleft(w)
            parent[w] = v

    return 0


graph = Wikigraph()
length_of_shortest_path("Out of memory", "Solar power in Germany", graph)
