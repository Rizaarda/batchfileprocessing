import subprocess
import time
import os
import datetime
from shutil import copyfile, rmtree

camera_path = "C:\\FtpCamera\\Record\\test\\"
input_path = "C:\\ShareVM\\input\\"
output_path = "C:\\ShareVM\\output\\"

def format_date(date):
	result = str(date.year) + '-'
	if date.month < 10:
		result += '0' + str(date.month) + '-'
	else:
		result += str(date.month) + '-'
	if date.day < 10:
		result += '0' + str(date.day)
	else:
		result += str(date.day)
	return result

while True:

	today_date = format_date(datetime.datetime.now())
	tomorrow_date = format_date(datetime.datetime.now() + datetime.timedelta(days=1))
	
	if os.path.isdir(camera_path + tomorrow_date):
		
		#src_files = os.listdir(camera_path + today_date)
		
		#for file_name in src_files:
		#	full_file_name = os.path.join(camera_path + today_date, file_name)
		#	if (os.path.isfile(full_file_name)):
		#		copyfile(full_file_name, input_path + file_name)
		#		conversion_file_name = file_name.replace("dav", "mp4")
		#		command = "ffmpeg -loglevel quiet -i " + input_path + file_name + " -vcodec copy -scodec mov_text " + input_path + conversion_file_name
		#		proc = subprocess.Popen(command)
		#		while proc.poll() is None:
		#			time.sleep(1)
		#		os.remove(input_path + file_name)
		
		command = "python RunStDocker_060419.py HLSOFF"
		proc = subprocess.Popen(command)

		while proc.poll() is None:
			time.sleep(1)

		output_folders = os.listdir(output_path)
		os.mkdir(output_path + today_date)

		for folder_name in output_folders:
			output_files = os.listdir(output_path + folder_name)
			for output_file in output_files:
				if output_file.endswith(".mp4"):
					copyfile(output_path + folder_name + output_file, output_path + today_date + output_file)
					rmtree(output_path + folder_name, ignore_errors=True)

	while format_date(datetime.datetime.now()) is not tomorrow_date:
		time.sleep(1)
		print("sleep :)")


