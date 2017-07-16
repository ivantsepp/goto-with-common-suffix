Goto With Common Suffix plugin
================

This plugin extends the usage of Sublime's File navigation by allowing you to use common suffix paths.

For example, I have opened up a Sublime window at `/Users/ivan/projects` and I have a file located at `/Users/ivan/projects/example/readme.txt`. I can use any arrangement of prefixes and input paths like `/var/www/example/readme.txt` and the plugin will correctly determine the common suffix (`example/readme.txt`) and opens the [Goto Anything](http://docs.sublimetext.info/en/latest/file_management/file_navigation.html#goto-anything) with it.

The use case is that I sometimes get GitHub urls that point to a file. I would like to simply copy that address and use this plugin to determine the file I want. It removes the step of me manually figuring out the common suffix to put in the quick finder. Other times, stack traces from other machines include file location but those locations are specific to that machine's file system. This plugin can help you get to the file you want.

Installation
------------

Install via [Package Control](https://packagecontrol.io) or you can [manually install the package](http://sublimetext.info/docs/en/extensibility/packages.html).

Usage
--------

There is now a method named `goto_with_common_suffix` and command name `Goto With common suffix` that invokes it. You can use this plugin by opening the [Command Palette](http://docs.sublimetext.info/en/latest/extensibility/command_palette.html) and selecting this command.

You can also set your custom key binding to invoke the command. Here's my user sublime key map file:

```json
[
    { "keys": ["ctrl+p"], "command": "goto_with_common_suffix"}
]

```

Here is a gif showing how I have this project opened in sublime and that by invoking this plugin (with ctrl+p), I can paste `https://github.com/ivantsepp/goto-with-common-suffix/blob/master/goto_with_common_suffix.py` and it will correctly find the common suffix.

![screencast](https://user-images.githubusercontent.com/4662860/28236073-40d7ae98-68ea-11e7-8f13-d7706ccbdee0.gif)
