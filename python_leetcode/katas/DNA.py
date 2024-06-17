
def pair_dna(dna_string):
    dna_pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return [[base, dna_pairs[base]] for base in dna_string]