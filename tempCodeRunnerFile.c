#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data, height;
    struct Node *left, *right;
};

int max(int a, int b) {
    return (a > b) ? a : b;
}

int height(struct Node *n) {
    if (n == NULL)
        return 0;
    return n->height;
}

int balanceFactor(struct Node *n) {
    if (n == NULL)
        return 0;
    return height(n->left) - height(n->right);
}

int main() {
    struct Node *root = malloc(sizeof(struct Node));

    root->data = 10;
    root->left = NULL;
    root->right = NULL;
    root->height = 1;

    printf("AVL Tree Node: %d", root->data);
    printf("\nBalance Factor: %d", balanceFactor(root));

    return 0;
}