import os
import shutil

s1_folder = 'Your Dir'
#for example,d:/news/s4
for root, dirs, files in os.walk(s1_folder):
    # 遍历每个子文件夹的文件
    for file in files:
        # 构建源文件的完整路径
        source_file = os.path.join(root, file)
        
        # 移动文件到S1文件夹的目录下
        shutil.move(source_file, s1_folder)
#move the files in the subfolders to /s4