# commit-ranking
hackit-vol2 コミット数集計用

> [!IMPORTANT]
> 以下shellの表記はPowerShellの表記です

# 使い方

1. リポジトリをクローンする
    ```shell
    git clone https://github.com/yoshiyuki-140/commit-ranking.git
    ```

1. 必要なモジュールのインストール
    ```shell
    cd commit-ranking # main.pyと同階層に移動
    pip install -r requirements.txt
    ```

1. main.pyと同階層に`.env`ファイルを作成しておく。
    - ファイル作成後のディレクトリ構造
        ```
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

1. "個人用アクセストークン(classic)"を取得する
    - 作成場所
      - https://github.com/settings/tokens/new

    1. 項目[Note]に使用目的を簡単に記述する
    2. 項目[Expiration]にtokenの有効期限を設定する
    3. 項目[Select scopes]に権限を設定する
    4. [Generate token]をクリックし、アクセストークンを取得する
    5. 取得したアクセストークンを、先ほど作成した`.env`ファイルに記述する
        ```text:.env
        # .envファイルの中身
        API_TOKEN = "{ghpから始まるアクセストークン}"
        ```

> [!NOTE]
> 権限は基本的に`repo`のみで良い


1. `main.py`を実行する
    ```shell
    python main.py
    ```

# 参考文献
- [GithubGraphQLに関する公式ドキュメント](https://docs.github.com/ja/graphql)
- [アクセストークン取得方法(公式)](https://docs.github.com/ja/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
- [アクセストークンの権限設定方法(公式)](https://docs.github.com/ja/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps)
- [`.env`環境ファイルを読み込む方法](https://zenn.dev/nakashi94/articles/9c93b6a58acdb4)
- [GraphQL入門](https://zenn.dev/yoshii0110/articles/2233e32d276551)

# その他参考にしたQiita記事

- https://qiita.com/besmero628/items/4f6d7e9c34c88c4b8e6e
- https://qiita.com/besmero628/items/823a7630c77318d910b0

