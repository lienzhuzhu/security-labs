import subprocess, os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('program', type=str, help='program to fuzz')
parser.add_argument('arg_pattern', type=str, help='char to build up fuzz test argument')
parser.add_argument('pattern_max', type=int, help='maximum number of arg_pattern chars in a test case')
args = parser.parse_args()

# The following variables control the command line
program = args.program
arg_pattern = args.arg_pattern
pattern_max = args.pattern_max

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

