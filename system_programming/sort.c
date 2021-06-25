#include <stdio.h>
#include <stdlib.h>

// 値を入れ替える
void swap (int *x, int *y) {
    int tmp;

    tmp = *x;
    *x = *y;
    *y = tmp;
}

// バブルソート
void bubble_sort (int array[], int array_size) {
    int i, j;

    for (i=0; i<array_size-1; i++) {
        for (j=array_size-1; j>=i+1; j--) {
            if (array[j] < array[j-1]) { 
                swap(&array[j], &array[j-1]);
            }
        }
    }
}

int main (int argc, char *argv[]) {
    int size;
    size = atoi(argv[1]);
    int a[size];

    for (int i=0; i<size; i++) {
        a[i] = rand();
    }

    bubble_sort(a, size);

    printf("After sort: ");
    for (int i=0; i<size-1; i++) {
        printf("%d\n", a[i]);
    }

    return 0;
}