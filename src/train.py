"""模型训练脚本
"""
import os
import config
import model_dispatcher
import joblib
import pandas as pd
from sklearn import metrics
from sklearn import tree


def run(fold):
    # 使用config中的路径读取数据
    df = pd.read_csv(config.TRAINING_FILE)
    df_train = df[df.kfold != fold].reset_index(drop=True)
    df_valid = df[df.kfold == fold].reset_index(drop=True)
    x_train = df_train.drop("label", axis=1).values
    y_train = df_train.label.values
    x_valid = df_valid.drop("label", axis=1).values
    y_valid = df_valid.label.values

    # 训练模型
    clf = model_dispatcher.models[config.MODEL]
    clf.fit(x_train, y_train)

    # 评估模型效果
    preds = clf.predict(x_valid)
    accuracy = metrics.accuracy_score(y_valid, preds)
    print(f"Fold={fold}, Accuracy={accuracy}")
    joblib.dump(clf,os.path.join(config.MODEL_OUTPUT, f"dt_{fold}.bin") )

if __name__ == "__main__":
    # 运行每个折叠
	run(fold=0)
	run(fold=1)
	run(fold=2)
	run(fold=3)
	run(fold=4)