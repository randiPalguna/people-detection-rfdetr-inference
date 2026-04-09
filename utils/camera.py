import cv2
import yt_dlp

class VideoStream:
    def __init__(self, source, yt_livestream=False):
        if yt_livestream:
            ydl_opts = {
                'format': 'bestvideo',
                'quiet': True,
                'noplaylist': True,
                'live_from_start': False,
                'no_warnings': True,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(source, download=False)
                stream_url = info['url']
            
            self.cap = cv2.VideoCapture(stream_url)
            self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        else:
            self.cap = cv2.VideoCapture(source)
            
        if not self.cap.isOpened():
            raise RuntimeError(f"Failed to open video source: {source}")
            
    def read(self):
        success, frame = self.cap.read()
        if not success:
            return None
        return frame
        
    def release(self):
        self.cap.release()