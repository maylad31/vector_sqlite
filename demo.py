from vector_utils import build_index,add_to_index,save_index,load_index,store_to_db,search_index,retrieve,grouper
from data_schema import IndexData
from sentence_transformers import SentenceTransformer
import sqlite3
import numpy as np
from tqdm import tqdm
sqlite3.register_adapter(np.int64, int)

# 1. Load a pretrained Sentence Transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")


data_chunks = [
    "The weather is lovely today.",
    "It's so sunny outside!",
    "He drove to the stadium.",
    "Mayank is a software developer.",
    "I don't think it works.",
    "why do you want to know about my profession?",
    "what is your salary?",
    "have conviction in the power of goodness.",
    "Mayank works as a software developer."
]



index = build_index(dimension=384)
connection = sqlite3.Connection("demo.db",isolation_level=None)
step_size = 3


print("adding to index")
id=0
for batch in tqdm(list(grouper(data_chunks,step_size))):  
    # Calculate embeddings
    embeddings = model.encode(batch)
    all_points = [] 
    for i in range(step_size):
        point = IndexData(vector=embeddings[i],content=batch[i],id=id)
        id+=1
        all_points.append(point)
    #add to index
    add_to_index(index=index,data=all_points)
    store_to_db(data=all_points,connection=connection,index_name="demo")
    
save_index(index=index,index_name="demo")
index = load_index(index_name="demo")
query = "Who is Mayank?"
print("searching for query: ",query)
embeddings = model.encode([query])
#print(embeddings[0])
#vector => ids
D,I =search_index(index=index,query=embeddings,k=2)
print("distances and ids:",D,I)
#sql => ids => text/metadata
res = retrieve(index_name="demo",ids=I,connection=connection) 
print("result:",res)
    
    
    





