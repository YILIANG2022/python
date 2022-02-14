from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print(f"I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What tink of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}.   Not sure where that is.
And you have a {computer} computer.   Nice.
""")

#在运行时，不能自动运行了，自动运行需要配置命令行，所以你就自己开个终端，在终端里运行，
#执行/usr/local/bin/python3 /Users/mac/python/vscode/习题十四.py Jeffrey