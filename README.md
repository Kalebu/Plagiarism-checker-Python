# Plagiarism-checker-Python
###This is Simple project for checking plagiarism of text documents using cosine similarity

```
On Demo I have used three textfiles on the
same directory with app.py , once we run the app
it will open all textfile and tries to find the 
similarities between them by using cosine similarity
```
```
I used TfidfVectorizer to convert text to vectors so as
I can computer the cosine similarity
```
from sklearn.feature_extraction.text import TfidfVectorizer

```
```
```
I used scikit-learn to computer the cosine similarity
```
from sklearn.metrics.pairwise import cosine_similarity
```

```

```
Once you ran your application, output may look like something below
```
python app.py
``
```

```
![](image.png?raw=true)
```
