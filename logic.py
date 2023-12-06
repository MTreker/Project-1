from PyQt6.QtWidgets import *
from gui import *
import csv


class Logic(QMainWindow, Ui_Main_Window):
    john = 0
    jane = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.john_button.hide()
        self.jane_button.hide()
        self.vote_button.hide()
        self.clear_button.hide()
        self.vote_button.clicked.connect(lambda: self.candidate_menu())
        self.clear_button.clicked.connect(lambda: self.clear())
        self.varify_button.clicked.connect(lambda: self.varify())
        self.john_button.clicked.connect(lambda: self.john_vote())
        self.jane_button.clicked.connect(lambda: self.jane_vote())
        self.exit_button.clicked.connect(lambda: self.exit())
        self.just_voted = False
        with (open('vote.cvs', 'r') as vote_csv_file):  # This calculates and displays the total number of votes
            # that are already in the csv file
            vote_reader = csv.reader(vote_csv_file)
            for row in vote_reader:
                if row[1] == 'john':
                    self.john += 1
                elif row[1] == 'jane':
                    self.jane += 1
                else:
                    pass
            self.text_menu.setPlainText(f"             Total "
                                        f"\nJohn: {self.john} "
                                        f"\nJane: {self.jane} "
                                        f"\n\nPlease put in your NUID to vote")

    def varify(self):
        """Checks to see if the user has already voted or not

        """
        with (open('vote.cvs', 'r') as vote_csv_file):
            vote_reader = csv.reader(vote_csv_file)
            for row in vote_reader:
                if row[0] == self.no_vote_text.text():
                    no_vote = False
                else:
                    no_vote = True
        if not no_vote:
            self.text_menu.setPlainText(f"             Total "
                                        f"\nJohn: {self.john}"
                                        f"\nJane: {self.jane}"
                                        f"\n\nYou have already voted")
        else:
            if self.no_vote_text.text() == '':
                self.text_menu.setPlainText(f"             Total "
                                            f"\nJohn: {self.john}"
                                            f"\nJane: {self.jane}"
                                            f"\n\nCan not be blank. Please enter NUID")
            else:
                self.text_menu.setPlainText(f"             Total "
                                            f"\nJohn: {self.john}"
                                            f"\nJane: {self.jane}"
                                            f"\n\nPlease click Vote or Clear for next option")
            self.no_vote_text.hide()
            self.varify_button.hide()
            self.vote_button.show()
            self.vote_button.setDisabled(False)
            self.clear_button.show()
            self.clear_button.setDisabled(False)

    def vote_menu(self):
        """Displays the menu for the person to vote or not

        """
        self.john_button.hide()
        self.john_button.setDisabled(True)
        self.jane_button.hide()
        self.jane_button.setDisabled(True)
        self.vote_button.show()
        self.vote_button.setDisabled(False)
        self.clear_button.show()
        self.clear_button.setDisabled(False)
        self.text_menu.setPlainText(f"             Total "
                                    f"\nJohn: {self.john}"
                                    f"\nJane: {self.jane}")
        self.vote_button.hide()
        self.vote_button.setDisabled(True)
        self.clear_button.hide()
        self.clear_button.setDisabled(True)

    def candidate_menu(self):
        """Displays the menu for the person to choose who to vote for

        """
        self.john_button.show()
        self.john_button.setDisabled(False)
        self.jane_button.show()
        self.jane_button.setDisabled(False)
        self.vote_button.hide()
        self.vote_button.setDisabled(True)
        self.clear_button.hide()
        self.clear_button.setDisabled(True)
        self.text_menu.setPlainText(f"             Total "
                                    f"\nJohn: {self.john}"
                                    f"\nJane: {self.jane}"
                                    f"\n\nPlease press the button for the person you want to vote for")

    def john_vote(self):
        """Increases the john variable if the vote for John

        """
        data = [self.no_vote_text.text(), 'john']
        with open('vote.cvs', 'a', newline='') as vote_csv_file:
            csvwriter = csv.writer(vote_csv_file)
            csvwriter.writerow(data)
        self.john += 1  # adds to john
        self.just_voted = True
        return self.vote_menu()

    def jane_vote(self):
        """Increases the jane variable if the vote for Jane

        """
        data = [self.no_vote_text.text(), 'jane']
        with open('vote.cvs', 'a', newline='') as vote_csv_file:
            csvwriter = csv.writer(vote_csv_file)
            csvwriter.writerow(data)
        self.jane += 1  # adds to jane
        self.just_voted = True
        return self.vote_menu()

    def clear(self):
        """Resets the variables john and jane to 0 and returns the beginning text to the menu

        """
        self.john = 0
        self.jane = 0
        with open('vote.cvs', 'r+') as f:
            f.readline()  # read one line
            f.truncate(f.tell())  # terminate the file here
        self.no_vote_text.clear()
        return self.vote_menu()

    def exit(self):
        """Exits the program when button is clicked

        """
        exit()
