'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Collection of topics.
  This class contains a 'plain' topic set - with additional information
  about the commit.
   
 (c) 2010-2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.logging.EventLogging import tracer

class TopicSetWCI:
    '''Class for storing topic set and it's commit info.
       This is implemented in the way it is (using fields
       instead of inheritance) because in this way the topic_set
       object can be reused (and stored in the object cache).'''
    
    def __init__(self, topic_set, commit_info):
        '''Creates an object with the given values.'''
        self.__topic_set = topic_set
        self.__commit_info = commit_info
        
    def get_topic_set(self):
        '''Returns the underlaying topic set.'''
        return self.__topic_set
    
    def get_commit_info(self):
        '''Returns the commit info.'''
        return self.__commit_info
        
    def execute(self, executor):
        '''Execute the parts which are needed for TopicsSet.'''
        tracer.info("Calling pre.")
        executor.topics_set_pre(self)
        tracer.info("Calling sub topic.")
        self.__topic_set.execute(executor)
        tracer.info("Calling post.")
        executor.topics_set_post(self)
        tracer.info("Finished.")