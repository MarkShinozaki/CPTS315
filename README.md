# Homeworks 

## [Homework 1](https://github.com/MarkShinozaki/CPTS315-IntroductionToDataMining/tree/Homeworks/HW1)

### Overview

- Homework 1 for the CptS 315 course focuses on data mining techniques, specifically the analysis of market-basket data and the implementation of the A-priori algorithm for product recommendations. The homework is divided into two parts: Analytical and Programming.

### Analytical Part (40 points)
#### 1. Market-Basket Analysis
- Analyze a given set of baskets to determine the support and confidence of itemsets.
- **Tasks**:
  - Calculate absolute support for itemsets.
  - Compute relative support for itemsets.
  - Evaluate confidence for association rules.

#### 2. Storing Frequent Pairs
- Compare methods for storing pairs using a triangular matrix and a tabular approach.
- **Tasks**:
  - Calculate index positions for pair counts in a triangular matrix.
  - Decide the best method for storing pairs based on given conditions.

#### 3. PCY Algorithm
- Implement and analyze the PCY algorithm to count frequent item pairs.
- **Tasks**:
  - Calculate support for items and item pairs.
  - Determine bucket assignments for item pairs using a hash function.
  - Identify frequent buckets and item pairs for the second pass.

#### 4. Research Summary
- Summarize the main points from a specified paper on document fingerprinting.

### Programming and Experimental Part (60 points)

#### 1. Product Recommendations using A-priori Algorithm

- Implement a program to identify frequent product combinations from browsing data.
- **Tasks**:
  - Identify item pairs with support ≥ 100 and calculate confidence scores for association rules.
  - Identify item triples with support ≥ 100 and calculate confidence scores for associated rules.
  - Sort and list the top rules based on confidence scores.

#### 2. Implementation Details

- Use Python to write the program.
- Execute the code using a shell script `run_code.sh`.
- Output results to `output.txt` in a specified format, listing top association rules by confidence.

### Files Explanation
#### 1. HW-1.py: Python script implementing the A-priori algorithm.
#### 2. HW-1.sh: Shell script to execute the Python code.
#### 3.  output.txt: File containing the output from the Python script, listing frequent item pairs and triples along with their confidence scores.
#### 4. Part-1.pdf: Document with analytical answers to the questions in the homework.
#### 5. browsing-data.txt and partial-browsing-data.txt: Datasets containing online browsing sessions, each line representing a session with items browsed.

### Key Takeaways
- The homework emphasizes both theoretical understanding and practical implementation of data mining techniques.
- It covers concepts such as support, confidence, frequent itemset mining, and the use of algorithms like PCY and A-priori.
- Proper documentation and output formatting are critical for demonstrating the results effectively.

--- 

## [Homework 2](https://github.com/MarkShinozaki/CPTS315-IntroductionToDataMining/tree/Homeworks/HW2)

### Overview

- Homework 2 for the CptS 315 course builds on the concepts of data mining, focusing on similarity measures and collaborative filtering techniques used in recommendation systems. The homework includes both analytical and programming components to deepen understanding and apply practical skills.

### Analytical Part (40 points)
#### 1. Similarity Computation
- Calculate similarity metrics using a given ratings matrix.
- **Tasks**:
  - **Jaccard Similarity**: Compute the similarity between users treating missing values as zero.
  - **Cosine Similarity**: Compute the similarity between users treating missing values as zero.
  - **Normalization**: Subtract the average value from each user's non-zero ratings to normalize the matrix.
  - **Centered Cosine Similarity**: Calculate the similarity using the normalized matrix.

#### 2. Research Summaries
- Summarize key points from two academic papers related to recommendation systems at Amazon.
- **Tasks**:
  - Discuss Amazon's use of item-based collaborative filtering and its evolution.
  - Compare different recommendation algorithms, including traditional collaborative filtering, cluster models, and search-based methods.

### Programming and Experimental Part (60 points)

#### 1. Movie Recommendations via Item-Item Collaborative Filtering
- Implement the item-item collaborative filtering algorithm using the Movie-Lens dataset.
- **Tasks**:
  - **Profile Construction**: Develop profiles for each movie based on user ratings and optionally include additional information such as genres or tags.
  - **Similarity Score Calculation**: Use the centered cosine similarity metric to calculate similarity scores between movie pairs.
  - **Neighborhood Selection**: Identify the top 5 most similar movies for each movie based on similarity scores.
  - **Rating Estimation**: Estimate user ratings for movies they haven't rated using the neighborhood set.
  - **Recommendation Generation**: Recommend the top 5 movies with the highest estimated ratings for each user, resolving ties with lexicographic ordering.

#### 2. Implementation Details
- Utilize programming languages like Python, Java, or C++ for coding.
- Execute the program with a shell script run_code.sh.
- Output the recommendations to output.txt with each line listing a user ID followed by the recommended movie IDs.

### Key Takeaways
- This homework emphasizes the application of collaborative filtering techniques to real-world datasets.
- It covers important concepts such as similarity measures, normalization, and algorithmic scalability in the context of recommendation systems.
- The combination of theoretical understanding and practical implementation enhances the learning experience, preparing students for real-world data mining challenges.


---

## [Homework 3](https://github.com/MarkShinozaki/CPTS315-IntroductionToDataMining/tree/Homeworks/HW3)

### Overview
- Homework 3 for the CptS 315 course explores the application of machine learning algorithms, specifically focusing on the perceptron algorithm and binary classification problems. The homework consists of both analytical and programming components designed to reinforce theoretical understanding and practical implementation skills.

### Analytical Part (50 points)
#### 1. Perceptron Decision Boundaries
- Analyze the linearity of decision boundaries in perceptron variants.
- **Tasks**:
  - Determine whether the decision boundaries of the voted and averaged perceptrons are linear and provide justification.

#### 2. Importance Weighting in Perceptron
- Modify the perceptron algorithm to incorporate importance weights for training examples.
- **Tasks**:
  - Explain how to adjust the perceptron algorithm to leverage the additional information of example importance.

#### 3. Imbalanced Data Handling
- Adapt the perceptron algorithm to address class imbalance in the training data.
- **Tasks**:
  - Propose modifications to the perceptron algorithm to improve accuracy for minority class examples.

#### 4. Perceptron for Candidate Evaluation
- Use the perceptron algorithm to evaluate and rank job candidates.
- **Tasks**:
  - Represent each candidate using a 6-dimensional feature vector.
  - Describe the intuition behind using a perceptron to learn the weight vector.
  - Provide pseudocode for the algorithm to update weights based on candidate comparisons.

#### 5. CLOSE Classifier Analysis
- Analyze the decision boundary of the CLOSE classifier.
- **Tasks**:
  - Demonstrate that the decision boundary is a linear hyperplane.
  - Calculate the values of 𝑤 and 𝑏 based on the centers of positive and negative examples.

#### 6. Research Summary
- Summarize the main points of an academic paper on machine learning.
- **Tasks**:
  - Read and summarize "A few useful things to know about machine learning" by Pedro M. Domingos.

### Programming and Experimental Part (50 points)

#### 1. Fortune Cookie Classifier
- Implement a binary classifier to categorize fortune cookie messages.
- **Tasks**:
  - Preprocess messages into a bag-of-words feature representation, removing stop words.
  - Use the perceptron algorithm to classify messages into predictive (class 1) or wise sayings (class 0).
  - Compute mistakes, training accuracy, and testing accuracy over 20 iterations for both standard and averaged perceptrons.

#### 2. Optical Character Recognition (OCR) Classifier
- Build a classifier to predict whether handwritten characters are vowels or consonants.
- **Tasks**:
  - Convert image features into input vectors.
  - Implement the perceptron algorithm for classification.
  - Track mistakes and accuracy over 20 iterations for both standard and averaged perceptrons.

#### 3. Implementation Details
- Write code in Python, Java, or C++.
- Execute the program using a shell script `run_code.sh`.
- Output results to `output.txt`, detailing iteration statistics and final accuracy for both classifiers.

### Key Takeaways
- Homework 3 emphasizes the practical application of perceptron algorithms in real-world scenarios.
- It covers essential concepts like linearity in decision boundaries, handling imbalanced data, and modifying algorithms to incorporate additional information.
- The programming component reinforces theoretical knowledge by requiring students to implement classifiers and analyze their performance on provided datasets.














