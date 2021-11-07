package fidodata;

import java.util.LinkedList;

public class FidoProtein {
	
	public String sequence = "";
	public String name;
	public LinkedList<FidoPeptide> peptides = new LinkedList<FidoPeptide>();
	
	public FidoProtein(String name) {
		this.name = name;
	}
	
	public void addPeptide(FidoPeptide pep) {
		this.peptides.add(pep);
	}

	public void generateSequence() {
		this.sequence += "MFIDQK";
		for (FidoPeptide pep : this.peptides) {
			if (pep.sequence.equals("")) {
				pep.generateRandomSequence();
			}
			this.sequence += pep.sequence;
		}
		// add one more random peptide, so that the proteins are all different
		FidoPeptide fp = new FidoPeptide();
		fp.generateRandomSequence();
		this.sequence += fp.sequence;
		this.sequence += "SCKS";
	}

}
