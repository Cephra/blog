
This program is a command-line interface (CLI) that generates blog posts using AI-powered models. It allows users to interact with the program through a series of commands, which can be used to generate, extend, and summarize blog posts.

**Program Structure**

The program consists of several components:

1. **Argument Parsing**: The `argparse` module is used to parse command-line arguments.
2. **Blog Post Generation Interface**: This is the main interface that users interact with. It provides a series of commands (generate, extend, summarize) that allow users to generate, extend, and summarize blog posts.
3. **Agents**: These are AI-powered models that generate responses based on user input. There are three agents:
	* `BlogAgent`: Generates a blog post from scratch.
	* `ExtendAgent`: Extends an existing blog post with more content.
	* `SummaryAgent`: Generates a summary of an existing blog post.

**Commands**

The program provides the following commands:

1. **generate**: Generates a new blog post using the `BlogAgent`.
2. **extend**: Extends an existing blog post using the `ExtendAgent`.
3. **summarize**: Generates a summary of an existing blog post using the `SummaryAgent`.
4. **bye**: Exits the program.

**Program Flow**

Here is an overview of how the program flows:

1. The user starts the program by running it from the command line.
2. The program parses the command-line arguments and initializes the blog post generation interface.
3. The user interacts with the program using one of the available commands (generate, extend, summarize).
4. The program uses the corresponding agent to generate a response based on the user's input.
5. The program updates the blog post with the generated content and saves it to disk.
6. The program continues running until the user exits using the `bye` command.

**Requirements**

This program requires:

1. Python 3.x
2. The `argparse` module
3. The `ollama` library 

**Screenshots**

![generation](generation.png)