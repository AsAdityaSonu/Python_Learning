from moviepy.editor import VideoFileClip

# Path to the video file
video_path = 'path/to/video/file.mp4'

# Convert video to audio
video_clip = VideoFileClip(video_path)
audio_path = 'path/to/save/audio/file.mp3'
video_clip.audio.write_audiofile(audio_path)

print(f"Converted to audio: {audio_path}")
