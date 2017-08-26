#include <stdio.h>

int recurse(int add_me) {
    if (add_me == 1) {
        return add_me;
    }
    return recurse(add_me + add_me);
}

int main() {
    printf("%d\n", recurse(2));
}
