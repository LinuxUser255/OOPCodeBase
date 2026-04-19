# Demo OOP Codebase

### Mission
This project is to demonstrate the use of Object-Oriented Programming and
basics of how a code-base is built and works.

---

## Code Execution Flow Chart

```
══════════════════════════════════════════════════════════════════════════════
                           $ python3 main.py
══════════════════════════════════════════════════════════════════════════════
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  PHASE 1: MODULE LOADING                                                     │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   main.py (line 3)                                                           │
│   from src.say_hello import Printer                                          │
│        │                                                                     │
│        ▼                                                                     │
│   src/say_hello/__init__.py                                                  │
│   from src.say_hello.hello import Printer                                    │
│        │                                                                     │
│        ▼                                                                     │
│   src/say_hello/hello.py                                                     │
│   ┌────────────────────────────────────────┐                                 │
│   │  class Printer:                        │                                 │
│   │      __init__(ink_level, paper_level)  │                                 │
│   │      print_document(pages)             │  ◄── Class definition loaded   │
│   │      check_status()                    │                                 │
│   │      notify_low_ink()                  │                                 │
│   │      notify_out_of_paper()             │                                 │
│   └────────────────────────────────────────┘                                 │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  PHASE 2: ENTRY POINT CHECK                                                  │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   main.py (line 44-45)                                                       │
│   if __name__ == "__main__":  ──► TRUE (running as script)                   │
│       main()                                                                 │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  PHASE 3: main() EXECUTION                                                   │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   STEP 1: Object Instantiation (line 29)                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐    │
│   │  printer = Printer(100, 100)                                        │    │
│   │       │                                                             │    │
│   │       ▼                                                             │    │
│   │  Printer.__init__(self, 100, 100)                                   │    │
│   │       │                                                             │    │
│   │       ├──► self.ink_level = 100                                     │    │
│   │       └──► self.paper_level = 100                                   │    │
│   │                                                                     │    │
│   │  [Printer object created in memory]                                 │    │
│   └─────────────────────────────────────────────────────────────────────┘    │
│                                    │                                         │
│                                    ▼                                         │
│   STEP 2: Greeting (line 30)                                                 │
│   ┌─────────────────────────────────────────────────────────────────────┐    │
│   │  print_hello()                                                      │    │
│   │       │                                                             │    │
│   │       ▼                                                             │    │
│   │  OUTPUT: "Hello, Object-Oriented Programming!"                      │    │
│   └─────────────────────────────────────────────────────────────────────┘    │
│                                    │                                         │
│                                    ▼                                         │
│   STEP 3: Check Initial Status (line 34)                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐    │
│   │  printer.check_status()                                             │    │
│   │       │                                                             │    │
│   │       ├──► notify_low_ink()                                         │    │
│   │       │         │                                                   │    │
│   │       │         └──► [100 > 10] ──► OUTPUT: "Ink level: 100%"       │    │
│   │       │                                                             │    │
│   │       └──► notify_out_of_paper()                                    │    │
│   │                 │                                                   │    │
│   │                 └──► [100 > 10] ──► OUTPUT: "Paper remaining: 100"  │    │
│   └─────────────────────────────────────────────────────────────────────┘    │
│                                    │                                         │
│                                    ▼                                         │
│   STEP 4: Print 33 Pages (line 38)                                           │
│   ┌─────────────────────────────────────────────────────────────────────┐    │
│   │  printer.print_document(33)                                         │    │
│   │       │                                                             │    │
│   │       ├──► [33 ≤ 100?] ──► YES, proceed                             │    │
│   │       │                                                             │    │
│   │       ├──► OUTPUT: "Printing 33 pages..."                           │    │
│   │       │                                                             │    │
│   │       ├──► paper_level = 100 - 33 = 67                              │    │
│   │       ├──► ink_level = 100 - (33 × 0.5) = 83.5                      │    │
│   │       │                                                             │    │
│   │       └──► check_status()                                           │    │
│   │                 │                                                   │    │
│   │                 ├──► notify_low_ink()                               │    │
│   │                 │         └──► OUTPUT: "Ink level: 83.5%"           │    │
│   │                 │                                                   │    │
│   │                 └──► notify_out_of_paper()                          │    │
│   │                           └──► OUTPUT: "Paper remaining: 67"        │    │
│   └─────────────────────────────────────────────────────────────────────┘    │
│                                    │                                         │
│                                    ▼                                         │
│   STEP 5: Print 20 More Pages (line 41)                                      │
│   ┌─────────────────────────────────────────────────────────────────────┐    │
│   │  printer.print_document(20)                                         │    │
│   │       │                                                             │    │
│   │       ├──► [20 ≤ 67?] ──► YES, proceed                              │    │
│   │       │                                                             │    │
│   │       ├──► OUTPUT: "Printing 20 pages..."                           │    │
│   │       │                                                             │    │
│   │       ├──► paper_level = 67 - 20 = 47                               │    │
│   │       ├──► ink_level = 83.5 - (20 × 0.5) = 73.5                     │    │
│   │       │                                                             │    │
│   │       └──► check_status()                                           │    │
│   │                 │                                                   │    │
│   │                 ├──► notify_low_ink()                               │    │
│   │                 │         └──► OUTPUT: "Ink level: 73.5%"           │    │
│   │                 │                                                   │    │
│   │                 └──► notify_out_of_paper()                          │    │
│   │                           └──► OUTPUT: "Paper remaining: 47"        │    │
│   └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  PHASE 4: PROGRAM EXIT                                                       │
├──────────────────────────────────────────────────────────────────────────────┤
│   main() returns ──► exit code 0                                             │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## File Dependency Diagram

```
                    ┌─────────────────┐
                    │    main.py      │  ◄── Entry point
                    │   (runs first)  │
                    └────────┬────────┘
                             │ imports
                             ▼
                    ┌─────────────────┐
                    │ src/__init__.py │  ◄── Package init (optional path)
                    └────────┬────────┘
                             │ re-exports
                             ▼
              ┌──────────────────────────────┐
              │ src/say_hello/__init__.py    │  ◄── Subpackage init
              └──────────────┬───────────────┘
                             │ imports
                             ▼
              ┌──────────────────────────────┐
              │ src/say_hello/hello.py       │  ◄── Printer class definition
              │                              │
              │   class Printer              │
              │     ├── __init__()           │
              │     ├── print_document()     │
              │     ├── check_status()       │
              │     ├── notify_low_ink()     │
              │     └── notify_out_of_paper()│
              └──────────────────────────────┘
```

## Packages and Modules `__init__.py` explained

## Dev: Python Packages vs Modules



- **Directories/Folders** → **Packages** (when they contain `__init__.py`)
- **Individual `.py` files** → **Modules**

---

## Visual Breakdown of Project

```
src/                                    ← PACKAGE (directory + __init__.py)
├── __init__.py                         ← Makes src/ a package
└── say_hello/                          ← PACKAGE (directory + __init__.py)
    ├── __init__.py                     ← Makes say_hello/ a package
    └── hello.py                        ← MODULE (individual .py file)
```

---

## The Rules

### For a Directory to be a Package:
1. It must be a **directory/folder**
2. It must contain an `__init__.py` file (can be empty)
3. Example: `say_hello/` is a package

### For a File to be a Module:
1. It must be a **`.py` file**
2. It contains Python code (classes, functions, variables)
3. Example: `hello.py` is a module

---

## Terminology Summary

| Term | What It Is | Example in OOP Project       |
|------|-----------|------------------------------|
| **Package** | Directory with `__init__.py` | `src/`, `say_hello/`         |
| **Module** | Individual `.py` file | `hello.py`, `main.py`        |
| **Subpackage** | Package inside another package | `say_hello/` (inside `src/`) |

---

## Import Implications

```python
# Importing from a PACKAGE (directory)
from src.say_hello import Printer        # Goes through say_hello/__init__.py

# Importing from a MODULE (file)
from src.say_hello.hello import Printer  # Directly from hello.py module
```

---

## Key Insight

The `__init__.py` file is what **transforms a regular directory into a Python package**. Without it (in Python 2 and older Python 3 versions), the directory would just be a folder, not importable as a package.
