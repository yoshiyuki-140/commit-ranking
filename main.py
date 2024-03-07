import requests
from datetime import datetime

# 複数のリポジトリURL
# 形式 : "https://github.com/ユーザー名/リポジトリ名1",
repos = {
    # {チーム名}
    # {リポジトリURL} : {チーム名}
    # ------------------------------
    # パモ
    "https://github.com/Yukkin395/hackit_terayuki": "パモ",
    # 味玉
    "https://github.com/hamanakayuya/ajitama": "味玉",
    # s3cprj
    "https://github.com/s3cprj/mega-evolution": "s3cprj",
    # 天丼
    "https://github.com/elca-hub/hackit_2024": "天丼",
    # CDA
    "https://github.com/HIROMU522/AnzenNavi": "CDA",
    # 頑張りたいと感じている
    "https://github.com/HANABUSAHayato/AWS": "頑張りたいと感じている",
    # タイポ戦隊
    "https://github.com/Sakauchi444/argut_ai": "タイポ戦隊",
    # スマプロ
    "https://github.com/NonokaM/hackit-vol2-smapro": "スマプロ",
    # 野良猫
    "https://github.com/Hackit-Nora-2024/KIT-Board": "野良猫",
}

# 特定期間の設定
since = datetime(2024, 3, 2, 0, 0, 0).isoformat() + "Z"  # ISO8601フォーマット
until = datetime(2024, 3, 19, 0, 0, 0).isoformat() + "Z"


# GitHub APIを使ってコミット数を取得する関数
def get_commit_count(repo_url, since, until):
    # リポジトリのGitHub API URLを構築
    repo_name = repo_url.replace("https://github.com/", "")
    api_url = (
        f"https://api.github.com/repos/{repo_name}/commits?since={since}&until={until}"
    )

    # GitHub APIを呼び出し
    response = requests.get(api_url)

    # レスポンスからコミット数を取得
    if response.status_code == 200:
        return len(response.json())
    else:
        return 0


# 各リポジトリのコミット数を取得し、チーム名と組み合わせて辞書に格納
commit_counts = {
    team: get_commit_count(repo, since, until) for repo, team in repos.items()
}

# コミット数でソートし、ランキングを出力
sorted_commit_counts = sorted(commit_counts.items(), key=lambda x: x[1], reverse=True)


for rank, (team, count) in enumerate(sorted_commit_counts, start=1):
    print(f"{rank}", f"team:{team}", f"{count}コミット", sep="/", end="\n")
