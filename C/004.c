#include <stdio.h>
#include <stdlib.h>

#define TRUE 1
#define FALSE 0

int isPalindrome(int *number);

int main(void)
{
    int largestNum = 0;

    for (int i = 100; i < 1000; i++)
    {
        for (int j = 100; j < 1000; j++)
        {
            int product = i * j;

            if (isPalindrome(&product) == TRUE && product > largestNum)
                largestNum = product;
        }
    }

    printf("%d\n", largestNum);

    return 0;
}

int isPalindrome(int *number)
{
    // count number of digits in *number for memory allocation
    int tmp = *number;
    int length = 0;
    do
    {
        tmp /= 10;
        length++;
    } while (tmp != 0);

    // convert int to string
    char *n = malloc(sizeof(char) * (length + 1));
    if (NULL == n)
        exit(EXIT_FAILURE);

    sprintf(n, "%d", *number);

    for (int i = 0; i < length / 2; i++)
    {
        if (n[i] != n[length - 1 - i])
        {
            free(n);
            return FALSE;
        }
    }
    free(n);
    return TRUE;
}
