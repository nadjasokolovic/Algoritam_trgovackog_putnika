#Tabu pretrazivanje za rjesavanje problema trgovacog putnika

def izracunajUdaljenost(graf, cvorovi):
    udaljenost = 0
    i = 0
    while i < (len(cvorovi) - 1):
        j = i + 1
        udaljenost += graf[cvorovi[i]][cvorovi[j]] 
        i += 1
        
    return udaljenost

#pohlepni algoritam koji kada pronadje prvi cvor u koji moze da predje to i radi
#ne gleda kolika je putanja
def greedyTSP(graf):
    #formiramo pocetno rjesenje, tj. pocetnu permutaciju
    pocetnaPermutacija = [0] #na pocetku dodajemo nulu jer krecemo od nultog cvora
    ukupnaUdaljenost = 0 #varijabla u kojoj cuvamo ukupnu duzinu puta pri obilasku svih cvorova
    for i in range(len(graf)):
        j = 1
        presloUDrugiRed = False
        while(j < len(graf[i])):
            #ako postoji grana izmedju i-tog i j-tog cvora i ako pocetnaPermutacija ne sadrzi j-ti cvor
            if graf[i][j] != 0 and j not in pocetnaPermutacija:
                pocetnaPermutacija.append(j) #dodajemo j-ti cvor u rjesenje
                ukupnaUdaljenost += graf[i][j]
                i = j #dalje pretrazujemo j-ti red
                presloUDrugiRed = True
                break
            j += 1
        if presloUDrugiRed:
            i -= 1

    ukupnaUdaljenost += graf[pocetnaPermutacija[len(pocetnaPermutacija) - 1]][0]
    pocetnaPermutacija.append(0)
    
    return pocetnaPermutacija, ukupnaUdaljenost  

    
def formirajOkolinuTacke(najboljeRjesenje):
    okolneTacke = []
    j = 0
    while j < (len(najboljeRjesenje) - 2):
        k = j + 1
        while k < len(najboljeRjesenje) - 1:
            najboljeRjesenjeTmp = najboljeRjesenje.copy()
            
            #vrsimo izmjenu odgovarajucih elemenata
            tmp = najboljeRjesenjeTmp[j]
            najboljeRjesenjeTmp[j] = najboljeRjesenjeTmp[k]
            najboljeRjesenjeTmp[k] = tmp

            okolneTacke.append(najboljeRjesenjeTmp)
            k += 1
        j += 1

    for i in range(len(okolneTacke)):
        okolneTacke[i][len(okolneTacke[i])-1] = okolneTacke[i][0]

    return okolneTacke

def postojiGrana(graf, cvorovi):
    postoji = True
    i = 0
    while i < (len(cvorovi) - 1):
        j = i + 1
        if graf[cvorovi[i]][cvorovi[j]] == 0:
            postoji = False
            break
        i += 1

    return postoji

def TS(graf, N, L):
    tabuLista = []
    #formiramo pocetno rjesenje, tj. pocetnu permutaciju
    tmp = greedyTSP(graf)
    pocetnaPermutacija = tmp[0].copy()
    #print(pocetnaPermutacija)
    pocetnaUdaljenost = tmp[1]
    #print(pocetnaUdaljenost)
    
    #na pocetku smatramo da je najbolje rjesenje pocetno
    najboljeRjesenje = pocetnaPermutacija.copy()
    najboljaUdaljenost = pocetnaUdaljenost

    trenutnoRjesenje = najboljeRjesenje.copy()
    trenutnaUdaljenost = najboljaUdaljenost
        
    #u svrhu boljih performansi programa pocetnu tacku dodajemo u tabu listu
    tabuLista.append(pocetnaPermutacija)
    
    for i in range(0, N):
        #formiramo okolinu tacke
        okolneTacke = formirajOkolinuTacke(trenutnoRjesenje).copy()
        #provjeravamo da li postoji neka tacka iz okoline koja daje bolju udaljenost
        postojiBolja = False
        for j in range(len(okolneTacke)):
            #provjeravamo da li postoji neka dozvoljena tacka
            #tacka je dozvoljena ako se ne nalazi u tabu listi
            #i ako izmedju svakog cvora postoji grana u grafu
            if okolneTacke[j] not in tabuLista and postojiGrana(graf, okolneTacke[j]):
                #treba naci kolika je udaljenost 
                udaljenost = izracunajUdaljenost(graf, okolneTacke[j].copy())
                if (udaljenost < trenutnaUdaljenost):
                    postojiBolja = True
                    trenutnaUdaljenost = udaljenost
                    trenutnoRjesenje = okolneTacke[j].copy()
        
        # ako ne postoji nijedna dozvoljena tacka
        #pronalazimo najbolju tacku iz okoline u koju je moguce preci, ne mora biti bolja od trenutne
        if not postojiBolja:
            minUdaljenost = izracunajUdaljenost(graf, okolneTacke[0])
            indeksMin = 0
            for j in range(len(okolneTacke)):
                if izracunajUdaljenost(graf, okolneTacke[j]) < minUdaljenost:
                    minUdaljenost = izracunajUdaljenost(graf, okolneTacke[j])
                    indeksMin = j
            
            trenutnoRjesenje = okolneTacke[indeksMin]
            trenutnaUdaljenost = izracunajUdaljenost(graf, okolneTacke[indeksMin])
                           
        if trenutnaUdaljenost < najboljaUdaljenost:
            najboljaUdaljenost = trenutnaUdaljenost
            najboljeRjesenje = trenutnoRjesenje.copy()
        
        #azuriranje tabu liste
        if (tabuLista.count(najboljeRjesenje) == 0):
            tabuLista.append(najboljeRjesenje)
            azurirajTabuListu(tabuLista, L)
            
    return najboljeRjesenje, najboljaUdaljenost  
    
                
def azurirajTabuListu(tabuLista, L):
    #ako je tabu lista popunjena izbacamo jedan element
    if len(tabuLista) > L: 
        tabuLista.pop(0)
        
#Definisanje grafova za testiranje algorima
W1 = [[0,3,3,8,6],
      [3,0,7,2,8],
      [3,7,0,5,2],
      [8,2,5,0,1],
      [6,8,2,1,0]]
# opt = 11

W2 = [[0,2,2,2,7,5,2],
      [2,0,4,7,9,1,3],
      [2,4,0,3,6,6,5],
      [2,7,3,0,4,9,6],
      [7,9,6,4,0,4,9],
      [5,1,6,9,4,0,2],
      [2,3,5,6,9,2,0]]
# opt = 19

W3 = [[ 0,28, 7,15, 9,24, 8,30,29,16],
      [28, 0,28, 7,12,14, 2,26,19, 0],
      [ 7,28, 0,15,20, 1,19, 0, 3,17],
      [15, 7,15, 0,19,30, 6,17, 0,13],
      [ 9,12,20,19, 0,11,30,18, 0, 2],
      [24,14, 1,30,11, 0, 1,29,29,13],
      [ 8, 2,19, 6,30, 1, 0,25,30,22],
      [30,26, 0,17,18,29,25, 0, 6,26],
      [29,19, 3, 0, 0,29,30, 6, 0,29],
      [16, 0,17,13, 2,13,22,26,29, 0]]
# opt = 34

prviGraf = TS(W1, 100, 100)
print("Rješenje problema trgovackog putnika za W1: ")
print(prviGraf[0])
print("Ukupna udaljenost iznosi: ", prviGraf[1])

drugiGraf = TS(W2, 100, 100)
print("Rješenje problema trgovackog putnika za W2: ")
print(drugiGraf[0])
print("Ukupna udaljenost iznosi: ", drugiGraf[1])

treciGraf = TS(W3, 100, 100)
print("Rješenje problema trgovackog putnika za W3: ")
print(treciGraf[0])
print("Ukupna udaljenost iznosi: ", treciGraf[1])        

