import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os


def process_strace_output(file):
    calls = {"syscall": [], "calls": []}
    with open(file, 'r') as f:
        f.readline()
        f.readline()
        for line in f:
            if not line.startswith("-"):
                line = line.strip().split()
                calls["syscall"].append(line[-1])
                calls["calls"].append(int(line[3]))
            else:
                break

    return calls


def barplot(data, title):
    df = pd.DataFrame(data=data)
    df = df.sort_values(by=["calls"], ascending=False)

    # plt.rcParams["figure.figsize"] = (6, 8)

    sns.barplot(x="calls", y="syscall", data=df, palette="Blues_d")
    plt.title(title)
    plt.savefig("barplots/{}.png".format(title), bbox_inches="tight")
    plt.close()


dir = "ipc_syscalls"
for f in os.listdir(dir):
    file = dir + "/" + f
    data = process_strace_output(file)
    barplot(data, f[:-4])
