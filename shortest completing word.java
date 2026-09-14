class Solution {
    public String shortestCompletingWord(String licensePlate, String[] words) {

        int[] need = new int[26];

        // Count letters in licensePlate
        for (char c : licensePlate.toLowerCase().toCharArray()) {
            if (c >= 'a' && c <= 'z') {
                need[c - 'a']++;
            }
        }

        String answer = "";

        for (String word : words) {
            int[] count = new int[26];

            // Count letters in the word
            for (char c : word.toCharArray()) {
                count[c - 'a']++;
            }

            boolean complete = true;

            // Check if word contains all required letters
            for (int i = 0; i < 26; i++) {
                if (count[i] < need[i]) {
                    complete = false;
                    break;
                }
            }

            // Update shortest word
            if (complete) {
                if (answer.equals("") || word.length() < answer.length()) {
                    answer = word;
                }
            }
        }

        return answer;
    }
}
