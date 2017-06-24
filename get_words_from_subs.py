from pathlib import Path
import re
import enchant

def filter_words(word_list):

	#unique
	result = set(word_list)
	
	#words only
	result = [word for word in result if not any(symbol.isdigit() for symbol in word)] 
	
	#check for english words
	dict_checker = enchant.Dict("en_US")
	result = [word for word in result if dict_checker.check(word)] 
	
	#remove <i>
	result = [word.replace('<i>', '') for word in result] 
	
	#only words with 3 or more letters
	result = [word for word in result if len(word) > 2]
	
	#lower case
	result = [word.lower() for word in result]
	
	return result

def get_words_from_file(file_name):
	with open(file_name, 'r', encoding='latin-1') as f:
		subtitles_text = f.read()
		
		return filter_words(re.findall(r"[\w']+", subtitles_text))

if __name__ == '__main__':
	p = Path('.')
	srt_list = list(p.glob('*.srt'))
	final_result = set()
	
	for str_file in srt_list:
		print(str_file)
		final_result.update(get_words_from_file(str_file.name))
	
	final_result = list(final_result)
	final_result.sort()
	
	print(final_result)