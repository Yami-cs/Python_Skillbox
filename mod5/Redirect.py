import sys

class Redirect:
    def __init__(self, stdout=None, stderr=None):
        self.stdout = stdout
        self.stderr = stderr

    def __enter__(self):
        self.old_stdout, self.old_stderr = sys.stdout, sys.stderr
        if self.stdout is not None:
            sys.stdout = self.stdout
        if self.stderr is not None:
            sys.stderr = self.stderr

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout, sys.stderr = self.old_stdout, self.old_stderr
        if exc_type is not None:
            print(exc_val, file=self.stderr)
