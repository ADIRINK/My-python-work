import customtkinter as tk
from pytube import YouTube

def download_video():
    video_url = entry.get()
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        max_filesize = stream.filesize
        bytes_downloaded = 0
        progress_var = tk.DoubleVar()
        progress_var.set(0)
        progress_bar['maximum'] = max_filesize

        def progress_callback(stream, chunk, bytes_remaining):
            nonlocal bytes_downloaded
            bytes_downloaded += len(chunk)
            progress_var.set(bytes_downloaded)
            root.update_idletasks()

        stream.download(output_path='/YT_DOWNLOADER', filename=stream.default_filename, on_progress=progress_callback)
        progress_var.set(max_filesize)
    except Exception as e:
        print(e)

root = tk.CTk()
root.geometry("360x140")
root.title('YouTube Downloader')
tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

label = tk.CTkLabel(root, text='Enter YouTube URL:')
label.pack(pady=3)

entry = tk.CTkEntry(root)
entry.pack(pady=3)

button = tk.CTkButton(root, text='Download', command=download_video)
button.pack(pady=3)

progress_bar = tk.CTkProgressBar(root, orientation='horizontal', width=300,height=10, mode='determinate')
progress_bar.pack(pady=12)

root.mainloop()
