#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/6/9 14:13
# @Author : "zhy"


class CaptchaError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)
