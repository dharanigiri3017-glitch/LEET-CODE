import java.util.*;

class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {

        // Store banned words
        HashSet<String> bannedSet = new HashSet<>();

        for (String word : banned) {
            bannedSet.add(word);
        }

        // Remove punctuation and convert to lowercase
        paragraph = paragraph.toLowerCase();
        paragraph = paragraph.replaceAll("[!?',;.]", " ");

        // Split into words
        String[] words = paragraph.split("\\s+");

        // Count word frequencies
        HashMap<String, Integer> count = new HashMap<>();

        String answer = "";
        int max = 0;

        for (String word : words) {

            if (bannedSet.contains(word)) {
                continue;
            }

            count.put(word, count.getOrDefault(word, 0) + 1);

            if (count.get(word) > max) {
                max = count.get(word);
                answer = word;
            }
        }

        return answer;
    }
}
