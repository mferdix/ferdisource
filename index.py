print(" ")
print("----------------------------------------------------------------------")
print("                   Created by Muhamad Ferdiansyah - 2020              ")
print("----------------------------------------------------------------------")
print(" Analisis Pertumbuhan Kasus Covid-19 Indonesia by Jalan Gedong Coding ")
print("----------------------------------------------------------------------")
print("                               Version 2                              ")
print("----------------------------------------------------------------------")

ulang = 1

while(ulang > 0) :
        print(" ")
        print("----------------")
        print("Waiting Dlu Gays")
        print("----------------")
        print(" ")
        
        res = requests.get('https://api.kawalcorona.com/indonesia')
        data = res.json()
        
        
        print("==============================================================")
        print("||      Negara     ||   Positif   ||  Sembuh  || Meninggal ||")
        print("==============================================================")
        print("||   ", data[0]['name'],"   ||   ", data[0]['positif'],"   ||   ", data[0]['sembuh'],"   ||   ", data[0]['meninggal'], "   ||")
        print("==============================================================")

        tanya = input("Ulang Perhitungan atau tidak (y/n) : ")
        if (tanya == 'n'):
            break

print(" ")
print("Terima kasih sudah menggunakan aplikasi ini :)")
