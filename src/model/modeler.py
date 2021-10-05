"""複数の回帰モデルを学習・推論するクラス"""

import os
import pickle
import shutil
from os import listdir
from os.path import join


class Modeler:
    def __init__(self):
        self.models = {}

    def add(self, model):
        """回帰モデルのインスタンスを生成

        Args:
            model : scikit-learnのクラス.

        """
        self.models[model] = model()

    def train(self, output_dir_path, train, target, param_dict):
        """回帰モデルを学習する

        Args:
            output_dir_path (str): アウトプット先のフォルダパス
            train (nd.array)     : 学習データの説明変数
            target (Series)      : 学習データの目的変数

        """

        path_train_target = join(output_dir_path, f"trained_model/")
        # trained_modelディレクト作成
        os.makedirs(path_train_target, exist_ok=True)

        for model in self.models:
            train_model = model()
            train_model.set_params(
                **param_dict[train_model.__class__.__name__]
            )
            train_model.fit(train, target)

            filename = f"{train_model.__class__.__name__}.pickle"

            with open(join(path_train_target, filename), "wb") as f:
                pickle.dump(train_model, f)

        return print("学習完了")

    def predict(self, output_dir_path, test):
        """学習済みの回帰モデルを使用して推論する

        Args:
            output_dir_path (str): 学習済みのモデルが格納されたフォルダパス
            test (nd.array)      : 評価データの説明変数

        Returns:
            pred_dict (dict)     : モデルに対応した予測結果を持つ辞書.

        """
        path = join(output_dir_path, f"trained_model/")
        trained_files = [
            filename
            for filename in listdir(path)
            if not filename.startswith(".")
        ]
        pred_dict = {}

        for trained_file in trained_files:
            with open(
                f"{output_dir_path}/trained_model/{trained_file}", "rb"
            ) as f:
                model = pickle.load(f)
            pred_dict[trained_file[:-7]] = model.predict(test)

        return pred_dict
