from src.load_docs import load_documents
from src.get_embeddings import get_embeddings
from src.vector_store import create_vector_store
from src.rag_pipeline import get_llm

def main():
    print("Loading documents...")
    docs = load_documents()

    print("Creating embeddings...")
    embeddings = get_embeddings()

    print("Building vector store...")
    vector_store = create_vector_store(docs, embeddings)

    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    llm = get_llm()

    while True:
        query = input("\nAsk a question (or type 'exit'): ")
        if query.lower() == "exit":
            break

        context_docs = retriever.invoke(query)
        context = "\n".join([doc.page_content for doc in context_docs])

        prompt = f"""
        Use the following context to answer the question.
        If you don't know, say you don't know.

        Context:
        {context}

        Question:
        {query}
        """

        response = llm.invoke(prompt)
        print("\nAnswer:", response.content)

if __name__ == "__main__":
    main()
