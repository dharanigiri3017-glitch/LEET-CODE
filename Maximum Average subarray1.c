#include <stdio.h>

double findMaxAverage(int* nums, int numsSize, int k) {
    // Step 1: Calculate the sum of the first 'k' elements
    double current_sum = 0;
    for (int i = 0; i < k; i++) {
        current_sum += nums[i];
    }
    
    // Initialize max_sum with the sum of the first window
    double max_sum = current_sum;
    
    // Step 2: Slide the window across the rest of the array
    for (int i = k; i < numsSize; i++) {
        // Add the next element and remove the first element of the previous window
        current_sum += nums[i] - nums[i - k];
        
        // Update max_sum if the new window's sum is larger
        if (current_sum > max_sum) {
            max_sum = current_sum;
        }
    }
    
    // Step 3: Return the maximum average
    return max_sum / k;
}
