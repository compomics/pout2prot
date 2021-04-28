# only for Occams razor (PAPSSO): go through proteins and remove those that have no unique peptides
# Remove all proteins that don't contain unique peptides

# Input
# 1) Peptide -> Set<Protein>
# 2) Protein -> Set<Peptide>

# We need to check whether some of these proteins do not contain unique peptides. We can check this by iterating over
# all proteins, for each protein extract all associated peptides and check if these peptides are all associated to
# another at least one other protein. If that's the case, we remove the current protein.


def occam_filter(peptides_to_proteins, proteins_to_peptides):
    """ Perform filtering on the proteins, based on Occam's razor decisions.

    :param peptides_to_proteins: A dictionary that maps every peptide onto a set of all proteins (that are associated
    with ths peptide).
    :param proteins_to_peptides: A dictionary that maps every protein onto a set of all peptides (which are associated
    with this protein).
    :return: Both set's given are updated in-place. This means that no explicit value is returned, but rather that the
    arguments passed will be changed.
    """

    # Keep track of which proteins are marked for removal (these will be removed after the algorithm has been run).
    proteins_marked_for_removal = set()
    peptides_marked_for_removal = set()

    for [prot, pepts] in proteins_to_peptides.items():
        prots_to_check = set()
        for pept in pepts:
            prots_to_check.update(peptides_to_proteins[pept])
        prots_to_check.discard(prot)

        for otherProt in prots_to_check:
            otherPepts = proteins_to_peptides[otherProt]
            if pepts.issubset(otherPepts) and len(pepts) < len(otherPepts):
                proteins_marked_for_removal.add(prot)
                peptides_marked_for_removal.update(pepts)

    for prot in proteins_marked_for_removal:
        del proteins_to_peptides[prot]

    for pept in peptides_marked_for_removal:
        peptides_to_proteins[pept] = peptides_to_proteins[pept].difference(proteins_marked_for_removal)


