from pylint.lint import Run

results = Run(['uc.py', '-rn', '-sn'], exit=False)
print(results.linter.stats['global_note'])
