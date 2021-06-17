import glob
import re


def parser(my_path, fdr_threshold, decoy_flag):

    """Read in data from output files, return 4 dicts:
    PSM - experiment; peptide - PSMs; peptide - proteins; proteins - peptides"""

    ### Initiate dictionaries ###
    # 1) PSM -> experiment dict(PSM : exp (string of file name), ...)
    psm_exp = dict()

    # 2) Peptide -> Set<PSM>
    pep_psm = dict()

    # 3) Peptide -> Set < Protein >, dict(peptide: set(PSMs))
    # if peptide is assigned to only decoys, then remove peptide; if not remove decoy protein
    # leave peptide as I and L for now, don't replace to J
    pep_prot = dict()

    # 4) Protein -> Set<Peptide>,  dict(protein_id : set(peptides)
    # UniProtKB accession if possible, otherwise complete name
    prot_pep = dict()

    ### Iterate over subdirectories (sample_categories) files and pout_files in that folder (replicates) ###
    pout_files = list()
    sample_categories = glob.glob(my_path + "/**/")
    rep_cat = dict()  # maps all replicates or experiments to the sample category

    # First, map all experiments/replicates to the sample_category
    if sample_categories:
        for category in sample_categories:
            pouts = glob.glob(category + "/*.pout")
            for pout in pouts:
                rep_cat[pout] = category
                pout_files.append(pout)
    else:
        pout_files = glob.glob(my_path + "/*.pout")
        for pout in pout_files:
            rep_cat[pout] = pout

    # iterate over all pout_files
    for pout_file in pout_files:
        with open(pout_file, "r") as f:
            next(f)  # skip header
            for line in f:
                psm_id, _, q, _, peptide, proteins = line.rstrip().split("\t", maxsplit=5)
                if float(q) < fdr_threshold:
                    # retrieving all information
                    peptide = re.sub("\[.*?\]", "", peptide)
                    peptide = peptide.split(".")[1]
                    proteins = proteins.split("\t")
                    for i, protein in enumerate(proteins):
                        # SwissProt proteins: # >sp|<accession>|<description>
                        try:
                            protein = protein.split("|", maxsplit=2)[1]
                            if protein != "" and protein != "sp" and protein != "tr":  # could be the case in typo,
                                # e.g. >generic||<accession>|<description>; sometimes empty with sp or tr
                                proteins[i] = protein

                        except IndexError:
                            pass  # leave protein name just as complete header

                    # Normally, only decoy proteins are returned IF there's other proteins linked to a PSM as well
                    assert not all(decoy_flag in protein for protein in proteins), \
                        "{} is only contained in decoy proteins".format(psm_id)

                    # update psm_exp
                    assert psm_id not in psm_exp.keys(), "Only one experiment should be mapped to PSM"
                    psm_exp[psm_id] = pout_file

                    # update pep_psm
                    if peptide not in pep_psm.keys():
                        pep_psm[peptide] = set()
                        pep_psm[peptide].add(psm_id)
                    else:
                        pep_psm[peptide].add(psm_id)

                    # update pep_prot and prot_pep
                    for protein in proteins:
                        if decoy_flag not in protein:
                            if peptide not in pep_prot.keys():
                                pep_prot[peptide] = set()
                                pep_prot[peptide].add(protein)
                            else:
                                pep_prot[peptide].add(protein)

                            if protein not in prot_pep.keys():
                                prot_pep[protein] = set()
                                prot_pep[protein].add(peptide)
                            else:
                                prot_pep[protein].add(peptide)

    return psm_exp, pep_psm, pep_prot, prot_pep, rep_cat

