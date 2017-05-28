#this kml file open in Google Earth
import simplekml

file_path = "C:\\Andre\\points.kml"

kml = simplekml.Kml()

print(kml.newpoint(name = "Sample", coords=[(10, 10)]))
print(kml.newpoint(name = "Sample", coords=[(15, 15)]))

kml.save(file_path)