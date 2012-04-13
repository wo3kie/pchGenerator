import argparse
import os

def processArgv( argv ):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description =
            "PCHGenerator is a tool for support precompiled header generation. "
            "It scans source files in project and selects the most often used headers "
            "for putting them into precompiled header.",

        epilog =
            "Examples:\n"
            "pch.py -c='-I. -I.. -DDEBUG' main.cpp impl.cpp\n"
            "pch.py -c='-I/boost' -e boost -x serialization thread -- main.cpp\n\n"
            "Author: Lukasz Czerwinski (wo3kie@gmail.com)(https://github.com/wo3kie/pchGenerator)"
    )

    parser.add_argument(
        '-w', '--watch-header',
        default="",
        help=
            'Print debug information for particular header.'
            ' Exact full path expected (eg.:'
            ' C:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/c++/3.4.5/vector).'
    )

    parser.add_argument(
        '-t', '--threshold',
        default=50,
        type=int,
        help=
            'Threshold in range 1-100 (default 50) (%%).'
            ' Specifies in how many percent of source files'
            ' a header should appeared, to put it into precompiled header.'
    )

    parser.add_argument(
        '-c', '--compilation-options',
        default="",
        help=
            'Options passed to compiler.'
            ' Compilation options are removed (g++: -c -fPIC).'
            ' Preprocessing option is added (g++: -E).'
            ' Header usage info option is added (g++: -H).'
    )

    parser.add_argument(
        '-e', '--exclude',
        default=[],
        nargs='*',
        help=
            'Do not put such files in PCHeader'
            ' (eg.: -e boost, ignore all boost headers).'
    )

    parser.add_argument(
        '-x', '--exclude-except',
        default=[],
        nargs='*',
        help=
            'Exceptions from exclude list'
            ' (eg.: -e boost -x thread, ignore all boost but thread headers).'
    )

    parser.add_argument(
        '-o', '--output',
        default='precompiled.h',
        help=
            'Output filename (default precompiled.h).'
    )

    parser.add_argument(
        '-p', '--project-path',
        default='',
        help=
            'Path to your project (default `cwd`).'
            ' Used to distinguish projects headers from others.'
    )

    parser.add_argument(
        'files',
        nargs='+',
        help=
            'Source files to be processed.'
    )

    result = parser.parse_args( argv )

    if result.project_path == '':
        result.project_path = os.getcwd()

    return result
