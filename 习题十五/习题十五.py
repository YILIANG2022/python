from distutils import text_file
from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

#在运行时，不能自动运行了，自动运行需要配置命令行，所以你就自己开个终端，在终端里运行，
#执行/usr/local/bin/python3 /Users/mac/python/vscode/习题十五/习题十五.py ex15_sample.txt