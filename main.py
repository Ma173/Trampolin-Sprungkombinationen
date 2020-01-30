import random

elemente = {
    "Stand": [
        "Bauch", "halbe Bauch", "Sitz", "halbe Sitz", "Rücken", "halbe Rücken",
        "ganze Rücken", "halbe Schraube", "ganze Schraube", "Grätsche",
        "Hocke", "Bücke", "halbe Grätsche", "halbe Hocke",
        "Hocke in den halben Sitz"
    ],
    "Rücken": [
        "Stand", "habe Stand", "ganze Stand", "halbe Rücken", "Bauch",
        "halbe Bauch", "Sitz", "halbe Sitz", "Muffel", "Muffel in den Sitz",
        "Muffel in den Bauch", "Muffel in den Rücken","Wende in den Bauch"
    ],
    "Sitz": [
        "Stand", "halbe Stand", "ganze Stand", "Sitz", "Bauch", "halbe Bauch",
        "Rücken", "halbe Rücken"
    ],
    "Bauch": ["Stand","halbe Stand","Rücken","halbe Heli","Bauch","Wende in den Rücken"],
    ""
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
