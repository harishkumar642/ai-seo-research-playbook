
from youtube_transcript_api import YouTubeTranscriptApi

video_ids = [
    "xsVTqzratPs",   # Ahrefs
    "abcd1234",      # Neil Patel
    "xyz5678"        # Julian Goldie
]

for vid in video_ids:
    print(f"\n--- Transcript for {vid} ---\n")
    
    try:
        transcript = YouTubeTranscriptApi().fetch(vid)
        
        for line in transcript:
            print(line.text)
            
    except Exception as e:
        print("Error:", e)
