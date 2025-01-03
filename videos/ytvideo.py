import yt_dlp

video_url = "https://www.youtube.com/shorts/hCfHsSIgvAM"
ydl_opts = {
    "format": "bestvideo",  # Download the best video format (no audio)
    "outtmpl": "videos/left_elbow_plank_video.mp4",  # Specify output path and name
    "noplaylist": True,  # Ensure only the single video is downloaded
    "quiet": False,  # Show output messages for better debugging
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    try:
        ydl.download([video_url])
        print("Video downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")