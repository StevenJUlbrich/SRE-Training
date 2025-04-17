# Mermaid Diagram Generation Guidelines
# Mermaid Diagram Generation Guidelines

When creating Mermaid diagrams, follow these best practices to ensure proper rendering:

## Core Rules
1. **Always quote text** containing spaces, punctuation, or syntax characters
2. **Use HTML entities** for problematic characters inside quoted text
3. **Apply HTML tags** for text formatting (not escape sequences like \n)

## Character Handling Guide

### Quotes (`"` and `'`)
- Replace double quotes with `&quot;` or `&#34;`
- Replace single quotes with `&apos;` or `&#39;`
- Example: `A["Node with a &quot;quoted&quot; word"]`

### Semicolons (`;`)
- Replace with `&#59;` especially within node text
- Example: `A["This node has a semicolon&#59; inside"]`

### Brackets, Parentheses, Braces (`[](){}`)
- Enclose entire node text in double quotes
- Example: `A["Function call: myFunction()"]`

### HTML Reserved Characters (`<`, `>`, `&`)
- Use `&lt;` for `<`
- Use `&gt;` for `>`
- Use `&amp;` for `&`
- Example: `A["Compare: 5 &lt; 10"]`

### Hash/Pound Sign (`#`)
- Use `&#35;` if causing problems
- Example: `A["Item &#35;1"]`

## Text Formatting

### Supported HTML Tags
- `<br>` - Line break
- `<b>` or `<strong>` - Bold text
- `<i>` or `<em>` - Italic text
- Occasionally supported: `<u>`, `<sub>`, `<sup>`

### Example with Formatting
```mermaid
graph LR
    A["<b>Important Note:</b><br>Use <i>HTML tags</i><br>for text formatting."] --> B(Okay);