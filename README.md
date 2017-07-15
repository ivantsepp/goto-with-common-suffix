Goto With Common Suffix plugin
================

This plugin extends the usage of Sublime's File navigation by allowing you to use common-suffixed paths.

For example, I have opened up a Sublime window at `/Users/ivan/projects` and I have a file located at `/Users/ivan/projects/example/readme.txt`. I can use any arrangement of prefixes and input paths like `/var/www/example/readme.txt` into the input of this plugin and it will correctly determine the common suffix which is `example/readme.txt` and opens the [Goto Anything](http://docs.sublimetext.info/en/latest/file_management/file_navigation.html#goto-anything) with it.

The use case is that I sometimes get GitHub urls that point to a file. I would like to simply copy that address and use this plugin to determine the file I want. It removes the step of me manually figuring out the common suffix to put in the quick finder. Other times, stack traces from other machines shows file location but I can use this plugin to quickly get to the file I want.

Installation
------------
TBD

Usage
--------

There is now a method named `goto_with_common_suffix` and command name `Goto With common suffix` that invokes it. You can use this plugin by opening the [Command Palette](http://docs.sublimetext.info/en/latest/extensibility/command_palette.html) and selecting this command.

You can also set your custom key binding to invoke the command. Here's my user sublime key map file:

```json
[
    { "keys": ["ctrl+p"], "command": "goto_with_common_suffix"}
]

```
