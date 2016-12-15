
import java.util.Scanner;

public class Scrabble {

	public static void main(String[] args) {
		Scanner kb = new Scanner(System.in);
		System.out.println("Enter your letters: ");
		String letters = kb.next();
		System.out.println("Enter your word: ");
		String word = kb.next();
		kb.close();
		System.out.println("Can you make that word from your letters: " + scrabble(letters, word));

	}

	public static boolean scrabble(String rack, String test) {
		boolean word = false;
		StringBuilder rackSB = new StringBuilder(rack);
		int match = 0;
		for (int i = 0; i < test.length(); i++) {
			for (int x = 0; x < rackSB.length(); x++) {
				if(test.charAt(i) == rackSB.charAt(x)){
					rackSB.deleteCharAt(x);
					match++;
					break;
				}
			}
		}
		if(match == test.length()){
			word = true;
		}

		return word;
	}

}
