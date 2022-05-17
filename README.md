# Plagiarism Detector
This project is about building a plagiarism detector that examines a text file and performs binary classification; labeling that file as either plagiarized or not, depending on how similar the text file is when compared to a provided source text. 

## Types of Plagiarism

Each text file is associated with one **Task** (task A-E) and one **Category** of plagiarism, which you can see in the above DataFrame.

###  Tasks, A-E

Each text file contains an answer to one short question; these questions are labeled as tasks A-E. For example, Task A asks the question: "What is inheritance in object oriented programming?"

### Categories of plagiarism 

Each text file has an associated plagiarism label/category:

**1. Plagiarized categories: `cut`, `light`, and `heavy`.**
* These categories represent different levels of plagiarized answer texts. `cut` answers copy directly from a source text, `light` answers are based on the source text but include some light rephrasing, and `heavy` answers are based on the source text, but *heavily* rephrased (and will likely be the most challenging kind of plagiarism to detect).
     
**2. Non-plagiarized category: `non`.** 
* `non` indicates that an answer is not plagiarized; the Wikipedia source text is not used to create this answer.
    
**3. Special, source text category: `orig`.**
* This is a specific category for the original, Wikipedia source text. We will use these files only for comparison purposes.

## The challenge

### NLP

Text is a type of unstructured data so the way to deal with this kind of data is different from a standard dataset.
In addition the goal requires to engine new feature that can help the model to detect how much two text are similars in a numeric way.

Another situation to address properly is that the dataset counts barely 100 rows so the risk to overfit in these cases is quite feasible.
We need to use and then test the model in order to make sure that it is stable and reliable as much as possible.


## Milestone 1 EDA and Feature Engineering

We have basically 100 text(original text included) and the distribuition among the plagiarism is more or less the same as shown in the picture below:

![alt text](https://github.com/alessandroNarcisi96/PlagiarismDetector/blob/master/Images/PlagNotPlag.PNG)

The following image shows the distribuition for the types of plagiarism
![alt text](https://github.com/alessandroNarcisi96/PlagiarismDetector/blob/master/Images/AllPlag.PNG)

By using the filename let's add the text in order to count the length.
The question is:Is length useful to predict whether a text is a plagiarism or not?

As the boxplots show below every type of text has a different distribuition so it will be a relevant feature.
![alt text](https://github.com/alessandroNarcisi96/PlagiarismDetector/blob/master/Images/Length.PNG)

### N-Grams
Te detect similar text we are going to create **containment features**. To understand containment, let's first revisit a definition of [n-grams](https://en.wikipedia.org/wiki/N-gram). An *n-gram* is a sequential word grouping. For example, in a line like "bayes rule gives us a way to combine prior knowledge with new information," a 1-gram is just one word, like "bayes." A 2-gram might be "bayes rule" and a 3-gram might be "combine prior knowledge."

> Containment is defined as the **intersection** of the n-gram word count of the Wikipedia Source Text (S) with the n-gram word count of the Student  Answer Text (S) *divided* by the n-gram word count of the Student Answer Text.


If the two texts have no n-grams in common, the containment will be 0, but if _all_ their n-grams intersect then the containment will be 1. Intuitively, you can see how having longer n-gram's in common, might be an indication of cut-and-paste plagiarism. 

![alt text](https://github.com/alessandroNarcisi96/PlagiarismDetector/blob/master/Images/NGrams1.PNG)

So let's see the result by checking for 4-grams in common.
![alt text](https://github.com/alessandroNarcisi96/PlagiarismDetector/blob/master/Images/NgramsBoxPlot.PNG)
As we can see the result is great!


### Longest Common Subsequence

Containment a good way to find overlap in word usage between two documents; it may help identify cases of cut-and-paste as well as paraphrased levels of plagiarism. Since plagiarism is a fairly complex task with varying levels, it's often useful to include other measures of similarity.

> The longest common subsequence is the longest string of words (or letters) that are *the same* between the Wikipedia Source Text (S) and the Student Answer Text (A). This value is also normalized by dividing by the total number of words (or letters) in the  Student Answer Text. 

As the boxplots show the distribuition of the values change along the different types of plagiarism 
![alt text](https://github.com/alessandroNarcisi96/PlagiarismDetector/blob/master/Images/LCS.PNG)

### Common KeyWords
Yake is a library that reads a text and find the keyword.In case of a plagiarism we can assume that there a lot of keywords in common.
So basically I am going to compare the first 15 keywords that the text provided have in common.

As the boxplots show the distribuition of the values change along the different types of plagiarism
![alt text](https://github.com/alessandroNarcisi96/PlagiarismDetector/blob/master/Images/KeyWords.PNG)

## Milestone 2 Feature Selection
As Applied Predictive Modeling at page 488 states 
>"Feature selection is primarily focused on removing non-informative or redundant predictors from the model."

We have already seen on EDA that all the features presented so far are important.We want know to avoid that they are too much correlated in order to make sure to don't overfit
Since they are all continuos variable we can display the correlation matrix:

Except for Ngrams and LCS the other ones are not high correlated.
![alt text](https://github.com/alessandroNarcisi96/PlagiarismDetector/blob/master/Images/Correlation1.PNG)
## Milestone 3 Model

As the dataset is very small we are going to select model that don't tend to overfit such as:Logistic Regression and Naive Bayes.
Furthermore a model like RandomForest which combines more weak learners could perform very well.

## Milestone 4 Performance and Testing

It could be quite difficult making sure that we get a reliable performance as the dataset is very small.
For this reason we are going to apply a specific type of Cross Validation which is particularly helpful in these cases:LOOCV

In this tecnique if there are n observation only 1 is left for the testing set the remaining points are used for the training set.
Then all the process is reiterated until all the point are used for the testing set.
The final accuracy is the average of the results

As the project shows all the models in the end achieve the same accuracy:0.94
Since the dataset is quite balanced between plagiarism and not plagiarism it is a good measure