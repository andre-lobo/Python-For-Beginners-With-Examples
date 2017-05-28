import simplekml
import pandas

file_path = "C:\\Andre\\Work\\Python\\Files\\points.kml"
csv_path = "C:\\Andre\\Work\\Python\\Files\\coords_csv.csv"

df = pandas.read_csv(csv_path)
kml = simplekml.Kml()

for lon, lat in zip(df["Longitude"], df["Latitude"]):
	kml.newpoint(coords = [(lon, lat)])

kml.save(file_path)

