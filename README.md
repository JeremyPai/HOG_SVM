# HOG + SVM

HOG + SVM is a classic object detection method for it is fast to use and can get acceptable accuracy.

For more description about this project, I wrote a medium artical about it. Go check this out! [link](https://medium.com/lifes-a-struggle/hog-svm-c2fb01304c0)

After running HOG + SVM, we could probably get the following result.
![before_nms](https://github.com/JeremyPai/HOG_SVM/blob/master/image/before_nms.jpg)

However, we don't want too much bounding boxes overlapping one another. So we can choose to run non-maximum suppression after that to remove too much overlapping boxes.
![after_nms](https://github.com/JeremyPai/HOG_SVM/blob/master/image/after_nms.jpg)
