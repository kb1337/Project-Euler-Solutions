#include <stdio.h>

int main(void)
{
    int total = 0;
    for (int i = 3; i < 1000; i++)
    {
        if (i % 3 == 0 || i % 5 == 0)
            total += i;
    }
    printf("Total: %d", total);
}