import argparse
import spacy
import networkx as nx
from networkx.algorithms.similarity import graph_edit_distance

# Load SpaCy model for dependency parsing
nlp = spacy.load("en_core_web_sm")

def sentence_to_graph(sentence):
    """
    Convert a sentence into a graph representation.
    Nodes: Words in the sentence.
    Edges: Dependency relationships between words.
    """
    doc = nlp(sentence)
    G = nx.DiGraph()
    for token in doc:
        G.add_node(token.text, pos=token.pos_)
        if token.head is not token:  # Avoid self-loops
            G.add_edge(token.head.text, token.text, dep=token.dep_)
    return G

def compute_similarity(graph1, graph2):
    """
    Compute graph edit distance between two graphs.
    Lower values indicate higher similarity.
    """
    return graph_edit_distance(graph1, graph2)

def main():
    parser = argparse.ArgumentParser(description="Compute sentence similarity using graph edit distance.")
    parser.add_argument("--sentence1", type=str, required=True, help="First sentence")
    parser.add_argument("--sentence2", type=str, required=True, help="Second sentence")
    args = parser.parse_args()

    # Convert sentences to graphs
    graph1 = sentence_to_graph(args.sentence1)
    graph2 = sentence_to_graph(args.sentence2)

    # Compute similarity
    similarity_score = compute_similarity(graph1, graph2)
    print(f"Graph Edit Distance: {similarity_score}")

if __name__ == "__main__":
    main()