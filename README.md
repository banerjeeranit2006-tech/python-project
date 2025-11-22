<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/VIT_Bhopal_logo.svg/2500px-VIT_Bhopal_logo.svg.png" alt="logo" width="400">
</div>
<h2 align="center"><strong>COURSE 1021 :</strong> INTRODUCTION TO PROBLEM AND PROGRAMMING</h2>
<h2 align="center"><strong>SLOT :</strong> A11,A12,A13</h2>
<h2 align="center"><strong>FACULTY NAME :</strong> PAVITHRA</h2>
<h2 align="center"><strong>STUDENT NAME :</strong> RANIT BANERJEE</h2>
<h2 align="center"><strong>STUDENT REGISTRATION NO :</strong> 25MIP10012</h2>
<h2 align="center"><strong>STUDENT COURSE :</strong> MTECH-INTEGRATED COMPUTER SCIENCE ENGINEERING (COMPUTATIONAL  AND DATA SCIENCE)</h2>
<h2 align="center"><strong>STUDENT SCHOOL :</strong> SCAI</h2>
<hr>
<h1 align="center">VITYARTHI PROJECT</h1>
<h2 align="center">MARKS ANALYSER AND GRADING SYSTEM</h2>
<p align="center">  <strong>A Python-based marks analysing processs and make grading of that </strong></p>
<div class="container">
        <hr>
        <h2> Table of Contents</h2>
        <ul>
            <li>OVERVIEW</li>
            <li>FEATURES</li>
            <li>HOW TO USE</li>
            <li>CODE STRUCTURE</li>
            <li>PRICING DETAILS</li>
        </ul>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <div class="container">
        <h1> Student Marks Analyzer & Grading System</h1>  
        <p>
            <span class="badge">Python</span>
            <span class="badge">CSV Processing</span>
            <span class="badge">Data Analysis</span>
        </p>
        <p>A comprehensive Python application that analyzes student marks, calculates grades, and generates detailed performance reports. Perfect for educators and institutions looking to automate their grading workflow.</p>
        <h2><span class="emoji"></span> Features</h2>
        <div class="feature-grid">
            <div class="feature-card">
                <h3> Automated Grading</h3>
                <p>Automatically calculates grades based on percentage using a standard A+ to F scale.</p>
            </div>
            <div class="feature-card">
                <h3> Class Statistics</h3>
                <p>Generates class average, identifies topper and lowest performer instantly.</p>
            </div>
            <div class="feature-card">
                <h3> CSV Report Generation</h3>
                <p>Exports comprehensive results to CSV format for easy sharing and record-keeping.</p>
            </div>
            <div class="feature-card">
                <h3> Multi-Subject Support</h3>
                <p>Handles 5 core subjects: Calculus, Physics, Chemistry, English, and Computer Science.</p>
            </div>
        </div>
        <h2><span class="emoji"></span> Grading Scale</h2>
        <table>
            <thead>
                <tr>
                    <th>Percentage</th>
                    <th>Grade</th>
                    <th>Description</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>90% and above</td><td><strong>A+</strong></td><td>Outstanding</td></tr>
                <tr><td>80% - 89%</td><td><strong>A</strong></td><td>Excellent</td></tr>
                <tr><td>70% - 79%</td><td><strong>B</strong></td><td>Good</td></tr>
                <tr><td>60% - 69%</td><td><strong>C</strong></td><td>Average</td></tr>
                <tr><td>50% - 59%</td><td><strong>D</strong></td><td>Pass</td></tr>
                <tr><td>Below 50%</td><td><strong>F</strong></td><td>Fail</td></tr>
            </tbody>
        </table>
        <h2><span class="emoji"></span> Getting Started</h2>        
        <h3>Prerequisites</h3>
        <ul>
            <li>Python 3.6 or higher</li>
            <li>CSV module (included in Python standard library)</li>
        </ul>
        <h3>Installation</h3>
        <pre>git clone https://github.com/yourusername/marks-analyzer.git
cd marks-analyzer</pre>
        <h3>Input File Format</h3>
        <p>Create a <code>marks.csv</code> file with the following structure:</p>
        <pre>Roll,Name,Calculus,Physics,Chemistry,English,Computer Science
101,John Doe,85,90,78,88,92
102,Jane Smith,92,88,95,90,94
103,Mike Johnson,75,70,80,72,78</pre>
        <h3>Running the Program</h3>
        <pre>python "Marks Analyzer and Grading System.py"</pre>
        <h2><span class="emoji"></span> Output</h2>
        <h3>Console Output</h3>
        <div class="output-sample">
            <pre style="background: transparent; color: #2d3748; border: none; padding: 0;">===== CLASS REPORT =====
101 | John Doe | Total: 433 | %: 86.6 | Grade: A
102 | Jane Smith | Total: 459 | %: 91.8 | Grade: A+
103 | Mike Johnson | Total: 375 | %: 75.0 | Grade: B

===== CLASS STATISTICS =====
Class Average Percentage: 84.47
Topper: Jane Smith – 91.8%
Lowest: Mike Johnson – 75.0%

Report saved to file: report.csv</pre>
        </div>
        <h3>Generated Files</h3>
        <p>The program creates <code>report.csv</code> containing:</p>
        <ul>
            <li>Student Roll Number</li>
            <li>Student Name</li>
            <li>Total Marks</li>
            <li>Percentage</li>
            <li>Final Grade</li>
        </ul>
        <h2><span class="emoji"></span> Customization</h2>
        <p>You can easily modify the program to:</p>
        <ul>
            <li>Add or remove subjects by updating the <code>subject_columns</code> list</li>
            <li>Adjust grading thresholds in the <code>get_grade()</code> function</li>
            <li>Change the maximum marks per subject (currently 100)</li>
            <li>Customize output format and statistics</li>
        </ul>
    </div>
</body>
</html>
