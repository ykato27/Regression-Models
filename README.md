# Regression_Models
* 回帰モデル全般のプログラム

## リポジトリ構成
```
.
├── README.md                 READMEファイル
├── Dockerfile                Dockerファイル
├── data                      データの格納場所
│   ├── processed             前処理後データ
├── notebook                  ノートブック
├── src                       ソースコード
│   └── preprocess            前処理
│   └── utils                 モデル共通
└── work                      実行ファイル
```

## 環境構築
### Dockderfileがあるホスト側のフォルダへ移動（例：Desktop/Regression_Models）
```
cd Desktop/Regression_Models
```
### Dockerによる環境構築
```
docker build .
```
docker run実行（対象フォルダをマウントする／例：Desktop/Regression_Models）
```
docker run -p 8888:8888 -v ~/Desktop/Regression_Models/:/work --name Regression_Models <docker image>
```
ブラウザーを立ち上げてlocalhost:8888へアクセス
workフォルダ内が対象フォルダにマウントされている