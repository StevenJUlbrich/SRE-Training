# Day 5: Quiz Answer Key with Explanations

Below are the suggested answers to the Day 5 quiz questions. The explanations expand on why the particular answer is correct and how it connects back to our training.

---

## Beginner Tier (4 Questions)

1. **sed Substitution**: Which sed command replaces all instances of `apple` with `Apple` in `fruits.txt`?

   **Answer**: `sed 's/apple/Apple/g' fruits.txt`

   **Explanation**: The `s` command performs a substitution. `apple` is the search pattern, `Apple` is the replacement string, and `g` denotes a global replacement on each line.

2. **awk Fields**: In `awk '{print $3}'`, which part of the line are we extracting?

   **Answer**: The **third field** from each line.

   **Explanation**: awk automatically divides each line into fields (space-delimited by default) and assigns them to `$1`, `$2`, `$3`, etc. `$3` extracts the third field in each line.

3. **sort Default Behavior**: By default, does `sort` order data numerically or lexicographically?

   **Answer**: **Lexicographically** (alphabetical ordering by characters).

   **Explanation**: Without any flags (e.g., `-n`), `sort` sorts based on ASCII values, meaning numeric strings like `10` come before `2`.

4. **wc -l**: If a file has 100 lines, what numeric output does `wc -l filename` provide?

   **Answer**: `100`

   **Explanation**: `wc -l` prints only the number of lines in the file, which would be 100.

---

## Intermediate Tier (4 Questions)

1. **Removing Comments**: How can you remove lines starting with `#` in a config file using sed?

   **Answer**: `sed '/^#/d' config.ini`

   **Explanation**: `^#` matches lines beginning with `#`, and `d` deletes those lines. Thus you’re removing comment lines.

2. **Combining sort & uniq**: Why do we typically run `sort` before `uniq`?

   **Answer**: Because **uniq only removes adjacent duplicates**, and sorting first ensures all duplicate lines are placed next to each other.

   **Explanation**: If you don’t sort before running uniq, repeated lines that aren’t adjacent will be missed.

3. **Filtering with awk**: What does `awk '$2 > 50 {print $0}' file.txt` do?

   **Answer**: It **prints the entire line** (`$0`) for every line where the **second field** (`$2`) is greater than 50.

   **Explanation**: The pattern `$2 > 50` is checked on every line. If true, the action `{print $0}` outputs the entire original line.

4. **Memory Usage**: Why might `sort -nr largefile.log` consume a lot of resources?

   **Answer**: Sorting large amounts of data can require **significant CPU and memory**. The entire file (or large chunks of it) may be loaded into memory, and sorting is computationally intensive.

   **Explanation**: For massive files, sort can create large temporary files and heavily use CPU. Memory and disk usage can spike.

---

## SRE-Level Tier (4 Questions)

1. **In-Place Editing**: What risk does `sed -i` present when used on critical config files?

   **Answer**: If a system crash or mistake occurs during in-place editing, **the file can be partially overwritten** or corrupted.

   **Explanation**: `-i` modifies the file directly. Without backups or version control, you can’t easily revert if something goes wrong.

2. **Regex Complexity**: How could advanced regex in sed or awk help parse multiline data?

   **Answer**: By enabling multiline patterns or extended regex features, you can **search across line boundaries** or handle more complex patterns that single-line matches miss.

   **Explanation**: Tools like `sed -E` or certain `awk` record-separator techniques let you capture multi-line log entries or complicated data structures.

3. **Advanced Pipelines**: Provide one advantage of chaining grep → awk → sort → uniq → wc in a single pipeline.

   **Answer**: **Efficiency and speed**—data can be processed in a **single pass** (streaming) without writing intermediate files.

   **Explanation**: Also a shorter workflow for the user, with each command refining the data for the next, preventing repeated reads of the same file.

4. **Performance Monitoring**: How would you use `wc` in a script to detect an abnormally large log growth event?

   **Answer**: Periodically check line counts or byte sizes with `wc` and compare against a threshold; **if counts spike** beyond normal, trigger an alert.

   **Explanation**: For instance, `size=$(wc -c < /var/log/app.log); if [ "$size" -gt 500000 ]; then echo "High log growth"; fi`. This helps detect unusual logging rates indicating potential issues.
