# /usr/bin/env python3
# -*- coding: utf-8 -*-

import re

class tool:

    	def change(self, result):
		# 将换行符或双换行符替换为\n
        	result = re.sub('<br.*?>', '\n', result)
		# 将img标签替换为\n
        	result = re.sub('<img.*?>', '\n', result)
		# 将a标签替换为空
        	result = re.sub('<a.*?>.*?</a>', '', result)
		return result
