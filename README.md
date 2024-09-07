# Local RAG System with FAISS and SQLite

## Overview

This repository provides a solution for setting up a local Retrieval-Augmented Generation (RAG) system using FAISS for high-performance vector search and SQLite for managing text metadata. This setup is particularly suited for projects with a few thousand documents but can be scaled as needed. You may choose a different index/database i.e modify the code as per your needs. This is mainly to show how to synchronize data between FAISS and SQLite. This repo currently does not include steps like preprocessing/connecting to a LLM. I am planning to build over this as and when I get time.

<img width="655" alt="Screenshot 2024-09-07 at 7 06 24 PM" src="https://github.com/user-attachments/assets/9b71dfe5-3bbd-4dd0-819c-ff4005ef76bb">


### 1. FAISS for Vector Search

**FAISS (Facebook AI Similarity Search)** is an efficient library for performing similarity search on high-dimensional vectors. In this setup:
- **`IndexIDMap2`**: This FAISS index stores vectors and maps them to unique IDs. 

### 2. SQLite for Metadata Storage

- **Metadata Table**: Stores text and other information related to each vector. The table uses the same IDs as FAISS to link vectors to their metadata.


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

Check faiss github repo for instructions on how to install it.

## Contact

If you have an interesting project, you may connect with me on https://www.linkedin.com/in/mayankladdha31/
