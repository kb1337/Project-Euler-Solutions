#include <stdio.h>

#define TRUE 1
#define FALSE 0

int divideBelow20(int *n);

int main(void)
{
    int i = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19;

    while (TRUE)
    {
        if (divideBelow20(&i))
        {
            printf("%d\n", i);
            break;
        }
        i++;
    }
}

int divideBelow20(int *n)
{
    for (int i = 1; i < 20; i++)
    {
        if (*n % i != 0)
            return FALSE;
    }
    return TRUE;
}