# read in PSM files
# PSMID = id given in input file
# PEPTIDEID = sequence
# PROTEINID = accession or entire header
# EXPID = filename
# structure data → put into dictionaries
# 1) PSM -> experiment dict(PSM : exp (string of file name), …)
# 2) Peptide -> Set<Protein>, dict(peptide : set(PSMs))
# if peptide is assigned to only decoys, then remove peptide; if not remove decoy protein
# leave peptide as I and L for now, don;t replace to J (just take amino acids as they are, no handling of any ambiguous aas)
# 3) Protein -> Set<Peptide>,  dict(protein_id : set(peptides)
# check what’s best for now, either accession or fasta header
# 4) Peptide -> Set<PSM>
