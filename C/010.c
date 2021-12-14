#include <stdio.h>
#include <math.h>

#define TRUE 1
#define FALSE 0

int isPrime(int *n);

int main(void)
{
    long long sum = 0;

    for (int i = 2; i < 2000000; i++)
        if (isPrime(&i))
            sum += i;

    printf("%lld\n", sum);
}

int isPrime(int *n)
{
    for (long i = 2, sq = sqrt(*n); i < sq + 1; i++)
        if (*n % i == 0)
            return FALSE;
    return TRUE;
}
