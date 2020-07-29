import numpy as np
from utils.helperfuncs import get_matrix_from_img
from sklearn.linear_model import LogisticRegression

pos_examples_path = "C:/Users/admin/Desktop/DinoGameRewrite/data/pos examples"
neg_examples_path = "C:/Users/admin/Desktop/DinoGameRewrite/data/neg examples"

pos_features = get_matrix_from_img(pos_examples_path)
neg_features = get_matrix_from_img(neg_examples_path)


pos_target = np.ones(pos_features.shape[0],dtype="int64")
neg_target = np.zeros(neg_features.shape[0],dtype="int64")

X = np.concatenate([pos_features,neg_features],axis=0)
y = np.concatenate([pos_target,neg_target],axis=0)


model = LogisticRegression(solver="lbfgs")
model.fit(X,y)

