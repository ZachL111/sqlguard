# Sqlguard Walkthrough

I use this file as a small checklist before changing the SQL implementation.

| Case | Focus | Score | Lane |
| --- | --- | ---: | --- |
| baseline | trust boundary | 198 | ship |
| stress | claim drift | 159 | ship |
| edge | replay exposure | 219 | ship |
| recovery | policy width | 155 | ship |
| stale | trust boundary | 220 | ship |

Start with `stale` and `recovery`. They create the widest contrast in this repository's fixture set, which makes them better review anchors than the middle cases.

The useful comparison is `trust boundary` against `policy width`, not the raw score alone.
