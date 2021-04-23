from ProteinGrouping import create_protein_groups
from ProteinSubGrouping import create_protein_subgroups


def protein_grouping_analysis(parameters):
    # TODO: this is temporary test-data, remove once parsers are finished
    protein_peptide_dict, peptide_protein_dict = create_test_data()

    # Inspect parameters, decide which grouping to output
    if parameters['method'] == 'occam':
        # call OccamsRazorPreprocessor
        # TODO
        print('Occams Razor')
    # Call ProteinGrouping
    protein_groups = create_protein_groups(protein_peptide_dict, peptide_protein_dict)
    # Call ProteinSubGrouping
    protein_subgroups = create_protein_subgroups(protein_groups, protein_peptide_dict)
    # output protein group and subgroup dicts
    # TODO

    return protein_groups, protein_subgroups


def create_test_data():
    protein_peptide_dict = dict()
    peptide_protein_dict = dict()
    protein_peptide_dict['1'] = set({'AAAAAAA', 'BBBBBBB', 'CCCCCCC'})
    protein_peptide_dict['2'] = set({'AAAAAAA', 'BBBBBBB'})
    protein_peptide_dict['3'] = set({'AAAAAAA', 'BBBBBBB', 'CCCCCCC', 'DDDDDDD'})
    protein_peptide_dict['4'] = set({'AAAAAAA', 'BBBBBBB', 'EEEEEEE'})
    protein_peptide_dict['5'] = set({'XXXXXXX', 'ZZZZZZZ'})
    protein_peptide_dict['6'] = set({'UUUUUUU', 'WWWWWWW'})
    peptide_protein_dict['AAAAAAA'] = set({'1', '2', '3', '4'})
    peptide_protein_dict['BBBBBBB'] = set({'1', '2', '3', '4'})
    peptide_protein_dict['CCCCCCC'] = set({'1', '3'})
    peptide_protein_dict['DDDDDDD'] = set({'3'})
    peptide_protein_dict['EEEEEEE'] = set({'4'})
    peptide_protein_dict['XXXXXXX'] = set({'5'})
    peptide_protein_dict['ZZZZZZZ'] = set({'5'})
    peptide_protein_dict['UUUUUUU'] = set({'6'})
    peptide_protein_dict['WWWWWWW'] = set({'6'})
    return protein_peptide_dict, peptide_protein_dict


dict_protein_groups, dict_protein_subgroups = protein_grouping_analysis({'method': 'occam'})
print(dict_protein_groups)
print(dict_protein_subgroups)
