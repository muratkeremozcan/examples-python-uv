from typing import Dict, List, Set, Tuple

roster: Dict[str, int] = {"Chuck": 37, "Devin": 2, "Steven": 4}

agents: List[str] = [
    f"Agent {agent}, {missions} missions" for agent, missions in roster.items()
]

print(agents)

#############


class Agent:
    def __init__(self, codename: str, missions: int):
        self.codename: str = codename
        self.missions: int = missions

    # Create the add_mission() method, add type hinting
    def add_mission(self, location: str) -> None:
        self.missions += 1
        print(
            f"{self.codename} completed a mission in "
            + f"{location}. This was mission #{self.missions}"
        )


# Create an Agent object, add type hints
chuck: Agent = Agent("Charles Carmichael", 37)

# Create a list of locations, add a mission for each
locations: List[str] = ["Burbank", "Paris", "Prague"]
for location in locations:
    chuck.add_mission(location)

print(chuck.missions)
