# Elektrothnički fakultet, Univerzitet u Sarajevu
# Predmet: Optimizacija resursa, 2020/2021

Implementirano je rješenje problema trgovačkog putnika koristeći tabu pretraživanje.

Na početku je potrebno pronaći početnu tačku pretraživanja za koju je korišten pohlepni algoritam. Ideja pohlepnog algoritma jeste da kreće od početnog čvora grafa (konkretno u implementaciji čvor 0) te prelazi u njegov susjedni čvor koji prvi pronađe. Dalju pretragu nastavlja od tog susjednog čvora, te ponavlja isti postupak sve dok ne posjeti sve  čvorove grafa. Na taj način formira putanju koja nije optimalna ali je prva pronađena, što i jeste rezultat svakog pohlepnog algoritma.
Ideja tabu pretraživanja za ovaj problem jeste da ima neku trenutno posmatranu tačku koja predstavlja trenutno rješenje, te da formira okolinu te tačke i za svaku tačku iz okoline provjerava da li je dozvoljena. Formiranje okoline tačke se zasniva na kreiranju svih permutacija čvorova koji predstavljaju trenutno rješenje. Tačka je dozvoljena ako se ne  nalazi u tabu listi i ako postoji grana u grafu između svih čvorova te tačke, tako da se može formirati put. Za svaku tačku se računa udaljenost, tj. put koji je potrebno preći, te ako je dobijena udaljenost bolja od trenutne najbolje udaljenosti, ta tačka postaje najbolja i algoritam se nastavlja izvršavati za tu tačku. U slučaju da nema bolje tačke u okolini, kako bi se izbjegla stagnacija algoritma ideja je da se u okolini pronađe tačka koja daje najmanju udaljenost od svih.

Rješenje je testirano na primjeru 3 grafa.
