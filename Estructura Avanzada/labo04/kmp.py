# Python program for KMP Algorithm
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    lps = [0]*M
    j = 0 # index for pat[]
    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)
    i = 0 # index for txt[]
    #Hace la busqueda
    while i < N:
        #si el caracter es igual en ambos strings sigue y revisa el siguiente
        if pat[j] == txt[i]:
            i += 1
            j += 1
        # llego hasta el final del patron sin haber tenido un mismatch
        if j == M:
            # print("Found pattern at index " + str(i-j))
            j = lps[j-1] # indica cuando debe retroceder en pat para antes de seguir verificando
        # ocurre un mismatch antes que termine de verificar el patron
        elif i < N and pat[j] != txt[i]:
            # si el mismatch ocurrio durante una secuencia de aciertos
            if j != 0:
                j = lps[j-1]
            #si el primer caracter no hizo match, se revisa el segundo
            else:
                i += 1
 
def computeLPSArray(pat, M, lps):
    len = 0 
    lps[0]
    i = 1
    while i < M:
        #compara un lps[i+1] con un lps[i] para ver 
        if pat[i]==pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1
 
# pattern = "bla"
# string = "blablablabla"
# KMPSearch(pattern, string)