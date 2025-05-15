import pdfplumber

# Step 1: Extract Text from IPC PDF
def extract(file):
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text
    
# Step 2: Search for Relevant Sections in IPC
def search(query, ipc):
    query = query.lower()
    lines = ipc.split("\n")
    results = [line for line in lines if query in line.lower()]
    return results if results else ["No relevant section found."]

# Step 3: Main Chatbot Function
def chatbot():
    print("Loading IPC document...")
    ipc = extract("IPC.pdf")
    while True:
        query = input("Ask a question about the IPC: ")
        if query.lower() == "exit":
            print("Goodbye!")
            break
        
        results = search(query, ipc)
        print("\n".join(results))
        print("-" * 75)
chatbot()
