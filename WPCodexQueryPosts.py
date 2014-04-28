#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Myles McNamara, Matthias Krok, Eric Martel
# @Date:   2014-02-13 01:16:04
# @Last Modified by:   Myles McNamara
# @Last Modified time: 2014-02-13 01:26:15
# @Author URL: http://smyl.es
# @Plugin URL: https://github.com/tripflex/SublimeWordpressCodexQueryPosts
# @License: GPL 3+

# available commands
#   wordpress_codex_open_selection
#   wordpress_codex_search_selection
#   wordpress_codex_search_from_input

import sublime
import sublime_plugin
import subprocess
import webbrowser

def OpenInBrowser(url):
    webbrowser.open_new_tab(url)

def SearchWpCodexFor(text):
    url = 'http://developer.wordpress.org/?s=' + text.replace(' ','%20')
    OpenInBrowser(url)

def SearchQPFor(text):
    url = 'http://queryposts.com/?s=' + text.replace(' ','%20')
    OpenInBrowser(url)

def OpenWpFunctionReference(text):
    url = 'http://codex.wordpress.org/Function_Reference/' + text.replace(' ','%20')
    OpenInBrowser(url)

def OpenQPFunctionReference(text):
    url = 'http://queryposts.com/function/' + text.replace(' ','%20')
    OpenInBrowser(url)

class WordpressCodexOpenSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                selection = self.view.word(selection)

            text = self.view.substr(selection)
            OpenWpFunctionReference(text)

class WordpressCodexSearchSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                selection = self.view.word(selection)

            text = self.view.substr(selection)
            SearchWpCodexFor(text)

class WordpressCodexSearchFromInputCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Get the search item
        self.window.show_input_panel('Search WordPress Codex for', '',
            self.on_done, self.on_change, self.on_cancel)
    def on_done(self, input):
        SearchWpCodexFor(input)

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass
# query_posts_search_selection
class QueryPostsOpenSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                selection = self.view.word(selection)

            text = self.view.substr(selection)
            OpenQPFunctionReference(text)

class QueryPostsSearchSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                selection = self.view.word(selection)

            text = self.view.substr(selection)
            SearchQPFor(text)

class QueryPostsSearchFromInputCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Get the search item
        self.window.show_input_panel('Search QueryPosts.com for', '',
            self.on_done, self.on_change, self.on_cancel)
    def on_done(self, input):
        SearchQPFor(input)

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass
