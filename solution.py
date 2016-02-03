#!/usr/bin/env python3
# Modifiez ce fichier si votre solution est en Python.
# Ce programme est un court exemple du protocol et d'une réponse au
# premier challenge "Ping".
# Modifiez "run.sh" pour exécuter ce programme python et
# exécutez la suite de test avec la commande "./runner ./run.sh"
#
# Pour l'exemple en java regardez "solution.java". Pour d'autre langage,
# faites un programme qui lit et écrit par les entrées et sorties standard
# et modifier "run.sh" pour compiler et exécuter votre programme.
#
# N'OUBLIER PAS DE "FLUSHER" VOS SORTIES!

import sys
m, msg = sys.stdin.readline().split(':')

# damn Windows who doesn't play well with script outputs... Had to test manually with examples
#_, m, msg = sys.argv

flush = sys.stdout.flush

if m == "1":
	print(msg)
	flush()

elif m == "2":
	result = False

	if len(msg) % 2 == 0:
		halfL = len(msg)//2
		
		firstHalf = msg[:halfL]
		secHalf = msg[halfL:]
				
		if firstHalf == secHalf[::-1]:
			result = True			
	else:
		halfL = (len(msg)-1)//2
		
		firstHalf = msg[:halfL]
		secHalf = msg[halfL+1:]
		
		if firstHalf == secHalf[::-1]:
			result = True		

	print(result)
	flush()

elif m == "3":
	arr = msg.split(',')
	arr.sort()
	print(arr)
	flush()

elif m == "4":

	from collections import defaultdict
	dic = defaultdict(int)

	w = msg.split(' ')
	w.sort()

	for i in w:
		
		dic[i] = dic[i] +1
		pass
	
	s = ""
	for j in dic:
		s = s + j + ";" + str(dic[j]) + " "
	print(s)
	flush()

elif m == "5":
	print("did not finish, thanks Windows...")
	flush()

