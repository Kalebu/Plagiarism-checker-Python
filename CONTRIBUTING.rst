============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

installation
===========
git clone https://github.com/Kalebu/Plagiarism-checker-Python
cd Plagiarism-checker-Python
docker run -it --name Renormalizer-devPlagiarism-checker-Python -w /opt -v %cd%:/opt python:latest bash
 pip3 install -r requirements.txt
 
 running
===========
$ Plagiarism-checker-Python-> python3 app.py
('john.txt', 'juma.txt', 0.5465972177348937)
('fatma.txt', 'john.txt', 0.14806887549598566)
('fatma.txt', 'juma.txt', 0.18643448370323362)
