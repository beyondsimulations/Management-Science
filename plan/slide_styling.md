# Lecture Template - Styling Guide

## Overview
This template is designed to create engaging, well-structured lectures that promote active learning and student engagement. It follows proven patterns for educational content delivery.

## Key Styling Elements

### 1. Progressive Disclosure (`. . .`)
- Use `. . .` to reveal content incrementally
- Prevents cognitive overload
- Maintains attention and pacing
- Allows for pauses and discussion

Best Practice: Place `. . .` before:
- Code examples you want to discuss after introduction
- Follow-up explanations
- Questions that students should think about first
- Tips and notes that reinforce main content

### 2. Highlighting (`.highlight`)
- Use `[text]{.highlight}` for key terms and important concepts
- First mention of new terminology
- Critical takeaways
- Concepts students must remember

Best Practice: Limit to 1–3 highlights per slide to avoid dilution

### 3. Callout Boxes

Types:
- `:::{.callout-tip}` - Best practices, helpful hints
- `:::{.callout-note}` - Additional information, context
- `:::{.callout-warning}` - Cautions, common pitfalls
- `:::{.callout-important}` - Critical information

Best Practice: Use sparingly (0–1 per slide) for maximum impact

### 4. Interactive Elements

Questions — `[Question:]{.question}` or `[Question]{.question}`
- Engage critical thinking
- Check understanding before revealing answers
- Create discussion opportunities
- Use before demonstrating code output

Code-based questions (strongly encouraged in early lectures)
- Ask for predictions about code behavior or output
- Then reveal the code execution and results
- Use progressive disclosure to separate “think time” from “answer reveal”
- Keep questions tightly scoped to one concept or function

Examples:
- “What do you expect `np.random.normal(0,1, size=10000).mean()` to be approximately?”
- “If we double `scale`, what happens to the probability of loss?”

### 5. Code Examples

Structure:
```python
#| eval: true
#| output-location: fragment
```

Options:
- `#| eval: true` - Execute code and show results
- `#| eval: false` - Show code only (for discussion/prediction)
- `#| output-location: fragment` - Show output progressively

Best Practice:
- Keep examples short and focused (< 10 lines)
- Use clear, descriptive comments
- Show both input and output (after a prediction question)
- Progress from simple to slightly more complex
- Prefer code-based questions over hands-on tasks in the first hour

## Lecture Structure

### Opening: Quick Recap (3–5 slides)
- Review 2–3 key concepts from previous lecture
- Refresh memory and create continuity
- Connect to today's topic
- Include at least one callout-tip for reinforcement

### Core Content: Main Topic Introduction (2–3 slides)
- "What is X?" — Definition and context
- "Why is X important?" — Motivation and benefits
- "How to get started" — Quick setup/first example
- Use progressive disclosure to control pacing

### Middle: Deep Dive (6–10 slides)
- Introduce core features one by one
- Provide multiple examples per concept
- Mix explanations with code demonstrations
- Include edge cases and considerations
- Incorporate interactive code-based questions
- Defer hands-on tasks to later sessions (practice notebooks or competitions)

### Advanced: Going Deeper (3–5 slides)
- Advanced features and methods
- Technical deep-dives
- Performance considerations
- Real-world applications
- Mark as “necessary” here if later practice/competition relies on these techniques

### Closing (2 slides)
- Summary callout box
- Literature and resources

## Pacing and Flow

### Cognitive Load Management
1. Introduce one concept at a time
2. Provide 2–3 examples per concept
3. Follow with interactive element (question or code-based prediction)
4. Reinforce with callout box

### The Slide Rhythm
- Odd slides: Introduce new concepts
- Even slides: Practice or apply concepts via code-based questions
- Questions before answers: Always ask before revealing
- Code-based questions immediately after explanations

## Typography and Formatting

### Bold Text (`**text**`)
- Use for emphasis within sentences
- Actions (“provide”, “change”, “create”)
- Important warnings
- Keep to minimum (1–2 per bullet point max)

### Inline Code (`code`)
- Function names, method names
- Variable names
- File extensions
- Technical keywords

### Lists
- Use bullet points for conceptual content
- Use numbered lists for procedures/steps
- Keep items parallel in structure
- Aim for 3–5 items per list

## Questions: Types and Purposes

### Knowledge Check Questions
- “Have you heard of X?”
- “Do you know what X means?”
- Purpose: Assess prior knowledge

### Prediction Questions (Code-Based)
- “What do you expect will be printed?”
- “What will happen if we change parameter Y?”
- Purpose: Engage active thinking before demonstration

### Conceptual Questions
- “Why does X matter?”
- “How does X differ from Y?”
- Purpose: Deepen understanding

## Common Patterns

### The “Sidenote” Pattern
Use for tangential but important concepts:
1. Introduce with a question
2. Provide progressive explanation
3. Connect back to main topic

### The “In Action” Pattern
For code-centered practice (without tasks):
1. Introduce feature/concept
2. Show a small example
3. Ask a code-based prediction question
4. Reveal the output with `#| output-location: fragment`

### The “Common Methods” Pattern
For toolbox-style content:
1. List methods with brief descriptions
2. Follow with a callout encouraging experimentation
3. Optionally add a comparative code-based question (predict differences in outputs)

## Visual Hierarchy

### Title Slides
```
# [Title Text]{.flow} {.title}
```
- Use for section breaks
- Keep text short and impactful
- Use sparingly (beginning, main topic, literature)

### Regular Slides
```
## Slide Title
```
- Use descriptive, action-oriented titles
- Make titles questions when appropriate
- Avoid generic titles like “Example 1”

## Best Practices Summary

### Do:
✓ Use progressive disclosure (`. . .`)  
✓ Ask questions before showing answers  
✓ Use code-based prediction questions after explanations  
✓ Include callouts for reinforcement  
✓ Keep code examples short and focused  
✓ Use highlighting sparingly for key terms  
✓ Connect new content to previous knowledge  
✓ Emphasize clarity of code and output

### Don’t:
✗ Overuse highlighting (max 3 per slide)  
✗ Put multiple callouts on one slide  
✗ Show code without explanation or prediction  
✗ Skip the recap section  
✗ Use jargon without definition  
✗ Create walls of text  
✗ Forget pacing for code walkthroughs  
✗ Mix too many concepts on one slide

## Adaptation Guidelines

When adapting this template:
1. Keep the overall structure (recap → intro → deep dive → advanced → closing)
2. Maintain the rhythm of explanation → example → code-based question
3. Adjust the number of slides per section based on complexity
4. Scale the difficulty of examples to your audience
5. Preserve interactive elements (questions)
6. Keep progressive disclosure for pacing control
7. Mark “Advanced” as required when later practice/competition depends on it

## Accessibility Considerations

- Use descriptive alt text for any images (not in this template but add when needed)
- Ensure code examples have sufficient comments
- Provide both visual and text-based explanations
- Use clear, simple language
- Avoid color as the only means of conveying information
- Keep text high contrast against background

Remember: The goal is to create lectures that are:
- Engaging through questions and interactivity
- Clear through progressive disclosure and examples
- Practical through code-based predictions and demonstrations
- Memorable through highlighting and repetition
- Accessible through multiple explanation modes