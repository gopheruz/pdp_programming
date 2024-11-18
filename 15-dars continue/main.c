#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main() {
    int n;
    scanf("%d", &n);   
    int bufferSize = n * n * 5;  
    char *pattern = (char *)malloc(bufferSize * sizeof(char));

    if (pattern == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return 1;
    }
    pattern[0] = '\0'; 
    for (int i = n / 2; i < n; i += 2) {
        for (int j = 1; j < n - i; j += 2) {
            strcat(pattern, " ");
        }
        for (int j = 1; j <= i; j++) {
            strcat(pattern, "*");
        }
        for (int j = 1; j <= n - i; j++) {
            strcat(pattern, " ");
        }
        for (int j = 1; j <= i; j++) {
            strcat(pattern, "*");
        }
        strcat(pattern, "\n");
    }

    for (int i = n; i > 0; i--) {
        for (int j = 0; j < n - i; j++) {
            strcat(pattern, " ");
        }
        for (int j = 1; j < i * 2; j++) {
            strcat(pattern, "*");
        }
        strcat(pattern, "\n");
    }

    printf("%s", pattern);

    free(pattern);

    return 0;
}
