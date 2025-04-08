# ouverture d'un fichier en mode lecture brute, sans mémoire tampon
with open('text.txt', 'rb', buffering=0) as raw_reader:
    print(type(raw_reader))
    c =  raw_reader.read(1)
    print(c)
    while c:
        c = raw_reader.read(1)
        print(c)

