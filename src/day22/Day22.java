package day22;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.stream.IntStream;

public class Day22 {
	
	public static int[] getCoefficients(String line) {
		int[] coeffs = new int[2];
		
		String[] words = line.split(" ");
		if (words[0].compareTo("cut")==0) {
			coeffs[0] = 1;
			coeffs[1] = Integer.parseInt(words[1]);
		} else if (words[1].compareTo("with") == 0) {
			coeffs[0] = Integer.parseInt(words[3]);
			coeffs[1] = 0;
		} else {
			coeffs[0] = -1;
			coeffs[1] = -1;
		}
		
		return coeffs;
	}
	
	public static int calcNewPos(int[] coeffs, int x) {
		return coeffs[0]*x + coeffs[1];
	}
	
	public static int part1(ArrayList<String> lines) {
		// Setup the deck
		int m = 10;
		int[] deck = IntStream.range(0, m).toArray();
		
		// Get the final coefficients numbers
		int[] coeffs = null;
		for (String line:lines) {
			if (coeffs == null) {
				coeffs = getCoefficients(line);
			} else {
				int[] coeffs2 = getCoefficients(line);
				coeffs[0] = (coeffs[0] * coeffs2[0]) % m;
				coeffs[1] = ((coeffs[1] * coeffs2[0]) + coeffs2[1]) % m;
			}
		}
		
		// Track position 9 through these coefficients
		for (int i =0; i<m; i++)
			System.out.println("Pos " + i + ": " + calcNewPos(coeffs, i) % m);
		
		return -1;
	}
	
	public static int part2(ArrayList<String> lines) {
		return 0;
	}
	
	public static void main(String[] argv) {
		BufferedReader input = null;
//		String filename="src/day22/input";
		String filename="src/day22/sample1";
//		String filename="src/day22/sample2";
//		String filename="src/day22/sample3";
//		String filename="src/day22/sample4";
		
		ArrayList<String> lines = new ArrayList<>();
		
		try {
			// Open the input file
			input = new BufferedReader(new FileReader(filename));
			
			// Read every line
			String line;
			while ((line = input.readLine()) != null)
				if (line.length()>0)
					lines.add(line);
		} catch (Exception e) {
			System.out.println("Problem reading input");
			System.exit(1);
		}

		System.out.println("Part 1: " + part1(lines));
		System.out.println("Part 2: " + part2(lines));

	}
}

