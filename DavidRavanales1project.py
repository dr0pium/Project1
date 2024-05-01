import tkinter as tk
from tkinter import messagebox, simpledialog

class VotingSystem:
    """
    A simple voting system that allows adding candidates.
    """

    def __init__(self):
        self.candidates = {}
        self.vote_buttons = []  # Define vote_buttons here
        self.root = tk.Tk()
        self.root.title("Voting System")
        self.create_widgets()



    def create_widgets(self):
        """
        Creates the necessary widgets for the voting system.
        """
        tk.Label(self.root, text="Vote for:").pack()
        self.vote_frame = tk.Frame(self.root)
        self.vote_frame.pack()
        self.add_vote_button("John")
        self.add_vote_button("Jane")
        tk.Button(self.root, text="Add Candidate", command=self.add_candidate).pack()
        tk.Button(self.root, text="Results", command=self.show_results).pack()

    def add_vote_button(self, name):
        """
        Adds a vote button for the specified candidate.
        """
        self.candidates[name] = 0
        button = tk.Button(self.vote_frame, text=name, command=lambda: self.vote(name))
        button.pack(side=tk.TOP)
        self.vote_buttons.append(button)

    def add_candidate(self):
        """
        Adds a new candidate.
        """
        name = simpledialog.askstring("Add Candidate", "Enter candidate's name:")
        if name:
            self.add_vote_button(name)

    def vote(self, name):
        """
        Increments the vote count for the specified candidate.
        """
        self.candidates[name] += 1

    def show_results(self):
        """
        Displays the voting results.
        """
        results = "\n".join(f"{name}: {votes} votes" for name, votes in self.candidates.items())
        messagebox.showinfo("Results", results)

        # Save results to a file
        with open('voting_results.txt', 'w') as f:
            f.write(results)

    def run(self):
        """
        Starts the Tkinter event loop.
        """
        self.root.mainloop()

if __name__ == "__main__":
    voting_system = VotingSystem()
    voting_system.run()