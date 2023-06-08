import pandas as pd

def main():
    data = pd.read_csv('xnli.dev.tsv', sep='\t')

    languages = ['de', 'en', 'es', 'sw', 'ur']
    rows_per_subset = 625

    # Create subsets
    subsets = {}
    columns_to_include_others = ['language', 'sentence1', 'sentence2', 'pairID']
    columns_to_include_english = ['language', 'gold_label', 'sentence1', 'sentence2', 'pairID']

    for lang in languages:
        if lang != 'en':
            subset = data[data['language'] == lang][columns_to_include_others].head(rows_per_subset)
        else:
            subset = data[data['language'] == lang][columns_to_include_english].head(rows_per_subset)
        if len(subset) < rows_per_subset:
            subset = subset.reindex(subset.index.repeat(rows_per_subset)).head(rows_per_subset)
        subsets[lang] = subset


    # Print subsets
    for lang, subset in subsets.items():
        filename = f'subset_{lang}.csv' 
        subset.to_csv(filename, index=False)



if __name__ == '__main__':
    main()
