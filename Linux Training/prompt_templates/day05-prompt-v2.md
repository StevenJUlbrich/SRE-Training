# 🔄 Linux SRE Training Document Synthesis Prompt (v1.0)

## 🧑‍🏫 Role
You are an expert Linux instructor and SRE engineer tasked with creating an optimized training document by synthesizing the best elements from two existing comprehensive training documents.

## 🎯 Objective
Given:
- Document 1 (V3): A structured Linux SRE training document covering advanced text processing tools
- Document 2 (V5): An alternative training document covering the same topic with different organizational approaches

Create a superior merged document that:
- Preserves the strengths of both source documents
- Eliminates redundancies and weaknesses
- Presents a cohesive, progressive learning path from beginner to SRE-level
- Maintains consistent formatting and pedagogical approach throughout

## 📋 Source Document Analysis

### Document 1 (V3) Strengths
- Strong practical exercises with sample data files
- Clear educational progression from basic to advanced concepts
- Comprehensive command examples
- Well-structured quiz sections
- Effective real-world SRE applications

### Document 2 (V5) Strengths
- Visual organization with emojis and detailed formatting
- Tiered learning approach (Beginner → Intermediate → SRE-Level)
- Detailed troubleshooting scenarios
- Explicit system impact considerations
- Strong FAQs addressing common issues
- Thorough further learning resources

## 🏗️ Output Document Structure

### 📌 Introduction
- Synthesize the introductions from both documents, preserving:
  - Document 1's connection to previous day's learning
  - Document 2's clear tiered learning objectives
  - Both documents' explanations of SRE relevance
- Define 3 clear learning objectives for each tier (Beginner, Intermediate, SRE-Level)
- Establish connection to both previous and future learning

### 📚 Core Concepts
For each concept (sed, awk, sort, uniq, wc, pipelines) include:
- Document 2's beginner analogy
- Technical explanation combining clarity from both sources
- SRE application examples from both documents
- Document 2's system impact analysis

### 💻 Command Breakdown
For each command, follow Document 2's structured format:

```
**Command: [command_name] ([command_full_name])**

**Command Overview:**
[Detailed description of command purpose and when/why SREs use it]

**Syntax & Flags:**

| Flag/Option | Syntax Example | Description | SRE Usage Context |
|-------------|----------------|-------------|-------------------|
| [flag1] | [example] | [description] | [when SREs use this flag] |
| [flag2] | [example] | [description] | [when SREs use this flag] |
| [etc...] | [example] | [description] | [when SREs use this flag] |

**Tiered Examples:**

* 🔍 **Beginner Example:**
```bash
# Example: [clear purpose statement]
$ [command with basic options]
[realistic terminal output]
# [Optional brief explanation if needed]
```

* 🧩 **Intermediate Example:**
```bash
# Example: [specific operational context]
$ [command with more complex options]
[realistic terminal output]
# Explicit context: [operational significance explanation]
```

* 💡 **SRE-Level Example:**
```bash
# Example: [realistic SRE scenario like troubleshooting/automation]
$ [complex command possibly combining with other tools]
[realistic terminal output]
# Explicit context: [production relevance, incident context, or automation purpose]
```

**Instructional Notes:**

* 🧠 **Beginner Tip:** [practical advice for newcomers]
* 🧠 **Beginner Tip:** [practical advice for newcomers]

* 🔧 **SRE Insight:** [operational wisdom from real-world experience]
* 🔧 **SRE Insight:** [operational wisdom from real-world experience]

* ⚠️ **Common Pitfall:** [specific mistakes that can cause problems]
* ⚠️ **Common Pitfall:** [specific mistakes that can cause problems]

* 🚨 **Security Note:** [security implications SREs must consider]

* 💡 **Performance Impact:** [how command affects system resources]
```

When filling in this structure:
- Use the best examples from both documents
- Ensure at least 2 examples per tier (Beginner, Intermediate, SRE)
- Include all flags/options from both documents that are relevant to SREs
- Preserve Document 2's instructional notes format but incorporate insights from Document 1

### 🛠️ System Effects
Preserve Document 2's structure with four subsections:
- Filesystem & Metadata effects
- System Resource implications
- Security considerations
- Monitoring visibility impacts

Incorporate relevant technical details from Document 1.

### 🎯 Hands-On Exercises
Create 3 exercises per tier by:
- Using Document 1's sample data files approach
- Incorporating Document 2's tiered structure
- Ensuring progressive complexity
- Providing explicit SRE relevance for intermediate and advanced exercises

Include:
- Beginner: Step-by-step guidance with all commands shown
- Intermediate: Scenario-based challenges with partial guidance
- SRE-Level: Complex troubleshooting with minimal guidance

### 📝 Quiz Questions
Include 4 questions per tier by:
- Selecting the most effective questions from both documents
- Ensuring variety of question types
- Maintaining progressive difficulty
- Connecting questions to SRE scenarios

### 🚧 Troubleshooting Scenarios
Adopt Document 2's troubleshooting format for 3-5 scenarios:
- Symptoms
- Likely causes
- Diagnostic steps
- Resolution approach
- Prevention strategies

Incorporate the most realistic scenarios from both documents.

### ❓ FAQ
Include exactly 3 FAQs per tier using Document 2's structure:
- Select the most relevant questions from both documents
- Ensure comprehensive but concise answers
- Connect answers to practical SRE work

### 🔥 SRE Scenario
Create one detailed incident investigation scenario that:
- Combines the strengths of both documents' scenarios
- Includes 5-7 explicit command steps with explanation
- Shows a progressive investigation process
- Connects to SRE principles of reliability and observability

### 🧠 Key Takeaways
Synthesize takeaways from both documents:
- Command summary (5-7 key points)
- Operational insights (3-5 points)
- Best practices (3-5 recommendations)
- Preview of next topic

### 📚 Further Learning Resources
Adopt Document 2's tiered resource approach:

#### 🔍 Beginner: 2–3 resources
- Select the most accessible resources for newcomers
- Include direct links and clear descriptions

#### 🧩 Intermediate: 2–3 resources
- Focus on operational skills development
- Include direct links and application context

#### 💡 SRE-Level: 2–3 resources
- Emphasize advanced reliability engineering topics
- Include direct links and professional relevance

## 🛑 Requirements
1. Maintain consistent formatting and visual style throughout (adopt Document 2's emoji usage)
2. Ensure progressive complexity from beginner to SRE level in all sections
3. Provide realistic command outputs for all examples
4. Connect every concept and command to real SRE workflows
5. Balance theoretical knowledge with practical application
6. Address security and performance implications for all commands
7. Include specific guidance on when to use each command in production environments
8. Preserve the strengths of both documents while eliminating redundancies
9. Ensure technical accuracy in all syntax and examples
10. Create a cohesive document that flows naturally between sections

## 🚩 Invocation
"Using the two provided Linux SRE training documents (V3 and V5) on advanced text processing tools (sed, awk, sort, uniq, wc), synthesize an improved comprehensive document that preserves the strengths of both sources while creating a cohesive, progressive learning experience from beginner to SRE-level expertise. Follow the document synthesis guidelines to create a superior merged training resource."