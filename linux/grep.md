<div dir="ltr" align="left">

# grep Command Usage

`grep` is a command-line tool used to search for text patterns inside files or command output.

The name `grep` comes from:

```bash
g/re/p
```

This means:

> globally search for a regular expression and print matching lines

In simple terms, `grep` finds lines that match a word, phrase, or pattern.

---

<details>
<summary><strong>📑 Table of Contents</strong> — <em>click to expand / collapse</em></summary>

| # | Section |
| ---: | --- |
| 1 | [Basic Usage](#basic-usage) |
| 2 | [Common Examples](#common-examples) |
| 3 | [Useful Options](#useful-options) |
| 4 | [Developer Example](#developer-example) |
| 5 | [Modern Alternative](#modern-alternative) |
| 6 | [Summary](#summary) |

[↑ Top](#grep-command-usage)

</details>

---

## Basic Usage

<details>
<summary>Basic Usage</summary>

```bash
grep "error" app.log
```

This searches inside `app.log` and prints every line that contains `error`.

---

</details>


<div align="center">

[↑ Top](#grep-command-usage) · [Next →](#common-examples)

</div>


---

## Common Examples

<details>
<summary>Common Examples</summary>

### Search for text in a file

```bash
grep "TODO" src/index.ts
```

Finds all lines containing `TODO` in `src/index.ts`.

---

### Search recursively in a directory

```bash
grep -r "useEffect" src/
```

Searches for `useEffect` inside all files under the `src/` directory.

---

### Case-insensitive search

```bash
grep -i "error" app.log
```

Matches `error`, `Error`, `ERROR`, and other case variations.

---

### Show line numbers

```bash
grep -n "failed" app.log
```

Prints matching lines with their line numbers.

---

### Invert match

```bash
grep -v "debug" app.log
```

Prints lines that do **not** contain `debug`.

---

### Search command output

```bash
ps aux | grep nginx
```

Searches the output of `ps aux` for lines containing `nginx`.

---

</details>


<div align="center">

[↑ Top](#grep-command-usage) · [← Previous](#basic-usage) · [Next →](#useful-options)

</div>


---

## Useful Options

<details>
<summary>Useful Options</summary>

| Option | Meaning |
|---|---|
| `-r` | Search recursively inside directories |
| `-i` | Ignore case |
| `-n` | Show line numbers |
| `-v` | Show lines that do not match |
| `-c` | Count matching lines |
| `-l` | Show only file names with matches |
| `-w` | Match whole words only |

---

</details>


<div align="center">

[↑ Top](#grep-command-usage) · [← Previous](#common-examples) · [Next →](#developer-example)

</div>


---

## Developer Example

<details>
<summary>Developer Example</summary>

```bash
grep -r "function login" .
```

This searches the whole current project for `function login`.

---

</details>


<div align="center">

[↑ Top](#grep-command-usage) · [← Previous](#useful-options) · [Next →](#modern-alternative)

</div>


---

## Modern Alternative

<details>
<summary>Modern Alternative</summary>

For large codebases, many developers use `ripgrep`, which is usually faster than `grep`.

Its command is `rg`:

```bash
rg "useEffect" src
```

However, `grep` is still very useful because it is available by default on most Unix, Linux, and macOS systems.

---

</details>


<div align="center">

[↑ Top](#grep-command-usage) · [← Previous](#developer-example) · [Next →](#summary)

</div>


---

## Summary

<details>
<summary>Summary</summary>

`grep` is useful for:

- Finding text inside files
- Searching logs
- Searching source code
- Filtering command output
- Debugging from the terminal

It is one of the most important command-line tools for developers and system administrators.

</details>


<div align="center">

[↑ Top](#grep-command-usage) · [← Previous](#modern-alternative)

</div>


</div>
