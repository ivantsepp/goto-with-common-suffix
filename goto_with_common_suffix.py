import os, re
from urllib.parse import urlparse
import sublime, sublime_plugin

class GotoWithCommonSuffixCommand(sublime_plugin.WindowCommand):

    def run(self):
        sublime.active_window().show_input_panel("Enter (copied) file path", "", self.on_done, None, None)

    def on_done(self, text):
        original_text = text
        text = text.strip()
        parse_result = urlparse(text).path
        text = text if not parse_result else parse_result
        text = text[1:] if text[0] == os.sep else text
        basename = os.path.basename(text)
        for path in self.window.folders():
            prefix_path = path
            folders = text.split(os.sep)
            while len(folders) > 0:
                for directory in os.listdir(path):
                    matched = False
                    if os.path.isdir(os.path.join(path, directory)) and folders[0] == directory:
                        path = path + os.sep + folders[0]
                        folders = folders[1:]
                        matched = True
                        break
                folders = folders[1:] if not matched else folders

            if os.path.exists(os.path.join(prefix_path, basename)):
                path = os.path.join(prefix_path, basename)

            if path != '' and path != prefix_path:
                matched_file = os.path.exists(path + os.sep + basename)
                path = path.replace(prefix_path, '')
                path = path[1:] if path[0] == os.sep else path
                path = path + os.sep + basename if matched_file else path


                self.window.run_command("show_overlay", {
                    "overlay": "goto",
                    "text": path
                })
                return
        self.window.run_command("show_overlay", {"overlay": "goto", "text": original_text})
        self.window.status_message("Sorry, there was no common suffix match")
