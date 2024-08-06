#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @DarkzzAngel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", "29640188"))
    API_HASH = os.environ.get("API_HASH","e470abc84a3bc445997ee4ea5be87deb")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7406110931:AAGiW_lENMzLpPfRErJmmCmhU25472Kh2Pg") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "Downloaded")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "document")
    OWNER_ID = os.environ.get("OWNER_ID","6364152774")
    SESSION = os.environ.get("SESSION")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
