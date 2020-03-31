import requests
import time
        
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
        
        ticks = time.asctime( time.localtime(time.time()) )
        
        print(" ")
        print("-------------------------------------")
        print("     Info Update Corona Covid-19     ")
        print("-------------------------------------")
        print("Waktu saat ini:", ticks)
        print(" ")   
        
        
        print("Negara           : ", data[0]['name'])
        print("Jumlah Positif   : ", data[0]['positif'])
        print("Jumlah Sembuh    : ", data[0]['sembuh'])
        print("Jumlah Meninggal : ", data[0]['meninggal'])
        
        print(" ")

        tanya = input("Ulang Perhitungan atau tidak (y/n) : ")
        if (tanya == 'n'):
            break

print(" ")
print("Terima kasih sudah menggunakan aplikasi ini :)")
