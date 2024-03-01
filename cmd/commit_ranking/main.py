import requests
from datetime import datetime

# 複数のリポジトリURL
repos = [
    # "https://github.com/ユーザー名/リポジトリ名1",
    # "https://github.com/ユーザー名/リポジトリ名2",
    # その他のリポジトリURLを追加
    "https://github.com/yoshiyuki-140/atcoder",
]

# 特定期間の設定
since = datetime(2024, 3, 2, 0, 0, 0).isoformat() + "Z"  # ISO8601フォーマット
until = datetime(2024, 3, 19, 0, 0, 0).isoformat() + "Z"

# コミット数を格納するリスト
commit_counts = []

for repo_url in repos:
    owner, repo = repo_url.split("/")[-2:]
    commits_url = f"https://api.github.com/repos/{owner}/{repo}/commits?since={since}&until={until}"

    response = requests.get(commits_url)
    if response.status_code == 200:
        commits = response.json()
        commit_counts.append((f"{owner}/{repo}", len(commits)))
    else:
        print(
            f"リポジトリ '{owner}/{repo}' のデータ取得に失敗しました。ステータスコード: {response.status_code}"
        )

# コミット数でソートし、ランキングを作成
from pprint import pprint

pprint(commit_counts)

commit_counts.sort(key=lambda x: x[1], reverse=True)

# ランキングを表示
print("リポジトリのコミット数ランキング:")
for rank, (repo, count) in enumerate(commit_counts, start=1):
    print(f"{rank}. {repo}: {count} コミット")
