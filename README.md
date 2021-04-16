# Plagiarism-checker-Python

This repo consists of a source code of a python script to detect plagiarism in textual document using **cosine similarity**

[![Become a patron](pictures/become_a_patron_button.png)](https://www.patreon.com/kalebujordan)

How is it done?
-----------------
You might be wondering on how plagiarism detection on textual data is done, well it aint that complicated as you may think.

We all all know that computer are good at numbers, so in order to compute the simlilarity between on two text documents, the textual  raw data is transformed into vectors => arrays of numbers and then from that we are going to use a basic knowledge vector to compute the the similarity between them.

This repo consist of a basic example on how to do that.


Getting started 
------------------
To get started with the code on this repo, you need to either *clone* or *download* this repo into your machine just as shown below;

```bash
$-> git clone https://github.com/Kalebu/Plagiarism-checker-Python
```

Dependencies 
--------------
Before you begin playing with the source code you might need to install the following libaries just as shown below;

```bash
$-> pip install scikit-learn
```

Running the App
----------------
To run this code you need to have your textual document in your project directory with extension **.txt** and then when you run the script, it will automatically loads all the document with that extension and then compute the similarity between them just as shown below;

```bash
$-> cd Plagiarism-checker-Python
$ Plagiarism-checker-Python-> python3 app.py
('john.txt', 'juma.txt', 0.5465972177348937)
('fatma.txt', 'john.txt', 0.14806887549598566)
('fatma.txt', 'juma.txt', 0.18643448370323362)
```

Explore it 
-----------
Explore it and twist it to your own use case, in case of any question feel free to reach me out directly *isaackeinstein(at)gmail.com*

Issues 
-----------

Incase you have any difficulties or issues while trying to run the script
you can raise it on the issues. 

Pull Requests
----------------

If you have something to add I welcome pull requests on improvement , you're helpful contribution will be merged as soon as possible 

Give it a Star ✴️
--------------------
If you find this repo useful , give it a star

Credits
-----------
All the credits to [kalebu](https://github.com/kalebu)
