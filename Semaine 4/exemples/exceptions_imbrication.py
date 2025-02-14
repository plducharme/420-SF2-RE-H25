
try:
    print("Bloc try supérieur")
    try:
        print("Bloc try inférieur")
        raise ValueError
    except AttributeError:
        print("Bloc except inférieur")


except ValueError:
    print("Bloc except supérieur")
