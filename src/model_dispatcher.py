"""调度可用的模型
"""
from sklearn import tree
models = {
    # 以gini系数度量的决策树
    "decision_tree_gini": tree.DecisionTreeClassifier(
        criterion="gini"
    ),
    # 以entropy系数度量的决策树
    "decision_tree_entropy": tree.DecisionTreeClassifier(
        criterion="entropy"
    ),
}