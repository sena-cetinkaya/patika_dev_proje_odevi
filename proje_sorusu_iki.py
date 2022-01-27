from traceback import print_tb


#Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. 
# Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. 
# Örnek olarak:
# input: [[1, 2], [3, 4], [5, 6, 7]]
# output: [[[7, 6, 5], [4, 3], [2, 1]]

liste = [[1, 2], [3, 4], [5, 6, 7]]
liste.reverse() 
for l in liste:
    l.reverse() 

print(liste)