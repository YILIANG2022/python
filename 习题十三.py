from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

#在运行时，不能自动运行了，自动运行需要配置命令行，所以你就自己开个终端，在终端里运行，
#执行/usr/local/bin/python3 /Users/mac/python/vscode/习题十三.py first 2nd 3rd