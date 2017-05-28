import pandas
import simplekml
import tkinter
from tkinter.filedialog import askopenfilename

global file_path

# methods
def browse():
    global in_file
    in_file = askopenfilename()

def kmlFunction():
    df = pandas.read_csv(in_file)
    kml = simplekml.Kml()
    
    for lon, lat in zip(df["Longitude"], df["Latitude"]):
        kml.newpoint(coords = [(lon, lat)])
       
    file_path = "C:\\Andre\\Work\\Python\\Files\\points.kml"
    kml.save(file_path)

# program
root = tkinter.Tk()
root.title("KML Generator")

label = tkinter.Label(root, text = "This program generates a KML file")
label.pack()

browse_button = tkinter.Button(root, text = "Browse", command = browse)
browse_button.pack()

kml_button = tkinter.Button(root, text = "Generate KML", command = kmlFunction)
kml_button.pack()

root.mainloop()