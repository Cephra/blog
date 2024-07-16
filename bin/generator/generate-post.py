#!/usr/bin/env python3

import argparse

from blog_post_generator import BlogPostGenerator

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Blog Post Generator')
    parser.add_argument('postname', help='The name of the blog post')
    parser.add_argument('instructions', help='The instructions for the blog post')
    parser.add_argument('-s', '--start-line', type=int, default=None, help='The starting line number (optional)')
    parser.add_argument('-e', '--end-line', type=int, default=None, help='The ending line number (optional)')
    parser.add_argument('-m', '--model', type=str, default='llama3', help='The model to use (optional)')
    parser.add_argument('-S', '--skip-summary', action='store_true', help='Skip summary generation (optional)')
    parser.add_argument('-G', '--skip-generate', action='store_true', help='Skip post generation (optional)')

    args = parser.parse_args()

    blog_post_generator = BlogPostGenerator(args.postname, args.instructions, model=args.model)
    #blog_post_generator.generate_post(
    #    args.start_line,
    #    args.end_line,
    #    args.skip_summary,
    #    args.skip_generate
    #)
    blog_post_generator.repl()