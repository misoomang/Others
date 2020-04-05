#! /usr/bin/python3
# -*- encoding: utf-8 -*-


import time
import threading
from kazoo.client import KazooClient
from kazoo.client import KazooState
from kazoo.retry import KazooRetry


def restart_zk_client():
    """
    重启zookeeper会话
    :return:
    """
    global zk_client
    global zk_conn_status

    try:
        zk_client.restart()
    except Exception as e:
        print('重启zookeeper客户端异常：%s' % e)

zk_conn_status = 0  # zookeeper连接状态 1-LOST   2-SUSPENDED 3-CONNECTED/RECONNECTED


def zk_conn_listener(state):
    global zk_conn_status
    if state == KazooState.LOST:
        print('zookeeper connection lost')
        zk_conn_status = 1
        thread = threading.Thread(target=restart_zk_client)
        thread.start()
    elif state == KazooState.SUSPENDED:
        print('zookeeper connection dicconnected')
        zk_conn_status = 2
    else:
        zk_conn_status = 3
        print('zookeeper connection cconnected/reconnected')


def event_listener(event):
    print(event)


if __name__ == '__main__':
    # try:
        zk_client = KazooClient(hosts='127.0.0.1:2181')
        zk_client.add_listener(zk_conn_listener)    # 添加watcher。监听链接状态
        zk_client.start()
        print('zk_client state：', zk_client.state)  # 查看链接状态

        zk_client.ensure_path('/node1')
        if not zk_client.exists('/node1/subNode1'):
            zk_client.create('/node1/subNode1', b'sub node1')

        if not zk_client.exists('/node1/subNode2'):
            zk_client.create('/node1/subNode2', b'sub node2', ephemeral=True)

        zk_client.create('/node1/subNode', b'sub nodexxx', ephemeral=True, sequence=True)

        if zk_client.exists('/node1'):
            print('存在节点node1,节点路径/node1')

        data, stat = zk_client.get('/node1')
        if stat:
            print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))

        children = zk_client.get_children('/node1')
        print('node1子节点 有 %s 子节点，节点名称为: %s' % (len(children), children))
        print('/ 子节点', zk_client.get_children('/'))

        zk_client.set('/node1/subNode2', b'some new data')
        zk_client.delete('/node1', recursive=True)

        try:
            result = zk_client.retry(zk_client.get, '/node1/subNode3')
            print(result)
            kr = KazooRetry(max_tries=3, ignore_expired=False)
            result = kr(zk_client.get, '/node1/subNode3')
        except Exception as e:
            print('/node1/subNode3 不存在，所以会运行出错')
            zk_client.stop()

        while zk_conn_status != 3:
            continue
        else:
            i = 0
            while i < 300:
                if i % 20 == 0:
                    time.sleep(2)
                    print('创建新节点')
                    zk_client.ensure_path('/node1')
                    zk_client.ensure_path('/node1/subNode2')
                    zk_client.create('/node1/subNode', b'sub nodexxxx', ephemeral=True, sequence=True)
                    zk_client.set('/node1/subNode2', b'new data')
                i += 1
        zk_client.stop()
        zk_client.close()
    # except Exception as e:
    #     print('运行出错：%s' % e)
