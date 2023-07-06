import pandas as pd

def main():
    # Get data and initialize variables // comment- and uncomment for each model
    data = pd.read_csv('bart_classifications.tsv', sep='\t')
    #data = pd.read_csv('deberta_classifications.tsv', sep='\t')
    languages = ['English','German', 'Spanish',  'Swahili', 'Urdu']
    same_entailments = [0,0,0,0,0]
    same_contradictions = [0,0,0,0,0]
    same_neutrals = [0,0,0,0,0]
    same_as_en = [0, 0, 0, 0, 0]


    # Get results
    for index, row in data.iterrows():
        english_label = row['English']
        for i in range(len(languages)):
            lang_val = row[languages[i]]
            if english_label == 'entailment' and english_label == lang_val:
                same_entailments[i] += 1
                same_as_en[i] += 1
            elif english_label == 'contradiction' and english_label == lang_val:
                same_contradictions[i] += 1
                same_as_en[i] += 1
            elif english_label == 'neutral' and english_label == lang_val:
                same_neutrals[i] += 1
                same_as_en[i] += 1

                
            
     
    for i in range(len(languages)):
        print(languages[i], '--> same entailents:', same_entailments[i], '        score:', same_entailments[i]/same_entailments[0])
        print(languages[i], '--> same contradictions:', same_contradictions[i], '        score:', same_contradictions[i]/same_contradictions[0])
        print(languages[i], '--> same neutrals:', same_neutrals[i], '        score:', same_neutrals[i]/same_neutrals[0])
        print(languages[i], '--> Total score:', same_as_en[i]/same_as_en[0], '\n')

        




if __name__ == '__main__':
    main()