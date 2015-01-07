class Entrata:
	def __init__(self, data, animale, peso, luogo):
		self.animale = animale
		self.peso = peso
		self.luogo = luogo


entrate = {
	"1/1/10" : Entrata("Cervo", 10, 9, "Trento")
}


def inserisci(data, animale, peso, luogo):
	entrate[data] = Entrata(animale, peso, lunghezza)


def visualizza():
	for data in entrate:
		print"Data: " + data
		print"Tipo di animale: " + str(entrate[data].animale)
		print"Peso: " + str(entrate[data].peso)
		print"Luogo: " + entrate[data].luogo


def rimuovi(data):
	del entrate[data]


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
		data = raw_input("insrire la data: ")
		animale = raw_input("inserire l'animale cacciato: ")
		peso = raw_input("inserire il peso dell'animale: ")
		luogo = raw_input("inserisci il luogo dove hai caccito l'animale:")


	if operazione == 3:
		data = raw_input("inserire la data: ")
		eliminare(data)






