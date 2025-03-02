import socket
import time
from pydub import AudioSegment
import json
from pathlib import Path
import sys
sys.path.append('..')
from common.constants import *

class Broadcaster:
    def __init__(self):
        # Initialize UDP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
        
        # Current track info
        self.current_track = {
            "title": "",
            "artist": "",
            "duration": 0
        }

    def load_audio(self, file_path):
        """Load audio file using pydub"""
        print(f"Loading audio file: {file_path}")
        self.audio = AudioSegment.from_file(file_path)
        self.current_track["title"] = Path(file_path).stem
        self.current_track["duration"] = len(self.audio)
        return True

    def broadcast_audio(self):
        """Broadcast audio in chunks"""
        if not hasattr(self, 'audio'):
            print("No audio loaded!")
            return

        # Convert audio to raw data
        raw_data = self.audio.raw_data
        chunks = [raw_data[i:i+CHUNK_SIZE] for i in range(0, len(raw_data), CHUNK_SIZE)]

        print(f"Broadcasting to {MULTICAST_GROUP}:{PORT}")
        
        for chunk in chunks:
            try:
                self.sock.sendto(chunk, (MULTICAST_GROUP, PORT))
                # Calculate sleep time based on chunk size and sample rate
                sleep_time = CHUNK_SIZE / (RATE * CHANNELS * 2)
                time.sleep(sleep_time)  # More accurate timing
            except Exception as e:
                print(f"Error broadcasting: {e}")

    def send_metadata(self):
        """Send current track metadata"""
        metadata = json.dumps(self.current_track).encode()
        packet = METADATA_HEADER + metadata
        self.sock.sendto(packet, (MULTICAST_GROUP, PORT))

if __name__ == "__main__":
    broadcaster = Broadcaster()
    # Example usage with a test audio file
    if broadcaster.load_audio("blue .mp3"):
        broadcaster.broadcast_audio() 