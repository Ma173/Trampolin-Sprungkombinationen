import random

elemente = {
    "Stand": [
        ("Bauch","Bauch", ("halbe Bauch","Bauch"), ("Sitz","Sitz"), ("halbe Sitz","Sitz"), ("Rücken","Rücken"), ("halbe Rücken":"Rücken"),
        ("ganze Rücken","Rücken"), ("halbe Schraube","Stand"), ("ganze Schraube":"Stand"), ("Grätsche","Stand")
        ("Hocke","Stand"), ("Bücke", "Stand"),("halbe Grätsche","Stand"), ("halbe Hocke","Stand)",
        ("Hocke in den halben Sitz","Sitz")
    ],
    "Rücken": [
        ("Stand","Stand", ("habe Stand","Stand"), ("ganze Stand","Stand"), ("halbe Rücken","Rücken"), ("Bauch","Bauch"),
        ("halbe Bauch","Bauch"),("Sitz","Sitz"), ("halbe Sitz","Sitz"), ("Muffel","Stand"), ("Muffel in den Sitz","Sitz"),
        ("Muffel in den Bauch","Bauch"), ("Muffel in den Rücken","Rücken"),("Wende in den Bauch","Bauch")
    ],
    "Sitz": [
        ("Stand","Stand"), ("halbe Stand","Stand"), ("ganze Stand","Stand"), ("Sitz","Sitz"), ("Bauch", "Bauch"),("halbe Bauch","Bauch"),
        ("Rücken","Rücken", ("halbe Rücken","Rücken")
    ],
    "Bauch": [("Stand","Stand"),("halbe Stand","Stand"),("Rücken","Rücken"),("halbe Heli","Bauch"),("Bauch","Bauch"),("Wende in den Rücken","Rücken"],
    
}

uebung = []
spruengeInUebung = 0
while spruengeInUebung < 10:
	if spruengeInUebung == 0:
	  #Beginn im Stand
		erstesElement = elemente["Stand"][random.randrange(0, len(elemente))]
		uebung.append(erstesElement)
	elif spruengeInUebung > 0:
		letztesElement=uebung[-1]
		erlaubtesElement="nein"
		while erlaubtesElement=="nein":
		  zufallselement= list(elemente.keys())[random.randrange(0,len(elemente))]
		  if letztesElement in elemente[zufallselement]:
		    erlaubtesElement="ja"
		uebung.append(zufallselement)
	spruengeInUebung += 1
print("\n\n")
for sprung in uebung:
  print (sprung)
