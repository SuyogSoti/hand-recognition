from PIL import Image
import numpy as np
# import tensorflow as tf
import os
import pickle
from sklearn import tree
from skimage.measure import structural_similarity as ssim
from sklearn.externals import joblib
# from sklearn.cross_validation import cross_val_score
# from sklearn import grid_search


def main():
    folders = os.listdir("./dataset")
    x_point = []
    y_point = []
    test_x = []
    test_y = []
    for i in folders:
        pictures = os.listdir("./dataset/" + i)
        count = 0
        for pic in pictures:
            img = Image.open("./dataset/" + i + "/" + pic)
            img = img.convert("L")
            basewidth = 50
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((basewidth, hsize), Image.ANTIALIAS)
            img = np.asarray(img, dtype=np.uint8).reshape(1, -1)[0]
            if count:
                x_point.append(img)
                y_point.append(i)
            else:
                test_x.append(img)
                test_y.append(i)
            count = 1
        print(i)
    filename = 'data.sav'
    pickle.dump([
        np.asarray(x_point),
        np.asarray(y_point),
        np.asarray(test_x),
        np.asarray(test_y)
    ], open(filename, 'wb'))
    return [
        np.asarray(x_point),
        np.asarray(y_point),
        np.asarray(test_x),
        np.asarray(test_y)
    ]


# im = Image.open("test.png")
# im.save("test-600.png", dpi=(600,600))
if __name__ == '__main__':
    # redo = False
    arr = pickle.load(open("data.sav", 'rb'))
    x = arr[0]
    y = arr[1]
    xt = arr[2]
    yt = arr[3]
    # # if x is None or redo:
    # # x, y, xt, yt = main()
    # # import pdb; pdb.set_trace()
    clf = tree.DecisionTreeClassifier(max_features="auto", max_depth=100)
    clf = clf.fit(x, y)
    filename = 'finalized_model.sav'
    joblib.dump(clf, filename)
    test = clf.predict(xt)
    # folders = os.listdir("./dataset")
    for i in test:
        print(i)

    """
    depth = []
    for i in range(3,20):
        clf = tree.DecisionTreeClassifier(max_depth=i)
        # Perform 7-fold cross validation 
        scores = cross_val_score(estimator=clf, X=x, y=y, cv=7, n_jobs=4)
        depth.append((i,scores.mean()))
        print(scores)
    print(depth)
    parameters = {'max_depth':range(3,20)}
    clf = grid_search.GridSearchCV(tree.DecisionTreeClassifier(), parameters, n_jobs=4)
    clf.fit(X=x, y=y)
    tree_model = clf.best_estimator_
    print (clf.best_score_, clf.best_params_) 
    """
