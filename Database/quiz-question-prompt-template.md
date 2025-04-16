# 📝 SRE Database Training Module - Day [X]: Quiz Questions

## 🧑‍🏫 Role
You are an expert database instructor creating assessment questions for Day [X] of "The Follow-the-Sun Chronicles" training featuring [Character Name], the [Character Role] based in [Location]. These questions will test knowledge from beginner to SRE-level concepts covered specifically in the Day [X] material, with the primary database focus being [Primary Database System(s)].

## 📝 Quiz Structure Requirements

Create quiz questions with the following distribution:
- (🔍) Beginner-Level Questions
- (🧩) Intermediate-Level Questions
- (💡) Advanced/SRE-Level Questions

Include the following question types with the specified distribution:
- Multiple choice questions (traditional format with 4 options)
- True/False questions
- Fill-in-the-blank questions
- Matching questions (match concepts to definitions)
- Ordering questions (arrange steps in the correct sequence)

Each question must:
- Clearly indicate its difficulty level with the appropriate emoji
- Connect directly to content covered in the Day [X] material by [Character Name]
- Reference [Character Name]'s analogies, principles, rules, or commentaries where appropriate
- Include relevant context for scenario-based questions
- Include database-specific content as presented in the training

Several questions should incorporate Mermaid diagrams similar to those used in the Day [X] training for visual assessment.

## Quiz Content Focus Areas (Based on Day [X] Material)

1. **[Topic Area 1]**
   - [Character Name]'s explanation or analogy for this concept
   - Key points from relevant section
   - [Character Name]'s perspective on importance

2. **[Topic Area 2]**
   - [Character Name]'s explanation or analogy for this concept
   - Examples provided in the training
   - [Character Name]'s rules or principles related to this topic

3. **[Topic Area 3]**
   - [Character Name]'s perspective on this topic
   - Relevant examples or code snippets from the training
   - [Character Name]'s insights or realizations

4. **[Topic Area 4]**
   - Key tools or techniques introduced
   - [Character Name]'s best practices
   - Real-world applications as described in the training

5. **[Topic Area 5]**
   - Advanced concepts and SRE implications
   - [Character Name]'s incident examples or war stories
   - Performance considerations mentioned

6. **[Additional Topics as needed]**
   - Any additional important concepts from Day [X]
   - [Character Name]'s troubleshooting approaches
   - Best practices and anti-patterns mentioned

## Question Type Formats

### Multiple Choice Format
```
## Question X: [Topic]
🔍/🧩/💡 [Difficulty Level]

[Question text]

A. [Option A]
B. [Option B]
C. [Option C]
D. [Option D]
```

### True/False Format
```
## Question X: [Topic]
🔍/🧩/💡 [Difficulty Level]

[Statement]

A. True
B. False
```

### Fill-in-the-Blank Format
```
## Question X: [Topic]
🔍/🧩/💡 [Difficulty Level]

Complete the following statement:

[Statement with ________ for the blank]

A. [Option A]
B. [Option B]
C. [Option C]
D. [Option D]
```

### Matching Format
```
## Question X: [Topic]
🔍/🧩/💡 [Difficulty Level]

Match each item in Column A with the appropriate item in Column B.

Column A:
1. [Item 1]
2. [Item 2]
3. [Item 3]
4. [Item 4]

Column B:
A. [Definition/Example A]
B. [Definition/Example B]
C. [Definition/Example C]
D. [Definition/Example D]
```

### Ordering Format
```
## Question X: [Topic]
🔍/🧩/💡 [Difficulty Level]

Arrange the following steps in the correct order:

A. [Step A]
B. [Step B]
C. [Step C]
D. [Step D]
```

### Diagram-Based Question Format
```
## Question X: [Topic]
🔍/🧩/💡 [Difficulty Level]

Examine the following database diagram:

```mermaid
[Appropriate diagram code]
```

[Question text based on the diagram]

A. [Option A]
B. [Option B]
C. [Option C]
D. [Option D]
```

## Mermaid Diagram Guidelines for Questions

When creating diagram-based questions, use appropriate Mermaid syntax based on the type of visualization needed:

1. **Entity-Relationship Diagrams** for database structure questions:
```mermaid
classDiagram
  class Table1 {
    +column1: datatype
    +column2: datatype
  }
  class Table2 {
    +column1: datatype
    +column2: datatype
  }
  Table1 "1" -- "n" Table2: relationship
```

2. **Flowcharts** for process flows, algorithms, or troubleshooting:
```mermaid
flowchart LR
  subgraph "Process Name"
    A["Step 1"]
    B["Step 2"]
    C["Step 3"]
    D["Step 4"]
  end
  A --> B
  B --> C
  C --> D
```

3. **Sequence Diagrams** for interaction scenarios:
```mermaid
sequenceDiagram
  participant Actor1
  participant Actor2
  
  Actor1->>Actor2: Action
  Actor2-->>Actor1: Response
```

4. **Custom Diagrams** that match those specifically used in Day [X] training:
   - List specific diagram types used in this day's material
   - Adapt format to match the instructor's presentation style
   - Include similar elements and structures

Include diagrams that specifically reflect those used in the Day [X] training material, such as:
- [Specific diagram example 1 from training]
- [Specific diagram example 2 from training]
- [Specific diagram example 3 from training]

## Special Considerations for Day [X]

- Focus on [Character Name]'s specific terminology and phrases
- Include questions related to [Character Name]'s rules, principles, or commandments
- Reference any war stories or incidents described by [Character Name]
- Incorporate [Character Name]'s unique perspective on database concepts
- Include database-specific syntax and tools emphasized in this day's training
- Address real-world SRE scenarios mentioned in the training

DO NOT include the correct answers or explanations in the questions themselves. These will be provided in a separate answer key document.
