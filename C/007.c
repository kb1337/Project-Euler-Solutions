#include <stdio.h>
#include <math.h>

#define TRUE 1
#define FALSE 0

int isPrime(int *n);

int main(void)
{
    int i = 2;
    int amount = 0;

    while (TRUE)
    {
        if (isPrime(&i))
        {
            if (++amount == 10001)
            {
                printf("%d\n", i);
                break;
            }
        }

        i++;
    }
}

int isPrime(int *n)
{
    for (long i = 2, sq = sqrt(*n); i < sq + 1; i++)
        if (*n % i == 0)
            return FALSE;
    return TRUE;
}
