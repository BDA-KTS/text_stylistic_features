from lexicalrichness import LexicalRichness

#Returns the list of UNIQUE Words present in a text.
def get_tokens(text):
    return LexicalRichness(text).terms

#TTR: Total number of different words / Total number of words (tokens). It depends on the length of the text.
def get_ttr(text):
    return round(LexicalRichness(text).ttr, 2)

#rTTR: Number of unique words / Square root of the total number of words. 
#To provide a more consistent measure of lexical diversity across texts of varying lengths.
def get_rttr(text):
    return round(LexicalRichness(text).rttr, 2)

#cTTR is less sensitive to text length and might be preferable due to its more stringent adjustment.
def get_cttr(text):
    return round(LexicalRichness(text).cttr, 2)

#Logarithmic and Normalized. Herdan's C (C=logV/logN) 
#High C Value: Indicates high lexical diversity, meaning the text uses a wide range of different words relative to its length.
def get_herdan(text):
    return round(LexicalRichness(text).Herdan, 2)

#Logarithmic measure independent of text length. Maas' T decreases as lexical richness increases.
def get_maas(text):
    return round(LexicalRichness(text).Maas, 2)

#Probability-based measure of encountering different types of words. Yule's K decreases as lexical richness increases.
def get_yulei(text):
    try:
        return LexicalRichness(text).yulei
    except ValueError as e:
        return None
    