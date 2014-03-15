#!python3
import os, subprocess, shutil, shlex, codecs


def resetProgress():
	"""
	Удаляет результаты предыдущих запусков
	"""
	try:
		shutil.rmtree("myfirstrepo")  # hope no rm -rm /*
	except:
		pass  # seems there's no repo


def setUpWorkspace():
	"""
	Создаёт папку и устанавливает её как текущую
	"""
	try:
		os.mkdir("myfirstrepo")
	except:
		print("Error creating folder")

	os.chdir("myfirstrepo")


baseDir = os.getcwd()


def commandInput():
	"""
	Получает команду, запускает и получает вывод 
	"""
	s = input(os.getcwd().replace(baseDir, "")[1:]+">")
	t = shlex.split(s)
	out = "error"

	try:
		out = subprocess.check_output(t, shell=True)
		try:
			out = codecs.decode(out)
		except:
			out = codecs.decode(out, 'cp866', 'ignore')
		print(out)

	except:
		print(t)
		print("Something going wrong")

	return (t, out)


def lesson2hook():
	"""
	Создаёт файл, нужный для второго (с 0) урока
	"""
	with open("reallynewfile.txt", "w") as f:
		f.write("42 is the answer to life the universe and everything")


lessons = [

(
"""Мы находимся в почти-настоящем-терминале в папке myfirstrepo.
И нам нужно создать здесь новый git репозиторий.
Для этого нужно просто ввести команду: git init
""",
lambda it, ot: "git" in it and "init" in it and "Initialized" in ot
), 

(
"""Отлично! Как сказал Git, наша папка myfirstrepo теперь содержит пустой репозиторий в папке /.git/. Это скрытая папка, где Git хранит все свои файлы.
Можно посмотреть список файлов в текущей папке с помощью команды dir или dir /a чтобы увидеть и скрытые файлы. Эту команду можно использовать в любой момент.
Далее, введём команду git status и посмотрим текущее состояние нашего проекта.
""",
lambda it, ot: "git" in it and "status" in it and "On branch" in ot
),

(
"""Я создал файл reallynewfile.txt в нашем репозитории (Его можно увидеть с помощью команды dir).
Снова выполни команду git status чтобы посмотреть что изменилось.
""",
lambda it, ot: "git" in it and "status" in it and "On branch" in ot,
lesson2hook
)


]


resetProgress()

setUpWorkspace()


lesson = 0
while lesson<len(lessons):
	print(lessons[lesson][0])
	while True:
		try:
			lessons[lesson][2]()
		except IndexError:
			pass
		
		it, ot = commandInput()

		suc = False
		if "dir"==it[0]:
			pass
		elif lessons[lesson][1](it, ot):
			# print("PROFIT")
			suc = True
		else:
			print("Что-то не так, попробуй ещё раз")

		if suc:
			break
	lesson+=1

print("Нет больше уроков")


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