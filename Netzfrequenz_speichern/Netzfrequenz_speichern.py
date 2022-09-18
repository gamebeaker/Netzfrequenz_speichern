from keep_alive import keep_alive
import urllib.request, json, time, os


def write_data(AntwortArray):
    DateiPfad = "./Daten/"+str(time.time())[:4]+".csv"
    try:
        Datei = open(DateiPfad,"a")
    except:
        print("Datei konnte nicht geoeffnet werden: "+time.localtime())
        time.sleep(1)
    try:
        Datei.write(str(AntwortArray[0])+";"+str(AntwortArray[1])+"\n")
    except:
        print("Daten konnten nicht geschrieben werden: "+time.localtime())
        time.sleep(1)
    try:
        Datei.close()
    except:
        print("Dateei konnten nicht geschlossen werden: "+time.localtime())
        time.sleep(1)

def get_data_from_url():
    UrlAntwort = None
    while UrlAntwort is None:
        try: 
            UrlAntwort = urllib.request.urlopen("https://www.netzfrequenz.info/json/aktuell2.json")
        except:
            print("url fehler um "+time.strftime("%Y%m%d%H", time.localtime()))
            time.sleep(10)
    AntwortArray = json.loads(UrlAntwort.read())
    UrlAntwort.close()
    return AntwortArray


keep_alive()
os.makedirs(os.path.dirname("./Daten/"), exist_ok=True)
while True:
    time.sleep(0.5)
    write_data(get_data_from_url())


