
# -*- coding: utf-8 -*-
"""TwitchToolsDetection

This is a python library that allows users to find the tools a particular
Twitch.tv channel is using in their streams. The purpose of this work is
to understand how channels use different types of tools in their streams
to improve the quality.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * Add Examples
    * Add Attibutes if necessary

.. _Twitch Tools Detection:
   https://github.com/juanpflores/twitch-tool-detection

"""


from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
import logging
import sys


class TwitchToolsDetection():

    def __init__(self, channel):
        self.channel = channel
        self.channel_soup = ""




    def initialize(self):
        """
        Gets the HTML landing page of the streamer and saves it in a soup variable.
        
        Args:
            channel (str): The username or channel that we want to target. 
        
        Returns:
        """
        self.setLogger(True)

        # First we get the channel url in Twitch
        twitch_url = "https://www.twitch.tv/" + str(self.channel)

        # Query Twitch for the Channel.
        try:
            channel_page = urlopen(twitch_url)
            self.channel_soup = BeautifulSoup(channel_page, 'html.parser')
            logging.info("Connection to Twitch was succesfull.")

        except HTTPError:
            logging.error("Channel was not found in Twitch!")
            sys.exit()


    def findDiscord(channel_soup, channel_name):
        """
        Search in the Twitch Channel page for a Discord link. In case the channel doesn't
        has any link it will look for a Discord server using the name of the channel in
        the usual Discord url.
        
        Args:
            channel_name (str): The name of the channel we will look for.
            channel_soup (soup): The raw HTML of the channel landing page. 
            
        Returns:
            discord_url (str): The url to the channel's discord server.
        """

        all_links = channel_soup.find_all("a")
        for link in all_links:
            if link.get("href").contains("discord"):
                return link.get("href")

        # If there's no url to a Discord server this searchs
        # it directly by url on discord.
        try:
            discord_url = "discord.gg/" + str(channel_name)
            urlopen(discord_url)
            return discord_url
        except HTTPError:
            return None


    def setLogger(self, flag):
        """
        Sets up a logging system for the object which would allow us to inform the
        user if something went wrong or allow other developers to see if everything 
        is working as it should.
        
        Args:
            flag (bool): Flags that sets up the logging system or not.
        
        Returns:
        
        """
        if flag:
            logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
            logging.basicConfig(filename='report.log', filemode='w', level=logging.DEBUG)









