#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int check_answer(char *ans) {
    
    int ans_flag = 0;
    char ans_buf[34];

    printf("ans_buf is at address %p\n", &ans_buf);

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

    printf("About to exit!\n");
    fflush(stdout);

    /* system("/bin/sh"); // used for NX exploration */
}
