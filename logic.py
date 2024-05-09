import sys


class VotingLogic:
    def __init__(self, ui):
        """
        Initialize the VotingLogic class.
        """
        self.ui = ui
        self.ui.pushButton.clicked.connect(self.cast_vote)
        self.voted_ids: set[str] = set()
        # Starts vote tally with Joe Biden, Donald Trump, and Mickey Mouse
        # all start at 0 votes
        self.votes: dict[str, int] = {'Joe Biden': 0, 'Donald Trump': 0, 'Mickey Mouse': 0}

    def cast_vote(self):
        """
        Casts a vote based on user input
        """
        voter_id: str = self.ui.lineEdit.text().strip().lower()  # Convert input to lowercase and strip any whitespace
        voter_name: str = self.ui.idinput.text().strip()  # Strip any leading or trailing whitespace
        if not voter_id or not voter_name: # Gives an error message if no id and or name is entered
            self.ui.label_6.setText("<html><head/><body><p><span style=\" color:#ff0000; font-weight:bold;\">Enter both Voter ID and Name</span></p></body></html>")
            return
        if voter_id in self.voted_ids: # Gives an error message if voter id already voted
            self.ui.label_6.setText("<html><head/><body><p><span style=\" color:#ff0000; font-weight:bold;\">ALREADY VOTED</span></p></body></html>")
            return
        candidate = ""
        # Determine the selected candidate, Biden, Trump, Or Mickey mouse is clicked
        if self.ui.radioButton.isChecked():
            candidate = "Joe Biden"
        elif self.ui.radioButton_2.isChecked():
            candidate = "Donald Trump"
        elif self.ui.radioButton_3.isChecked():
            candidate = "Mickey Mouse"
        if candidate:
            # Write the vote information to the file votes.txt
            with open("votes.txt", "a") as f:
                f.write(f"{voter_name:<30} {voter_id:<30} {candidate}\n")  # Write formatted data
            # Update the voted_ids set and increment vote count for the selected candidate
            self.voted_ids.add(voter_id)
            self.votes[candidate] += 1
            # Display "VOTE SUBMITTED" in bold and blue when submit is selected, and it is a good vote
            self.ui.label_6.setText("<html><head/><body><p><span style=\" color:#0000ff; font-weight:bold;\">VOTE SUBMITTED</span></p></body></html>")
            # Clear input fields and radio button selection
            self.ui.idinput.clear()
            self.ui.lineEdit.clear()
            self.ui.radioButton.setChecked(False)
            self.ui.radioButton_2.setChecked(False)
            self.ui.radioButton_3.setChecked(False)

    def close_application(self, _) -> None:
        """
        Closes the application and writes the final vote tally to files.
        """
        # Determine the winner
        winner: str = max(self.votes, key=self.votes.get)
        max_votes: int = max(self.votes.values())
        winners: list[str] = [c for c, v in self.votes.items() if v == max_votes]

        # Write the tally to a file
        with open("vote_tally.txt", "w") as f:
            f.write("Candidate\tVotes\n")
            for candidate, votes in self.votes.items():
                f.write(f"{candidate}\t{votes}\n")
            if len(winners) > 1:
                f.write(f"\n\nIt's a tie between: " + ", ".join(winners) + " with " + str(max_votes) + " votes.\n")
            else:
                f.write(f"\n\nThe winner is {winner} with {max_votes} votes.\n")

        # Write the winner or winners via(tie) to the votes.txt file
        with open("votes.txt" , "a") as f:
            if len(winners) > 1:
                f.write(f"\n\nIt's a tie between: " + ", ".join(winners) + " with " + str(max_votes) + " votes.\n")
            else:
                f.write(f"\n\nThe winner is {winner} with {max_votes} votes.\n")

        # Close the application
        sys.exit(0)  # Exit the application
