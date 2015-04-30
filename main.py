import sublime
import sublime_plugin

class LogalyzeEventListener(sublime_plugin.EventListener):
  def on_query_context(self, view, key, operator, operand, match_all):

    if not key.startswith('logalizer-key.'):
      return None

      print("apretaron algo")

      return False

class RunLogalyzerAction(sublime_plugin.TextCommand):
  def run(self, edit, action=None, **kw):
    print("apretaron argooooooooo")
