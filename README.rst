devpi-discord: Discord notification plugin for devpi-server
===========================================================

Installation
------------

``devpi-discord`` needs to be installed alongside ``devpi-server``.

You can install it with::

    pip install devpi-discord

For ``devpi-server`` there is no configuration needed, as it will automatically discover the plugin through calling hooks using the setuptools entry points mechanism.

Configuration
-------------

devpi-discord can trigger Discord notifications upon package upload.

    devpi index /testuser/dev discord_hook=https://discord.com/api/webhooks/...

Environment Variables:

You can also pass environment variables to configure the plugin. Yes it can be more simplier but it's less secure and flexible be aware of that

- ``DISCORD_HOOK`` to adjust the Discord hook URL used. Defaults to the devpi discord_hook value above. (Note: discord_hook provided by devpi takes precedence. Setting both will default to the value specified in devpi)

Disable it !
------------

By removing the index configuration the plugin will not send any notification anymore:

    devpi index /testuser/dev discord_hook-=