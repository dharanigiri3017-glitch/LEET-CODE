class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int originalColor = image[sr][sc];

        // If the color is already the same, no changes needed
        if (originalColor == color) {
            return image;
        }

        dfs(image, sr, sc, originalColor, color);

        return image;
    }

    private void dfs(int[][] image, int r, int c, int originalColor, int color) {
        // Check boundaries
        if (r < 0 || r >= image.length ||
            c < 0 || c >= image[0].length) {
            return;
        }

        // Stop if pixel has a different color
        if (image[r][c] != originalColor) {
            return;
        }

        // Change the color
        image[r][c] = color;

        // Up
        dfs(image, r - 1, c, originalColor, color);

        // Down
        dfs(image, r + 1, c, originalColor, color);

        // Left
        dfs(image, r, c - 1, originalColor, color);

        // Right
        dfs(image, r, c + 1, originalColor, color);
    }
}
