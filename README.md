# Facebook-Hacker-Cup 2018


**Tourist**  

Overall, Alex will want to first see attractions 1 to N in order, then see them all a second time in the same order, then all a third time in the same order, and so on. 
If we write out an infinite sequence of attractions 1, 2, ..., N-1, N, 1, 2, ..., N-1, N, 1, ..., then Alex will see the first K attractions in this list on his first visit, the next K on his second visit, and so on. This means that, on his Vth visit, Alex will see the (K*(V-1)+i)th attraction in the list for i=1..K. We can convert each of these values into its corresponding attraction index between  1 and N using modulus, sort these indices in increasing order, and then output their corresponding attraction names in that order.


**Interception**  

Writing out how the polynomial will be evaluated once the order of operations is reversed, we end up with a series of N+2 terms all exponentiated together (right-associatively): (P_N * x) ^ ((N * P_{N-1}) * x) ^ ... ^ ((2 + P_1) * x) ^ ((1 + P_0) * x) ^ (0). The only way for such an expression to potentially evaluate to 0 is if the first term is equal to 0, as a^b ≠ 0 when a is a non-zero real number (unless b = -infinity, which isn't possible here). Since P_N is guaranteed to be non-zero, this means that the polynomial can only possibly evaluate to 0 when x = 0.
Now, when x = 0, it’s clear that each of the N+2 terms above is also equal to 0. So, we’re interested in evaluating the expression 0^0^...^0^0, with N+2 0’s. We can observe an alternating pattern based on the number of 0’s: 0^0 = 1, 0^0^0 = 0^1 = 0, 0^0^0^0 = 1, 0^0^0^0^0 = 0, and so on. So, this expression evaluates to 0 when the number of 0’s is odd, and to 1 when the number of 0’s is even. It follows that the polynomial has a single x-intercept at x = 0 when N is odd, and no x-intercepts when N is even, independent of its coefficients.
