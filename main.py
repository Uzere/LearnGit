#!python3
import os, subprocess, shutil


def resetProgress():
	try:
		shutil.rmtree("myfirstrepo")  # hope no rm -rm /*
	except:
		pass  # seems there's no repo

def setUpWorkspace():
	try:
		os.mkdir("myfirstrepo")
	except:
		print("Error creating folder")

	os.chdir("myfirstrepo")




resetProgress()

setUpWorkspace()


# Our terminal prompt below is currently in an octobox directory. To initialize a Git repository here, type the following command:
# git init

# Good job! As Git just told us, our octobox directory now has an empty repository in /.git/. The repository is a hidden directory where Git operates.
# Next up, let's type the git status command to see what the current state of our project is:
# git status

# - add file
# I created a file called octocat.txt in the octobox repository for you (as you can see in the browser below).
# You should run the git status command again to see how the repository status has changed:
# git status

# Good, it looks like our Git repository is working properly. Notice how Git says octocat.txt is "untracked"? That means Git sees that octocat.txt is a new file.
# To tell Git to start tracking changes made to octocat.txt, we first need to add it to the staging area by using git add.
# git add octocat.txt

# Good job! Git is now tracking our octocat.txt file. Let's run git status again to see where we stand:
# git status

# Notice how Git says changes to be committed? The files listed here are in the Staging Area, and they are not in our repository yet. We could add or remove files from the stage before we store them in the repository.
# To store our staged changes we run the commit command with a message describing what we've changed. Let's do that now by typing:
# git commit -m "Add cute octocat story"

# Great! You also can use wildcards if you want to add many files of the same type. Notice that I've added a bunch of .txt files into your directory below.
# I put some in an octofamily directory and some others ended up in the root of our octobox. Luckily, we can add all the new files using a wildcard with git add. Don't forget the quotes!
# git add '*.txt'

# Okay, you've added all the text files to the staging area. Feel free to run git status to see what you're about to commit.
# If it looks good, go ahead and run:
# git commit -m 'Add all the octocat txt files'

# So we've made a few commits. Now let's browse them to see what we changed.
# Fortunately for us, there's git log. Think of Git's log as a journal that remembers all the changes we've committed so far, in the order we committed them. Try running it now:
# git log