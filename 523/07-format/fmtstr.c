#include <stdio.h>
int main(int argc, char **argv) {
	char buf[200];
	int val = 1;
	printf("buf is at: %p\n", &buf);
	printf("val is at %p\n", &val);
	if (argc != 2) {
		printf("usage: %s [user string]\n", argv[0]);
		return 1;
	}
	snprintf(buf, sizeof(buf), argv[1]);
	printf("buffer is %s\n", buf);
	printf("val is %d/%#x (@ %p)\n", val, val, &val);
	return 0;
}
