# /usr/bin/env python3
# -*- coding: utf-8 -*-

import re

class tool:

    def change(self, result):
		# �����з���˫���з��滻Ϊ\n
        result = re.sub('<br.*?>', '\n', result)
		# ��img��ǩ�滻Ϊ\n
        result = re.sub('<img.*?>', '\n', result)
		# ��a��ǩ�滻Ϊ��
        result = re.sub('<a.*?>.*?</a>', '', result)
        return result