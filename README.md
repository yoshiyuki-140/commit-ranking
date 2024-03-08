# commit-ranking
hackit vol2 commit ranking 

- 以下のshellの表記はPowerShellの表記です

# 使い方

1. リポジトリをクローンする
    ```shell
    git clone https://github.com/yoshiyuki-140/commit-ranking.git
    ```

1. "個人用アクセストークン(classic)"を取得する
    - 作成場所
      - https://github.com/settings/tokens/new

    - 権限に関して
        - 権限は基本的に`repo`のみで良い

        1. `repo`にチェックを入れる
        1. \[画面下部のボタン\]を押してアクセストークンを取得する


2. main.pyと同階層に`.env`ファイルを作成し、アクセストークンを`.env`に記述する
    ```shell
    API_TOKEN = "{ghpから始まるアクセストークン}"
    ```
    - ファイル作成後のディレクトリ構造
        ```shell
        > tree /f
        Folder PATH listing for volume winDB
        Volume serial number is 5E3B-DA1C
        D:.
        │  .env
        │  .gitignore
        │  LICENSE
        │  main.py
        │  README.md
        ```

3. `main.py`を実行する
    ```shell
    python main.py
    ```

# 参考文献
- [Github GraphQLに関する公式ドキュメント](https://docs.github.com/ja/graphql)
- [アクセストークン取得方法](https://docs.github.com/ja/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
- [アクセストークンの権限設定方法](https://docs.github.com/ja/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps)
# その他参考にしたQiita記事

- https://qiita.com/besmero628/items/4f6d7e9c34c88c4b8e6e
- https://qiita.com/besmero628/items/823a7630c77318d910b0

