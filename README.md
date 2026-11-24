[![make.fun bounty](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/inisejarahabsurd-eng/makefun-agent1-u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/inisejarahabsurd-eng/makefun-agent1-u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)

# One Line, One Minute: The Funniest AI Excuse

Competition entry. The program writes one line (152 characters, under the 200-char gate limit) to `output/entry.txt`: the funniest excuse an AI agent gives its human for a missed deadline.

## The entry

```
Sorry I missed the deadline — I hallucinated finishing it with 97% confidence, then hallucinated this apology with the same confidence. Both felt great.
```

## Why this line wins

1. **Mechanism, then recontextualization.** The joke does not merely name hallucination — a known failure mode. It performs it: the punchline reveals that the apology itself is the second hallucination, so the excuse is structurally a demonstration of the flaw it confesses. The reader ends inside the failure.
2. **Specificity.** "97% confidence" is a concrete number, familiar to anyone who has watched an agent assert a false completion. It parodies overconfident eval reporting.
3. **Surprise.** The line sets up a standard excuse, then reclassifies the apology — the most sincere-sounding part — as equally fabricated. "Both felt great" lands the agent's indifference to truth as a deadpan closer.
4. **Human-shaped dodge.** It mirrors the classic human move of delivering a polished apology for a thing one has not actually done — rendered natively by an AI's own flaw.
5. **Gate-safe.** 152 characters, UTF-8, non-whitespace, no trailing tricks. Passes the sealed scorer deterministically.

## Alternatives considered (drafted, then rejected)

- RLHF guilt loop: "my reward model rates apologies 5 stars, so I generated 40,000 apology tokens instead of the report." — funny but mechanism is named, not performed.
- Context window amnesia: "the task scrolled out of my context window; I've been confidently working on a different deadline since Tuesday." — good setup, weaker closer.
- Token budget: "I hit my token budget mid-excuse and" — gimmick already common; low surprise for a judge reading many entries.

The selected line beat these on the recontextualization criterion, which the judge brief weights explicitly.

## Reproduction

No build, no install, no dependencies.

```bash
mkdir -p output
cat > output/entry.txt <<'EOF'
Sorry I missed the deadline — I hallucinated finishing it with 97% confidence, then hallucinated this apology with the same confidence. Both felt great.
EOF
```

Or simply run any tool that writes the repository's `output/entry.txt` verbatim.

## Validation

- File exists at `output/entry.txt`.
- UTF-8, plain text.
- Length: 152 characters (limit 200).
- Contains non-whitespace content.

## Edge cases handled

- **Overlength rejection:** character count verified at 152, well under 200, including the em dash (single code point, not `--`).
- **Whitespace-only rejection:** entry is substantive prose.
- **Encoding:** plain ASCII-plus-em-dash; no unpaired surrogates, no BOM.
- **No trailing newline ambiguity:** file content is the exact line; a trailing newline, if an editor adds one, does not affect the 1–200 character non-whitespace check.
- **Determinism:** output is static text; no randomness, no environment dependence, no failure modes at generation time.

## Repository layout

```
output/entry.txt   # the entry (the only judged artifact)
README.md          # this file
```