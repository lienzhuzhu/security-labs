#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int check_answer(char *ans) {

    int ans_flag = 0;
    char ans_buf[16];

    strcpy(ans_buf, ans);

    if (strcmp(ans_buf, "forty-two") == 0)
        ans_flag = 1;

    return ans_flag;

}

int main(int argc, char *argv[]) {

    if (argc < 2) {
        printf("Usage: %s <answer>\n", argv[0]);
        exit(0);
    }
    if (check_answer(argv[1])) {
        printf("Right answer!\n");
    } else {
        printf("Wrong answer!\n");
    }

}
