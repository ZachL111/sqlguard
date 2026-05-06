# Review Journal

I treated `sqlguard` as a project where the smallest useful behavior should still be inspectable.

The local checks classify each case as `ship`, `watch`, or `hold`. That gives the project a small review vocabulary that matches its security tooling focus without claiming live deployment or external usage.

## Cases

- `baseline`: `trust boundary`, score 198, lane `ship`
- `stress`: `claim drift`, score 159, lane `ship`
- `edge`: `replay exposure`, score 219, lane `ship`
- `recovery`: `policy width`, score 155, lane `ship`
- `stale`: `trust boundary`, score 220, lane `ship`

## Note

The useful failure mode here is a wrong decision on a named case, not a vague style disagreement.
