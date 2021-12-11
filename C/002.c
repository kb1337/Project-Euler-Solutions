#include <stdio.h>

int main(void)
{
    int a = 1, b = 1, total = 0, tmp;

    while (b < 4000000)
    {
        tmp = a + b;
        a = b;
        b = tmp;

        if (b % 2 == 0)
            total += b;
    }

    printf("Total: %d", total);
}
