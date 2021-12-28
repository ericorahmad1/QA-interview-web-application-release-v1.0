## Overview

1. This app has been seeded with a variety of bugs:

    * a major functional bug
    * a data limit bug
    * a usability bug
    * a typo
    * a bug on the page content
    * a slightly weird wording 
    * a cross-browser bug 

2. You should check several workflows available on this app. 

    `E.g.: Entering an integer followed by a string followed by an integer (does the form validation clear?)`

3. You need to write a Selenium script to test that the factorial of 5 is 120

4. write a bug report and document a test case


## Setup

Follow this setup to use a local copy of this application. 

`pip install requirements.txt`


## How to run the QA interview application

To start the application, run `python qa_interview.py` and visit `localhost:6464` in your browser.


## What the application does

The application calculates the factorial of a given number. We have exactly one page with:

* one text box 
* one submit button
* a page title 
* three hyperlinks 
* a copyright message

By keeping the application this simple, we are increasing the likelihood of the interviewer and the candidate agreeing upon what is important. You can also reasonably expect QA to be able to verbalize their testing for such limited functionality.


## What we're expecting

This task is not a mandatory but is preferrable. Try to do both as far as you can and we'll discuss more in our concall.