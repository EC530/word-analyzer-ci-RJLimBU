# word-analyzer-ci-RJLimBU
## word-analyzer-ci-RJLimBU created by GitHub Classroom <br />
### Description <br />
this project reads contents in a txt or PDF file, counts the word frequency <br />
and display the histogram. NLTK stop words are removed from the count. <br />
### How to Use <br />
-run the 'mainloop.py' file <br />
-enter the filename with .txt or .pdf suffix in the same directory <br />
<br />
once user input the filename, the program will show word frequency <br />
and display a histogram. It will remove NLTK stop words from the count. <br />
### Dependencies <br />
see "requirement.txt" <br />
### Requirement
System: latest version of Ubuntu <br />
Python version: 3.8, 3.9, 3.10 <br />
### Unit tests
-test the open file function and check if it correctly read words from the txt/pdf file <br />
-check if correctly remove punctuation <br />
-correctly split strings into list of words <br /> 
-extract distinct words from the string <br />
-NLTK stop words removal <br />
-correct word count for each distinct words <br />
### sample result
The histogram displays the word frequency in the example2.txt. The x-axis shows the distinct words <br /> 
in the text, the y-axis shows the frequency of each word <br />
<br />
![histogramResult](/images/sample_output.png)
<br />
This histogram displays the output from "sample.pdf" <br />
<br />
![histogramResultPDF](/images/sample_outputpdf.png)
<br />
<br />
Here is the sample output from terminal <br />
<br />
![terminalResult](/images/sample_output_terminal.png)
<br />
