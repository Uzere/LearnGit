#!python3
import sys, os, subprocess, codecs
import shutil, shlex

if os.name == 'nt':
	from ctypes import windll
	STD_OUTPUT_HANDLE = -11
	stdout_handle = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


DEFAULT, COMMAND, GREEN, RED = 7, 11, 10, 12
COLORS = {
	'd': DEFAULT,
	'c': COMMAND,
	'g': GREEN,
	'r': RED
}

LIN_COLORS = {
	DEFAULT: '\033[0m',
	COMMAND: '\033[94m',
	GREEN: '\033[92m',
	RED: '\033[91m'
}

def setColor(color):
	if os.name == 'nt':
		windll.kernel32.SetConsoleTextAttribute(stdout_handle, color)
	else:
		print(LIN_COLORS[color], end="")

def colorPrint(s):
	a = s.split('$')
	for l in a:
		if l[0]=='~':
			setColor(COLORS[l[1]])
		else:
			print(l, end="")
			sys.stdout.flush()
	print("")

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
		setColor(RED)
		print("Error creating folder")

	os.chdir("myfirstrepo")


baseDir = os.getcwd()


def commandInput():
	"""
	Получает команду, запускает и получает вывод 
	"""
	setColor(DEFAULT)
	s = input(os.getcwd().replace(baseDir, "")[1:]+">")
	t = shlex.split(s)
	out = "error"

	try:
		if os.name == 'nt':
			out = subprocess.check_output(t, shell=True)
		else:
			out = subprocess.check_output(" ".join(t), shell=True)

		try:
			out = codecs.decode(out)
		except:
			out = codecs.decode(out, 'cp866', 'ignore')
		setColor(DEFAULT)
		print(out)

	except Exception as e:
		#if e.returncode!=1:
			print("TTT", t)
			print("EEE", e)
			setColor(RED)
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
"""Мы находимся в почти-настоящем-терминале в папке $~c$myfirstrepo$~d$.
И нам нужно создать здесь новый git репозиторий.
Для этого нужно просто ввести команду: $~c$git init$~d$
""",
lambda it, ot: "git" in it and "init" in it and ("Initialized" in ot or "Инициализированный" in ot)
), 

(
"""Отлично! Как сказал Git, наша папка $~c$myfirstrepo$~d$ теперь содержит пустой репозиторий в папке $~c$./.git/$~d$. Это скрытая папка, где Git хранит все свои файлы.
Можно посмотреть список файлов в текущей папке с помощью команды $~c$dir$~d$ или $~c$dir /a$~d$ чтобы увидеть и скрытые файлы. Эту команду можно использовать в любой момент.
Далее, введём команду $~c$git status$~d$ и посмотрим текущее состояние нашего проекта.
""",
lambda it, ot: "git" in it and "status" in it and ("On branch" in ot or "В ветке" in ot)
),

(
"""Я создал файл $~c$reallynewfile.txt$~d$ в нашем репозитории (Его можно увидеть с помощью команды $~c$dir$~d$).
Снова выполни команду $~c$git status$~d$ чтобы посмотреть что изменилось.
""",
lambda it, ot: "git" in it and "status" in it and ("On branch" in ot or "В ветке" in ot),
lesson2hook
),

(
"""Кажется, наш репозиторий работает правильно. Git говорит что $~c$reallynewfile.txt$~d$ - неотслеживаемый ($~c$untracked$~d$), значит Git обнаружил новый файл.
Чтобы Git начал отслеживать изменения в этом файле, нужно его проиндексировать ($~c$stage$~d$) с помощью команды $~c$git add reallynewfile.txt$~d$
""",
lambda it, ot: "git" in it and "add" in it
),

(
"""Отлично, git теперь следит за изменениями в файле $~c$reallynewfile.txt$~d$. 
Чтобы посмотреть текущее состояние, используем команду $~c$git status$~d$.
""",
lambda it, ot: "git" in it and "status" in it and ("On branch" in ot or "В ветке" in ot)
)

]


resetProgress()

setUpWorkspace()


lesson = 0
while lesson<len(lessons):
	# print(lessons[lesson][0])
	colorPrint(lessons[lesson][0])
	while True:
		try:
			lessons[lesson][2]()
		except IndexError:
			pass
		
		it, ot = commandInput()

		suc = False
		if "dir"==it[0]:
			pass
		elif "ls"==it[0]:
			pass
		elif lessons[lesson][1](it, ot):
			suc = True
		else:
			setColor(RED)
			print("Что-то не так, попробуй ещё раз")

		if suc:
			break
	lesson+=1

setColor(GREEN)
print("Нет больше уроков")


setColor(DEFAULT)



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
