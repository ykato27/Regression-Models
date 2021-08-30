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
│   ├── CatBoost.ipynb
│   ├── Google-Colab
│   │   └── interpretML-GoogleColab.ipynb
│   ├── LIME
│   │   └── LIME.ipynb
│   ├── LightGBM.ipynb
│   ├── NGBoost
│   │   └── NGBoost.ipynb
│   ├── Optuna
│   │   ├── CMA-ESSampler
│   │   │   ├── train-test
│   │   │   │   ├── CatBoost-Optuna.ipynb
│   │   │   │   ├── LightGBM-Optuna.ipynb
│   │   │   │   ├── XGBoost-Optuna.ipynb
│   │   │   └── train-valid-test
│   │   │       ├── CatBoost-Optuna-example.ipynb
│   │   │       ├── LightGBM-Optuna-example.ipynb
│   │   │       ├── XGBoost-Optuna-example.ipynb
│   │   └── TPESampler
│   │       ├── train-test
│   │       │   ├── CatBoost-Optuna.ipynb
│   │       │   ├── LightGBM-Optuna.ipynb
│   │       │   ├── XGBoost-Optuna.ipynb
│   │       └── train-valid-test
│   │           ├── CatBoost-Optuna-example.ipynb
│   │           ├── LightGBM-Optuna-example.ipynb
│   │           ├── XGBoost-Optuna-example.ipynb
│   ├── Regression_Models.ipynb
│   ├── Regression_Models_Modeler.ipynb
│   ├── SHAP
│   │   └── SHAP.ipynb
│   ├── XGBoost-Bayesian-Optimization.ipynb
│   └── XGBoost.ipynb
├── pyproject.toml
├── setup.cfg
├── src
│   ├── __init__.py
│   ├── evaluation
│   │   ├── __init__.py
│   │   └── eval_model.py
│   └── model
│       ├── __init__.py
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

## モジュールの説明（src/）
* [eval_model.py](https://github.com/ykato27/Regression-Models/blob/main/src/evaluation/eval_model.py) : 評価指標を計算するモジュール


## 動作環境
マシンスペック（Mac)
- MacBook Air (Retina, 13-inch, 2018)
- 1.6 GHz デュアルコアIntel Core i5
- 8 GB 2133 MHz LPDDR3
