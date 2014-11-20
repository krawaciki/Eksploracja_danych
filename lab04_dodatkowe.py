import numpy
import arcpy

sciezka = "D:/bdo/powiaty.shp"
powierzchnia = []
ludnosc = []

rows = arcpy.SearchCursor(sciezka) 

fields = arcpy.ListFields(sciezka, "", "String")

for row in rows:
    for field in fields:
            powierzchnia.append(row.getValue("POLE_KM2"))
            ludnosc.append(row.getValue("POP"))
print(numpy.corrcoef(powierzchnia, ludnosc))[0,1]
