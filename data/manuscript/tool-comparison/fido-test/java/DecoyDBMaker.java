package fidodata;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class DecoyDBMaker {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new FileReader(new File("uniprot-filtered-reviewed_yes+AND+organism__Escherichia+coli+(strain+K12--.fasta")));
		BufferedWriter bw = new BufferedWriter(new FileWriter(new File("ecoli_decoy.fasta")));
		String line = br.readLine();
		while (line != null) {
			if (line.startsWith(">sp")) {
				bw.append(line.replaceAll(">sp", ">decoy_sp") + "\n");
			} else if (line.equals("")) {
				// skip empty 
			} else {
				// reverse
				String s = "";
				for (char c : line.toCharArray()) {
					s = (c + "").concat(s);
				}
				bw.append(s + "\n");
			}
			
			line =  br.readLine();
		}
		bw.flush();
		bw.close();
		br.close();
		System.out.println("finished");
	}

}
