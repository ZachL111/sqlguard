# sqlguard

`sqlguard` explores security tooling with a small SQL codebase and local fixtures. The technical goal is to detect unsafe query construction and verify parameterized alternatives.

## Reason For The Project

This is intentionally local and self-contained so it can be inspected without credentials, services, or seeded history.

## Sqlguard Review Notes

Start with `trust boundary` and `policy width`. Those cases create the widest score spread in this repo, so they are the best quick check when the model changes.

## What It Does

- `fixtures/domain_review.csv` adds cases for trust boundary and claim drift.
- `metadata/domain-review.json` records the same cases in structured form.
- `config/review-profile.json` captures the read order and the two review questions.
- `examples/sqlguard-walkthrough.md` walks through the case spread.
- The SQL code includes a review path for `trust boundary` and `policy width`.
- `docs/field-notes.md` explains the strongest and weakest cases.

## How It Is Put Together

The repository has two validation layers: the original compact policy fixture and the domain review fixture. They are separate so one can change without hiding failures in the other.

The SQL checks add a separate view over the domain review fixture.

## Run It

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

## Check It

The check exercises the source code and the review fixture. `stale` is the high score at 220; `recovery` is the low score at 155.

## Boundaries

The repository is intentionally scoped to local checks. I would expand it by adding adversarial fixtures before adding features.
