"""http://rosalind.info/problems/iprb/"""

k=23.0
m=29.0
n=27.0
p=n+m+k

prob= k/p+  (m/p)*( (4.0*k+3.0*m+2.0*n-3.0)/(4.0*(p-1.0) ) )   + (n/p)*( (2.0*k+m) / (2.0*(p-1.0) ) )

print round(prob,5)
