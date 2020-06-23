import requests
def get_tasa(year,month,key, monto,plazo):

    response=requests.get('https://api.sbif.cl/api-sbifv3/recursos_api/tmc/' + str(year) + '/' + str(month) + '?apikey=' + key + '&formato=json').json()
    print (str(year) +  " " +  str(month) + " " + str(key) + " " + str(monto) + " " + str(plazo)) 
    tasa=getValor(response,monto,plazo) 
    return tasa
def getValor(response,monto,plazo):
    monto=float(monto)
    if 'TMCs' in response:
        for i in response['TMCs']:
            print(i['Tipo'] +" " + str(monto) + " " + str(plazo) )
            if monto <= 5000.0 and plazo <= 90 and plazo < 365 and i['Tipo'] == '26':
                return i['Valor']
            if monto >5000.0 and plazo <= 90 and plazo < 365 and i['Tipo'] == '25':
                return i['Valor']
            if monto <=50.0 and plazo >= 90 and plazo < 365 and i['Tipo'] == '45':
                return i['Valor']
            if monto <=200.9 and monto>50.0 and plazo < 365 and plazo >= 90 and i['Tipo'] == '44':
                return i['Valor']
            if monto <=5000.0 and monto>200.0 and plazo < 365 and plazo >= 90 and i['Tipo'] == '35':
                return i['Valor']
            if monto <=2000.0 and plazo >= 365  and i['Tipo'] == '24':               
                return i['Valor']
            if monto > 2000.0 and plazo >= 365  and i['Tipo'] == '22':               
                return i['Valor']
        return 'Sin tasa'
                            
                
        