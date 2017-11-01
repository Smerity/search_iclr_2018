# Search ICLR 2018

Searching papers submitted to ICLR 2018 can be painful.
You might want to know which paper uses technique X, dataset D, or cites author ME.
Unfortunately, search is limited to titles, abstracts, and keywords, missing the actual contents of the paper.
This Frankensteinian search has been made to help scour the papers by ripping out their souls using `pdftotext`.

This code is evil.
Truly mind boggingly evil.
If you read the 31 lines of Python code in reverse you'll likely summon division by zero demons that will slowly consume your sanity whilst NaN bugs work their way into all your deep learning code.

Having said that, to stare into the abyss of evil and run this for yourself:

```
pip install flask gunicorn
sudo apt-get install authbind
mkdir log
./serve.sh
```

By default it uses `authbind` to bind the privileged port 80 without root.
If you're running this locally you probably don't care either way.

Good luck, and may your reviewers have no commentary but praise.
