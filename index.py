from covid import Covid
from datetime import datetime as dt

def worldwide():
    totalcase = Covid().get_total_confirmed_cases()
    totalactive = Covid().get_total_active_cases()
    totaldeath = Covid().get_total_deaths()
    recovered = Covid().get_total_recovered()
    print("-------------------World-Wide---------------")
    print("Total case:   " + str(totalcase))
    print("Total Active cases: " + str(totalactive))
    print("Total Deaths:  "+ str(totaldeath))
    print("total recovered: "+str(recovered))
    print("-----------Country-Wise--------------------")
def countrywise(i_country):
    country_cases = Covid().get_status_by_country_name(i_country)
    totalcase=country_cases['confirmed']
    deaths=country_cases['deaths']
    totalactivecases=country_cases['active']
    update= country_cases['last_update']
    date_updated=dt.fromtimestamp(update/1000)
    print("\n"+i_country)
    print("Total cases: "+str(totalcase))
    print("total Active cases:  "+str(totalactivecases))
    print("Total deaths:  "+str(deaths))
    print("time:   "+ str(date_updated))
    print("-----------------Thank You---------------")
if __name__== '__main__':
    worldwide()
    country= input("Enter Country Name:  ")
    countrywise(country)
