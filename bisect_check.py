import shlex
import subprocess


def check():
    cmd = shlex.split("python -m pytest glotaran_tests")
    result = subprocess.run(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False
    )

    print(result.stdout.decode())  # For debugging
    if any(
        [
            substring in result.stdout
            for substring in [b"AttributeError", b"SyntaxError"]
        ]
    ):
        print("skipped!")
        return 125
    elif result.returncode == 0:
        print("good")
        return 0
    else:
        print("bad")
        return 1


if __name__ == "__main__":
    exit(check())
