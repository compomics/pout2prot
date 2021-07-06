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
    remove_proteins = set()
    unique_peptides = set()
    # check if a peptide is unique
    for [pep, prots] in peptides_to_proteins.items():
        is_unique = False
        if len(prots) == 1:
            is_unique = True
        else:
            exact_duplicates = set()
            for prot1 in prots:
                for prot2 in prots:
                    if prot1 != prot2:
                        if proteins_to_peptides[prot1] == proteins_to_peptides[prot2]:
                            exact_duplicates.add(prot1)
                            exact_duplicates.add(prot2)
            if exact_duplicates == prots:
                is_unique = True
        if is_unique:
            unique_peptides.add(pep)

    # check if proteins have a unique peptide
    for prot2, peps2 in proteins_to_peptides.items():
        has_unique = False
        for pep_test in peps2:
            if pep_test in unique_peptides:
                has_unique = True
        if not has_unique:
            # get the other proteins
            # check if there is another protein with the same set of peptides
            # if the other protein has more peptides, remove
            other_proteins = set()
            for pep_test2 in peps2:
                for other_prot in peptides_to_proteins[pep_test2]:
                    if other_prot not in remove_proteins:
                        other_proteins.add(other_prot)

            for prot3 in other_proteins:
                # check if one of these proteins has a superset of peptides to our current prot2
                if proteins_to_peptides[prot2].issubset(proteins_to_peptides[prot3]):
                    if proteins_to_peptides[prot2] != proteins_to_peptides[prot3]:
                        remove_proteins.add(prot2)

    # Removing step
    peptides_marked_for_update = set()
    for prot_remove in remove_proteins:
        for pep in proteins_to_peptides[prot_remove]:
            peptides_marked_for_update.add(pep)
        del proteins_to_peptides[prot_remove]

    for pept_marked in peptides_marked_for_update:
        peptides_to_proteins[pept_marked] = peptides_to_proteins[pept_marked].difference(remove_proteins)
