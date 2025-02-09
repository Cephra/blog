#!/usr/bin/env python3

import argparse

from app.interface import BlogGenerationInterface

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Blog Post Generator')

    parser.add_argument('postname', help='The name of the blog post')
    parser.add_argument('-m', '--model', type=str, default='llama3.1', help='The model to use (optional)')

    args = parser.parse_args()
    
    BlogGenerationInterface(**vars(args)).cmdloop()