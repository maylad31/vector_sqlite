import faiss 
import numpy as np
import sqlite3
from typing import Optional,List,Dict,Tuple
from data_schema import IndexData
from contextlib import closing
import pickle

def build_index(dimension:int)->faiss.IndexIDMap2:
    flat_index = faiss.IndexFlatL2(dimension)
    index = faiss.IndexIDMap2(flat_index)
    return index


def add_to_index(index:faiss.IndexIDMap2,data:List[IndexData])->None:
    ids = []
    vectors = []
    for point in data:
        ids.append(point.id)
        vectors.append(point.vector)
        
    ids = np.array(ids, dtype=np.int64)
    vectors = np.array(vectors, dtype=np.float32)
    index.add_with_ids(vectors, ids)
    
def save_index(index:faiss.IndexIDMap2,index_name:str)->None:
    chunk = faiss.serialize_index(index)
    with open(f"""{index_name}.pkl""", "wb") as f:
        pickle.dump(chunk, f)
    
def load_index(index_name:str)->faiss.Index:
    with open(f"""{index_name}.pkl""", "rb") as f:
        index = faiss.deserialize_index(pickle.load(f))
    return index
    
    
def store_to_db(data:List[IndexData],connection:sqlite3.Connection,index_name:str)->None:
    try:
        values = []
        for point in data:
            values.append((point.id,point.content,str(point.metadata)))
        with connection:
            
            res = connection.execute(
                f"""CREATE TABLE IF NOT EXISTS {index_name}(id INTEGER PRIMARY KEY, content TEXT, metadata TEXT)""")
            
            res = connection.executemany(
                f"""INSERT INTO {index_name} (id, content, metadata) VALUES (?,?,?)""", values)
            
            res = connection.execute(f"""SELECT * FROM {index_name}""")
            rows = res.fetchall()
            #print("here",rows)  # Print 
        
    except Exception as e:
        print('Could not complete operation:', e)


def search_index(index:faiss.IndexIDMap2,query:np.ndarray,k:int=3)->Tuple[List[float], List[int]]:
    D, I = index.search(query, k)
    #print(type(D),type(I))
    return list(D[0]),list(I[0])

def retrieve(index_name:str,ids:List[int],connection:sqlite3.Connection): 
    #ids = list(map(int,))
    cur = connection.cursor()
    rows = []
    qs = ", ".join("?" * len(ids))
    with closing(connection.cursor()) as cur:
        
        cur.execute(f"""SELECT * FROM {index_name} WHERE id IN ({','.join(['?']*len(ids))})""", ids)
        rows = cur.fetchall()
    return rows

def grouper(iterable:list, n:int):
    for i in range(0, len(iterable), n):
        yield iterable[i:i+n]
    

if __name__=="__main__":
    pass




