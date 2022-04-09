class Player:
    name: str
    drops: int
    turnovers: int
    points_played: int
    blocks: int
    scores: int
    assists: int

    def __init__(self, name: str, drops: int = 0, turnovers: int = 0, points_played: int = 0, blocks: int = 0, scores: int = 0, assists: int = 0):
        self.name = name
        self.drops = drops
        self.turnovers = turnovers
        self.points_played = points_played
        self.blocks = blocks
        self.scores = scores
        self.assists = assists




def add(p_list: list[Player], selected: str) -> None:
    for liner in p_list:
        if liner.name == selected:
            liner.drops += 1
    return 

# player_list: list[player] = [

# ThomasH: Player("Thomas Harley"),
# JonS: Player("Jon Su"),
# LiamSB: Player("Liam Searles-Bohs"),
# SethL: Player("Seth Lee"),
# AndrewL: Player("Andrew Li"),
# JasonM: Player("Jason")]
# # Max Goetz
# # Walker Garrett
# # Hawthorne Hamm
# # Ben Dameron
# # Luke Duan
# # Jack McCleary
# # Bodhi Harmony
# # Rutledge Smith
# # Wesley Britt
# # Jake Schwartz
# # frederick huang
# # tom will
# # Josh Singleton
# # Jayden Feagans
# # Matthew McKnight
# # Kevin Pignone
# # Bailey Roberts 
# # Grayson Trowbridge
# # Eli Fried
# # John McDonnell
# # Aaron Wei
# # Henry Chen]