import tkinter as tk
from tkinter import messagebox, simpledialog

class VotingSystem:
    """
    A simple voting system that allows adding and deleting candidates, and resetting votes.
    """

    def __init__(self):
        self.candidates = {}
        self.vote_buttons = {}  # Change to a dictionary
        self.root = tk.Tk()
        self.root.title("Voting System")
        self.root.configure(bg='light blue')  # Set background color
        self.create_widgets()

    def create_widgets(self):
        """
        Creates the necessary widgets for the voting system.
        """
        tk.Label(self.root, text="Vote for:", bg='light blue', font=('Arial', 14)).pack()
        self.vote_frame = tk.Frame(self.root, bg='light blue')
        self.vote_frame.pack()
        self.add_vote_button("John")
        self.add_vote_button("Jane")
        tk.Button(self.root, text="Add Candidate", command=self.add_candidate, bg='light green').pack()
        tk.Button(self.root, text="Delete Candidate", command=self.delete_candidate, bg='light green').pack()
        tk.Button(self.root, text="Reset Votes", command=self.reset_votes, bg='light green').pack()
        tk.Button(self.root, text="Results", command=self.show_results, bg='light green').pack()

    def add_vote_button(self, name):
        """
        Adds a vote button for the specified candidate.
        """
        self.candidates[name] = 0
        button = tk.Button(self.vote_frame, text=f"{name}: 0 votes", command=lambda: self.vote(name), bg='light yellow')
        button.pack(side=tk.TOP)
        self.vote_buttons[name] = button  # Store button in dictionary

    def add_candidate(self):
        """
        Adds a new candidate.
        """
        name = simpledialog.askstring("Add Candidate", "Enter candidate's name:")
        if name:
            self.add_vote_button(name)

    def delete_candidate(self):
        """
        Deletes a candidate.
        """
        name = simpledialog.askstring("Delete Candidate", "Enter candidate's name:")
        if name in self.candidates:
            del self.candidates[name]
            self.vote_buttons[name].destroy()
            del self.vote_buttons[name]

    def vote(self, name):
        """
        Increments the vote count for the specified candidate.
        """
        self.candidates[name] += 1
        self.vote_buttons[name]['text'] = f"{name}: {self.candidates[name]} votes"  # Update button text

    def reset_votes(self):
        """
        Resets all votes to zero.
        """
        for name in self.candidates:
            self.candidates[name] = 0
            self.vote_buttons[name]['text'] = f"{name}: 0 votes"  # Reset button text

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