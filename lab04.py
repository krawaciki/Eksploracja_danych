from math import sqrt
import numpy

users = {
        "Ania": 
            {"Blues Traveler": 1.,
            "Broken Bells": 1.5,
            "Norah Jones": 2,
            "Deadmau5": 2.5,
            "Phoenix": 3.0,
            "Slightly Stoopid": .5,
            "The Strokes": 0.0,
            "Vampire Weekend": 2.0},
         "Bonia":
            {"Blues Traveler": 4.0,
            "Broken Bells": 4.5, 
            "Norah Jones": 5.0,
            "Deadmau5": 5.5, 
            "Phoenix": 6.0, 
            "Slightly Stoopid": 3.5, 
            "The Strokes": 2.0,
            "Vampire Weekend": 5.0}
        }

def wspKorelacji(osoba1, osoba2, slownik):
    os1 = slownik[osoba1]
    os2 = slownik[osoba2]
    sumxy = 0
    sumx = 0
    sumy = 0
    sumx2 = 0
    sumy2 = 0
    i = 0
    for j in os1:
        for k in os2:
            if j==k:
                sumxy = sumxy+os1[j]*os2[j]
                sumx = sumx+os1[j]
                sumy = sumy+os2[j]
                sumx2 = sumx2+os1[j]**2
                sumy2 = sumy2+os2[j]**2
                i+=1
    return (sumxy-(sumx*sumy)/i)/(sqrt(sumx2-(sumx**2)/i)*sqrt(sumy2-(sumy**2)/i))          
    

def pearsonNumpy(osoba1, osoba2):
    osoba1=osoba1.values()
    osoba2=osoba2.values()
    return numpy.corrcoef(osoba1, osoba2)

print(wspKorelacji('Ania','Bonia',users))
print(str(pearsonNumpy(users['Ania'],users['Bonia'])[0,1]))
