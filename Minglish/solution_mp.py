#import Set module, some older versions of python don't carry
from sets import Set

#Set up directed graph with branches
def create_graph(words):
    alphabet = {}
    graph_size = len(words)
    for vert in range(graph_size - 1):
        #Combined Tuple then unpack
        # new_edge returning two variables creates TypeError
        item = new_edge(words[vert],words[vert+1])
        if item != None:
            vertice, weight = item
            if vertice in alphabet:
                alphabet[vertice].append(weight)
            else:
                #dict values must be lists to append
                alphabet[vertice] = [weight]
    return alphabet

    #Finding the order of characters in words
def new_edge(one, two):
    for char in range(min(len(one),len(two))):
        #First different letters will show the order in minglish
        if one[char] != two[char]:
            return one[char],two[char]
    return None

#Finding the root of our directional graph
def find_root(graph):
    #Using set instead of list, does not allow duplicates
    missing = Set()
    edges = Set()
    #Get each letter relationship in graph
    for rels in graph.values():
        for char in rels:
            edges.add(char)
    for key in graph:
        if key not in edges:
            missing.add(key)
    #Now we know where we don't have a relationship mapped
    return missing

def answer(words):
    #Create dictionary of words and relationships
    graph = create_graph(words)
    #Find missing values to start direction
    root = find_root(graph)
    tested=[]
    language = []
    #Recursive embedded function, standalone class sort failed
    def find_path(letter):
        if letter not in tested:
            tested.append(letter)
            if letter in graph:
                for value in graph[letter]:
                    find_path(value)
            language.append(letter)
    for char in root:
        find_path(char)
    #Running in set order will get order reverse from recursive function
    language.reverse()
    language = "".join(language)
    return language

print answer(["xys","zys","tuv"])
print answer(["y", "z", "xy"])