import socket
import struct
import pygame
import json
import io
import sys
sys.path.append('..')
from common.constants import *

class Listener:
    def __init__(self):
        # Initialize pygame mixer with optimal buffer
        pygame.mixer.pre_init(RATE, -16, CHANNELS, 1024)  # Smaller buffer for lower latency
        pygame.mixer.init()
        pygame.init()
        
        # Initialize UDP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Bind to the port
        self.sock.bind(('', PORT))
        
        # Join multicast group
        mreq = struct.pack('4sl', socket.inet_aton(MULTICAST_GROUP), socket.INADDR_ANY)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        
        # Improved buffering
        self.buffer = []
        self.buffer_size = 30  # Balance between latency and smoothness
        self.playing = False
        self.metadata = {}

    def start_listening(self):
        """Start receiving and playing audio"""
        print(f"Listening on {MULTICAST_GROUP}:{PORT}")
        
        while True:
            # Receive data
            data, addr = self.sock.recvfrom(BUFFER_SIZE)
            
            # Check if it's metadata
            if data.startswith(METADATA_HEADER):
                self.handle_metadata(data[len(METADATA_HEADER):])
                continue
            
            # Handle audio data
            self.handle_audio(data)

    def handle_metadata(self, metadata_bytes):
        """Process received metadata"""
        try:
            self.metadata = json.loads(metadata_bytes.decode())
            print(f"Now playing: {self.metadata.get('title', 'Unknown')}")
        except json.JSONDecodeError:
            print("Error decoding metadata")

    def handle_audio(self, audio_data):
        """Process and play received audio data"""
        try:
            self.buffer.append(audio_data)
            
            if len(self.buffer) >= self.buffer_size and not self.playing:
                self.playing = True
                combined_data = b''.join(self.buffer)
                sound = pygame.mixer.Sound(buffer=combined_data)
                sound.play()
                self.buffer = self.buffer[len(self.buffer)//4:]  # Keep 1/4 of buffer for overlap
                pygame.time.wait(10)  # Shorter wait time
                self.playing = False
        except Exception as e:
            print(f"Error playing audio: {e}")
            self.buffer = []

if __name__ == "__main__":
    listener = Listener()
    listener.start_listening() 