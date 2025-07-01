import argparse
import sys
from subprocess import run

def main():
    parser = argparse.ArgumentParser(description='OpenPIIMap CLI Toolkit')
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('validate', help='Run YAML schema validation')
    subparsers.add_parser('lint', help='Run YAML lint checks')
    subparsers.add_parser('generate-coverage', help='Regenerate coverage.json')

    args = parser.parse_args()

    if args.command == 'validate':
        run([sys.executable, 'scripts/validate-yamls.py'])
    elif args.command == 'lint':
        run([sys.executable, 'scripts/lint-yamls.py'])
    elif args.command == 'generate-coverage':
        run([sys.executable, 'scripts/generate-coverage-json.py'])
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
