import nltk
import spacy
from nltk.stem.snowball import SnowballStemmer


# Baixar o modelo em espanhol para spaCy
nlp = spacy.load("es_core_news_sm")

# Configurar stemmer para espanhol
stemmer = SnowballStemmer("spanish")

# Frases de exemplo
texto1 = "Los niños jugaban en el parque con sus amigos."
texto2 = "El niño juega en el parque con su amigo."

# Tokenização
tokens1 = nltk.word_tokenize(texto1, language='spanish')
tokens2 = nltk.word_tokenize(texto2, language='spanish')

# Aplicando Stemming
stems1 = [stemmer.stem(palavra) for palavra in tokens1]
stems2 = [stemmer.stem(palavra) for palavra in tokens2]

# Aplicando Lematização
doc1 = nlp(texto1)
doc2 = nlp(texto2)
lemmas1 = [token.lemma_ for token in doc1]
lemmas2 = [token.lemma_ for token in doc2]

# Ordenação dos resultados
stems1_sorted = sorted(set(stems1))
stems2_sorted = sorted(set(stems2))
lemmas1_sorted = sorted(set(lemmas1))
lemmas2_sorted = sorted(set(lemmas2))

# Exibir os resultados
print("Stemming do Texto 1:", stems1_sorted)
print("Stemming do Texto 2:", stems2_sorted)
print("Lematização do Texto 1:", lemmas1_sorted)
print("Lematização do Texto 2:", lemmas2_sorted)

# Comparação: mesmos resultados para textos diferentes
print("Resultado idêntico em Stemming?", stems1_sorted == stems2_sorted)
print("Resultado idêntico em Lematização?", lemmas1_sorted == lemmas2_sorted)
