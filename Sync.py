import os
import subprocess

input_folder = 'DirofYourInputFolder'   
output_folder = 'DirofYourOutputFolder'

os.makedirs(output_folder, exist_ok=True)


for filename in os.listdir(input_folder):
    if filename.endswith('.wav'):
        
        audio_file = os.path.join(input_folder, filename)
        
        video_file = os.path.join(input_folder, filename.replace('.wav', '.mp4'))
        
        output_file = os.path.join(output_folder, filename.replace('.wav', '.mp4'))        
        
        subprocess.run(['ffmpeg', '-i', audio_file, '-i', video_file, '-c:v', 'copy', '-c:a', 'aac', output_file])

