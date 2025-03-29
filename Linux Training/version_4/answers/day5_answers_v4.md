# Day 5 Instructor Answer Key for the quiz questions, with comprehensive explanations for each answer

## ✅ **Instructor Answer Key (Quiz Questions)**

### 🟢 **Beginner Tier Answers:**

**Question 1 (Fill-in-the-Blank):**  

```bash
wc -l system.log
```

**Explanation:**  

- The explicit option `-l` counts and displays the total number of lines.

---

**Question 2 (Multiple Choice):**  
**Correct Answer:**  

- **C) Replaces "http:" with "https:" in-place**

**Explanation:**  

- The explicit flag `-i` means "in-place editing," and the substitution `s/http:/https:/g` explicitly replaces all occurrences of "http:" with "https:".

---

**Question 3 (Scenario-Based):**  
**Correct Answer:**  

- **B) It explicitly displays sorted unique entries without modifying the original file.**

**Explanation:**  

- The pipeline `sort fruits.txt | uniq` explicitly outputs sorted, unique lines but explicitly does **not** alter the original file.

---

### 🟡 **Intermediate Tier Answers:**

**Question 1 (Multiple Choice):**  
**Correct Answer:**  

- **A) `sort ip.txt | uniq -c | sort -nr`**

**Explanation:**  

- The command explicitly sorts IP addresses first, counts each IP’s occurrences (`uniq -c`), then explicitly sorts numerically in reverse (`sort -nr`) to show the most frequent IP addresses first.

---

**Question 2 (Fill-in-the-Blank):**  

```bash
awk -F',' '{print $2}' data.csv
```

**Explanation:**  

- `-F','` explicitly sets the delimiter to comma for CSV files.
- `{print $2}` explicitly prints only the second field (column).

---

**Question 3 (Scenario-Based):**  
**Correct Answer:**  

- **C) `uniq -d`**

**Explanation:**  

- The explicit option `-d` specifically displays **only duplicated lines**. It's explicitly useful to quickly isolate recurring entries.

---

### 🔴 **SRE-Level Tier Answers:**

**Question 1 (Scenario-Based):**  
**Correct Answer:**  

- **B) `tail -f app.log | grep ERROR`**

**Explanation:**  

- `tail -f` explicitly monitors a file in real-time. Piping (`|`) explicitly passes this continuous stream through `grep ERROR`, explicitly highlighting lines containing "ERROR" immediately upon their appearance.

---

**Question 2 (Fill-in-the-Blank):**  

```bash
sed -i.bak 's/password=.*/password=REDACTED/' config.ini
```

**Explanation:**  

- `-i.bak` explicitly edits `config.ini` in place, creating a backup named `config.ini.bak`.
- The pattern explicitly matches lines starting with `password=` and explicitly replaces the remainder of the line with `password=REDACTED`.

---

**Question 3 (Multiple Choice):**  
**Correct Answer:**  

- **A) `watch -n 60 wc -l logfile`**

**Explanation:**  

- `watch -n 60` explicitly repeats the command every 60 seconds.
- `wc -l logfile` explicitly provides a line count of `logfile` each interval, explicitly showing changes in log size regularly.
