# DVLA reader thingy

things_i_care_about = []

import csv
with open('DVLA_FOI_LSOA_v2.csv') as csvfile:
	dvla_reader = csv.DictReader(csvfile)
	for row in dvla_reader:
		#print ( row.keys() )
		
		# lan2020 -- location
		# year -- year :/
		# cars
		# pop18plus -- over 18s
		
		#lsoan -- Lower layer Super Output Area (LSOA)
		# https://www.doogal.co.uk/LSOA.php?code=E01000003
        #City of London 001A

		if "poole" in row['lsoan'].lower() :
			things_i_care_about.append( row )
			print('*', end='')
		else:
			print('.',end='')
		
for thing in things_i_care_about:
	print (thing['lsoan'], thing['year'], thing['cars'], thing['pop18plus'])
	
with open('poole.csv', 'w', newline='') as csvfile:
	fieldnames = ['year', 'cars', 'pop18plus']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for thing in things_i_care_about:
		writer.writerow({'year': thing['year'], 'cars': thing['cars'], 'pop18plus' : thing['pop18plus'] })
	
