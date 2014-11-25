import os
try: import json
except ImportError: import simplejson as json
import agent_util
import datetime

# TODO: Rename class to an appropriate name, must end in "Plugin"
class MinecraftMonitorPlugin(agent_util.Plugin):

    # TODO: Replace textkey and label with appropriate values
    textkey = "template_textkey"
    label = "Minecraft Monitor"

    @classmethod
    def get_metadata(self, config):

        status = agent_util.SUPPORTED
        msg = None

        # TODO: Check that the plugin can run successfully and has all of the necessary
        # prerequesites.  If not, set status to agent_util.MISCONFIGURED and set a message
        # to describe what is wrong.
        if not True:
            status = agent_util.MISCONFIGURED
            msg = "Hey! Something is wrong!"

        # TODO: add dictionaries for each metric that can be measured.  Each key in the 
        # metadata dictionary is a textkey for that metric (all lower case letters, numbers 
        # and underscores, no spaces or special characters)
        metadata = {
            "metric1": {
                "label": "If server is running",
                "options": None,
                "status": status,
                "error_message": msg,
                "unit": "unit description"
            },
            "metric2": {
                "label": "Number of users currently on server",
                "options": None,
                "status": status,
                "error_message": msg,
                "unit": "unit description"
            }
        }
        return metadata

    def check(self, textkey, data, config):
        # TODO: Add code to perform the actual checks for the metric described by textkey. 
        # If options are avaiable for the metric and one is selected it will be included
        # in the data parameter.  Return value should be an integer or floating point value.

        if textkey == 'metric1': 
            return 1
        elif textkey == 'metric2':
            return 2

        return 0


