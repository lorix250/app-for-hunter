import re

class Entrata:
	def __init__(self, animale, peso, luogo):
		self.animale = animale
		self.peso = peso
		self.luogo = luogo


entrate = {}

def inserisci(data, animale, peso, luogo):
	if dataValida(data):
		entrate[data] = Entrata(animale, peso, luogo)



def visualizza():             
	for data in entrate:
		print"Data: " + data
		print"Tipo di animale: " + str(entrate[data].animale)
		print"Peso: " + str(entrate[data].peso)
		print"Luogo: " + entrate[data].luogo


def rimuovi(data):
	del entrate[data]


def dataValida(data):
	
	if re.match("^[\w]*$", data):
		return False

	if data[2] != "/" or data[5] != "/":
		return False

	return True

print "Cosa hai cacciato oggi Lorenzo"
while True:
	operazione = input("1 per visualizzare, 2 per inserire l'animale, 3 per eliminarlo dalla lista.")


	if operazione < 1 or operazione > 3:
		print "Error, scegli un opzione valida"
		continue

	if operazione == 1:
		try:
			visualizza()
		except:
			print"Eccezione"
			continue


	if operazione == 2: 
		data = raw_input("inserire la data: ")
		if not dataValida(data):
			print "data non e valida"
			continue
		animale = raw_input("inserire l'animale cacciato: ")
		peso = raw_input("inserire il peso dell'animale: ")
		luogo = raw_input("inserisci il luogo dove hai caccito l'animale:")
		inserisci(data, animale, peso, luogo)

	if operazione == 3:
		data = raw_input("inserire la data: ")
		rimuovi(data)