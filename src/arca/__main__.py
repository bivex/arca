import sys
from .arca import Program

def main():
    if len(sys.argv) < 2:
        print("Usage: arca <program_file.txt> [output_file.musicxml]")
        sys.exit(1)
    
    program_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    p = Program(program_file)
    if output_file:
        p.show_XML(output_file)
    else:
        # Default behavior if no output file specified?
        # Maybe just run it.
        pass

if __name__ == "__main__":
    main()
