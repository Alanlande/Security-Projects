# PDF-ZIP polyglot file generator
Run with (using the included sample files) : 
```
./poly_generate.py --out magic.pdf --in "YOUR_OWN_PDF.pdf" --message happy_hacking.txt --zip THE_ZIP_FILE_LIST.jpg
```

Let's break this up : 
* `--out` is the path/name of the resulting file – which will be a perfectly valid PDF file
* `--in` is your original PDF file
* `--message` is the plaintext message that should appear when the resulting file will be opened in a hex editor, or directly `cat`-ed in a terminal
	* in my example : a rendition of my greeting in ASCII
* `--zip` is the (list of) file(s) that are to be zipped and appended in the original PDF


Still, with all this stuff appended to and included at the beginning of the PDF, it stays valid and viewable in any standard PDF viewer (such as Adobe Reader, Preview on macOS, etc...)
All of this is possible thanks to the fact that the PDF header does not have to be at the beginning of the file, for it to be a valid PDF.