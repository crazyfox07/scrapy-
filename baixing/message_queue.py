# -*- coding:utf-8 -*-

"""
File Name : 'message_queue'.py
Description:
Author: 'chengwei'
Date: '2016/6/2' '15:48'
"""
import sys
import pika
import codecs
import ConfigParser
import os

reload(sys)
sys.setdefaultencoding('utf-8')

def message(queue_name, handle_data=None, confirm_delivery=0):
    """
    类的实例化，作为接口
    :param queue_name:对列名
    :param handle_data:接收消息时的消息内容处理函数, 默认为None,在发送消息时可不设置
    :param confirm_delivery 是否开启消息投递确认模式, 1为开启，默认为0
    :return:
    """
    message = message_queue(queue_name, handle_data, confirm_delivery)
    return message

class message_queue(object):
    def __init__(self, queue_name, handle_data=None, confirm_delivery=0):
        """
        初始化
        :param queue_name: 对列名
        :param handle_data: 接收消息时的消息内容处理函数
        :param confirm_delivery: 是否开启投递确认模式
        :return:
        """
        self.parasecname = "RabbitMQ"
        self.queue_name = queue_name
        self.confirm_delivery = confirm_delivery
        self.connection, self.channel = self.message_queue_init()
        self.handle_data = handle_data

    def message_queue_init(self):
        """
        消息队列初始化, 默认开启持久化， 使用实例化的参数
        """
        cur_script_dir = os.path.split(os.path.realpath(__file__))[0]
        cfg_path = os.path.join(cur_script_dir, "db.conf")

        cfg_reder = ConfigParser.ConfigParser()
        secname = self.parasecname
        cfg_reder.readfp(codecs.open(cfg_path, "r", "utf_8"))
        rabbitmq_host = cfg_reder.get(secname, "host")
        rabbit_username = cfg_reder.get(secname, "username")
        rabbitmq_pass = cfg_reder.get(secname, "passwd")

        credentials = pika.PlainCredentials(rabbit_username, rabbitmq_pass)
        connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitmq_host, 5672, '/', credentials,
                                                                       heartbeat_interval=0))
        channel = connection.channel()
        # durable 表示是否持久化，exclusive是否排他，如果为True则只允许创建这个队列的消费者使用， auto_delete 表示消费完是否删除队列
        channel.queue_declare(queue=self.queue_name, durable=True, exclusive=False, auto_delete=False)

        if self.confirm_delivery == 1:
            channel.confirm_delivery()
        return connection, channel

    def send_message(self, message):
        """
        发送消息到队列
        # delivery_mode=2 make message persistent
        :param message: 要投递的消息，字符串格式
        confirm_delivery: 如果开启消息投递确认模式，那么可以返回True或False,未开启则只是发送消息，默认不开启
        :return:
        """
        if self.confirm_delivery == 1:
            return self.channel.basic_publish(exchange='', routing_key=self.queue_name,
                                              body=message, properties=pika.BasicProperties(delivery_mode=2))
        else:
            self.channel.basic_publish(exchange='', routing_key=self.queue_name,
                                       body=message, properties=pika.BasicProperties(delivery_mode=2))

    def message_queue_close(self):
        self.channel.close()
        self.connection.close()
        print "stoped!"

    def callback(self, ch, method, properties, body):
        """
        回调函数，其中handle_data为处理接收到的消息，处理正确返回1，如果返回1，那么发送消息确认
        :param ch:和rabbitmq通信的信道
        :param method:一个方法帧对象
        :param properties:表示消息头对象
        :param body:消息内容
        :return:
        """
        print " [x] Received %r" % (body.encode('utf-8'),)
        result = self.handle_data(body)
        if result == 1:
            print " [x] Done"
            ch.basic_ack(delivery_tag=method.delivery_tag)
        else:
            print " [x] handle data error"
            ch.basic_reject(delivery_tag=method.delivery_tag)

    def receive_message(self):
        """
        接收消息队列中的消息, 并调用回调函数处理
        """
        # 同一时刻，不要发送超过一个消息到消费者，直到它已经处理完了上一条消息并作出了回应
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(self.callback, queue=self.queue_name)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        try:
            self.channel.start_consuming()
        except KeyboardInterrupt:
            self.message_queue_close()

if __name__ == '__main__':
    # example
    def get_info(body):
        """
        注意在处理接收到得消息时，请自行进行错误处理，如果返回0，那么消息将回到队列，如果此时只有一个消费者，那么将进入死循环
        """
        print body
        return 1
    # 生产者
    test_1 = message('test')
    test_1.send_message(u"测试")

    # 消费者
    test_2 = message('test', handle_data=get_info)
    test_2.receive_message()
