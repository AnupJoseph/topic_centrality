import pandas as pd
def write_to_file(file_path,new_data):
	"""
		Writes a dataframe to file
	"""
	data_frame = new_data
	csvFile = open(file_path, 'w' ,encoding='utf-8')
	data_frame.to_csv(csvFile, mode='w', index=False, encoding="utf-8")