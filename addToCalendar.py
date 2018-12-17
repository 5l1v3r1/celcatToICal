import os
from lxml import etree
import datetime
from extract import extract

def addToCalendar(xml):
		
	
	tree = etree.fromstring(xml)
	length = len(tree.getchildren())
	if length == 0 :
		print("Nothing to be done")
	else:
		print('Deleting all events from today to the end')
		os.system('''osascript -e 'tell application "iCal"
    tell calendar "ISTY"
       delete every event where its start date is greater than or equal to current date
	
    end tell
end tell'
''')
		print('ok , now adding new events')
		for matiere in tree.getchildren():
			date = datetime.datetime.strptime(matiere.findtext('date')+" "+matiere.findtext('debut'), "%Y-%m-%d %H:%M")
			now = datetime.datetime.now()
			if date >= now :
				dateFin= datetime.datetime.strptime(matiere.findtext('date')+" "+matiere.findtext('fin'), "%Y-%m-%d %H:%M")
				matiereEtProf=matiere.findtext('matiere')+" - "+matiere.findtext('prof')
				salle=matiere.findtext('salle')
				#print("Ajout")
				#print(date.strftime('%d/%m/%Y %H:%M'))
				#print(dateFin.strftime('%d/%m/%Y %H:%M'))
				#print(matiereEtProf)
				#print(salle)
				#print("ok")
				commande="osascript -e \'tell application \"iCal\" to make new event at end of calendar \"ISTY\" with properties {start date:date \"%s\",end date:date \"%s\", summary:\"%s\" , location:\"%s\" } \' \n" % (date.strftime('%d/%m/%Y %H:%M'),dateFin.strftime('%d/%m/%Y %H:%M'),matiereEtProf.replace("'"," "),salle)
				print(commande)
				os.system(commande)
		print('ok')
	
	
	
	
	



addToCalendar(extract())
