import argparse

def processArgv( argv ):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description =
            "PCHGenerator is a tool for support precompiled header generation. "
            "It scans source files in project and selects the most often used headers "
            "for putting them into precompiled header.",

        epilog =
            "Examples:\n"
            "-c \"-I. -I.. -DDEBUG\" -t 80 -p \"/home/test\" main.cpp impl.cpp\n"
            "-e boost -x serialization thread -p \"/home/test\" -- main.cpp\n\n"
            "Author: Lukasz Czerwinski (wo3kie@gmail.com)"
    )

    parser.add_argument(
        '-t', '--threshold',
        default=50,
        type=int,
        help='threshold in range 1-100 (default 50) (%%)'
    )

    parser.add_argument(
        '-c', '--compilation-options',
        default="",
        help='options passed to compiler'
    )

    parser.add_argument(
        '-e', '--exclude',
        default="",
        nargs='*',
        help='do not put such files in PCHeader'
    )

    parser.add_argument(
        '-x', '--exclude-except',
        default="",
        nargs='*',
        help='enforce to put such files in PCHeader'
    )

    parser.add_argument(
        '-o', '--output',
        default="precompiled.h",
        help='enforce to put such files in PCHeader'
    )

    parser.add_argument(
        '-p', '--project-path',
        required=True,
        help='path to your project'
    )
    
    parser.add_argument(
        'files',
        nargs='+',
        help='source files to be processed'
    )

    result = parser.parse_args( argv )

    return result
