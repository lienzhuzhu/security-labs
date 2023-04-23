#include <stdio.h>

int main() {
	char buf[100];
	char s[100];
	int x = 1;
	fgets(s, 100, stdin);
	snprintf(buf, sizeof(buf), s);
	printf("Buffer size is: (%d) \nData input: %s \n", strlen(buf), buf);
	printf("X equals: %d/ in hex: %x\nMemory address for x: (%p) \n", x, x, &x);
	return 0;
}
