# Contributing to BatterUp

Thank you for your interest in contributing! BatterUp thrives on a diverse library of exercises that help people learn TDD.

## How to Contribute

### Adding New Exercises

The most valuable contributions are well-designed exercises. Follow these guidelines:

#### Exercise Requirements

1. **Completion Time**: 10-15 minutes for someone learning
2. **Clear Scope**: Single, focused concept or feature
3. **Real-World Relevance**: Something learners can relate to
4. **Progressive Complexity**: Start simple, build to harder cases
5. **No Unrelated Cognitive Load**: Provide all boilerplate

#### Exercise Structure

Create a new directory: `exercises/{number}-{name}/`

Required files:

```
exercises/XX-your-exercise/
├── spec.md                    # Requirements specification
└── template/
    ├── your_module.py         # Implementation file (stubs only)
    ├── test_your_module.py    # Test file (empty, Senior will fill)
    ├── requirements.txt       # Python dependencies
    └── .gitignore            # Standard Python .gitignore
```

#### Writing spec.md

Your spec should include:

```markdown
# Exercise N: [Name]

## Overview
Brief description (1-2 sentences)

## Requirements
Clear list of what should be implemented

## Specifications
Technical details:
- Input/output types
- Method signatures
- Error handling requirements
- Edge cases

## Example Usage
```python
# Concrete examples showing expected behavior
```

## Tips
Helpful hints without giving away solutions

## Time Estimate
10-15 minutes
```

#### Creating Template Files

**Implementation file** (`your_module.py`):
- Include module docstring
- Define class/functions with signatures
- Add method docstrings
- Use `pass` for empty implementations
- Include type hints if appropriate

Example:
```python
"""
Module description.
"""


class YourClass:
    """Class description."""

    def method_name(self, param):
        """Method description.

        Args:
            param: Parameter description.

        Returns:
            Return value description.

        Raises:
            ExceptionType: When this exception is raised.
        """
        pass
```

**Test file** (`test_your_module.py`):
- Import pytest and the module
- Add a comment that Senior will fill it
- That's it! Keep it minimal

**requirements.txt**:
```
pytest>=7.4.0
pytest-cov>=4.1.0
# Add any specific libraries needed for the exercise
```

### Testing Your Exercise

Before submitting:

1. Start a batterup session with your exercise:
   ```
   /batterup start your-exercise
   ```

2. Verify the Senior agent:
   - Writes appropriate tests
   - Covers all requirements
   - Explains clearly

3. Implement the solution yourself
   - Takes 10-15 minutes?
   - Requirements clear?
   - Boilerplate sufficient?

4. Verify the Reviewer agent:
   - Provides helpful feedback
   - Identifies real issues
   - Explains improvements

### Updating the Command

Add your exercise to `.claude/commands/batterup.md`:

```markdown
## Exercise Directory Mapping

Map user input to directory names:
- "your-exercise" → "XX-your-exercise"
```

### Exercise Ideas

Good exercise topics:
- Data structure operations (stack, queue)
- Text processing (word counter, palindrome checker)
- Simple algorithms (fibonacci, prime checker)
- Format converters (JSON, CSV)
- Validators (email, password, credit card)
- Games (tic-tac-toe, rock-paper-scissors)
- Utilities (date calculator, unit converter)

Avoid:
- Exercises requiring external APIs
- Complex setup (databases, servers)
- Multiple file coordination
- Domain-specific knowledge
- More than 15 minutes of work

## Improving Agent Prompts

The agents are defined in `lib/`:
- `senior-agent-prompt.md` - Test writing behavior
- `reviewer-agent-prompt.md` - Code review behavior

When modifying:
- Keep language encouraging and supportive
- Focus on learning, not perfection
- Provide examples
- Test with multiple exercises

## Submission Process

1. Fork the repository
2. Create a feature branch: `git checkout -b add-exercise-name`
3. Add your exercise with all required files
4. Test thoroughly with Claude Code
5. Update README.md to list your exercise
6. Submit a pull request with:
   - Description of the exercise
   - What concepts it teaches
   - Screenshot of successful completion (optional)

## Code Review Process

Maintainers will check:
- [ ] Exercise is 10-15 minutes
- [ ] spec.md is clear and complete
- [ ] Template files are minimal but sufficient
- [ ] Boilerplate is appropriate
- [ ] Exercise works end-to-end with Claude Code
- [ ] No unrelated cognitive load

## Style Guidelines

### Markdown
- Use headers appropriately
- Include code blocks with syntax highlighting
- Keep lines under 100 characters
- Use lists for clarity

### Python
- Follow PEP 8
- Use type hints for clarity (optional)
- Include docstrings
- Keep examples simple

### Writing Style
- Use clear, simple language
- Address learners directly ("you")
- Be encouraging
- Avoid jargon without explanation

## Questions?

Open an issue with the label `question` or `exercise-idea`.

## License

By contributing, you agree your contributions will be licensed under the MIT License.

---

Thank you for helping others learn TDD! 🙏
