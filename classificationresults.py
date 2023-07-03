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
    all_corr_ent = 0
    all_corr_con = 0
    all_corr_neu = 0
    all_corr_tot = 0
    all_tot_ent = 0
    all_tot_con = 0
    all_tot_neu = 0

    # Get results
    for index, row in data.iterrows():
        gold_label = row['gold_label']
        for i in range(len(languages)):
            lang_val = row[languages[i]]
            if gold_label == 'entailment':
                if lang_val == gold_label:
                    correct_entailments[i] += 1
                    correct_total[i] += 1
                    total_entailments[i] += 1
                elif lang_val == 'contradiction':
                    total_contradictions[i] += 1
                else:
                    total_neutrals[i] += 1
            elif gold_label == 'contradiction':
                if lang_val == gold_label:
                    correct_contradictions[i] += 1
                    correct_total[i] += 1
                    total_contradictions[i] += 1
                elif lang_val == 'entailment':
                    total_entailments[i] += 1
                else:
                    total_neutrals[i] += 1
            else:
                if lang_val == gold_label:
                    correct_neutrals[i] += 1
                    correct_total[i] += 1
                    total_neutrals[i] += 1
                elif lang_val == 'entailment':
                    total_entailments[i] += 1
                else:
                    total_contradictions[i] += 1


    for i in range(len(languages)):
        print(languages[i],'--> Correct entailments:', correct_entailments[i])
        print(languages[i],'--> Correct contradictions:', correct_contradictions[i])
        print(languages[i],'--> Correct neutrals:', correct_neutrals[i])
        print(languages[i],'--> Correct total:', correct_total[i])
        print(languages[i],'--> Total entailments:', total_entailments[i])
        print(languages[i],'--> Total contradictions:', total_contradictions[i])
        print(languages[i],'--> Total neutrals:', total_neutrals[i], '\n')

        all_corr_ent += correct_entailments[i]
        all_corr_con += correct_contradictions[i]
        all_corr_neu += correct_neutrals[i]
        all_corr_tot += correct_total[i]
        all_tot_ent += total_entailments[i]
        all_tot_con += total_contradictions[i]
        all_tot_neu += total_neutrals[i]
    
    print('Total correct entailments:', all_corr_ent)
    print('Total correct contradictions:', all_corr_con)
    print('Total correct neutrals:', all_corr_neu)
    print('Total classifications for entailment:', all_tot_ent)
    print('Total classifications for contradiction:', all_tot_con)
    print('Total classifications for neutral:', all_tot_neu)



if __name__ == '__main__':
    main()