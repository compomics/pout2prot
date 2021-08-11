'use strict';
import {
    AssertionError,
    AttributeError,
    BaseException,
    DeprecationWarning,
    Exception,
    IndexError,
    IterableError,
    KeyError,
    NotImplementedError,
    RuntimeWarning,
    StopIteration,
    UserWarning,
    ValueError,
    Warning,
    __JsIterator__,
    __PyIterator__,
    __Terminal__,
    __add__,
    __and__,
    __call__,
    __class__,
    __envir__,
    __eq__,
    __floordiv__,
    __ge__,
    __get__,
    __getcm__,
    __getitem__,
    __getslice__,
    __getsm__,
    __gt__,
    __i__,
    __iadd__,
    __iand__,
    __idiv__,
    __ijsmod__,
    __ilshift__,
    __imatmul__,
    __imod__,
    __imul__,
    __in__,
    __init__,
    __ior__,
    __ipow__,
    __irshift__,
    __isub__,
    __ixor__,
    __jsUsePyNext__,
    __jsmod__,
    __k__,
    __kwargtrans__,
    __le__,
    __lshift__,
    __lt__,
    __matmul__,
    __mergefields__,
    __mergekwargtrans__,
    __mod__,
    __mul__,
    __ne__,
    __neg__,
    __nest__,
    __or__,
    __pow__,
    __pragma__,
    __pyUseJsNext__,
    __rshift__,
    __setitem__,
    __setproperty__,
    __setslice__,
    __sort__,
    __specialattrib__,
    __sub__,
    __super__,
    __t__,
    __terminal__,
    __truediv__,
    __withblock__,
    __xor__,
    abs,
    all,
    any,
    assert,
    bool,
    bytearray,
    bytes,
    callable,
    chr,
    copy,
    deepcopy,
    delattr,
    dict,
    dir,
    divmod,
    enumerate,
    filter,
    float,
    getattr,
    hasattr,
    input,
    int,
    isinstance,
    issubclass,
    len,
    list,
    map,
    max,
    min,
    object,
    ord,
    pow,
    print,
    property,
    py_TypeError,
    py_iter,
    py_metatype,
    py_next,
    py_reversed,
    py_typeof,
    range,
    repr,
    round,
    set,
    setattr,
    sorted,
    str,
    sum,
    tuple,
    zip
} from "./org.transcrypt.__runtime__.js";

var __name__ = "OccamsRazorPreprocessor";
export var occam_filter = function (peptides_to_proteins, proteins_to_peptides) {
    var unique_peps = set();
    var unique_proteins = set();
    var explained_peps = set();
    for (var [pep1, prots1] of peptides_to_proteins.py_items()) if (len(prots1) ==
        1) {
        for (var protein of prots1) break;
        unique_proteins.add(protein);
        unique_peps.add(pep1);
        for (var pep of proteins_to_peptides[protein]) explained_peps.add(pep)
    }
    var remove_proteins = set();
    for (var [prot2, peps2] of proteins_to_peptides.py_items()) if (!__in__(prot2, unique_proteins)) {
        var is_explained = true;
        for (var pep_test of peps2) if (!__in__(pep_test, explained_peps)) var is_explained = false;
        var sharing_proteins = set();
        for (var pep_group of peps2) for (var protein_share of peptides_to_proteins[pep_group]) sharing_proteins.add(protein_share);
        for (var protein_test of sharing_proteins) if (peps2.issubset(proteins_to_peptides[protein_test]) && len(peps2) < len(proteins_to_peptides[protein_test])) var is_explained = true;
        if (is_explained) remove_proteins.add(prot2)
    }
    var peptides_marked_for_update = set();
    for (var prot_remove of remove_proteins) {
        for (var pep of proteins_to_peptides[prot_remove]) peptides_marked_for_update.add(pep);
        delete proteins_to_peptides[prot_remove]
    }
    for (var pept_marked of peptides_marked_for_update) peptides_to_proteins[pept_marked] = peptides_to_proteins[pept_marked].difference(remove_proteins)
};

//# sourceMappingURL=OccamsRazorPreprocessor.map
