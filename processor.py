import subprocess
import time
import os
import datetime
from shutil import copyfile

camera_path = "C:\\FtpCamera\\Record\\NVR\\"
input_path = "C:\\ShareVM\\input\\"

while True:

	today_date = format_date(datetime.datetime.now())
	tomorrow_date = format_date(datetime.datetime.now() + datetime.timedelta(days=1))
	
	if os.path.isdir(camera_path + tomorrow_date):

		src_files = os.listdir(camera_path + today_date)
		
		for file_name in src_files:
			full_file_name = os.path.join(camera_path + today_date, file_name)
			if (os.path.isfile(full_file_name)):
				copyfile(full_file_name, input_path + file_name)
				conversion_file_name = file_name.replace("dav", "mp4")
				command = "ffmpeg -i " + input_path + file_name + " -vcodec copy -scodec mov_text " + input_path + conversion_file_name
				proc = subprocess.Popen(command)
				while proc.poll() is None:
					time.sleep(1)
				os.remove(input_path + file_name)

	while format_date(datetime.datetime.now()) is not tomorrow_date:
		time.sleep(1000)
		print("sleep :)")


def format_date(date):
	return str(date.year) + '-' + str(date.month) + '-' + str(date.day)