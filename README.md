# BatterUp: Learn TDD Through Pair Programming

<div align="center">

**A [Vibe Academy](https://www.vibe.academy/) Learning Tool**

*Learn Test-Driven Development through hands-on, AI-powered pair programming*

---

</div>

BatterUp is an interactive learning environment that teaches Test-Driven Development (TDD) through AI-powered pair programming. Experience the "batter up" approach where a senior developer writes tests and you implement the code to pass them.

## What is BatterUp?

The "batter up" pairing technique is especially effective for learning:
- **Senior Developer** (more experienced) writes the test specifications
- **Junior Developer** (learner) focuses on implementation
- **Code Reviewer** provides constructive feedback

This approach helps learners:
- Focus on implementation without design paralysis
- Learn TDD methodology naturally
- Understand requirements through tests
- Receive personalized code review feedback

## Prerequisites

- Python 3.8 or higher
- [Claude Code CLI](https://docs.claude.com/en/docs/claude-code) installed and configured
- Basic understanding of Python syntax

## Quick Start

### 1. Clone and Setup

```bash
git clone https://github.com/yourusername/batterup.git
cd batterup
```

### 2. Start Claude Code

```bash
claude
```

### 3. Start a Learning Session

In Claude Code, run:

```
/batterup start calculator
```

That's it! Claude will guide you through the entire learning experience.

## How It Works

### The Learning Flow

```
┌─────────────────────────────────────────────────────────┐
│ 1. Choose Exercise                                      │
│    /batterup start calculator                           │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│ 2. Senior Developer Writes Tests                        │
│    - Reads exercise specification                       │
│    - Writes comprehensive pytest test suite            │
│    - Explains approach and requirements                 │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│ 3. You Implement (Interactive)                          │
│    - Write code to pass tests                           │
│    - Run tests iteratively: pytest -v                   │
│    - Ask questions anytime!                             │
│    - Focus on making tests green                        │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│ 4. Code Review                                          │
│    - Reviewer analyzes your passing code                │
│    - Provides constructive feedback                     │
│    - Suggests improvements                              │
│    - Explains best practices                            │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│ 5. Refine & Complete                                    │
│    - Apply feedback (if needed)                         │
│    - Learn from suggestions                             │
│    - Celebrate completion! 🎉                           │
└─────────────────────────────────────────────────────────┘
```

## Available Exercises

All exercises are designed to be completed in **10-15 minutes** and teach fundamental programming concepts:

### 1. Calculator
**Concepts**: Basic methods, arithmetic operations, error handling

Build a simple calculator with add, subtract, multiply, and divide operations.

```
/batterup start calculator
```

### 2. Temperature Converter
**Concepts**: Mathematical formulas, floating-point arithmetic, validation

Convert between Celsius, Fahrenheit, and Kelvin with proper rounding.

```
/batterup start temperature-converter
```

### 3. String Calculator
**Concepts**: String parsing, incremental development, validation

A classic TDD kata - add numbers from a delimited string.

```
/batterup start string-calculator
```

### 4. Todo List
**Concepts**: Data structures, state management, CRUD operations

Build a simple todo list manager with task tracking.

```
/batterup start todo-list
```

## During Your Session

### Running Tests

Each session creates a workspace in `sessions/`. To run tests:

```bash
cd sessions/calculator-2025-01-15-143022/  # Your session directory
pip install -r requirements.txt            # First time only
pytest -v                                  # Run tests
```

### Getting Help

You can ask questions anytime during your session:
- "Can you explain what this test is checking?"
- "I'm getting an error, what does it mean?"
- "What's the best way to handle this edge case?"
- "Can you give me a hint without showing the solution?"

### Interactive Review

When the code reviewer provides feedback, you can:
- Ask for clarification on suggestions
- Discuss trade-offs
- Request examples
- Ask about best practices

## Project Structure

```
batterup/
├── .claude/
│   └── commands/
│       └── batterup.md          # Main orchestration command
│
├── exercises/                   # Exercise library
│   ├── 01-calculator/
│   │   ├── spec.md             # Requirements
│   │   └── template/           # Boilerplate code
│   ├── 02-temperature-converter/
│   ├── 03-string-calculator/
│   └── 04-todo-list/
│
├── lib/                        # Agent behavior definitions
│   ├── senior-agent-prompt.md
│   └── reviewer-agent-prompt.md
│
├── sessions/                   # Your work sessions (git-ignored)
│   └── calculator-2025-01-15-143022/
│
└── README.md
```

## Tips for Success

### For Beginners
1. **Read test names carefully** - they describe what to implement
2. **Run tests often** - see immediate feedback
3. **Start simple** - get one test passing at a time
4. **Ask questions** - that's what the Senior is for!
5. **Learn from review** - feedback is a gift

### TDD Best Practices
- Red → Green → Refactor cycle
- Write minimal code to pass tests
- Don't over-engineer
- Let tests guide your design
- Refactor with confidence (tests protect you)

### Python-Specific Tips
- Use descriptive variable names
- Follow PEP 8 style guidelines
- Handle edge cases (empty inputs, zeros, negatives)
- Use appropriate data structures
- Write clear docstrings

## Customization

### Adding Your Own Exercises

1. Create a new directory: `exercises/05-your-exercise/`
2. Add `spec.md` with clear requirements
3. Create `template/` with boilerplate:
   - Empty implementation file with class/function stubs
   - Empty test file with imports
   - `requirements.txt` with pytest
   - `.gitignore` for Python

4. Update the command mapping in `.claude/commands/batterup.md`

### Modifying Agent Behavior

Edit the agent prompts to customize the learning experience:
- `lib/senior-agent-prompt.md` - How tests are written and explained
- `lib/reviewer-agent-prompt.md` - Code review style and focus areas

## Troubleshooting

### Claude Code not found
Install Claude Code CLI: https://docs.claude.com/en/docs/claude-code

### Tests won't run
```bash
# Install pytest in your session directory
cd sessions/your-session-directory/
pip install -r requirements.txt
```

### Session directory unclear
Check Claude's output for the full path, or:
```bash
ls -lt sessions/  # Shows most recent sessions first
```

## Learning Path

Recommended progression:

1. **Calculator** - Easiest, learn the flow
2. **Temperature Converter** - Similar difficulty, different domain
3. **String Calculator** - Introduces string parsing and complexity
4. **Todo List** - Most complex, uses data structures

## Philosophy

BatterUp is built on these principles:

- **Low cognitive load**: Boilerplate provided, focus on learning
- **Immediate feedback**: Tests show progress instantly
- **Safe to fail**: Make mistakes in a supportive environment
- **Real-world practice**: TDD is how professionals code
- **Interactive learning**: Ask questions, get personalized help

## Contributing

Want to add exercises or improve the experience?

1. Fork the repository
2. Create a new exercise following the structure
3. Test it with Claude Code
4. Submit a pull request

## License

MIT License - feel free to use this for learning and teaching!

## 📚 Continue Learning

Want to level up your coding skills even further? Check out [How to Read Code](https://www.vibe.academy/how-to-read-code) - a comprehensive course from Vibe Academy that teaches you the essential skill of understanding and navigating codebases like a pro.

---

**Ready to learn TDD?**

```bash
cd batterup
claude
```

Then:
```
/batterup start calculator
```

Happy coding! 🚀

---

<div align="center">

**Made with ❤️ by [Vibe Academy](https://www.vibe.academy/)**

*Empowering developers through practical, hands-on learning*

</div>
