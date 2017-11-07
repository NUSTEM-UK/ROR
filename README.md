# ROR
Robot Orchestra Returns

## GUIzero & Mac notes
At time of writing (2017-11-07), this code relies on prerelease [GUIzero](https://github.com/lawsie/guizero) additions. Today, the forthcoming GUIzero 0.4 is not working (with Waffle objects). Instead, I did a straight
`sudo pip3 install guizero`, then integrated the clickable waffle pull request by hand (!). That is: amend `/usr/local/lib/python3.6/site-packages/guizero/Waffle.py` with the changes from [this pull request](https://github.com/lawsie/guizero/pull/28/files).

This is not a pretty way of working. However, hopefully the issue will go away with the release of GUIzero 0.4.

## Experiments
The `experiments` folder contains test code and in-progress work along the way. This is mostly lifted from documentation, but it might reveal our learning process. A little.

* `tkinter01.py`  
Basic Tkinter GUI app, to test the Python3 Tkinter libraries are installed correctly.

* `waffle01.py`  
Basic GUIzero Waffle object test, to check GUIzero is installed correctly.

* `waffle02.py`
Massive clickable Waffle object, to check GUIzero patches for clickable Waffles installed correctly.

* `waffle04.py`  
Stripped-back initial version of what we want, with networking code removed for clarity.
