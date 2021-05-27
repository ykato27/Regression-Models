# Regression-Models
* 回帰モデル全般のプログラム

## リポジトリ構成
```
.
├── Dockerfile
├── README.md
├── docker-compose.yml
├── example
│             └── eval_model_example.ipynb
├── interpretML.ipynb
├── models
│             └── trained_model
├── notebook
│             ├── CatBoost-Optuna.ipynb
│             ├── CatBoost.ipynb
│             ├── LIME.ipynb
│             ├── LightGBM-Optuna.ipynb
│             ├── LightGBM.ipynb
│             ├── NGBoost.ipynb
│             ├── Regression_Models.ipynb
│             ├── Regression_Models_Modeler.ipynb
│             ├── SHAP.ipynb
│             ├── XGBoost-Optuna.ipynb
│             ├── XGBoost.ipynb
│             └── models
│                 └── trained_model
└── src
    ├── __init__.py
    └── evaluation
        ├── __init__.py
        └── eval_model.py
```

## 環境構築

* Dockderfileがあるホスト側のフォルダへ移動（例：Desktop/Regression-Models）
```
cd Desktop/Regression-Models
```

* Dockerによる環境構築（フォルダをマウント：Desktop/Regression_Models）
```
docker-compose up --build
```

* ブラウザーを立ち上げてlocalhost:8888へアクセス
* ローカルフォルダがマウントされている

## jupyter notebook説明
* [CatBoost-Optuna.ipynb](https://github.com/ykato27/Regression-Models/blob/main/notebook/CatBoost-Optuna.ipynb) : CatBoost-Optunaのnotebook
* [CatBoost.ipynb](https://github.com/ykato27/Regression-Models/blob/main/notebook/CatBoost.ipynb) : CatBoostのnotebook
* [LIME.ipynb](https://github.com/ykato27/Regression-Models/blob/main/notebook/LIME.ipynb) : LIMEのnotebook(機械学習モデルを解釈するためのライブラリー)
* [LightGBM-Optuna.ipynb](https://github.com/ykato27/Regression-Models/blob/main/notebook/LightGBM-Optuna.ipynb) : LightGBM-Optunaのnotebook
* [LightGBM.ipynb](https://github.com/ykato27/Regression-Models/blob/main/notebook/LightGBM.ipynb) : LightGBMのnotebook
* [NGBoost.ipynb](https://github.com/ykato27/Regression-Models/blob/main/notebook/NGBoost.ipynb) : NGBoostのnotebook(不確かさを扱える新しい勾配ブースティング)
* [Regression_Models.ipynb](https://github.com/ykato27/Regression-Models/blob/main/notebook/Regression_Models.ipynb) : 回帰モデル全般のnotebook
* [SHAP.ipynb](https://github.com/ykato27/Regression-Models/blob/main/notebook/SHAP.ipynb) : SHAPのnotebook(機械学習モデルを解釈するためのライブラリー)
* [XGBoost-Optuna.ipynb](https://github.com/ykato27/Regression-Models/blob/main/notebook/XGBoost-Optuna.ipynb) : XGBoost-Optunaのnotebook
* [XGBoost.ipynb](https://github.com/ykato27/Regression-Models/blob/main/notebook/XGBoost.ipynb) : XGBoostのnotebook

## 動作環境
マシンスペック（Mac)
- MacBook Air (Retina, 13-inch, 2018)
- 1.6 GHz デュアルコアIntel Core i5
- 8 GB 2133 MHz LPDDR3
