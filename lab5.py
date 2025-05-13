from gensim.downloader import load
import random
# Load the pre-trained GloVe model
print("Loading pre-trained GloVe model (50 dimensions)...")
model = load("glove-wiki-gigaword-50")
print("Model loaded successfully!")
# Function to construct a meaningful paragraph
def create_paragraph(iw, sws):
    
    paragraph = "The topic of "+iw+" is fascinating, often linked to terms like "
    random.shuffle(sws) # Shuffle to add variety
    for word in sws:
        paragraph += str(word) + ", "
    paragraph = paragraph.rstrip(", ") + "."
    return paragraph
iw = "hacking"
sws = model.most_similar(iw, topn=5)
words = [word for word, s in sws]
paragraph = create_paragraph(iw, words)
print(paragraph)
