import os
try: import json
except ImportError: import simplejson as json
import agent_util
import datetime
from mcstatus import MinecraftServer

class MinecraftPlugin(agent_util.Plugin):

    textkey = "minecraft"
    label = "Minecraft"

    @classmethod
    def get_metadata(self, config):

        status = agent_util.SUPPORTED
        msg = None
        if not True:
            status = agent_util.MISCONFIGURED
            msg = "The Minecraft plugin is not configured properly"

        metadata = {
            "players": {
                "label": "Players online",
                "options": None,
                "status": status,
                "error_message": msg,
            },
            "latency": {
                "label": "Server latency",
                "options": None,
                "status": status,
                "error_message": msg,
                "unit": "ms"
            }
        }
        return metadata

    def check(self, textkey, data, config):
        server = MinecraftServer.lookup("localhost:25565")
        srv = server.status()
        players = srv.players.online
        latency = server.ping()

        if textkey == 'players': 
            return players

	elif textkey == 'latency':
            return latency

        return 0

