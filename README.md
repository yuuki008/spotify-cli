# Spotify CLI

Spotify CLIは、Spotifyの再生をインタラクティブに制御するためのコマンドラインツールです。ユーザーは、アーティストの検索、曲の再生、一時停止、プレイリストのナビゲートをターミナルから直接行うことができます。

## 注意
このプロジェクトは現在開発中であり、すべての機能が完全に実装されているわけではありません。ご利用の際はご注意ください。

## 特徴

- **音楽の検索と再生**: アーティスト、アルバム、プレイリストを検索して音楽を再生できます。
- **インタラクティブなナビゲーション**: カーソルベースのインターフェースを使用して曲、アルバム、プレイリストを選択できます。
- **再生制御**: 曲の再生、一時停止、スキップが可能です。
- **お気に入りアーティスト**: お気に入りのアーティストの音楽に素早くアクセスして再生できます。

## インストール

1. リポジトリをクローンします:
   ```bash
   git clone https://github.com/yuuki008/spotify-cli.git
   cd spotify-cli
   ```

2. 仮想環境を作成してアクティベートします:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. 必要なパッケージをインストールします:
   ```bash
   pip install -r requirements.txt
   ```

4. Spotify Developerの認証情報を設定します:
   - [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications)でアプリケーションを作成します。
   - リダイレクトURIを `http://localhost:8888/callback` に設定します。
   - `Client ID`と`Client Secret`をコピーします。

5. プロジェクトのルートに`.env`ファイルを作成し、Spotifyの認証情報を追加します:
   ```env
   SPOTIPY_CLIENT_ID='your_client_id'
   SPOTIPY_CLIENT_SECRET='your_client_secret'
   SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'
   ```

## 使用方法

1. メインスクリプトを実行します:
   ```bash
   python src/main.py
   ```

2. 利用可能なコマンドが表示されます:
   ```plaintext
   Available commands:
     playlist  - Select and play a playlist
     pause     - Pause playback
     next      - Play next track
     artists   - Search and play music from your favorite artists
     help      - Show this help message
     exit      - Exit the CLI
   ```

3. コマンドを使用してSpotifyの再生をインタラクティブに制御します。

## 例

アーティストを検索して音楽を再生する場合:
1. `artists`コマンドを実行します。
2. アーティストを検索するオプションを選択します。
3. アーティスト名を入力します。
4. 検索結果からアーティストを選択します。
5. リストから曲を選択して再生を開始します。


