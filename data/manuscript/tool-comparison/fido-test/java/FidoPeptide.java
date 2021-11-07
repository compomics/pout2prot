package fidodata;

import java.util.LinkedList;
import java.util.Random;

public class FidoPeptide {
	
	static LinkedList<String> usedSeqs = new LinkedList<String>();
	static Random random = new Random();
	static String aas = "ACDEFGHILMNPQSTVWY"; // 18 chars
	static char[] aaarray = aas.toCharArray();
	
	public String sequence = "";
	
	public void generateRandomSequence() {
		
		String seq = "";
		while (true) {
			int i = 0;
			while (i < 10) {
				i++;
				seq += "" + aaarray[random.nextInt(12)];
			}
			if (!usedSeqs.contains(seq)) {
				if (!(seq.contains("KP") || seq.contains("PK") || seq.contains("RP") || seq.contains("PR"))) {
					break;
				} 
			} else {
				seq = "";
			}
		}
		if (random.nextInt(18) > 9) {
			this.sequence = seq + "K";
		} else {
			this.sequence = seq + "R";
		}
	}
	
}
