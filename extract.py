import urllib.request
from lxml import etree
import datetime

def extract():
		
	#output = open("output.xml","w") 
	rq=urllib.request.Request('http://chronos.iut-velizy.uvsq.fr/EDTISTY/g112050.xml')
	rq.add_header("Authorization", "Basic ZXR1aXN0eTppc3R5") # user:pass base64 encoded
	site=urllib.request.urlopen(rq)
	xmlResult=site.read().decode('utf8')
	#print(xmlResult)
	
	tree = etree.fromstring(xmlResult)
	semaines = {}
	for semaine in tree.xpath("/timetable/span"):
		semaines[semaine.findtext('alleventweeks')]=semaine.findtext('description')[-10:]
	#print(semaines)
	result="<matieres>\n"
	#print("<matieres>\n");
	
	for event in tree.xpath("/timetable/event"):
		#print("\nELEMENT ################")
		
	
	
		#print(event.findtext('starttime'))
		#print(event.findtext('endtime'))
		#print(semaines[event.findtext('rawweeks')])
		dateSemaine = datetime.datetime.strptime(semaines[event.findtext('rawweeks')], "%d/%m/%Y")
		jour = dateSemaine + datetime.timedelta(days=int(event.findtext('day')))
		#print(str(jour)[:10])
	
		resources=event.find("resources");
		try:
			matiere=resources.find("module").findtext("item")
		except AttributeError:
			matiere="ISTY"
		try:
			salle=resources.find("room").findtext("item")
		except AttributeError:
			salle="ISTY"
	
		try:
			prof=resources.find("staff").findtext("item")
		except AttributeError:
			prof="ISTY"
	
		#print(matiere)
		#print(salle)
		#print(prof)
		result+="	<matiere>\n"
		#print("	<matiere>\n");
		result+="		<date>"+str(jour)[:10]+"</date>\n"
		#print("		<date>"+str(jour)[:10]+"</date>\n");
		result+="		<debut>"+event.findtext('starttime')+"</debut>\n"
		#print("		<debut>"+event.findtext('starttime')+"</debut>\n");
		result+="		<fin>"+event.findtext('endtime')+"</fin>\n"
		#print("		<fin>"+event.findtext('endtime')+"<\/fin>\n");
		result+="		<matiere>"+matiere+"</matiere>\n"
		#print("		<matiere>"+matiere+"</matiere>\n");
		result+="		<prof>"+prof+"</prof>\n"
		#print("		<prof>"+prof+"</prof>\n");
		result+="		<salle>"+salle+"</salle>\n"
		#print("		<salle>"+salle+"</salle>\n");
		result+="	</matiere>\n"
		#print("	</matiere>\n");
		
	
	#print("</matieres>");
	result+="</matieres>"
	return result




