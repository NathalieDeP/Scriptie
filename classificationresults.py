import pandas as pd

def main():
    # Get data and initializa variables
    data = pd.read_csv('bart_classifications.tsv', sep='\t')
    correct_entailments = 0
    correct_contradictions = 0
    correct_neutrals = 0
    correct_total = 0
    total_entailments = 0
    total_contradictions = 0
    total_neutrals = 0

    # Calculate results
    for index, row in data.iterrows():
        gold_label = row['gold_label']
        english = row['English']
        german = row['German']
        spanish = row['Spanish']
        swahili = row['Swahili']
        urdu = row['Urdu']



if __name__ == '__main__':
    main()