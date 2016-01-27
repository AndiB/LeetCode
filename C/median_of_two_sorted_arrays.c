/*
Difficulty: Hard
There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
*/
double findMedianSortedArrays(int A[], int m, int B[], int n) {
    int C[n+m];
    int i,a,b;
    a = b = 0;
    
    for (i = 0 ; i < m+n; i++) {
        if (a<m && b < n) {
            if(A[a] < B[b]) {
                C[i] = A[a];
                a++;
            } else {
                C[i] = B[b];
                b++;
            }
        } else if (a<m) {
            C[i] = A[a];
            a++;
        } else {
                C[i] = B[b];
                b++;            
        }
        
        
    }
    if ((m+n)%2==0) {
        return (((double) C[(m+n)/2])+C[(m+n)/2-1])/2;
    } 
    return (double) C[(m+n)/2];
    
}
