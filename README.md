# one-liner

A tiny program that writes one deadpan one-line joke to a text file. The
line is a single sentence of at most 280 characters: a barber mishears a
request for a trim, and the haircut that follows changes what kind of man
the speaker looks like.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (`OUTPUT_DIR` overrides the
directory). Running it twice produces byte-identical output.
