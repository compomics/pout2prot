package fidodata;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Stack;

public class FidoDataCreator {

	public static void main(String[] args) throws IOException {
		// define proteins and peptides (relations)

		HashMap<String, FidoProtein> allProteins = new HashMap<String, FidoProtein>();

		// CASE 1

		allProteins.put("Case1_P1", new FidoProtein("Case1_P1"));
		allProteins.put("Case1_P2", new FidoProtein("Case1_P2"));
		FidoPeptide case1A = new FidoPeptide();
		allProteins.get("Case1_P1").addPeptide(case1A);
		allProteins.get("Case1_P2").addPeptide(case1A);

		// CASE 2

		allProteins.put("Case2_P1", new FidoProtein("Case2_P1"));
		allProteins.put("Case2_P2", new FidoProtein("Case2_P2"));
		FidoPeptide case2A = new FidoPeptide();
		FidoPeptide case2B = new FidoPeptide();
		allProteins.get("Case2_P1").addPeptide(case2A);
		allProteins.get("Case2_P2").addPeptide(case2A);
		allProteins.get("Case2_P1").addPeptide(case2B);
		allProteins.get("Case2_P2").addPeptide(case2B);

		// CASE 3
		
		allProteins.put("Case3_P1", new FidoProtein("Case3_P1"));
		allProteins.put("Case3_P2", new FidoProtein("Case3_P2"));
		FidoPeptide case3A = new FidoPeptide();
		FidoPeptide case3B = new FidoPeptide();
		allProteins.get("Case3_P1").addPeptide(case3A);
		allProteins.get("Case3_P2").addPeptide(case3A);
		allProteins.get("Case3_P1").addPeptide(case3B);
		
		// CASE 4
		
		allProteins.put("Case4_P1", new FidoProtein("Case4_P1"));
		allProteins.put("Case4_P2", new FidoProtein("Case4_P2"));
		FidoPeptide case4A = new FidoPeptide();
		FidoPeptide case4B = new FidoPeptide();
		FidoPeptide case4C = new FidoPeptide();
		allProteins.get("Case4_P1").addPeptide(case4A);
		allProteins.get("Case4_P1").addPeptide(case4B);
		allProteins.get("Case4_P2").addPeptide(case4B);
		allProteins.get("Case4_P2").addPeptide(case4C);
		
		// CASE 5
		
		allProteins.put("Case5_P1", new FidoProtein("Case5_P1"));
		allProteins.put("Case5_P2", new FidoProtein("Case5_P2"));
		allProteins.put("Case5_P3", new FidoProtein("Case5_P3"));
		FidoPeptide case5A = new FidoPeptide();
		FidoPeptide case5B = new FidoPeptide();
		FidoPeptide case5C = new FidoPeptide();
		allProteins.get("Case5_P1").addPeptide(case5A);
		allProteins.get("Case5_P1").addPeptide(case5B);
		allProteins.get("Case5_P2").addPeptide(case5B);
		allProteins.get("Case5_P3").addPeptide(case5B);
		allProteins.get("Case5_P2").addPeptide(case5C);
		allProteins.get("Case5_P3").addPeptide(case5C);
		
		// CASE 6
		
		allProteins.put("Case6_P1", new FidoProtein("Case6_P1"));
		allProteins.put("Case6_P2", new FidoProtein("Case6_P2"));
		allProteins.put("Case6_P3", new FidoProtein("Case6_P3"));
		allProteins.put("Case6_P4", new FidoProtein("Case6_P4"));
		FidoPeptide case6A = new FidoPeptide();
		FidoPeptide case6B = new FidoPeptide();
		FidoPeptide case6C = new FidoPeptide();
		allProteins.get("Case6_P1").addPeptide(case6A);
		allProteins.get("Case6_P2").addPeptide(case6A);
		allProteins.get("Case6_P1").addPeptide(case6B);
		allProteins.get("Case6_P2").addPeptide(case6B);
		allProteins.get("Case6_P3").addPeptide(case6B);
		allProteins.get("Case6_P4").addPeptide(case6B);
		allProteins.get("Case6_P3").addPeptide(case6C);
		allProteins.get("Case6_P4").addPeptide(case6C);
		
		// CASE 7
		
		allProteins.put("Case7_P1", new FidoProtein("Case7_P1"));
		allProteins.put("Case7_P2", new FidoProtein("Case7_P2"));
		allProteins.put("Case7_P3", new FidoProtein("Case7_P3"));
		FidoPeptide case7A = new FidoPeptide();
		FidoPeptide case7B = new FidoPeptide();
		FidoPeptide case7C = new FidoPeptide();
		allProteins.get("Case7_P1").addPeptide(case7A);
		allProteins.get("Case7_P3").addPeptide(case7A);
		allProteins.get("Case7_P1").addPeptide(case7B);
		allProteins.get("Case7_P2").addPeptide(case7B);
		allProteins.get("Case7_P2").addPeptide(case7C);
		allProteins.get("Case7_P3").addPeptide(case7C);
		
		// CASE 8
		
		allProteins.put("Case8_P1", new FidoProtein("Case8_P1"));
		allProteins.put("Case8_P2", new FidoProtein("Case8_P2"));
		allProteins.put("Case8_P3", new FidoProtein("Case8_P3"));
		FidoPeptide case8A = new FidoPeptide();
		FidoPeptide case8B = new FidoPeptide();
		FidoPeptide case8C = new FidoPeptide();
		allProteins.get("Case8_P1").addPeptide(case8A);
		allProteins.get("Case8_P1").addPeptide(case8B);
		allProteins.get("Case8_P2").addPeptide(case8B);
		allProteins.get("Case8_P3").addPeptide(case8B);
		allProteins.get("Case8_P3").addPeptide(case8C);
		
		// CASE 9
		
		allProteins.put("Case9_P1", new FidoProtein("Case9_P1"));
		allProteins.put("Case9_P2", new FidoProtein("Case9_P2"));
		allProteins.put("Case9_P3", new FidoProtein("Case9_P3"));
		FidoPeptide case9A = new FidoPeptide();
		FidoPeptide case9B = new FidoPeptide();
		FidoPeptide case9C = new FidoPeptide();
		FidoPeptide case9D = new FidoPeptide();
		allProteins.get("Case9_P1").addPeptide(case9A);
		allProteins.get("Case9_P3").addPeptide(case9A);
		allProteins.get("Case9_P1").addPeptide(case9B);
		allProteins.get("Case9_P2").addPeptide(case9B);
		allProteins.get("Case9_P2").addPeptide(case9C);
		allProteins.get("Case9_P3").addPeptide(case9C);
		allProteins.get("Case9_P1").addPeptide(case9D);
		
		// CASE 10
		
		allProteins.put("Case10_P1", new FidoProtein("Case10_P1"));
		allProteins.put("Case10_P2", new FidoProtein("Case10_P2"));
		allProteins.put("Case10_P3", new FidoProtein("Case10_P3"));
		FidoPeptide case10A = new FidoPeptide();
		FidoPeptide case10B = new FidoPeptide();
		FidoPeptide case10C = new FidoPeptide();
		FidoPeptide case10D = new FidoPeptide();
		allProteins.get("Case10_P1").addPeptide(case10A);
		allProteins.get("Case10_P2").addPeptide(case10A);
		allProteins.get("Case10_P3").addPeptide(case10A);
		allProteins.get("Case10_P1").addPeptide(case10B);
		allProteins.get("Case10_P2").addPeptide(case10B);
		allProteins.get("Case10_P1").addPeptide(case10C);
		allProteins.get("Case10_P3").addPeptide(case10D);
		allProteins.get("Case10_P2").addPeptide(case10D);
		// CASE 11
		
		allProteins.put("Case11_P1", new FidoProtein("Case11_P1"));
		allProteins.put("Case11_P2", new FidoProtein("Case11_P2"));
		allProteins.put("Case11_P3", new FidoProtein("Case11_P3"));
		FidoPeptide case11A = new FidoPeptide();
		FidoPeptide case11B = new FidoPeptide();
		FidoPeptide case11C = new FidoPeptide();
		FidoPeptide case11D = new FidoPeptide();
		allProteins.get("Case11_P1").addPeptide(case11A);
		allProteins.get("Case11_P1").addPeptide(case11B);
		allProteins.get("Case11_P2").addPeptide(case11B);
		allProteins.get("Case11_P2").addPeptide(case11C);
		allProteins.get("Case11_P3").addPeptide(case11C);
		allProteins.get("Case11_P3").addPeptide(case11D);
		
		// CASE 12
		
		allProteins.put("Case12_P1", new FidoProtein("Case12_P1"));
		allProteins.put("Case12_P2", new FidoProtein("Case12_P2"));
		allProteins.put("Case12_P3", new FidoProtein("Case12_P3"));
		allProteins.put("Case12_P4", new FidoProtein("Case12_P4"));
		FidoPeptide case12A = new FidoPeptide();
		FidoPeptide case12B = new FidoPeptide();
		FidoPeptide case12C = new FidoPeptide();
		FidoPeptide case12D = new FidoPeptide();
		FidoPeptide case12E = new FidoPeptide();
		allProteins.get("Case12_P1").addPeptide(case12A);
		allProteins.get("Case12_P1").addPeptide(case12B);
		allProteins.get("Case12_P2").addPeptide(case12B);
		allProteins.get("Case12_P2").addPeptide(case12C);
		allProteins.get("Case12_P3").addPeptide(case12C);
		allProteins.get("Case12_P3").addPeptide(case12D);
		allProteins.get("Case12_P4").addPeptide(case12D);
		allProteins.get("Case12_P4").addPeptide(case12E);
		
		// CASE 13
		
		allProteins.put("Case13_P1", new FidoProtein("Case13_P1"));
		allProteins.put("Case13_P2", new FidoProtein("Case13_P2"));
		allProteins.put("Case13_P3", new FidoProtein("Case13_P3"));
		allProteins.put("Case13_P4", new FidoProtein("Case13_P4"));
		allProteins.put("Case13_P5", new FidoProtein("Case13_P5"));
		allProteins.put("Case13_P6", new FidoProtein("Case13_P6"));
		FidoPeptide case13A = new FidoPeptide();
		FidoPeptide case13B = new FidoPeptide();
		FidoPeptide case13C = new FidoPeptide();
		allProteins.get("Case13_P1").addPeptide(case13A);
		allProteins.get("Case13_P3").addPeptide(case13A);
		allProteins.get("Case13_P4").addPeptide(case13A);
		allProteins.get("Case13_P1").addPeptide(case13B);
		allProteins.get("Case13_P2").addPeptide(case13B);
		allProteins.get("Case13_P5").addPeptide(case13B);
		allProteins.get("Case13_P2").addPeptide(case13C);
		allProteins.get("Case13_P3").addPeptide(case13C);
		allProteins.get("Case13_P6").addPeptide(case13C);
		
		// CASE 14
		
		allProteins.put("Case14_P1", new FidoProtein("Case14_P1"));
		allProteins.put("Case14_P2", new FidoProtein("Case14_P2"));
		allProteins.put("Case14_P3", new FidoProtein("Case14_P3"));
		allProteins.put("Case14_P4", new FidoProtein("Case14_P4"));
		allProteins.put("Case14_P5", new FidoProtein("Case14_P5"));
		FidoPeptide case14A = new FidoPeptide();
		FidoPeptide case14B = new FidoPeptide();
		FidoPeptide case14C = new FidoPeptide();
		FidoPeptide case14D = new FidoPeptide();
		FidoPeptide case14E = new FidoPeptide();
		allProteins.get("Case14_P1").addPeptide(case14A);
		allProteins.get("Case14_P2").addPeptide(case14A);
		allProteins.get("Case14_P3").addPeptide(case14A);
		allProteins.get("Case14_P4").addPeptide(case14A);
		allProteins.get("Case14_P5").addPeptide(case14A);
		allProteins.get("Case14_P2").addPeptide(case14B);
		allProteins.get("Case14_P3").addPeptide(case14B);
		allProteins.get("Case14_P4").addPeptide(case14B);
		allProteins.get("Case14_P3").addPeptide(case14C);
		allProteins.get("Case14_P4").addPeptide(case14D);
		allProteins.get("Case14_P5").addPeptide(case14E);

		for (String fpString : allProteins.keySet()) {
			FidoProtein p = allProteins.get(fpString);
			p.generateSequence();
		}

		// write fasta
		BufferedWriter brf = new BufferedWriter(new FileWriter(new File("fido_target.fasta")));
		for (FidoProtein fp : allProteins.values()) {
			brf.write(">" + fp.name + "\n");
			brf.write(fp.sequence + "\n");
		}
		brf.close();
		BufferedWriter brfdecoy = new BufferedWriter(new FileWriter(new File("fido_deocy.fasta")));
		for (FidoProtein fp : allProteins.values()) {
			String reverseSeq = reverse(fp.sequence);
			brfdecoy.write(">decoy_" + fp.name + "\n");
			brfdecoy.write(reverseSeq + "\n");
		}
		brfdecoy.close();
		
		HashSet<FidoPeptide> allPeptides = new HashSet<FidoPeptide>();
		for (FidoProtein fp : allProteins.values()) {
			allPeptides.addAll(fp.peptides);
		}

		// write mgf
		BufferedWriter brm = new BufferedWriter(new FileWriter(new File("fido.mgf")));
		for (FidoPeptide fpep : allPeptides) {
			brm.write("BEGIN IONS\n");
			brm.write("TITLE=PEPTIDE_" + fpep.sequence + ", +2 y- and b-series\n");
			brm.write("PEPMASS=" + FragmentCalculator.calculatePepmass(fpep.sequence) + "\t2000000\n");
			brm.write("CHARGE=2+\n");
			brm.write("RTINSECONDS=100\n");
			brm.write("SCANS=25000\n");
			double[] array = FragmentCalculator.calculateFragmentIons(fpep.sequence);
			for (double val : array) {
				brm.write(val + "\t100000\n");
			}
			brm.write("END IONS\n");
		}
		brm.close();
	}

	private static String reverse(String sequence) {
		Stack<String> textStack = new Stack<String>();
		// push the strings to the stack
		for (char c : sequence.toCharArray()) {
		    textStack.push(""+ c);
		}
		// pop the strings and add to the text builder
		StringBuilder builder = new StringBuilder(""); 
		while (!textStack.empty()) {
		      builder.append(textStack.pop());
		}
		// get the final string
		String finalText =  builder.toString();
		return finalText;
	}

}
