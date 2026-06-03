from ingestion.loader import load_text
from ingestion.preprocess import clean_text
from ingestion.chunker import chunk_text
from ingestion.indexer import Indexer

file_path = "data/sample.txt"

text = load_text(file_path)
text = clean_text(text)

chunks = chunk_text(text)

indexer = Indexer()
indexer.index(chunks)

print("Indexing complete!")
