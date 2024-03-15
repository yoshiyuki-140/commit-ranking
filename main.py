import os, requests
from datetime import datetime
from dotenv import load_dotenv

# 複数のリポジトリURL
# 形式 : "https://github.com/ユーザー名/リポジトリ名",
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
# datetime(年, 月, 日, 時, 分, 秒)
since = datetime(2024, 3, 2, 0, 0, 0).isoformat() + "Z"  # ISO8601フォーマット
until = datetime(2024, 3, 19, 0, 0, 0).isoformat() + "Z"


# GitHubアクセストークン
# 環境変数のセッティング
load_dotenv()
access_token = os.environ["API_TOKEN"]

# GraphQLエンドポイント
endpoint = "https://api.github.com/graphql"


headers = {"Authorization": f"bearer {access_token}"}


def convert_repo_format(original_repos):
    """辞書の形式を変換する関数"""
    new_repos = {}
    for url, team_name in original_repos.items():
        # URLからユーザー名/リポジトリ名を抽出
        _, user_repo = url.split("github.com/")
        # 新しい辞書にチーム名とユーザー名/リポジトリ名をセット
        new_repos[team_name] = user_repo
    return new_repos


def get_commit_count(repo, since, until):
    """各リポジトリのコミット数を取得する関数"""
    owner, name = repo.split("/")
    query = """
    query($owner: String!, $name: String!, $since: GitTimestamp!, $until: GitTimestamp!) {
      repository(owner: $owner, name: $name) {
        defaultBranchRef {
          target {
            ... on Commit {
              history(since: $since, until: $until) {
                totalCount
              }
            }
          }
        }
      }
    }
    """
    variables = {"owner": owner, "name": name, "since": since, "until": until}
    response = requests.post(
        endpoint, json={"query": query, "variables": variables}, headers=headers
    )
    if response.status_code == 200:
        data = response.json()
        return data["data"]["repository"]["defaultBranchRef"]["target"]["history"][
            "totalCount"
        ]
    else:
        raise Exception(f"status code: {response.status_code}, {response.text}")


# 複数のリポジトリURL
# {チーム名} : {ユーザー名/リポジトリ名}の形式に変換
repos = convert_repo_format(repos)

commit_counts = {
    team: get_commit_count(repo, since, until) for team, repo in repos.items()
}

# コミット数でソートし、ランキングを出力
sorted_commit_counts = sorted(commit_counts.items(), key=lambda x: x[1], reverse=True)

for rank, (team, count) in enumerate(sorted_commit_counts, start=1):
    print(f"{rank}", f"team:{team}", f"{count}コミット", sep="/")
