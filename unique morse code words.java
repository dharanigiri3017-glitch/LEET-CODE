import java.util.HashSet;

class Solution {
    public int uniqueMorseRepresentations(String[] words) {

        String[] morse = {
            ".-", "-...", "-.-.", "-..", ".", "..-.",
            "--.", "....", "..", ".---", "-.-", ".-..",
            "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-",
            "-.--", "--.."
        };

        HashSet<String> set = new HashSet<>();

        for (String word : words) {
            StringBuilder transformation = new StringBuilder();

            for (char c : word.toCharArray()) {
                transformation.append(morse[c - 'a']);
            }

            set.add(transformation.toString());
        }

        return set.size();
    }
}
