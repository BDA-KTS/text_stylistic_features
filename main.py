from features_util.lexicalanalysis import *
from features_util.profanity_analysis import *
from features_util.readability import *
from features_util.repetitiveness import *
from features_util.rhyme_scheme import *
from features_util.sentiments_and_emotions import *

import pandas as pd

if __name__ == "__main__":
    
    df = pd.read_csv("data/input_posts.tsv", sep='\t')

    # Lexical analysis
    df['tokens'] = df['posts'].apply(get_tokens)
    df['ttr'] = df['posts'].apply(get_ttr)
    df['rttr'] = df['posts'].apply(get_rttr)
    df['cttr'] = df['posts'].apply(get_cttr)
    df['herdan'] = df['posts'].apply(get_herdan)
    df['maas'] = df['posts'].apply(get_maas)
    #df['yulei'] = df['Posts'].apply(get_yulei)

    # profanity features
    df['profanity_count'] = df['posts'].apply(count_profanity)
    df['profanity_cleaned_text'] = df['posts'].apply(clean_document) 

    # readability
    df['flesch_reading_ease'] = df['posts'].apply(get_flesch_reading_ease)
    df['text_standard'] = df['posts'].apply(get_text_standard)
    df['reading_time'] = df['posts'].apply(get_reading_time)
    df['syllable_count'] = df['posts'].apply(get_syllable_count)
    df['sentence_count'] = df['posts'].apply(get_sentence_count)
    df['char_count'] = df['posts'].apply(get_char_count)
    df['polysyllable_count'] = df['posts'].apply(get_polysyllable_count)
    df['get_monosyllable_count'] = df['posts'].apply(get_monosyllable_count)
    
    # repetitiveness
    df['num_of_choruses'] = df['posts'].apply(num_of_choruses)

    # rhyme
    df['rhyme_scheme'] = df['posts'].apply(get_rhyme_scheme)
    
    # sentiment analysis
    df['sentiment_polarity'] = df['posts'].apply(get_vader_scores)

    df.to_csv("data/stylistic_features_enriched_posts.tsv", sep = '\t', index = False)
    