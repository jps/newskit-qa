"""Ask a question to the notion database."""
import faiss
from langchain import OpenAI
from langchain.chains import VectorDBQAWithSourcesChain
import pickle
import argparse
from termcolor import colored

parser = argparse.ArgumentParser(description='Ask a question to about the newskit design system?')
parser.add_argument('question', type=str, help='The question to ask about the newskit Design System')
args = parser.parse_args()

# Load the LangChain.
index = faiss.read_index("docs.index")

with open("faiss_store.pkl", "rb") as f:
    store = pickle.load(f)

store.index = index
chain = VectorDBQAWithSourcesChain.from_llm(llm=OpenAI(temperature=0.8), vectorstore=store)
result = chain({"question": args.question})

print(colored(f"Answer: {result['answer']}", 'magenta'))
print(colored(f"Sources: {result['sources']}", 'green'))