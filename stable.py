#! /usr/bin/env python
# -*- coding: utf-8 -*-


import traceback
import cgi
import json
import sys
sys.path.append('/home/l/lankssu/lib/python/')
import xlrd
from datetime import datetime
#from tempfile import TemporaryFile
from urllib import unquote_plus

def application(environ, start_response):
	
	months_entry_keeping = 1

	status = '200 OK'
	try:
		log_file = open('/home/l/lankssu/lanksnet/public_html/logs/log', 'a')
		log_file.write('.oriflame_upload_script.wsgi started on ' + str(datetime.now())[:19] + ' \n')
		#log_file.write('input: ' + str(environ['wsgi.input'].read())[:256] + ' \n')
		fields = cgi.FieldStorage(fp=environ['wsgi.input'],environ=environ, keep_blank_values=1)
		log_file.write('input: ' + str(fields['name'].value) + ' \n')

		filename = fields['file'].filename
		filename = filename.split(".")
		filename[0] = fields['name'].value
		
		current_month = int(str(datetime.now())[5:7])
		current_year = int(str(datetime.now())[0:4])

		#Open db
		json_file = open('/home/l/lankssu/lanksnet/public_html/dbs/oriflame_db.json', 'r')
		raw_json = json_file.read()
		#raw_json = raw_json.encode("utf-8")
		log_file.write("Opening oriflame_db.json...\n")
		db_fail = 0
		try:
			database = json.loads(raw_json)
			database["coding"] = "cyr"
			db = database["db"]
			for e in range(len(db)):
				#content = db[e]["content"]
				#log_file.write("content:"+str(content)+"\n")
				for i in range(len(content)):
					content[i]["title"] =  content[i]["title"].encode("utf8")
					content[i]["value"] = content[i]["value"].encode("utf8")
					#log_file.write("title:"+str(content[i]["value"])+"\n")
				#log_file.write("title:"+str(content)+"\n")
			#log_file.write("title:"+str(db)+"\n")
			#log_file.write("oriflame_db.json successfully opened\n")
		except:
			log_file.write("Cannot open oriflame_db.json\n")
			db_fail = 1
		json_file.close()
		
		#If failure make copy
		if db_fail:
			copy_file = open('/home/l/lankssu/lanksnet/public_html/dbs/oriflame_db_failure_' + str(datetime.now())[:19].replace(" ", "_") + '.json', 'w')
			copy_file.write(raw_json)
			copy_file.close()
		else:
			#Make previous day copy
			if database["version"] != str(datetime.now())[:10]:
				copy_file = open('/home/l/lankssu/lanksnet/public_html/dbs/oriflame_db_previous.json', 'w')
				copy_file.write(raw_json)
				copy_file.close()
			
			
		#Upload file
		upload_file = open('/home/l/lankssu/lanksnet/public_html/dbs/' + filename[0] + '.' + filename[-1], 'w+b')
		log_file.write("Beginning upload...\n")
		byte = fields["file"].file.read(1)
		while byte:
			upload_file.write(byte)
			byte = fields["file"].file.read(1)
		log_file.write("File " + str(filename) + " uploaded!\n")
		upload_file.close()
		
		#Open file
		log_file.write("Reading uploaded file...\n")
		read_fail = 0
		try:
			xls_file = xlrd.open_workbook('/home/l/lankssu/lanksnet/public_html/dbs/' + filename[0] + '.' + filename[-1])
			sheet = xls_file.sheet_by_index(0)
		except:
			log_file.write("Cannot open file! \n")
			read_fail = 1
		
		#Do if all is right
		if (not read_fail) and (not db_fail):
			database["version"] = str(datetime.now())[:10]
			database["coding"] = "Кириллица"
			data = []
			
			#Read uploaded file
			for rownum in range(sheet.nrows):
				row = sheet.row_values(rownum)
				c_row=[]
				for c_el in row:
					if type(c_el) == type(u''):
						#f.write(str([c_el]))
						c_el = c_el.encode("utf8")
					else:
						c_el = str(c_el)
						if c_el[-2:]=='.0':
							c_el = c_el[:-2]
					c_row.append(c_el)
				data.append(c_row)
			columns = data[2]
			data = data[3:]
			
			#Remove old entries
			for entry in database["db"]:
				entry_month = int(str(entry["date"])[5:7])
				entry_year = int(str(entry["date"])[0:4])
				months_entry_keeping
				if (current_year != entry_year) and (entry_month < (12-months_entry_keeping+current_month)) \
				or (current_year == entry_year) and (entry_month < (current_month-months_entry_keeping)):
					database["db"].remove(entry)
				
			#Write uploaded entries in db
			for line in data:
				is_present = 0
				if len(line)<4:
					continue
				for value in database["db"]:
					if line[4] == value["id"]:
						is_present = 1
						value["date"] = str(datetime.now())[:19]
						value["content"] = []
						for i in range(len(columns)):
							value["content"].append({"title":columns[i],"value":line[i]})
				if not is_present:
					value = {}
					value["id"] = line[4]
					value["date"] = str(datetime.now())[:19]
					value["content"] = []
					for i in range(len(columns)):
						value["content"].append({"title":columns[i],"value":line[i]})	
					database["db"].append(value)
		
		#Make new db if loading of old db failed		
		elif (not read_fail) and db_fail:
			database = {}
			database["version"] = str(datetime.now())[:10]
			database["coding"] = "Кириллица"
			database["db"] = []
			data = []
			
			#Read uploaded file
			for rownum in range(sheet.nrows):
				row = sheet.row_values(rownum)
				c_row=[]
				for c_el in row:
					if type(c_el) == type(u''):
						#f.write(str([c_el]))
						c_el = c_el.encode("utf8")
					else:
						c_el = str(c_el)
						if c_el[-2:]=='.0':
							c_el = c_el[:-2]
					c_row.append(c_el)
				data.append(c_row)
			columns = data[2]
			data = data[3:]
			
			#Write uploaded entries in db
			for line in data:
				value = {}
				value["id"] = line[4]
				value["date"] = str(datetime.now())[:19]
				value["content"] = []
				for i in range(len(columns)):
					value["content"].append({"title":columns[i],"value":line[i]})	
				database["db"].append(value)
						
		log_file.write("item:"+str(type(database["db"][2]['content'][2]["title"]))+"\n")	
		#Write db in file
		raw_data = json.dumps(database, sort_keys = True, indent = 4, separators = (',', ': '), ensure_ascii=False)
		#raw_data = raw_data.encode("utf8")
		json_file = open('/home/l/lankssu/lanksnet/public_html/dbs/oriflame_db.json', 'w')
		json_file.write(raw_data)
		json_file.close()


	except:
		tb = traceback.format_exc()
		errors_log = open('/home/l/lankssu/lanksnet/public_html/logs/error_log', 'a')
		errors_log.write('upload_script ended with error on ' + str(datetime.now())[:19] + ' \n')
		errors_log.writelines(tb)
		errors_log.write(' \n')
		errors_log.close()

	output = 'Кириллица'
	response_headers = [('Content-type', 'html'),
	                ('Content-Length', str(len(output)))]
	start_response(status, response_headers)
	 

	return [output]