# MathML to SVG converter

This converts MathML tags inside any .epub file with SVG elements. This script was designed due to the inability of Kindle e-readers to render MathML elements properly.

## Roadmap

This script is not yet finished, the roadmap so far is:

- [X] Use BeautifulSoup4 in each xhtml file in order to find any `math` tags.
- [X] Convert `math` elements to `img` elements using the `altimg` attribute.
- [ ] Convert `math` elements to `svg` elements using a known converter (replace previous functionality).
- [ ] Use zipfile to extract contents of .epub file and iterate through all of the xhtml files.

The idea is to have equations rendered as LaTeX ones, properly aligned and not inline. 

This is only a problema for a _very specific book_. YMMV depending on the book's structure.
