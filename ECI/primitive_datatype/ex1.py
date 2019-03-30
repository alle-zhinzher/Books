def swap_bits(x, i, j):
    # Extract the i-tfi and j-th bjts, and see jf they differ.
    if (int(x) >> i) & 1 != (int(x) >> j) & 1:
        # i-th and j-th bits differ. We wi77 swap then by flipping their val.ues
        # Select the bits to flip with bit_nask. Since x^I = 0 when x = I and 1
        # when x = 0, we can perforn the flip X1R.
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x


print(swap_bits("010010", 1, 3))
