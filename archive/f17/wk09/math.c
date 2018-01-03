#include <stdio.h>

int subtract (int a, int b) {
    return a - b;
}

int divide (int a, int* b) {
    return a / *b;
}

int do_math (int x, int y, int z) {
    int temp = subtract(x, y);
    temp = divide(z, &temp);
    return temp;
}

int main () {
    int temp;
    temp = do_math(10, 10, 20);
    printf("Result: %d\n", temp);
    return 0;
}
