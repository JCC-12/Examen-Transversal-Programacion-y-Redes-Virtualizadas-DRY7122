while True:
    AS = input ("\nIndique el número de AS o escriba 'salir' para terminar: ")
    if AS == 'salir': 
        break
    bgpNum = int(AS)
    if (bgpNum >= 64512 and bgpNum <= 65534) or (bgpNum >= 4200000000 and bgpNum <= 4294967294):
        print ("El AS indicado corresponde a un AS privado.")
    elif (bgpNum >=1 and bgpNum <= 64495) or (bgpNum >= 131072 and bgpNum <= 4199999999):
        print("El AS indicado corresponde a un AS público")
    else: 
        print("El número de AS indicado no es válido.")
