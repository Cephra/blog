import os
import subprocess
import tomllib
import tomli_w

from const import WORKSPACE

class BlogPost():
    def __init__(self, postname: str) -> None:
        self._postname = postname
        self._postfile = os.path.join(WORKSPACE, 'content/posts', self._postname + '.md')

        self._front_matter = {}
        self._front_matter_offset = 0
        self._content = []

        if not os.path.exists(self._postfile):
            self.is_fresh = True
            cmd = ['hugo', 'new', 'content', 'posts/{0}.md'.format(self._postname)]
            subprocess.run(cmd, check=True, cwd=WORKSPACE)
        else:
            self.is_fresh = False

        self._read_post()

    def _read_post(self) -> None:
        front_matter_raw = []
        try:
            with open(self._postfile, 'r') as file:
                is_front_matter = False

                for line in file:
                    if line.startswith('+++'):
                        is_front_matter = not is_front_matter
                        self._front_matter_offset += 1
                        continue

                    if is_front_matter:
                        front_matter_raw.append(line)
                        self._front_matter_offset += 1
                    else:
                        self._content.append(line)
        except FileNotFoundError as e:
            print(f"Error: File '{self._postfile}' not found.")
        except IOError as e:
            print(f"Error reading file '{self._postfile}': {e}")
        
        self._front_matter = tomllib.loads(''.join(front_matter_raw))
            
    def _adjust_line_numbers(self, start_line: int, end_line: int) -> (int, int):
        if self._front_matter:
            if start_line is not None:
                num_front_matter_lines = len(self._front_matter)
                start_line = max(0, start_line - self._front_matter_offset - 1)
            if end_line is not None:
                end_line = min(len(self._content), end_line - self._front_matter_offset)
        return start_line, end_line

    def join_content(self, start_line: int = None, end_line: int = None) -> str:
        start_line, end_line = self._adjust_line_numbers(start_line, end_line)
        return ''.join(self._content[start_line:end_line])

    def front_matter_to_toml(self) -> str:
        return tomli_w.dumps(self._front_matter)

    def update_content(
                self,
                new_content: str,
                start_line: int = None,
                end_line: int = None
            ) -> None:
        new_content = ["{}\n".format(line) for line in new_content.split('\n')]
        start_line, end_line = self._adjust_line_numbers(start_line, end_line)
        prefix = self._content[:start_line] if (start_line is not None) else []
        suffix = self._content[end_line:] if (end_line is not None) else []
        self._content = prefix + new_content + suffix
    
    def update_summary(self, new_summary: str) -> None:
        self._front_matter['summary'] = new_summary.strip()

    def save(self) -> None:
        with open(self._postfile, 'w') as file:
            if self._front_matter:
                file.write("+++\n{}+++\n".format(self.front_matter_to_toml()))
            if self._content:
                file.write(self.join_content())
        if self.is_fresh:
            self.is_fresh = False
