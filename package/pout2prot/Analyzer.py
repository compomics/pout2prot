from .ProteinGrouping import create_protein_groups
from .ProteinSubGrouping import create_protein_subgroups
from .OccamsRazorPreprocessor import occam_filter


def protein_grouping_analysis(occam_flag, protein_peptide_dict, peptide_protein_dict):
    # Inspect parameters, decide which grouping to output
    if occam_flag:
        occam_filter(peptide_protein_dict, protein_peptide_dict)

    # Call ProteinGrouping
    protein_groups = create_protein_groups(protein_peptide_dict, peptide_protein_dict)
    # Call ProteinSubGrouping
    protein_subgroups = create_protein_subgroups(occam_flag, protein_groups, protein_peptide_dict)
    # output protein group and subgroup dicts
    return protein_groups, protein_subgroups
