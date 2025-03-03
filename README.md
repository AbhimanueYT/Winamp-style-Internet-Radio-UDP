# Winamp-Style Internet Radio (UDP-Based)

## Overview
A **Winamp-style Internet Radio** application allows users to **broadcast audio streams** to multiple listeners using **UDP sockets**. Unlike TCP-based streaming, UDP ensures **low latency**, making it ideal for real-time audio broadcasting. This system is designed for efficiency, with a central broadcaster sending audio data packets that multiple listeners receive and play in real-time.

## Features
### **1. Live Audio Streaming**
- The broadcaster streams an **audio file or live audio feed** to connected listeners.
- Uses **UDP multicast** or **unicast** for efficient data distribution.

### **2. Low-Latency Streaming**
- UDP ensures quick delivery without waiting for acknowledgments, reducing delays.
- Buffering is implemented to handle packet loss and jitter.

### **3. Multiple Listeners Support**
- Many clients can tune in to the same stream simultaneously.
- Uses multicast to send data to multiple listeners efficiently.

### **4. Simple Station Selection**
- Users can choose different "stations" (audio streams) from a list.
- Each station has a unique port/IP for streaming.

### **5. Metadata Transmission (Song Title, Artist, etc.)**
- Alongside audio packets, metadata like **song title, artist, and duration** is sent.
- Metadata packets are sent periodically over UDP.

### **6. Basic GUI or CLI Interface**
- A simple **CLI-based player** or **lightweight GUI** (e.g., Tkinter, PyQt).
- Users can select a station and listen in real-time.

---

## Application Flow
### **1. Broadcaster (Server) Setup**
1. The broadcaster selects an **audio source** (file or live mic input).
2. Audio is **compressed and split into small packets**.
3. The broadcaster sends packets over **UDP to a specified IP and port**.
4. Metadata packets are sent periodically with song information.

### **2. Listener (Client) Tuning In**
1. The client selects a **station** and joins the corresponding UDP stream.
2. The client **receives and buffers audio packets**.
3. Metadata packets update the **song title and details**.
4. The client **decodes and plays** the audio in real-time.

### **3. Handling Packet Loss & Jitter**
- **Basic buffering** is implemented to handle minor packet loss.
- Clients attempt to **reconstruct missing packets** using interpolation techniques.
- If the connection is unstable, the client switches to a **lower bitrate stream** (if available).

### **4. Station Discovery & Switching**
- The broadcaster maintains a list of active stations.
- Clients can request available stations via a **separate UDP request**.
- Clients can switch between stations by changing the target IP/port.

---

## Technical Stack
### **Backend (Broadcaster/Server)**
- **Language**: Python (Socket programming with UDP)
- **Audio Processing**: FFmpeg or PyDub for encoding
- **Networking**: UDP Multicast/Unicast
- **Metadata Handling**: Custom UDP packets or JSON over UDP

### **Client (Listener)**
- **Language**: Python
- **Networking**: UDP sockets for receiving streams
- **Audio Playback**: Pygame, PyAudio, or VLC bindings
- **UI**: CLI-based player or minimal GUI (Tkinter/PyQt)

---

## Future Enhancements
- **Adaptive Bitrate Streaming**: Clients can switch to lower-quality streams if bandwidth is low.
- **Web-Based Interface**: A lightweight web app for selecting stations and listening.
- **Peer-to-Peer Relaying**: Allowing clients to redistribute streams to reduce server load.
- **Encrypted Streaming**: Secure audio transmission with encryption.

---

This document provides a structured guide for developing a **Winamp-style Internet Radio** using UDP sockets, aligned with the user's interest in **software testing, task automation, and embedded C/C++**. 🚀


## Implementation Steps:

**1. Download FFmpeg:**
    - Go to FFmpeg Windows Builds(https://github.com/BtbN/FFmpeg-Builds/releases)
    - Download ffmpeg-master-latest-win64-gpl.zip
    - Extract the zip file
    - Copy the three exe files from the bin folder (ffmpeg.exe, ffprobe.exe, ffplay.exe)
    - Paste them into your project's broadcaster folder
##OR

**2.Add FFmpeg to your system PATH:**
    - Download FFmpeg as above
    - Extract to a permanent location (e.g., C:\FFmpeg)
    - Add the bin folder path to your system's PATH environment variable

**3. Install Required Python Packages:**
    - pip install -r requirements.txt

**4. Run the Broadcaster:**
    - python broadcaster/broadcaster.py

**5. Run the Listener:**
    - python listener/listener.py


