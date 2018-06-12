Overview:
There are two perceptron classifiers (vanilla and averaged) to identify hotel reviews as either true or fake, and either positive or negative. Word tokens are used as features. 

Data:
1. One file train-labeled.txt containing labeled training data with a single training instance (hotel review) per line (total 960 lines). The first 3 tokens in each line are:
   a. a unique 7-character alphanumeric identifier
   b. a label True or Fake
   c. a label Pos or Neg
   These are followed by the text of the review.
2. One file dev-text.txt with unlabeled development data, containing just the unique identifier followed by the text of the review (total 320 lines).
3. One file dev-key.txt with the corresponding labels for the development data, to serve as an answer key.

Programs:
(The perceptron algorithms appear in Hal Daumé III, A Course in Machine Learning (v. 0.99 draft), Chapter 4: The Perceptron.)

1. There are two programs: perceplearn.py will learn perceptron models (vanilla and averaged) from the training data, and percepclassify.py will use the models to classify new data. The learning program will be invoked in the following way:

> python perceplearn.py /path/to/input

2. The argument is a single file containing the training data; the program will learn perceptron models, and write the model parameters to two files: vanillamodel.txt for the vanilla perceptron, and averagedmodel.txt for the averaged perceptron. 
The classification program will be invoked in the following way:

> python percepclassify.py /path/to/model /path/to/input

The first argument is the path to the model file (vanillamodel.txt or averagedmodel.txt), and the second argument is the path to a file containing the test data file; the program will read the parameters of a perceptron model from the model file, classify each entry in the test data, and write the results to a text file called percepoutput.txt in the same format as the answer key.
