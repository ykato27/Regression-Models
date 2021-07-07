# Regression-Models
* 回帰モデル全般のプログラム

## リポジトリ構成
```
.
├── README.md
├── data
├── docker
│   ├── Dockerfile
│   ├── LIME
│   │   └── Dockerfile
│   ├── NGBoost
│   │   └── Dockerfile
│   └── SHAP
│       └── Dockerfile
├── docker-compose-lime.yml
├── docker-compose-ngboost.yml
├── docker-compose-shap.yml
├── docker-compose.yml
├── docs
├── example
│   ├── eval_model_example.ipynb
│   └── modeler.ipynb
├── models
│   └── trained_model
│       ├── ElasticNet.pickle
│       ├── GradientBoostingRegressor.pickle
│       ├── Lasso.pickle
│       ├── RandomForestRegressor.pickle
│       ├── Ridge.pickle
│       └── SVR.pickle
├── notebooks
│   ├── CatBoost-Optuna-example2.ipynb
│   ├── CatBoost-Optuna.ipynb
│   ├── CatBoost.ipynb
│   ├── Google-Colab
│   │   └── interpretML-GoogleColab.ipynb
│   ├── LIME
│   │   └── LIME.ipynb
│   ├── LightGBM-Optuna-example2.ipynb
│   ├── LightGBM-Optuna.ipynb
│   ├── LightGBM.ipynb
│   ├── NGBoost
│   │   └── NGBoost.ipynb
│   ├── Regression_Models.ipynb
│   ├── Regression_Models_Modeler.ipynb
│   ├── SHAP
│   │   └── SHAP.ipynb
│   ├── XGBoost-Bayesian-Optimization.ipynb
│   ├── XGBoost-Optuna-example2.ipynb
│   ├── XGBoost-Optuna.ipynb
│   └── XGBoost.ipynb
├── pyproject.toml
├── setup.cfg
├── src
│   ├── __init__.py
│   ├── __pycache__
│   │   └── __init__.cpython-38.pyc
│   ├── evaluation
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-38.pyc
│   │   │   └── eval_model.cpython-38.pyc
│   │   └── eval_model.py
│   └── model
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-38.pyc
│       │   └── modeler.cpython-38.pyc
│       └── modeler.py
├── tests
│   └── __init__.py
└── work
```

## 環境構築

* Dockderfileがあるホスト側のフォルダへ移動（例：Desktop/Regression-Models）
```
cd Desktop/Regression-Models
```

* Dockerによる環境構築（ローカルフォルダをマウント：Desktop/Regression-Models）
```
docker-compose -f docker-compose-{*構築対象}.yml up --build
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
* [Regression_Models_Modeler.ipynb](https://github.com/ykato27/Regression-Models/blob/main/notebook/Regression_Models_Modeler.ipynb) : 回帰モデル全般のnotebook
* [SHAP.ipynb](https://github.com/ykato27/Regression-Models/blob/main/notebook/SHAP.ipynb) : SHAPのnotebook(機械学習モデルを解釈するためのライブラリー)
* [XGBoost-Optuna.ipynb](https://github.com/ykato27/Regression-Models/blob/main/notebook/XGBoost-Optuna.ipynb) : XGBoost-Optunaのnotebook
* [XGBoost.ipynb](https://github.com/ykato27/Regression-Models/blob/main/notebook/XGBoost.ipynb) : XGBoostのnotebook
* [eval_model_example.ipynb](https://github.com/ykato27/Regression-Models/blob/main/example/eval_model_example.ipynb) : eval_model.pyのexample


## モジュールの説明（src/）
* [eval_model.py](https://github.com/ykato27/Regression-Models/blob/main/src/evaluation/eval_model.py) : 評価指標を計算するモジュール


## 動作環境
マシンスペック（Mac)
- MacBook Air (Retina, 13-inch, 2018)
- 1.6 GHz デュアルコアIntel Core i5
- 8 GB 2133 MHz LPDDR3
