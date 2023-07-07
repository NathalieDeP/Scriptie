import pandas as pd

def main():
    # Get data and initialize variables // comment- and uncomment for each model
    data = pd.read_csv('bart_classifications.tsv', sep='\t')
    #data = pd.read_csv('deberta_classifications.tsv', sep='\t')
    languages = ['English', 'German', 'Spanish',  'Swahili', 'Urdu']
    correct_entailments = [0, 0, 0, 0, 0]
    correct_contradictions = [0, 0, 0, 0, 0]
    correct_neutrals = [0, 0, 0, 0, 0]
    correct_total = [0, 0, 0, 0, 0]
    tot_sys_ent = 0
    tot_sys_con = 0
    tot_sys_neu = 0
    line = 0

    # Get results
    for index, row in data.iterrows():
        gold_label = row['gold_label']
        for i in range(len(languages)):
            lang_val = row[languages[i]]
            if gold_label == 'entailment':
                tot_sys_ent += 1
                if lang_val == gold_label:
                    correct_entailments[i] += 1
                    correct_total[i] += 1
            elif gold_label == 'contradiction':
                tot_sys_con += 1
                if lang_val == gold_label:
                    correct_contradictions[i] += 1
                    correct_total[i] += 1
            else:
                tot_sys_neu += 1
                if lang_val == gold_label:
                    correct_neutrals[i] += 1
                    correct_total[i] += 1

            



    for i in range(len(languages)):
        print(languages[i],'--> Correct entailments:', correct_entailments[i], '        score:', correct_entailments[i]/(tot_sys_ent/5))
        print(languages[i],'--> Correct contradictions:', correct_contradictions[i],  '        score:', correct_contradictions[i]/(tot_sys_con/5))
        print(languages[i],'--> Correct neutrals:', correct_neutrals[i], '        score:', correct_neutrals[i]/(tot_sys_neu/5))
        print(languages[i],'--> Correct total:', correct_total[i], '        score:', correct_total[i]/(553), '\n')
   

    print('Total gold label entailments: ', tot_sys_ent/5)
    print('Total gold label contradictions: ', tot_sys_con/5)
    print('Total gold label neutrals: ', tot_sys_neu/5)




if __name__ == '__main__':
    main()