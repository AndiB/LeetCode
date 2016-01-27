/*
Difficulty: Easy
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
*/

/* Thank you Kerningham ;-) */
int hammingWeight(uint32_t n) {
    uint32_t bits_set = 0;
    while (n!=0) {
        if (n & 0x01) {
            bits_set++;
        }
        n = n >> 1;
    }
    return bits_set;
    
}
