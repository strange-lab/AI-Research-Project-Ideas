import spacy
import networkx as nx
import matplotlib.pyplot as plt

# Load the SpaCy English language model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "Barack Obama was born in Hawaii and served as the 44th President of the United States. He was the first African American to hold the office."

# Process the text using SpaCy
doc = nlp(text)

# Create a NetworkX graph
G = nx.Graph()

# Extract entities and add them as nodes
for entity in doc.ents:
    G.add_node(entity.text, type=entity.label_)

# Extract relationships between entities
for token in doc:
    if token.dep_ in ["nsubj", "dobj", "nmod"]:
        subject = token.head.text
        object = token.text
        if subject in [ent.text for ent in doc.ents] and object in [ent.text for ent in doc.ents]:
            G.add_edge(subject, object)

# Visualize the knowledge graph
pos = nx.spring_layout(G)
node_colors = [
    "orange" if G.nodes[node]["type"] == "PERSON" else
    "green" if G.nodes[node]["type"] == "LOCATION" else
    "blue" if G.nodes[node]["type"] == "ORGANIZATION" else
    "gray"
    for node in G.nodes
]
nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color="lightgray")
plt.show()
