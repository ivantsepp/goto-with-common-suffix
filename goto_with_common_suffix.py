import os, re
from urllib.parse import urlparse
import sublime, sublime_plugin

class GotoWithCommonSuffixCommand(sublime_plugin.WindowCommand):

    def run(self):
        sublime.active_window().show_input_panel("Enter (copied) file path", "", self.on_done, None, None)

    def on_done(self, text):
        original_text = text
        text = text.strip()
        line_number = None

        # Attempt to parse uri-like paths
        parse_result = urlparse(text)
        if parse_result:
            text = parse_result.path
            if parse_result.fragment and parse_result.fragment[1:]:
                # GitHub urls look like https://github.com/owner/repo/blob/master/lib/Example/Class.php#L714-L721
                line_number = re.sub(r'-L\d+', '', parse_result.fragment[1:])

        # Match line number format Class.php:220
        basename = os.path.basename(text)
        matches = re.match(r'(?P<basename>[^:]*):(?P<line_number>\d+)', basename)
        if matches:
            line_number = matches.group('line_number')
            basename = matches.group('basename')

        folders = list(filter(None, text.split(os.sep)))

        # Loop through each opened directory in the sublime window and open first match
        for path in self.window.folders():
            folders_to_match = list(folders)
            prefix_path = path
            while len(folders_to_match) > 0:
                matched = False
                current_folder = folders_to_match[0]
                for directory in os.listdir(path):
                    if os.path.isdir(os.path.join(path, directory)) and current_folder == directory:
                        path = os.path.join(path, current_folder)
                        folders_to_match = self.__pop_if(folders_to_match)
                        matched = True
                        break
                folders_to_match = self.__pop_if(folders_to_match, not matched)

            absolute_path = os.path.join(path, basename)
            if os.path.exists(absolute_path):
                absolute_path = absolute_path + ":" + line_number if line_number else absolute_path
                self.window.open_file(absolute_path, sublime.ENCODED_POSITION);
                return
            elif path != prefix_path:
                relative_path = path.replace(prefix_path, '')
                relative_path = self.__pop_if(relative_path, relative_path[0] == os.sep)
                self.window.run_command("show_overlay", {
                    "overlay": "goto",
                    "text": relative_path
                })
                return
        self.window.run_command("show_overlay", {"overlay": "goto", "text": original_text})
        self.window.status_message("Sorry, there was no common suffix match")

    def __pop_if(self, ary, cond = True):
        return ary[1:] if cond else ary
