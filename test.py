import pickle
from pprint import pprint

with open("commit_counts.pkl", "rb") as f:
    sorted_commit_counts = pickle.load(f)


for rank, (team, count) in enumerate(sorted_commit_counts, start=1):
    pprint(rank, team, count)
