def separate_syscalls(file):
    with open(file, "r") as f:
        line = f.readline()
        while True:
            if not (line.startswith("openat") and line.find("locale-archive") != -1):
                line = f.readline()
            else:
                break
        f.readline()
        f.readline()

        program_syscalls = ""
        for line in f:
            program_syscalls += line

    return program_syscalls


print(separate_syscalls("strace_outputs/strace-ls-output.txt"))

