from Parser import parser
from Analyzer import protein_grouping_analysis
from OutputWriter import write_to_file

# handling of command line (or config file) arguments

my_path = "./data/"  # be careful with / (linux) and \\ (windows)
fdr_threshold = 0.01
decoy_flag = "decoy"
occam_flag = True

# Parsing - input: folder, output: dicts
# calls Parser
psm_exp, pep_psm, pep_prot, prot_pep, rep_cat = parser(my_path, fdr_threshold, decoy_flag)

# Running grouping algorithm - input: dicts and parameters (occam, anti-occam), output: new dicts with groups
# calls Analyzer
protein_groups, protein_subgroups = protein_grouping_analysis(occam_flag, prot_pep, pep_prot)

# Output writer - input: all dicts, output: file
# calls OutputWriter
write_to_file(protein_groups, psm_exp, pep_psm, pep_prot, prot_pep, "groups.tsv")
write_to_file(protein_subgroups, psm_exp, pep_psm, pep_prot, prot_pep, "subgroups.tsv")
