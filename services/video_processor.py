from pytube import YouTube
import subprocess

def download_video(video_url, output_path="video.mp4"):
    yt = YouTube(video_url)
    stream = yt.streams.get_highest_resolution()
    stream.download(filename=output_path)
    print(f"Downloaded video to {output_path}")

def trim_video(input_path, start_time, end_time, output_path):
    command = [
        "ffmpeg", "-i", input_path,
        "-ss", str(start_time),
        "-to", str(end_time),
        "-c:v", "copy", "-c:a", "copy",
        output_path
    ]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Trimmed video saved to {output_path}")
