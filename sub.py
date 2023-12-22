from medlist import GI_LIST, MGI_LIST
from random import sample

def selfinput():
	allmech = set()
	allindi = set()
	alladr = set()
	allmed = set()
	mednum = input("how many med? : ")
	uncomplete = True
	while uncomplete:
		med = input("med input : ")
		if med in GI_LIST.keys():
			allmech.update([GI_LIST[med][0]])
			allindi.update(GI_LIST[med][1])
			alladr.update(GI_LIST[med][2])
			allmed.add(med)
			
			print(f"card number : {len(allmech) + len(allindi) + len(alladr)}      mednum : {len(allmed)}/{mednum}")
			if len(allmed) == int(mednum):
				save = input("save? : ")
				if save == "y":
					uncomplete = not uncomplete
					savet = f"card number : {len(allmech) + len(allindi) + len(alladr)}      mednum : {len(allmed)}/{mednum}\n\n" + f'medicine {len(allmed)}:\n' + str(allmed) + f'\n\nmechanism {len(allmech)}:\n' + str(allmech) + f'\n\nindication {len(allindi)}:\n' + str(allindi) + f'\n\nadr {len(alladr)}:\n' + str(alladr)
					filename = input("save file name : ") + '.txt'

					with open(filename,'w') as f:
					   f.write(savet)

				else:
					print(f"\nmedicine {len(allmed)} : \n", allmed)
					print(f"\n\nmechanism {len(allmech)} : \n", allmech)
					print(f"\n\nindication {len(allindi)} : \n", allindi)
					print(f"\n\nadr {len(alladr)} : \n", alladr)
	
					allmech = set()
					allindi = set()
					alladr = set()
					allmed = set()
					mednum = input("how many med? : ")
		elif med == "exit":
			uncomplete = not uncomplete
		else:
			print(f"{med} not in list")

def autorandom():
	mednum = input("how many med? : ")
	allmech = set()
	allindi = set()
	alladr = set()
	allmed = sample(list(MGI_LIST.keys()), k=int(mednum))
	for med in allmed:
		allmech.update([MGI_LIST[med][0]])
		allindi.update(MGI_LIST[med][1])
		alladr.update(MGI_LIST[med][2])
	print(f"card number : {len(allmech) + len(allindi) + len(alladr)}      mednum : {len(allmed)}/{mednum}")
	print(f"\nmedicine {len(allmed)} : \n", allmed)
	print(f"\n\nmechanism {len(allmech)} : \n", allmech)
	print(f"\n\nindication {len(allindi)} : \n", allindi)
	print(f"\n\nadr {len(alladr)} : \n", alladr)

while True:
	func = input("auto/self : ")
	if func == "a":
		autorandom()
	elif func == 's':
		selfinput()
	elif func == 'exit':
		break
