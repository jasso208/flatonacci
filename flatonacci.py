def flatonacci(signature: list, n: int) -> list:
	
	listaResp = []

	try:
		if n < 0:
			#print("El parametro n no puede ser menor a cero")
			return listaResp
		#validamos que el primer parametro sea una lista
		if type(signature) != type(listaResp):
			#print("El parametro signature debe ser una lista")
			return listaResp

		#val 1: Validamos que la lista recibida tenga 3 elementos
		if len(signature) != 3:
			#print("la lista recibida debe ser de 3 numeros.")
			return listaResp

		#val 2: Validamos que los 3 elementos sean numericos
		if type(signature[0]) != type(0) or type(signature[1]) != type(0) or type(signature[2]) != type(0):
			#print("la lista recibida debe ser de 3 numeros.")
			return listaResp


		listaResp.extend(signature)

		cont = 3
		while cont <= n-1:
			nvoValor = listaResp[cont-1] + listaResp[cont-2] + listaResp[cont-3]
			listaResp.append(nvoValor)
			cont += 1

		if n > 3:
			return listaResp
		else:
			return listaResp[:n]
	except Exception as e:
		print(e)
		return listaResp
