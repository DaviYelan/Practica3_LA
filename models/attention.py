from datetime import datetime

class Attention:
    def __init__(self, person_id, server_id, rating, date, time_taken):
        self.person_id = person_id
        self.server_id = server_id
        self.rating = rating
        self.date = date
        self.time_taken = time_taken

    def to_dict(self):
        return {
            "person_id": self.person_id,
            "server_id": self.server_id,
            "rating": self.rating,
            "date": self.date.strftime("%Y-%m-%d %H:%M:%S"),
            "time_taken": self.time_taken
        }

    @classmethod
    def from_dict(cls, data):
        date = datetime.strptime(data["date"], "%Y-%m-%d %H:%M:%S")
        return cls(data["person_id"], data["server_id"], data["rating"], date, data["time_taken"])