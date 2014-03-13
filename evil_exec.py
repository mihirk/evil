import subprocess
import sys

def execute_shell_command(*command):
    return subprocess.call(*command)

def compile_c_program(filename, compiled_filename):
    return ['cc', filename, '-o', compiled_filename]

def get_c_filename():
    return sys.argv[1]

def get_compiled_filename():
    return sys.argv[2]

def run_c_program(filename):
    return ['./'+ filename]

execute_shell_command(compile_c_program(get_c_filename(), get_compiled_filename()))
execute_shell_command(run_c_program(get_compiled_filename()))
