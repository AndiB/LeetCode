/*
Difficulty: Hard
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

*/

/* not linear :( */
void merge (int *a, int n, int m) {
    int i, j, k;
    int *x = malloc(n * sizeof (int));
    for (i = 0, j = m, k = 0; k < n; k++) {
        x[k] = j == n      ? a[i++]
             : i == m      ? a[j++]
             : a[j] < a[i] ? a[j++]
             :               a[i++];
    }
    for (i = 0; i < n; i++) {
        a[i] = x[i];
    }
    free(x);
}
 
void merge_sort (int *a, int n) {
    if (n < 2)
        return;
    int m = n / 2;
    merge_sort(a, m);
    merge_sort(a + m, n - m);
    merge(a, n, m);
}
 
int maximumGap(int num[], int n) {
    if (n < 2) {
        return 0;
    }
    
    
    int i = 1;
    int gap = 0;
    
    //sort
    merge_sort(num, n);
    
    // find gap
    for (i = 1; i < n; i++) {
        if (num[i] - num[i-1] > gap) {
            gap = num[i] - num [i-1];
        } else if (num[i-1] - num[i] > gap) {
            gap =  num[i-1] - num[i];    
        
        }
    }

    return gap;
    
    
}
