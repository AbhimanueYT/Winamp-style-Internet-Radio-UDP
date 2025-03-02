# Network settings
MULTICAST_GROUP = '224.1.1.1'
PORT = 12345
BUFFER_SIZE = 2048  # Smaller network buffer for more frequent updates

# Audio settings
CHUNK_SIZE = 1024   # Smaller chunks for more frequent updates
CHANNELS = 2
RATE = 44100
FORMAT = 'wav'

# Metadata packet identifier
METADATA_HEADER = b'META:' 