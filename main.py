import sublime
import sublime_plugin

class LogalyzeEventListener(sublime_plugin.EventListener):
  def on_query_context(self, view, key, operator, operand, match_all):
    print("key: %s" % key)
