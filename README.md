## Digit Recognition, Pattern Recognition, Classification Project

Use the template matching algorithm (function) you wrote. Make a small dataset of digits (0 to 9) with 5 samples in each class. You can use test images with only single digits and of the same size as the template, for simplicity and ease, if you want. This means you don’t need to move the template window over test image. Both are of same size! Use KNN algorithm to find the digit in the test image.

Digit recognition is a classical pattern recognition problem. Each digit 0-9 represents a class.  Features extracted from images of the digits can be used to generate a reference base (training data). A query digit image presented to the system can then be recognized using a classifier.

For this task, you are provided with multiple images of each digit as training data. Load each image, extract features and store the features of each image along with class label. Using k-nn classification scheme, classify each of the images in the test data set into one of the digit classes. Examples of digits are illustrated in the following table.


Please see report for all details