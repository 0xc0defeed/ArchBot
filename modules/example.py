# -*- coding: utf-8 -*-
from irc import IRCBot


class Example(IRCBot):
    """Example"""
    def example(self, nick, message, channel):
        return 'Example'
    def command_patterns(self):
        return (
            self.ping('!example', self.example),
        )
