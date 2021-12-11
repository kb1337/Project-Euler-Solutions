#include <stdio.h>
#include <math.h>

#define TRUE 1
#define FALSE 0

int isPrime(long long *n);
void primeFactors(long long *n);

int main(void)
{
    long long number = 600851475143;

    primeFactors(&number);
}

int isPrime(long long *n)
{
    for (long i = 2, sq = sqrt(*n); i < sq + 1; i++)
        if (*n % i == 0)
            return FALSE;
    return TRUE;
}

void primeFactors(long long *n)
{
    for (long long i = 2, sq = sqrt(*n); i < sq + 1; i++)
    {
        if (*n % i == 0 && isPrime(&i) == TRUE)
        {
            while (*n % i == 0)
                *n /= i;
            printf("%lld\n", i);
        }
    }
    if (*n != 1)
        printf("%lld", *n);
}
