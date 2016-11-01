# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class TutorialPipeline(object):
#     def process_item(self, item, spider):
#         return item


import json
import codecs


class housePipeline(object):
    def __init__(self):
        self.file = codecs.open('house.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        result = 1
        strlist = []
        temp = dict(item)
        for (k, v) in temp.items():
            for t in temp[k]:
                if k == 'cost':
                    t = int(t)
                elif k != 'url':
                    t = t.replace('\n','').strip().replace(' ','').replace('-','')
                if t == "":
                    continue
                strlist.append(t)
            temp[k] = strlist
            strlist = []
            if temp[k] == []:
                result = 0
                break
        if result==1 :
            line = json.dumps(temp) + '\n'
            self.file.write(line.decode("unicode_escape"))
        return item
