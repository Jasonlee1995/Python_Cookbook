import subprocess


def print_hello_world():
    print('Hello World!')

def run_terminal_command(terminal_command):
    subprocess.run(terminal_command, shell=True)


if __name__ == '__main__':
    terminal_command = "python -c 'from subprocess_example import print_hello_world; print_hello_world()'"
    run_terminal_command(terminal_command)

    '''print result
    Hello World!
    '''