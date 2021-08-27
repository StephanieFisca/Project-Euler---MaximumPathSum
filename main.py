#Project Euler- Maximum path sum

#Stocarea triunghiului intr-o lista de vectori (matrice)
triunghi = [[75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20, 4, 82, 47, 65],
            [19, 1, 23, 75, 3, 34],
            [88, 2, 77, 73, 7, 63, 67],
            [99, 65, 4, 28, 6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

#Functie care returneaza valoarea maxima din triunghi
def maxsum(values):
	#Parcurgem elementele triunghiului de jos in sus pentru a putea obtine suma maxima perfecta (de sus in jos ar fi ineficient, si ar putea genera o "suma maxima" gresita)
	#Parcurgem triunghiul incepand cu len(values)-2 deoarece vom incepe prin compararea elementelor de pe linia 13(penultima) cu linia 14(ultima) si tot asa in ordine descrescatoare pana la prima linie.
    for i in range(len(values)-2, -1, -1):
		#Parcurgem elementele de pe fiecare coloana a liniei i.
        for j in range(0, i+1):
			#Elementele liniei i vor fi inlocuite prin calcularea sumei intre valoarea curenta de pe pozitia respectiva (values[i][j]) si maximul determinat dintre elementele pe urmatoarea linie pe aceeasi coloana si coloana superioara (values[i+1][j] si values[i+1][j+1]).
            values[i][j] += max(values[i + 1][j], values[i + 1][j + 1])
	#Returnam primul element al listei care va reprezenta suma maxima
    return triunghi[0][0]


#Afisarea sumei maxime
print('Suma maxima este: '+str(maxsum(triunghi)))
