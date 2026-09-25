int daysFromStart(int y, int m, int d) {
    int days = 0;
    int monthDays[] = {31,28,31,30,31,30,31,31,30,31,30,31};

    for (int year = 1971; year < y; year++) {
        if ((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0))
            days += 366;
        else
            days += 365;
    }

    for (int month = 1; month < m; month++) {
        days += monthDays[month - 1];

        if (month == 2 &&
            ((y % 400 == 0) || (y % 4 == 0 && y % 100 != 0)))
            days++;
    }

    days += d;

    return days;
}

int daysBetweenDates(char* date1, char* date2) {
    int y1, m1, d1;
    int y2, m2, d2;

    sscanf(date1, "%d-%d-%d", &y1, &m1, &d1);
    sscanf(date2, "%d-%d-%d", &y2, &m2, &d2);

    int days1 = daysFromStart(y1, m1, d1);
    int days2 = daysFromStart(y2, m2, d2);

    return days1 > days2 ? days1 - days2 : days2 - days1;
}
