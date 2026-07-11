---
name: consider-article
description: Consider an article from a URL and decide whether it earns a note in this knowledge base. Fetches and summarises the source, checks it against existing notes, proposes new notes or edits (proposing before creating by default), then on approval creates the note following repo conventions with full bidirectional cross-linking and a link-integrity check. Use when the user shares a URL and wants it considered for the knowledge base.
allowed-tools: WebFetch Read Grep Glob Bash Edit Write
metadata:
  author: fabianmagrini
  version: "1.0"
  last-updated: 2026-06-14
---

Evaluate an article (given as a URL) for inclusion in this Markdown knowledge base, then either
propose changes or create the note — following [conventions.md](../../../conventions.md) and the
defaults below.

## Defaults (learned preferences)

- **Propose before creating.** Default to proposing new notes / edits and waiting for approval.
  Only skip straight to creating when the user clearly says so ("create the note", "add it").
  If the user says "consider … do not create, only propose", stop after the proposal.
- **Neutral, descriptive tone.** Rewrite skeptical, promotional, or vendor framing into neutral
  prose. Attribute claims ("the author argues…", "AWS's framing…") rather than asserting them.
  Flag vendor-cited or unverified metrics as such.
- **Australian English spelling** in note prose (organisation, behaviour, prioritise, recognise,
  optimise). Don't rewrite quoted titles or established proper nouns.
- **Source attribution.** Set `source:` to the URL and include the `reading` tag.
- **Fresh captures are `status: notes`** unless the user asks otherwise.
- **Cross-link in both directions.** Every `related:` you add must be reciprocated in the target.

## Workflow

### 1. Fetch and summarise

Use WebFetch to retrieve the URL. Ask for: thesis, key arguments, frameworks/models, concrete
practices, distinctive vocabulary, and references. If WebFetch returns a cross-host redirect,
call it again with the redirect URL.

### 2. Survey the existing knowledge base

Before proposing, find what already exists so the note complements rather than duplicates:

```bash
# concept / vocabulary overlap
grep -rli -e "<key term>" -e "<author>" --include='*.md' engineering leadership languages tools concepts reading
# candidate cluster index
cat <folder>/README.md
```

Read the closest 1-3 existing notes in full. Decide the note's **altitude** relative to them
(e.g. theory vs. concrete methodology vs. component anatomy) so it occupies a distinct niche.

### 3. Propose

Present a concise proposal — do not create yet (unless told to). Cover:

- **Whether** it earns a note at all (skip if it only duplicates existing notes).
- **Where** it fits: folder (`engineering/{architecture,practices,security}`, `leadership/`,
  `languages-and-frameworks/`, `tools/`, `concepts/`, `reading/`) and why.
- **New note vs. edits** to an existing note (fold in if the source only adds a section).
- **Scope** — what's genuinely new vs. cross-linked to avoid repetition.
- Any **bridge** role (a note relevant to two clusters belongs in both overview maps).
- Surface real forks (folder choice, scope, tone, merge-vs-new) as judgement calls; recommend
  one. Use AskUserQuestion only for decisions you can't resolve from defaults.

### 4. Create the note (on approval)

Follow `conventions.md`. Frontmatter starter:

```yaml
---
title:
tags: []          # lowercase-hyphenated; reuse the vocabulary in conventions.md; include `reading`
topic: folder/subfolder
status: notes
level: intermediate   # optional
related:
  - path/to/related.md
source: "<url>"
updated: YYYY-MM-DD   # today's date
---
```

- File name lowercase-hyphenated and descriptive (`learning-organisation.md`).
- Include a short **"Relationship to other notes"** section when the topic overlaps existing
  notes, stating how this one is distinct.
- Prefer tables/short sections over long prose; match the style of neighbouring notes.

### 5. Wire it in

- Add the note to its folder `README.md` index.
- Add reciprocal `related:` entries in every related note (both directions).
- Add a bullet + frontmatter entry to any relevant overview/thematic map
  (e.g. `engineering/ai-native/ai-native-engineering-overview.md`,
  `leadership/engineering-leadership-overview.md`).
- Inline-link related notes from the body where it aids navigation.

### 6. Verify link integrity

Confirm every relative link and `related:` path resolves (the `path/to/related.md` template
placeholders in `conventions.md`/`AGENTS.md` are the only expected misses):

```bash
for f in $(find . -name '*.md' -not -path './.git/*'); do
  dir=$(dirname "$f")
  grep -oE '\]\(([^)]+\.md)[^)]*\)' "$f" | sed -E 's/^\]\(//; s/[)#].*$//' | while read l; do
    case "$l" in http*) continue;; esac
    [ ! -f "$dir/$l" ] && echo "BROKEN: $f -> $l"
  done
done
```

Note: this repo uses **zsh**, which does not word-split unquoted variables — iterate with arrays
(`LEAD=(a b c); for n in $LEAD`) when scripting multi-file edits.

### 7. Offer to commit

Do not commit unless asked. When the user approves, use the project's PR flow: branch →
commit → push → open PR → merge with `--delete-branch` → return to `main` and pull. End commit
messages with the `Co-Authored-By` trailer and PR bodies with the Claude Code generated-with line.
```
git checkout -b add-<slug> && git add -A && git commit && git push -u origin add-<slug>
gh pr create ... && gh pr merge --merge --delete-branch
```
