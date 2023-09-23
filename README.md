# Preprocessed-CMLR-Dataset-For-Wav2Lip

Considering the original Wav2Lip was trained on LSR2 and didn't have good performance on Chinese. I preprocessed CMLR Dataset and would train Wav2Lip on CMLR. Wish it would do better in Chinese.  

The CMLR dataset was collected by the Visual Intelligence and Pattern Analysis (VIPA) group of Zhejiang University(Their website:https://vipazoo.cn/CMLR.html). Thanks to their excellent work.

As the VIPA group declared, this dataset is public to universities and research institutes for research purpose only. I actually use this dataset only for research in East China University of Science and Technology. If the VIPA group feel uncomfortable about my repository, please feel free to contact me via email（21013097@mail.ecust.edu.cn）

# How to use

1. download the original CMLR from https://vipazoo.cn/CMLR.html
2. Unzip the package.
3. cd to the directory of /s1 , /s2 etc.  For example, D:/news/s1
4. run the Unpack.py, and the files in the subfolders will be moved to /s1
5. run the Sync.py. You have to install FFmpeg before running it. The Sync.py is based on FFmpeg.
6. Now you get the .mp4 files. Use Rename.py to rename them as 00001.mp4 etc. Then these .mp4 files could be used by Wav2Lip.

# More details

If you find that it is hard for you to download CMLR from https://vipazoo.cn/CMLR.html, feel free to contact me for help. The download speed is so Fxxking slow, because Baidu, an annoying company in China, limits the download speed for more money.
