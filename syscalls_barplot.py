import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def process_strace_output(file):
    calls = {"name": [], "amount": []}
    with open(file, 'r') as f:
        f.readline()
        f.readline()
        for line in f:
            if not line.startswith("-"):
                line = line.strip().split()
                calls["name"].append(line[-1])
                calls["amount"].append(int(line[3]))
            else:
                break

    return calls


def barplot(data):
    df = pd.DataFrame(data=data)
    df = df.sort_values(by=["amount"], ascending=False)
    sns.barplot(x="amount", y="name", data=df, palette="Blues_d")


data = process_strace_output("ls.txt")
barplot(data)
plt.show()