"""Rules for one independent round of Rock, Paper, Scissors."""


def determine_winner(player: str, computer: str) -> str:
    """Return 'win', 'lose', or 'tie' from the player's perspective.

    The Flask server validates submitted moves before calling this function.
    """
    if player == computer:
        return "tie"

    winning_matchups = {
        ("rock", "scissors"),
        ("paper", "rock"),
        ("scissors", "paper"),
    }
    return "win" if (player, computer) in winning_matchups else "lose"
