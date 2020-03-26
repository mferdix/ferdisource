print(" ")
print("----------------------------------------------------------------------")
print("                   Created by Muhamad Ferdiansyah - 2020              ")
print("----------------------------------------------------------------------")
print(" Analisis Pertumbuhan Kasus Covid-19 Indonesia by Jalan Gedong Coding ")
print("----------------------------------------------------------------------")

ulang = 1

while(ulang > 0) :
        print(" ")
        print("----------------")
        print("Waiting Dlu Gays")
        print("----------------")
        print(" ")
        # Import Packages
        import pandas as pd
        import requests
        from bs4 import BeautifulSoup
        # Get the data in raw format
        # res = requests.get("http://www.nationmaster.com/country-info/stats/Media/Internet-users")
        res = requests.get("https://www.worldometers.info/coronavirus/")
        # Parse HTML
        soup = BeautifulSoup(res.content,'html.parser')
        # Find <table> tags in HTML, store them in a list
        # Get the first tag in the list (index 0)
        table = soup.find_all('table')[0]
        # It produces a list contains a dataframe
        df = pd.read_html(str(table))[0]
        index = df.index[df['Country,Other'] == 'Indonesia'].tolist()
        Country = df.loc[(df['Country,Other'] == 'Indonesia'), ['Country,Other']]
        TC = df.loc[(df['Country,Other'] == 'Indonesia'), ['TotalCases']].fillna(0)
        NC = df.loc[(df['Country,Other'] == 'Indonesia'), ['NewCases']].fillna(0)
        TD = df.loc[(df['Country,Other'] == 'Indonesia'), ['TotalDeaths']].fillna(0)
        ND = df.loc[(df['Country,Other'] == 'Indonesia'), ['NewDeaths']].fillna(0)
        TR = df.loc[(df['Country,Other'] == 'Indonesia'), ['TotalRecovered']].fillna(0)
        AC = df.loc[(df['Country,Other'] == 'Indonesia'), ['ActiveCases']].fillna(0)
        SC = df.loc[(df['Country,Other'] == 'Indonesia'), ['Serious,Critical']].fillna(0)
        import time
        ticks = time.asctime( time.localtime(time.time()) )
        print(" ")
        print("-------------------------------------")
        print("Info Update Corona Covid-19")
        print("       Notes : Abaikan angka ",index )
        print("-------------------------------------")
        print("Waktu saat ini:", ticks)
        print(" ")   
        print("Indonesia saat ini berada di Urutan", index)
        print(TC)
        print(NC)
        print(TD)
        print(ND)
        print(TR)
        print(AC)
        print(SC)
        tanya = raw_input("Ulang Perhitungan atau tidak (y/n) : ")
        if (tanya == 'n'):
            break

print(" ")
print("Terima kasih sudah menggunakan aplikasi ini :)")
