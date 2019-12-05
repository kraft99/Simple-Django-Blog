import os
import math
import uuid
import datetime
import re

from django.utils.html import strip_tags


def get_id_token():
	# @purpose : generate uuid token for Model id (PrimaryKey)
    return str(uuid.uuid4())


def upload_pic_location(instanse,file_obj):
	# PATH:media/backgrounds/username/file_name
	file_ext = file_obj.split('.')[-1]
	file_obj = '{}.{}'.format(uuid.uuid4().hex[:8],file_ext)
	return os.path.join("backgrounds",instanse.author.username,file_obj)


def words_count_from_html_tags(content):
	"""
	strip_tags -  remove anything that looks like an HTML tag from the string,<>
	"""
	# html_string = """
	# <p> i am the best </p>
	# """
	# word_string = strip_tags(content) #remove html tags from content <p></p>
	word_string = content
	count_words = len(re.findall(r'\w+',word_string)) #find and count every word in the content
	return count_words


def get_words_read_time(content):
	count = words_count_from_html_tags(content)
	#assume readtime per min == 200wpm
	readtime_min = math.ceil(count/200.0) 
	readtime_sec = readtime_min * 60 # 1 min == 60 sec
	read_time = str(datetime.timedelta(minutes=readtime_sec))
	return read_time






	