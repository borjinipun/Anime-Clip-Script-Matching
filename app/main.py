from services.youtube_fetcher import search_videos, get_transcript
from services.script_generator import generate_script
from services.embeddings import generate_embeddings, find_best_match
from services.video_processor import download_video, trim_video

if __name__ == "__main__":
    print("Welcome to the Anime Video Matching Project!")

    # Example Usage
    # Step 1: Search and fetch video transcripts
    query = "anime fight scenes"
    videos = search_videos(query, max_results=3)
    print(f"Found Videos: {videos}")
    
    video_id = videos[0]["id"]
    transcript = get_transcript(video_id)
    print(f"Transcript: {transcript}")

    # Step 2: Generate script
    prompt = "Write an anime scene where the hero saves a village from bandits."
    script = generate_script(prompt)
    print(f"Generated Script: {script}")

    # Step 3: Embedding and matching
    scene = script.split("\n")[0]
    best_match, similarity = find_best_match(scene, transcript)
    print(f"Best Match: {best_match}, Similarity: {similarity}")

    # Step 4: Download and trim video
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    download_video(video_url, "full_video.mp4")
    trim_video("full_video.mp4", best_match["start"], best_match["start"] + best_match["duration"], "scene_clip.mp4")
    print("Video segment saved!")
