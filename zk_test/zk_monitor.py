from kazoo.client import KazooClient
from kazoo.client import KazooState


zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()


@zk.add_listener
def my_listener(state):
    if state == KazooState.LOST:
        print('zookeeper connect lost')
    elif state == KazooState.SUSPENDED:
        print('zookeeper suspended')
    else:
        print('zookeeper connected')


def event_listener(event):
    print(event)


children = zk.get_children('/node1', watch=event_listener)
print('node1 has %s children with names %s' % (len(children), children))


@zk.ChildrenWatch('/node1')
def watch_children(children):
    print("Children are now: %s" % children)


@zk.DataWatch("/node1/subNode2")
def watch_node(data, state):
    if state:
        print("Version:", state.version, "data:", data)

