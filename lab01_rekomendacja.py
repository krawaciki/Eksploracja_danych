#  Wzorowane na przyk艂adzie Rona Zacharskiego
#

from math import sqrt

users = {"Ania": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bonia":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Celina": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dominika": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Ela": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Fruzia":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Gosia": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Hela": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }



def manhattan(rating1, rating2):
    """Oblicz odleg艂o艣膰 w metryce taks贸wkowej mi臋dzy dwoma  zbiorami ocen
       danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
       Zwr贸膰 -1, gdy zbiory nie maj膮 wsp贸lnych element贸w"""
  # TODO: wpisz kod
    klucze1 = rating1.keys()
    klucze2 = rating2.keys()
    odleglosc = 0
    udaloSiePorownac = False
    
    for klucz in klucze1 :
        if klucz in rating2.keys():
            udaloSiePorownac = True
            odleglosc = odleglosc + abs(rating2[klucz] - rating1[klucz]) #dla ka縟ego klucza z rating1 bie縠my z rating2

    if udaloSiePorownac: #lub (udalosSiePorownac==True)
        return odleglosc
    else:
        return -1

def testManhattan(rating1, rating2, odleglosc):
    if manhattan(rating1, rating2) == odleglosc:
        return True
    else:
        return False

##print (testManhattan({'硓y':5, 'TL':3},
##                     {'硓y':10},
##                     5)
##       )
##
##print (testManhattan({'硓y':5, 'TL':3},
##                     {'BS':10},
##                     -1)
##       )
##    
##odlegloscOdAniDoHeli = manhattan(users["Ania"], users["Hela"])
##print ("od Ani do Heli jest %f" % odlegloscOdAniDoHeli) #lub po przecinku

def obliczNajblizszegoSasiada(imie, uzytkownicy):
    """dla danego u偶ytkownika, zwr贸膰 list臋 innych u偶ytkownik贸w wed艂ug blisko艣ci preferencji"""
    odleglosci = []
    for imie2 in uzytkownicy:
        odleglosc = 0
        if imie!=imie2:
            odleglosc = manhattan(uzytkownicy[imie], uzytkownicy[imie2])
            odleglosci.append((odleglosc, imie2))
    return sorted(odleglosci)

##print(obliczNajblizszegoSasiada('Hela',users))

def recommend(username, users):
    """Zwr贸膰 list臋 rekomendacji dla u偶ytkownika"""
    # znajd藕 preferencje najbli偶szego s膮siada
    nearestName = obliczNajblizszegoSasiada(username, users)[0][1]
    print 'Najbli縮zy s箂iad to: %s' %nearestName
    recommendations = []
    ratingOfNearest = users[nearestName]
    print 'jego rekomendacje to: '
    print ratingOfNearest
    # zarekomenduj u偶ytkownikowi wykonawc臋, kt贸rego jeszcze nie oceni艂, a zrobi艂 to jego najbli偶szy s膮siada
    userRating = users[username]
    
    for artist in ratingOfNearest:
        if not artist in userRating:
            recommendations.append((artist, ratingOfNearest[artist]))
    # using the fn sorted for variety - sort is more efficient
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)

##recommend('Hela', users)
###print( recommend('Celina', users))

##lista = [[0, 1, 2], [10, 4], 'Ziutek']
##print lista[1:]
##print lista[1][1]
