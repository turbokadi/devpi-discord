# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests

class DiscordWebhook(object):
    def __init__(self, hook) -> None:
        self.hook = hook

    def startup_notify(self):
        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'user-agent': 'TurboBot v0.1 (Linux x86_64)'
        }

        payload.update({'embeds': [{
            'color': 0x26df34,
            'title':  "Repo Up and Ready !"
        }]})
        try:
            requests.post(self.hook,json=payload,headers=headers)
            return True
        except requests.HTTPError:
            return False

    def notify(self, message, **kwargs):
        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'user-agent': 'DevPiBot v0.1 (Linux x86_64)'
        }

        fields = []
        embed = None
        if kwargs.__len__() > 0:
            embed = {'color': 0xf5e942}
            embed["thumbnail"] = {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/115px-Python-logo-notext.svg.png"}
            embed["title"] = message

            for k,v in kwargs.items():
                if k == 'project':
                    fields.append({"name": "Project", "value": v, "inline": True})
                if k == 'version':
                    fields.append({"name": "Version", "value": v, "inline": True})
                elif k == 'url':
                    fields.append({"name": "Path", "value": v})
                else:
                    embed.update({k: v})

            if fields.__len__() > 0:
                embed.update({'fields': fields})
                payload.update({'embeds': [embed]})
                try:
                    requests.post(self.hook,json=payload,headers=headers)
                    return True
                except requests.HTTPError:
                    return False
