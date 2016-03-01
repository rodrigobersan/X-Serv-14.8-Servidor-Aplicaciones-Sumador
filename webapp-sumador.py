#!/usr/bin/python
import webapp
import random
import socket


class SumadorApp(webapp.webApp):
	primero = None

	def parse(self, peticion):
		try:
			num = int(peticion.split()[1][1:])
		except ValueError:
			return None
		return num

	def process(self, parsedRequest):
		if not parsedRequest:
			msg = 'Tienes que darme un numero. Ejemplo: localhost:1234/01'
			return("200 OK", "<html><body><h1>" + msg + "</html></body></h1>")
		else:
			if not self.primero:
				self.primero = parsedRequest
				msg = 'Primer numero guardado. Introduce el siguiente'
			else:
				msg = 'Resultado de la suma: ' + str(self.primero) + ' + ' + str(parsedRequest) + ' = ' + str(self.primero+parsedRequest)
				self.primero = None

		return("200 OK", "<html><body><h1>" + msg + "</html></body></h1>")

if __name__ == "__main__":
	testSumadorApp = SumadorApp("localhost", 1234)
