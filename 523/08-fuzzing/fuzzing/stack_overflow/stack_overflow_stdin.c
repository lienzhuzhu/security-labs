#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {

	int value = 5;
	char buffer_one[8], buffer_two[8];
	char s[64];

	strcpy(buffer_one, "one");
	strcpy(buffer_two, "two");
	
	printf("[BEFORE] buffer_two is at %p and contains \'%s\'\n", buffer_two, buffer_two);
	printf("[BEFORE] buffer_one is at %p and contains \'%s\'\n", buffer_one, buffer_one);
	printf("[BEFORE] value is at %p and contains %d (0x%08x)\n\n", &value, value, value);

	gets(s);
	printf("[STRCPY] copying %d bytes into buffer_two\n\n", strlen(s));
	strcpy(buffer_two, s);

	printf("[BEFORE] buffer_two is at %p and contains \'%s\'\n", buffer_two, buffer_two);
	printf("[BEFORE] buffer_one is at %p and contains \'%s\'\n", buffer_one, buffer_one);
	printf("[BEFORE] value is at %p and contains %d (0x%08x)\n\n", &value, value, value);

}
