import subprocess

# Run the `nodejs` binary, driven by python code
#
#   Start an interpreter
#
#   $ python -m node
#
def main():
    # Synchronous blocking call, wait for an exit code
    exit = subprocess.run(['node'])

    # Raises CalledProcessError if returncode != 0
    exit.check_returncode()


if __name__ == '__main__':
    main()
