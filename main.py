import random
elemente={

  #TODO: Elemente sollten über die Nummer im Dict sperrbar sein
  #TODO: Kombinationen erfragen und falls machbar in jeweiligem Tupel nachtragen:
  # Geht Bauch - halbe Sitz?
  # Geht Bauch - Ganze Stand?
  # Geht Bücke in den Sitz?
  # Wie viele Punkte gibt Sitz ganze Sitz? 0.2?
  
#INFO: Muffel zählt offiziell als Salto; Rücken vorwärtsrolle zählt auch als Salto oder Porpoise (Tümmler);


  #Elementname : (Schwierigkeit, Position vorher, Position nachher,Weirdheitsfaktor 0 (gewöhnlich)- 1 (ungewöhnlich) - 2 (schwer machbar/ sehr ungewohnt))

  #IN STAND
  "Stand":((0.1,"Rücken","Stand",0),(0.1,"Bauch","Stand",0),(0,"Sitz","Stand",0)),
  "Hocke":(0,"Stand","Stand",0),
  "Bücke":(0,"Stand","Stand",0),
  "Grätsche":(0,"Stand","Stand",0),
  "halbe Schraube":(0.1,"Stand","Stand",0),
  "halbe Hocke":(0.1,"Stand","Stand",1),
  "halbe Bücke":(0.1,"Stand","Stand",1),
  "halbe Grätsche":(0.1,"Stand","Stand",1),
  "ganze Schraube":(0.2,"Stand","Stand",0),
  "ganze Stand":((0.2,"Sitz","Stand",1),(0.3,"Rücken","Stand",1)),
  "Muffel":(0.3,"Rücken","Stand",0),
  "Salto vorwärts z. Stand":(0.6,"Rücken","Rücken",1),

  #IN SITZ
  "Sitz":((0,"Stand","Stand",0),(0,"Sitz","Sitz")),
  "halbe Sitz":((0.1,"Stand","Sitz",0),(0.1,"Sitz", "Sitz",0),(0.2,"Rücken","Sitz",1)),
  "ganze Sitz":((0.2,"Sitz","Sitz",0),(0.2,"Stand","Sitz",1)),
  "Hocke in den Sitz":(0,"Stand","Sitz",2),
  "Grätsche in den Sitz":(0,"Stand","Sitz",2),
  "Muffel in den Sitz":(0.3,"Rücken","Stand",0),
  
  #IN RÜCKEN
  "Rücken":((0.1,"Stand","Rücken",0),(0.1,"Sitz","Rücken",1),(0,"Rücken","Rücken",0),(0.2,"Bauch","Rücken",0)),
  "Halbe Rücken":((0.2,"Stand","Rücken",0),(0.3,"Rücken","Rücken",0),(0.2,"Sitz","Halbe Rücken",1)),
  "Salto vorwärts z. Rücken c":(0.5,"Rücken","Rücken"),
  "Muffel in den Rücken":(0.5,"Rücken","Stand",1),
  
  #IN BAUCH
  "Bauch":((0.1,"Stand","Bauch",0),(0.1,"Sitz","Bauch",0),(0,"Bauch","Bauch",0),(0.2,"Rücken","Bauch",1)),
  "halbe Heli":(0.1,"Bauch","Bauch",0),
  "Muffel in den Bauch":(0.2,"Rücken","Bauch",1)

}

ausStand=[]
ausSitz=[]
ausRücken=[]
ausBauch=[]

for element in elemente:
  varianten=elemente[element]
  for variante in varianten:
    startposition=variante[1]
    if startposition=="Stand":
      ausStand.append(variante)
    elif startposition=="Sitz":
      ausSitz.append(variante)
    elif startposition=="Rücken":
      ausRücken.append(variante)
    elif startposition=="Bauch":
      ausBauch.append(variante)

alteElementsammlung = {
  # Start-Position:[(Name des Sprungs,Ziel-Position)]
    "Stand": [
        ("Bauch","Bauch"), ("halbe Bauch","Bauch"), ("Sitz","Sitz"), ("halbe Sitz","Sitz"), ("Rücken","Rücken"), ("halbe Rücken","Rücken"),
        ("ganze Rücken","Rücken"), ("halbe Schraube","Stand"), ("ganze Schraube","Stand"), ("Grätsche","Stand"),
        ("Hocke","Stand"), ("Bücke", "Stand"),("halbe Grätsche","Stand"), ("halbe Hocke","Stand"),
        ("Hocke in den halben Sitz","Sitz")
    ],
    "Rücken": [
        ("Stand","Stand"), ("halbe Stand","Stand"), ("ganze Stand","Stand"), ("halbe Rücken","Rücken"), ("Bauch","Bauch"),
        ("halbe Bauch","Bauch"),("Sitz","Sitz"), ("halbe Sitz","Sitz"), ("Muffel","Stand"), ("Muffel in den Sitz","Sitz"),
        ("Muffel in den Bauch","Bauch"), ("Muffel in den Rücken","Rücken"),("Wende in den Bauch","Bauch")
    ],
    "Sitz": [
        ("Stand","Stand"), ("halbe Stand","Stand"), ("ganze Stand","Stand"), ("Sitz","Sitz"), ("Bauch", "Bauch"),("halbe Bauch","Bauch"),
        ("Rücken","Rücken"), ("halbe Rücken","Rücken")
    ],
    "Bauch": [("Stand","Stand"),("halbe Stand","Stand"),("Rücken","Rücken"),("halbe Heli","Bauch"),("Bauch","Bauch"),("Wende in den Rücken","Rücken")],
    
}

gesperrteElemente=[]
erlaubteWeirdheit=0
users={
  #Name: [gesperrte Elemente (List) ,weirde Sprünge (Int, 0 (keine) - 2 (alle))]
  "malte":[[13.2],1]
}


uebung = []
spruengeInUebung = 0
#currentuser=input("User?")
#if currentuser.lower() in users:
# print("Willkommen zurück,",currentuser)
# gesperrteElemente=users[currentuser][0]
# weirdheitsfaktor=users[currentuser][1]

while spruengeInUebung < 10:
	if spruengeInUebung == 0:
	  #Beginn im Stand
		erstesElement = ausStand[random.randrange(0, len(elemente))]
    weirdheitDesElements = erstesElement[3]
    while weirdheitDesElements>erlaubteWeirdheit:
      erstesElement = ausStand[random.randrange(0, len(elemente))]
      weirdheitDesElements = erstesElement[3]

		uebung.append(erstesElement)
	elif spruengeInUebung > 0:
		letztePosition=uebung[-1][1]
    if letztePosition=="Stand":
		  zufallselement= ausStand[letztePosition][random.randrange(0,len(elemente))]
    while weirdheitDesElements>erlaubteWeirdheit:

		uebung.append(zufallselement)
	spruengeInUebung += 1
print("\n\n")
for sprung in uebung:
  print (sprung[0])
