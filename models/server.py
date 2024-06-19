from models.attention import Attention

class Server:
    def __init__(self, server_id, name):
        self.server_id = server_id
        self.name = name
        self.attentions = []

    def add_attention(self, attention):
        self.attentions.append(attention)

    def get_average_time(self):
        if not self.attentions:
            return 0
        return sum(att.time_taken for att in self.attentions) / len(self.attentions)

    def get_most_frequent_rating(self):
        if not self.attentions:
            return None
        ratings = [att.rating for att in self.attentions]
        return max(set(ratings), key=ratings.count)

    def to_dict(self):
        return {
            "server_id": self.server_id,
            "name": self.name,
            "attentions": [att.to_dict() for att in self.attentions]
        }

    @classmethod
    def from_dict(cls, data):
        server = cls(data["server_id"], data["name"])
        server.attentions = [Attention.from_dict(att) for att in data["attentions"]]
        return server