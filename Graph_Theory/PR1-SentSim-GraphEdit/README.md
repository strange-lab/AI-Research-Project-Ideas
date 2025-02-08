# 1. Sentence Similarity Using Graph Edit Distance

## PR1 SentSim-GraphEdit

### Overview
This project explores sentence similarity using graph edit distance. Sentences are represented as graphs where nodes are words and edges represent relationships (e.g., syntactic dependencies). The similarity between two sentences is computed using graph edit distance.

### Objectives
- Represent sentences as graphs.
- Compute graph edit distance to measure sentence similarity.
- Evaluate the approach on small corpora like SNLI or GLUE.

### Dataset
- **SNLI**: [Stanford Natural Language Inference Corpus](https://nlp.stanford.edu/projects/snli/)
- **GLUE**: [General Language Understanding Evaluation Benchmark](https://gluebenchmark.com/)

### Dependencies
- Python 3.x
- Libraries:
  - `networkx` (for graph operations)
  - `nltk` or `spacy` (for tokenization and dependency parsing)
  - `numpy` (for numerical operations)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/strange-lab/AI-Research-Project-Ideas.git
   cd PR1-SentSim-GraphEdit