class Tournament:
    def __init__(self):
        self._participants = []

    def add_participant(self, participant_dict):
        if not isinstance(participant_dict, dict):
            raise TypeError("Participant must be a dictionary")

        if not all(key in participant_dict for key in ("name", "country", "points")):
            raise ValueError("Participant must contain 'name', 'country', and 'points' keys")

        if not isinstance(participant_dict["name"], str):
            raise TypeError("Participant name must be a string")

        if not isinstance(participant_dict["country"], str):
            raise TypeError("Participant country must be a string")

        if not isinstance(participant_dict["points"], int):
            raise TypeError("Participant points must be an integer")

        self._participants.append(participant_dict)

    def update_points(self, name, points):
        if not isinstance(name, str):
            raise TypeError("Participant name must be a string")
        if not isinstance(points, int):
             raise TypeError("Participant points must be an integer")

        found = False
        for participant in self._participants:
            if participant["name"] == name:
                participant["points"] = points
                found = True
                break
        if not found:
            raise ValueError(f"Participant with name '{name}' not found")

    def get_leaderboard(self):
        return sorted(self._participants, key=lambda x: x["points"], reverse=True)

    @property
    def participants_count(self):
        return len(self._participants)

    @property
    def top_participant(self):
        if not self._participants:
            return None
        return max(self._participants, key=lambda x: x["points"])



if __name__ == '__main__':
    tournament = Tournament()

    tournament.add_participant({"name": "Alice", "country": "USA", "points": 120})
    tournament.add_participant({"name": "Bob", "country": "Canada", "points": 150})
    tournament.add_participant({"name": "Charlie", "country": "UK", "points": 100})


    print(f"Number of participants: {tournament.participants_count}")

