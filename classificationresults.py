import pandas as pd

def main():
    # Get data and initializa variables // comment- and uncomment for each model
    #data = pd.read_csv('bart_classifications.tsv', sep='\t')
    data = pd.read_csv('deberta_classifications.tsv', sep='\t')
    languages = ['English', 'German', 'Spanish',  'Swahili', 'Urdu']
    correct_entailments = [0, 0, 0, 0, 0]
    correct_contradictions = [0, 0, 0, 0, 0]
    correct_neutrals = [0, 0, 0, 0, 0]
    correct_total = [0, 0, 0, 0, 0]
    total_entailments = [0, 0, 0, 0, 0]
    total_contradictions = [0, 0, 0, 0, 0]
    total_neutrals = [0, 0, 0, 0, 0]
    same_as_en = [625, 0, 0, 0, 0]
    all_corr_ent = 0
    all_corr_con = 0
    all_corr_neu = 0
    all_corr_tot = 0
    tot_sys_ent = 0
    tot_sys_con = 0
    tot_sys_neu = 0

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
                    total_entailments[i] += 1
                elif lang_val == 'contradiction':
                    total_contradictions[i] += 1
                else:
                    total_neutrals[i] += 1
            elif gold_label == 'contradiction':
                tot_sys_con += 1
                if lang_val == gold_label:
                    correct_contradictions[i] += 1
                    correct_total[i] += 1
                    total_contradictions[i] += 1
                elif lang_val == 'entailment':
                    total_entailments[i] += 1
                else:
                    total_neutrals[i] += 1
            else:
                tot_sys_neu += 1
                if lang_val == gold_label:
                    correct_neutrals[i] += 1
                    correct_total[i] += 1
                    total_neutrals[i] += 1
                elif lang_val == 'entailment':
                    total_entailments[i] += 1
                else:
                    total_contradictions[i] += 1
            
            if (languages[i] != 'English'):
                if lang_val == row['English']:
                    same_as_en[i] += 1


    for i in range(len(languages)):
        print(languages[i],'--> Correct entailments:', correct_entailments[i])
        print(languages[i],'--> Correct contradictions:', correct_contradictions[i])
        print(languages[i],'--> Correct neutrals:', correct_neutrals[i])
        print(languages[i],'--> Correct total:', correct_total[i])
        print(languages[i],'--> Total entailments:', total_entailments[i])
        print(languages[i],'--> Total contradictions:', total_contradictions[i])
        print(languages[i],'--> Total neutrals:', total_neutrals[i])
        print(languages[i],'--> Same as English:', same_as_en[i], '\n')

        all_corr_ent += correct_entailments[i]
        all_corr_con += correct_contradictions[i]
        all_corr_neu += correct_neutrals[i]
        all_corr_tot += correct_total[i]
    
    print('Total correct entailments:', all_corr_ent)
    print('Total correct contradictions:', all_corr_con)
    print('Total correct neutrals:', all_corr_neu)
    print('Total correct classifications:', all_corr_tot, '\n')

    print('Total gold label entailments: ', tot_sys_ent)
    print('Total gold label contradictions: ', tot_sys_con)
    print('Total gold label neutrals: ', tot_sys_neu)




if __name__ == '__main__':
    main()