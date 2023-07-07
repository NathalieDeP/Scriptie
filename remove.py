import pandas as pd

def main():
    data = pd.read_csv('en_subset.csv', sep='\t')
    data2 = pd.read_csv('subset_translated_ur.tsv', sep='\t')
    data3 = pd.read_csv('subset_translated_de.tsv', sep='\t')
    data4 = pd.read_csv('subset_translated_es.tsv', sep='\t')
    data5 = pd.read_csv('subset_translated_sw.tsv', sep='\t')
    new_df_en = pd.DataFrame(columns=['gold_label', 'sentence1', 'sentence2', 'pairID'])
    new_df_de = pd.DataFrame(columns=['sentence1', 'sentence2', 'pairID'])
    new_df_es = pd.DataFrame(columns=['sentence1', 'sentence2', 'pairI'])
    new_df_sw = pd.DataFrame(columns=['sentence1', 'sentence2', 'pairID'])
    new_df_ur = pd.DataFrame(columns=['sentence1', 'sentence2', 'pairID'])

    with open('non_english.txt', 'r') as f:
        to_be_removed = f.read().split('\n')
        for index, row in data.iterrows():
                 if str(row['pairID']) not in to_be_removed:
                    new_df_en.at[index, 'gold_label'] = row['gold_label']
                    new_df_en.at[index, 'sentence1'] = row['sentence1']
                    new_df_en.at[index, 'sentence2'] = row['sentence2']
                    new_df_en.at[index, 'pairID'] = row['pairID']
        
        for index, row in data2.iterrows():
                 if str(row['pairID']) not in to_be_removed:
                    new_df_ur.at[index, 'translated_sentence1'] = row['translated_sentence1']
                    new_df_ur.at[index, 'translated_sentence2'] = row['translated_sentence2']
                    new_df_ur.at[index, 'pairID'] = row['pairID']       
        
        for index, row in data3.iterrows():
                 if str(row['pairID']) not in to_be_removed:
                    new_df_de.at[index, 'translated_sentence1'] = row['translated_sentence1']
                    new_df_de.at[index, 'translated_sentence2'] = row['translated_sentence2']
                    new_df_de.at[index, 'pairID'] = row['pairID']

        for index, row in data4.iterrows():
                 if str(row['pairID']) not in to_be_removed:
                    new_df_es.at[index, 'translated_sentence1'] = row['translated_sentence1']
                    new_df_es.at[index, 'translated_sentence2'] = row['translated_sentence2']
                    new_df_es.at[index, 'pairID'] = row['pairID']                   

        for index, row in data5.iterrows():
                 if str(row['pairID']) not in to_be_removed:
                    new_df_sw.at[index, 'translated_sentence1'] = row['translated_sentence1']
                    new_df_sw.at[index, 'translated_sentence2'] = row['translated_sentence2']
                    new_df_sw.at[index, 'pairID'] = row['pairID']


    new_df_en.to_csv('subset_en.csv', sep='\t', index=False)
    new_df_de.to_csv('translated_subset_de.tsv', sep='\t', index=False)
    new_df_es.to_csv('translated_subset_es.tsv', sep='\t', index=False)
    new_df_sw.to_csv('translated_subset_sw.tsv', sep='\t', index=False)
    new_df_ur.to_csv('translated_subset_ur.tsv', sep='\t', index=False)



if __name__ == '__main__':
     main()