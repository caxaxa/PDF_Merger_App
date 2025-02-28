# PDF Merger

> _“Why trust your precious PDFs to some random, sketchy website when you can merge them in the comfort of your own command line?”_

## So, What's the Deal?

Welcome to the **PDF Merger** project: a small, mighty script that smooshes all your PDFs together into one glorious mega-PDF. No shady servers involved. No weird watermarks. No dancing goats (yet).

We know there are plenty of “free” PDF tools on the web, but let’s be honest:  
1. **They** might sneak in ads or spam.  
2. **They** might meddle with your data.  
3. **They** are suspiciously free (and we’ve heard rumors about them collecting your *cat pictures*).

With *this* script, **you** remain in control. No mysterious middlemen messing with your merges.

## Features

- **Alphabetical merging** for that oh-so-satisfying, orderly result.  
- **Local, local, local**—your PDFs never leave your computer’s side.  
- **Uses [PyPDF2](https://pypi.org/project/PyPDF2/)**, because reinventing the wheel is overrated.

## Requirements

- Python 3.6+ (Nobody uses Python 2 anymore… right?)  
- [PyPDF2](https://pypi.org/project/PyPDF2/) (because, well, it’s a PDF library)

Installation is as simple as:
```bash
pip install PyPDF2
```

## Project Structure

```text
pdf-merger/
├─ input_files/
│  ├─ file1.pdf
│  ├─ file2.pdf
│  └─ ... (the rest of your precious PDFs)
├─ merge_pdfs.py
└─ README.md
```

- `input_files/`: Where you keep your PDFs before merging them into one glorious super-document.
- `merge_pdfs.py`: The main script that does all the magic.
- `README.md`: The file you’re reading now.

## How to Use (Yes, It’s Easy)

1. **Install Requirements**  
   ```bash
   pip install PyPDF2
   ```

2. **Add Your PDF Files**  
   - Drop all the PDFs to be merged into the `input_files` folder like a tidy little squirrel storing nuts for winter.

3. **Run the Script**  
   ```bash
   python merge_pdfs.py
   ```
   - Voila! A `merged.pdf` file will appear as if by magic in the same directory as `merge_pdfs.py`.

## A Quick Note

- The PDFs are merged alphabetically because chaos is overrated. Rename your files for the desired order (`A.pdf`, `B.pdf`, `C.pdf`… or `01_file.pdf`, `02_file.pdf`—you do you).
- If you dislike the name **`merged.pdf`**, feel free to rename it in the code. We won’t take it personally.

## FAQ (Totally Anticipated Questions)

1. **Is this safer than that random free website from the 2007 internet era?**  
   - Absolutely. You’re in charge of your PDFs and your coffee breaks.

2. **Can I merge 100 PDFs at once?**  
   - Sure. Be bold. Test the limits. Just watch your RAM usage if your PDFs are massive tomes.

3. **Will you steal my data?**  
   - No. The code is open-source; there’s nowhere to hide anything sneaky (except maybe in the coffee machine… but we wouldn’t).

## License

This project is open-source and free to use. If you want to share it with your friends, your enemies, or your grandma, go right ahead. No disclaimers about goats were necessary during testing… but you never know. 

**Happy merging!**  
