import redis_server
from cache import timed_lru_cache

class Proxy:

    # Initialize Proxy
    def __init__(self):

        self.cache = 
        self.expiry = os.getenv('EXPIRY') // 1000
        self.max_connections = os.getenv('MAX_CONNECTIONS')
        self.

    @timed_lru_cache(self.expiry, self.max_connections)

    # initiate redis server, listen for connections
    def run(self, ):

        # Listen for and create connections
        while True:


    # Run

    # Manage Connections
    # Create New Connection


