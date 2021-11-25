from .ProteinGrouping import create_protein_groups
from .ProteinSubGrouping import anti_occam_create_protein_subgroups, occam_create_protein_subgroups
from .OccamsRazorPreprocessor import occam_filter


def protein_grouping_analysis(occam_flag, protein_peptide_dict, peptide_protein_dict):
    if occam_flag:
        pre_protein_groups = create_protein_groups(protein_peptide_dict, peptide_protein_dict)
        occam_filter(peptide_protein_dict, protein_peptide_dict, pre_protein_groups)
        protein_groups = create_protein_groups(protein_peptide_dict, peptide_protein_dict)
        protein_subgroups = occam_create_protein_subgroups(protein_groups, protein_peptide_dict)
    else:
        # Call ProteinGrouping (Anti-Occam)
        protein_groups = create_protein_groups(protein_peptide_dict, peptide_protein_dict)
        # Call ProteinSubGrouping (Anti-Occam)
        protein_subgroups = anti_occam_create_protein_subgroups(protein_groups, protein_peptide_dict)

    # output protein group and subgroup dicts
    return protein_groups, protein_subgroups
