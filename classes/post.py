class post:
    timestamp: str
    poster: str
    subject: str
    post_type: str
    message: str

    def __init__(self, timestamp, poster, subject, post_type, message):
        self.timestamp = timestamp
        self.poster = poster
        self.subject = subject
        self.post_type = post_type
        self.message = message