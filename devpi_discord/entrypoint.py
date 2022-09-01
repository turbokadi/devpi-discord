# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

import discord_api

def devpiserver_indexconfig_defaults():
    return {"discord_hook": None}

def devpiserver_on_upload_sync(log, application_url, stage, project, version):
    discord_hook = stage.ixconfig.get("discord_hook") or os.getenv("DISCORD_HOOK")
    if not discord_hook:
        return

    discord = discord_api.DiscordWebhook(discord_hook)
    if discord.notify(
        "A new release is available !",
        project=project,
        version=version,
        url=application_url
    ):
        log.info("Successfully sent Discord notification %s", project)
    else:
        log.error("Failed to send Discord notification")
        raise RuntimeError("%s: Failed to send Discord notification",project)
