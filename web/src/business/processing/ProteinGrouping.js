// Transcrypt'ed from Python, 2021-06-03 13:33:10
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
var __name__ = 'ProteinGrouping';
export var create_protein_groups = function (protein_peptide_dict, peptide_protein_dict) {
	var protein_groups = dict ();
	var protein_group_id = 0;
	var remaining_proteins = set (protein_peptide_dict.py_keys ());
	while (len (remaining_proteins) > 0) {
		var protein = remaining_proteins.py_pop ();
		protein_group_id++;
		protein_groups [protein_group_id] = new set ([protein]);
		recursion_check_for_more_linked_proteins (protein_group_id, remaining_proteins, protein_peptide_dict, protein_groups, peptide_protein_dict);
	}
	return protein_groups;
};
export var recursion_check_for_more_linked_proteins = function (protein_group_id, remaining_proteins, protein_peptide_dict, protein_groups, peptide_protein_dict) {
	var current_protein_set = set ();
	var peptide_set = set ();
	for (const protein of protein_groups [protein_group_id]) {
		current_protein_set.add (protein);
		peptide_set.py_update (protein_peptide_dict [protein]);
	}
	var new_protein_set = set ();
	for (var peptide of peptide_set) {
		new_protein_set.py_update (peptide_protein_dict [peptide]);
	}
	protein_groups [protein_group_id].py_update (new_protein_set);
	for (const protein of new_protein_set) {
		if (__in__ (protein, remaining_proteins)) {
			remaining_proteins.remove (protein);
		}
	}
	debugger;
	if (len (current_protein_set.difference (new_protein_set)) != 0 || len (new_protein_set.difference (current_protein_set)) != 0) {
		recursion_check_for_more_linked_proteins (protein_group_id, remaining_proteins, protein_peptide_dict, protein_groups, peptide_protein_dict);
	}
};

//# sourceMappingURL=ProteinGrouping.map
