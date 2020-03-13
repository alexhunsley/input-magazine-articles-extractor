# INPUT magazine articles extractor

This is a Python script that uses `qpdf` to build PDF collections of articles in a given series. See `scanInput.py` for more details.

You'll need to install qpdf (e.g. `brew install qpdf`).

There is also a script that can generate pngs showing where in the publish run of input articles of a certain type appeared (`visualiseInput.py`).
To run this you'll have to install pillow (`pip install pillow`).

# Stats on INPUT magazine contents

See `Input magazine content tagging.csv`.

# INPUT magazine minutiae and notes

* The peripheral series is not numbered

* P article in issue 50 has no name

* one of the machine code articles claims m/c is nice and easy, not like HLLs!

* mc sprite routines were using the usual &FFEE usual printing routine – kind of pointless?

# The article charts as a poster

Issues are shown as vertical strip of bars, each bar is an article. Heightwise, 8 pixels in a bar = 1 page (with Input 1 at left, Input 51 at right). First article in an issue is at the top of chart. The final index issue (52) is not included here.

![INPUT magazine article coverage as a poster](inputChart-poster.png)
