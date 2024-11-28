from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi

API_KEY = 'your_youtube_api_key'

def search_videos(query, max_results=5):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    request = youtube.search().list(
        q=query,
        part='snippet',
        type='video',
        maxResults=max_results
    )
    response = request.execute()
    return [{"id": item["id"]["videoId"], "title": item["snippet"]["title"]} for item in response["items"]]

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return [{"start": t["start"], "duration": t["duration"], "text": t["text"]} for t in transcript]
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None
