import subprocess, os

# The following variables control the command line
program = "./ans_check7 "
arg_pattern = 'a'
pattern_max = 100

for i in range(pattern_max):
	print("Trying input with length", i)
	cs = program + " " + arg_pattern*i
	print("Command: %s" % cs)
	print("******************")
	proc = subprocess.Popen([cs], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	print(proc.communicate()[0])
	print("******************")
	print("Return value: %i, %s" % (proc.returncode, os.strerror(proc.returncode)))
	print()

