char* generateTheString(int n) {
    static char result[501];
    int i;

    if (n % 2 == 1) {
        for (i = 0; i < n; i++)
            result[i] = 'a';
    } else {
        for (i = 0; i < n - 1; i++)
            result[i] = 'a';

        result[n - 1] = 'b';
    }

    result[n] = '\0';

    return result;
}
