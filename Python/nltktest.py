from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def filtrarPalabras(tokens, stopwords):
    for x in tokens: 
        if x in stopwords: 
            tokens.remove(x)
    return tokens
    

plano = open(r'Cuento_Policial.txt','rb')
texto = plano.read().decode('utf-8')
tokens = [t for t in texto.split()]
sr = stopwords.words('spanish')
palabras_filtradas = filtrarPalabras(tokens, sr)
#Trabajar con palabras_filtradas, el resto ya está hecho 
#print(palabras_filtradas)
