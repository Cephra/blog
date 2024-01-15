#!/usr/bin/env python3

import argparse

from interface import BlogGenerationInterface

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Blog Post Generator')
    parser.add_argument('postname', help='The name of the blog post')
    parser.add_argument('-s', '--start-line', type=int, default=None, help='The starting line number (optional)')
    parser.add_argument('-e', '--end-line', type=int, default=None, help='The ending line number (optional)')
    parser.add_argument('-m', '--model', type=str, default='llama3.1', help='The model to use (optional)')
    parser.add_argument('-S', '--skip-summary', action='store_true', help='Skip summary generation (optional)')
    parser.add_argument('-G', '--skip-generate', action='store_true', help='Skip post generation (optional)')

    args = parser.parse_args()
    
    BlogGenerationInterface(**vars(args)).cmdloop()