import os


# 1)
path1 = os.path.join(os.path.abspath(os.path.dirname(__file__)))
print(path1)

path2 = os.getcwd()
print(path2)


# 2)
# print(os.environ['SHELLL'])  


# 3)
os.system('ping google.com')

# os.system('touch file3.txt')

# os.mkdir('first_dir')
# os.makedirs('second_dir/inside/another_dir/and_one_more')

os.replace(
    path2+'file3.txt',
    path2+'first_dir/file7.txt'
)

os.rename(
    path2+'/file3.txt',
    path2+'/first_dir/file6364634.txt'
)

print(os.listdir(path2))
print(os.scandir(path2))


for item in os.scandir(path2):
    if item.is_file():
        print(item.name, '<-- file')
    if item.is_dir():
        print(item.name, '<-- folder')


for i in os.walk(path2):
    print(i)



os.remove(path1+'/file3.txt')

os.rmdir(path1+'/first_dir')
os.removedirs(path1+'/second_dir/inside/another_dir/and_one_more')

