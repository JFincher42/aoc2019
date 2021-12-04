package day22;

import java.io.BufferedReader;
import java.io.FileReader;
import java.math.BigInteger;
import java.util.ArrayList;

public class Day22 {
	
	public static long[] getCoefficients(String line) {
		long[] coeffs = new long[2];
		long a, b;
		
		String[] words = line.split(" ");
		if (words[0].compareTo("cut")==0) {
			// Cutting the deck with n cards moves pos x to pos x - n mod m 
			a = 1;
			b = Integer.parseInt(words[1]) * -1;
		} else if (words[1].compareTo("with") == 0) {
			// Deal with incremenht n moves pos x to pos x*n mod m  
			a = Integer.parseInt(words[3]);
			b = 0;
		} else {
			// Deal into new deck move pos x to pos -x - n mod m
			a = -1;
			b = -1;
		}
		coeffs[0]=a; coeffs[1]=b;
		return coeffs;
	}
	
	public static BigInteger calcNewPos(long[] coeffs, long x) {
		BigInteger a = BigInteger.valueOf(coeffs[0]), b = BigInteger.valueOf(coeffs[1]);
		return a.multiply(BigInteger.valueOf(x)).add(b);
	}
	
	public static long part1(ArrayList<String> lines) {
		// Setup the deck
//		BigInteger m = BigInteger.valueOf(10);  // For sample runs only
		BigInteger m = BigInteger.valueOf(10007);
		
		// Get the final coefficients numbers
		long[] coeffs = null;
		for (String line:lines) {
			if (coeffs == null) {
				coeffs = getCoefficients(line);
			} else {
				long[] coeffs2 = getCoefficients(line);
				coeffs = compose(coeffs, coeffs2, m);
			}
		}
		
		return calcNewPos(coeffs, 2019).mod(m).intValue();
	}
	
	public static long[] compose(long[] f, long[] g, BigInteger m) {
		// Compose two LCF's together. Compuites what g(f(x)) would be.
		
		// These definition just make life easier
		BigInteger a = BigInteger.valueOf(f[0]), b =BigInteger.valueOf(f[1]);
		BigInteger c = BigInteger.valueOf(g[0]), d = BigInteger.valueOf(g[1]);
		
		// Compose to (a*c mod m, b*c + d mod m)
		long newA = a.multiply(c).mod(m).longValue();
		long newB = b.multiply(c).add(d).mod(m).longValue();
		
		return new long[] {newA, newB};
	}
	
	public static long[] powerMod(long[] coeffs, BigInteger exp, BigInteger m) {
		// Iterative LCF exponentiation by squaring algorithm
		// Start with a multiplicative identity for coefficients
		long[] g = {1l, 0l};
		
		while (exp.longValue() > 0) {
			if (exp.remainder(BigInteger.TWO).intValue()==1) {
				// It's odd, so we can compose g:f into g
				g = compose(g, coeffs, m);
			} 
			// Halve the exponent
			exp = exp.divide(BigInteger.TWO);
			// Square our coefficients
			coeffs = compose(coeffs, coeffs, m);
		}
		return g;
	}
	
	public static long[] powerMod2(long[] coeffs, BigInteger exp, BigInteger m) {
		// Recursive LCF exponentiation by squaring algorithm
		
		if (exp.longValue() == 0 )
			return new long[] {1,0};
		
		long[] temp = powerMod2(coeffs, exp.divide(BigInteger.TWO), m);
		
		if (exp.remainder(BigInteger.TWO).intValue()==0) {
			return compose(temp, temp, m);
		} else {
			temp = compose(temp, temp, m);
			return compose(temp, coeffs, m);
		}
		
	}
	
	public static long part2(ArrayList<String> lines) {
		BigInteger m = BigInteger.valueOf(119315717514047l);   // Deck Size
		BigInteger k = BigInteger.valueOf(101741582076661l);   // Num Shuffles
		
		// Part 1: Compose F
		long[] coeffs = null;
		for (String line:lines) {
			if (coeffs == null) {
				coeffs = getCoefficients(line);
			} else {
				long[] coeffs2 = getCoefficients(line);
				coeffs = compose(coeffs, coeffs2, m);
			}
		}
		
		// Part 2: Compose F^k
		// Coeffs has F in it
//		long [] coeffsPower = powerMod(coeffs, k, m);
		long [] coeffsPower = powerMod2(coeffs, k, m);
		
		// Part 3: Figure out the modular multiplicative inverse of coeffsPower[0], which is A
		// We can then multiply that by coeffsPower[1] and x, which is 2020
		// Do I need all these BigIntegers? No, but it's easier to read this way IMO. Memory is cheap.
		
		BigInteger bigX = BigInteger.valueOf(2020);
		BigInteger inverseA = BigInteger.valueOf(coeffsPower[0]).modInverse(m);
		BigInteger numerator = bigX.subtract(BigInteger.valueOf(coeffsPower[1]));
		BigInteger result = numerator.multiply(inverseA).mod(m);
		return result.longValue();
		
	}
	
	public static void main(String[] argv) {
		BufferedReader input = null;
		String filename="src/day22/input";
//		String filename="src/day22/sample1";
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

