# -*- coding: utf-8 -*-
from irc import IRCConnection
import conf.config as c


class IRCConnectionHelper(IRCConnection):
    def load_class(self, bot_class):
       bot_instance = bot_class(self) 


class RunBot(object):
    def __init__(self, bot_class, host, port, nick, channels):
        self.conn = IRCConnectionHelper(host, port, nick)
        self.conn.connect()

        for channel in channels:
            self.conn.join(channel)

        for botclass in bot_class:
            self.conn.load_class(botclass)

    def run_bot(self):
        try:
            self.conn.enter_event_loop()
        except:
            pass


run = RunBot(c.BOT_IRC_MODULES,
             c.BOT_IRC_SERVER,
             c.BOT_IRC_PORT,
             c.BOT_IRC_NICK,
             c.BOT_IRC_CHANNELS)


run.run_bot()
