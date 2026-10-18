## 16.1. Interactive Mode

There are two variants of the interactive REPL. The classic basic interpreter is supported on all platforms with minimal line control capabilities.

Since Python 3.13, a new interactive shell is used by default. This one supports color, multiline editing, history browsing, and paste mode. To disable color, see Controlling color for details. Function keys provide some additional functionality. F1 enters the interactive help browser `pydoc`. F2 allows for browsing command-line history with neither output nor the \>\>\> and ... prompts. F3 enters "paste mode", which makes pasting larger blocks of code easier. Press F3 to return to the regular prompt.

When using the new interactive shell, exit the shell by typing exit or quit. Adding call parentheses after those commands is not required.

If the new interactive shell is not desired, it can be disabled via the `PYTHON_BASIC_REPL` environment variable.

### Sections

- [16.1.1. Error Handling](16.1.1-error-handling/README.md)
- [16.1.2. Executable Python Scripts](16.1.2-executable-python-scripts/README.md)
- [16.1.3. The Interactive Startup File](16.1.3-the-interactive-startup-file/README.md)
- [16.1.4. The Customization Modules](16.1.4-the-customization-modules/README.md)
