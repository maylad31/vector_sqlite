# FAISS with SQLite

## Overview

Connect faiss with sqlite. Keep vectors in faiss, data in sqlite. Planning to add usearch, qdrant and support for fts. Why use this? For RAG, libraries like langchain are overcomplicated, going through docs and changing stuff is hard, and on top of that they change frequently. I prefer to have much more control on my pipeline and if you feel the same, this code might be a good starting point.

<img width="655" alt="Screenshot 2024-09-07 at 7 06 24 PM" src="https://github.com/user-attachments/assets/9b71dfe5-3bbd-4dd0-819c-ff4005ef76bb">

## Detailed Solution

### FAISS Index Setup

1. **Creating the Index**: Use `IndexIDMap2`over flat(IndexFlatL2) to create and manage vectors.
2. **Serializing the Index**: Serialize the FAISS index to save it locally.
3. **Deserializing the Index**: Load the FAISS index from the serialized file when needed.

### SQLite Metadata Management

1. **Creating the Database**: Initialize a SQLite database with a table to store metadata.
2. **Inserting Metadata**: Add records with IDs that correspond to FAISS vector IDs.
3. **Querying Metadata**: Retrieve metadata based on vector IDs obtained from FAISS searches.

### Example Workflow


**Perform Search**:
    - Query FAISS to find nearest neighbors for a given vector.
    - Use the resulting IDs to query SQLite and retrieve metadata.

## Installation

For faiss, check its github repo for instructions on how to install it. Sqlite come with Python.

## Contact

If you have an interesting project, you may connect with me on https://www.linkedin.com/in/mayankladdha31/
Please star this repo if you found it useful.
