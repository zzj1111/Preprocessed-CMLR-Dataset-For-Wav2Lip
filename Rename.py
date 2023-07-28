import os

# get the files in the filefolder
files = os.listdir('D:/news/output_s5')
# rename the .mp4 file as 00001.mp4,00002.mp4 etc.
# please modify the dir
files.sort()

# define the counter
counter = 0

for file in files:
    # 获取文件的完整路径
    old_name = os.path.join('D:/news/output_s5', file)
    
    # 构造新的文件名
    new_name = os.path.join('D:/news/output_s5', f'{counter:05d}.mp4')
    
    # 重命名文件
    os.rename(old_name, new_name)
    
    # 增加计数器
    counter += 1
