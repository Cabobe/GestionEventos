from decouple import config
import requests

class GeoReferenciacion():

    #Georeferenciacion Inversa
    @classmethod
    def GeoRefInversa(self,latitud,longitud):
        try:
            url = config('GEOREF_URL_REVERSE')+"lat=" + latitud + "&lon="+longitud+"&format=json&zoom=18&key="+config('GEOREF_KEY')
            headers = {"accept": "application/json"}
            response = requests.get(url, headers=headers)
            return(response.json())

        except Exception as ex:
            raise Exception(ex)         

    #Georeferenciacion Sitios Cercanos
    @classmethod
    def GeoRefNearby(self,latitud,longitud):
        try:            
            url = config('GEOREF_URL_NEARBY')+"lat=" + latitud + "&lon="+longitud+"&limit=5&key="+config('GEOREF_KEY')
            headers = {"accept": "application/json"}
            response = requests.get(url, headers=headers)
            return(response.json())

        except Exception as ex:
            raise Exception(ex)   