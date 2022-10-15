# HOG + SVM

HOG + SVM is a classic object detection method for it is fast to use and can get acceptable accuracy.

For more description about this project, I wrote a medium artical about it. Check this out! [link](https://medium.com/lifes-a-struggle/hog-svm-c2fb01304c0)

After running HOG + SVM, we could probably get the following result.

![before_nms](https://github.com/JeremyPai/HOG_SVM/blob/master/image/before_nms.jpg)

However, we don't want too much bounding boxes overlapping one another. So we can choose to run non-maximum suppression after that to remove too much overlapping boxes.

![after_nms](https://github.com/JeremyPai/HOG_SVM/blob/master/image/after_nms.jpg)

Resource:

+ Navneet Dalal and Bill Triggs. “Histograms of oriented gradients for human detection.” 2005 IEEE computer society conference on computer vision and pattern recognition (CVPR’05). Vol. 1. Ieee, 2005.
+ Navneet Dalal. Finding People in Images and Videos. Human-Computer Interaction [cs.HC]. Institut National Polytechnique de Grenoble — INPG, 2006. English. ￿tel-00390303
+ Satya Mallick — Histogram of Oriented Gradients explained using OpenCV
+ PyImageSearch — Pedestrian Detection OpenCV
