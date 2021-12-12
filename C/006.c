#include <stdio.h>
#include <math.h>

double sumSquare(const int *n);
double squareSum(const int *n);

int main(void)
{
    int number = 100;

    printf("%.f\n", sumSquare(&number) - squareSum(&number));

    return 0;
}

double sumSquare(const int *n)
{
    double sum = 0;
    for (int i = 1; i < *n + 1; i++)
        sum += i;
    return pow(sum, 2);
}

double squareSum(const int *n)
{
    double sum = 0;
    for (int i = 1; i < *n + 1; i++)
        sum += pow(i, 2);
    return sum;
}
