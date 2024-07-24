
# Assignment Auto Grader Portal

Assignment submission and grading portal with both student and evaluator interfaces for simplifying and automating assignment submission and grading.  

# Features


1. Authentication and Uploading of files : Students can securely sign in and submit multiple files for all their assignments through the portal, streamlining the submission process and ensuring convenience and confidentiality.

2. Provision of late submission : The portal tracks and verifies submission times, distinguishing between submissions made before or after the assignment's specified deadline, aiding in enforcing timely submission policies.

3. Plagiarism detection : The evaluator can utilize the built-in plagiarism checker to compare each submitted file with those of other students, returning true if the similarity exceeds a predefined threshold, ensuring academic integrity and originality.
The plagiarism checker works as follows -

(i) Texts are stemmed using the Porter-Stemming algorithm.

(ii)TF-IDF (Term Frequency-Inverse Document Frequency) is utilized to convert text into numerical vectors.

(iii)Cosine similarity is calculated between the TF-IDF vectors of the texts.


4. Auto-grading : The evaluator is equipped to test submitted code against provided input files, comparing the output generated by the code with the corresponding expected output files, facilitating automated testing and validation of the code's functionality. The portal also prints syntax errors to assist evaluators in identifying and understanding any code issues. 

5. Review and Feedback : The portal evaluates code quality using diverse metrics, assigning scores based on performance in each metric. It then computes a total score for the submission, comprising points for test case success (out of 75) and code/documentation quality (out of 25), providing a comprehensive assessment of the submission's overall quality and functionality.

As of now, our code supports python and c++ files. For python, we are using the pylint module and for c++, we have written our own code.

We have used the following metrics for our c++ analyzer -

(i)Comment-to-code ratio

(ii)Complexity of expressions and constructs

(iii)Overall Improper Indentation Rate

(iv)Repetition Rate

(v)Variable Naming or Scoping Issue Level

6. No API calls - We are not using any API calls for anything. We have written the code for both the plag checker and the code analyzer for c++. For python, we are importing the pylint module.


# Future Updates

1. Support for Additional Programming Languages: Expand support for a wider range of programming languages, accommodating diverse curriculum requirements and student preferences.
2. Mobile Application: Develop a mobile application version of the portal, providing students with convenient access to assignment submission, grading feedback, and course materials on their smartphones or tablets.

# Known Errors
As of now there are no errors, atleast not that we know of.

### Installing the dependencies
**Make sure that you have `Python 3.10` installed in your system**

Run the following command in the terminal
```
pip install -r requirements.txt
```


### Running the program
Now, to run the script enter the following command in the terminal
```bash
streamlit run Login.py
```

# sample credentials to run :
Student
1. username : student_1, password : student_1
2. username : student_2, password : student_2

TA
1. username : ta_1, password : ta_1
2. username : ta_2, password : ta_2

# Screenshots

![Student Login](./images/real1.png)
![Make Submission](./images/real2.png)
![TA Login](./images/real3.png)
![Test Cases Evaluation and Plague Checker](./images/real4.png)
![Test Cases Evaluation and Plague Checker](./images/real5.png)
![View Submissions](./images/real6.png)
![Database Schema](./images/real7.png)
![Database Schema](./images/real8.png)
##
Link to demonstration : https://drive.google.com/drive/folders/1z3c3kWJSa13Wfinx4feV6KJnXSL8H8e3?usp=sharing 

Made by : 
1. Arush Shaleen Mathur(220101017)
2. Ayush Kumar(220101021)
3. Ayush Savar(220101022)
