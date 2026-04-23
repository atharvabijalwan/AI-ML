!pip install -q openai-whisper
!pip install -q faiss-cpu
!pip install -q sentence-transformers
!pip install -q yt-dlp

#step 2

import whisper
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import yt_dlp

#step 3

video_url = "https://www.youtube.com/watch?v=aircAruvnKk"  # you can change this

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'audio.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
    }],
}

#step 4 
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

    model = whisper.load_model("base")

result = model.transcribe("audio.wav")

segments = result['segments']

print("Sample Transcription:\n")
print(segments[:2])

#step 5

texts = []
timestamps = []

for seg in segments:
    text = seg['text']
    start = seg['start']
    end = seg['end']
    
    texts.append(text)
    timestamps.append((start, end))

    #step 6

    embed_model = SentenceTransformer('all-MiniLM-L6-v2')

embeddings = embed_model.encode(texts)

# step 7

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))

# step 8

def search(query, k=3):
    query_vec = embed_model.encode([query])
    
    distances, indices = index.search(np.array(query_vec), k)
    
    results = []
    
    for i in indices[0]:
        text = texts[i]
        start, end = timestamps[i]
        
        results.append({
            "text": text,
            "start": start,
            "end": end
        })
        
    return results

    #step 9

    query = "What is neural network?"

results = search(query)

for r in results:
    print(f"\n🧠 Answer: {r['text']}")
    print(f"⏱️ Timestamp: {round(r['start'],2)}s - {round(r['end'],2)}s")

    #step 10

    full_text = " ".join(texts[:50])  # limit for simplicity

print("\n📌 Summary:\n")
print(full_text[:1000])