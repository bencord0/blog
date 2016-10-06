from twisted.internet import reactor
from twisted.internet.defer import Deferred
from twisted.internet.protocol import Protocol
from twisted.web.client import Agent

agent = Agent(reactor)


class CounterProtocol(Protocol):
    def __init__(self, request, finish=None):
        self.request = request
        self.finish = finish or Deferred()

    def dataReceived(self, bytes):
        self.request.write(b"counter: " + bytes)
        self.request.finish()
        self.finish.callback(None)


class IndexView:
    async def GET(self, request):
        request.write("Hello World!\n".encode())
        async def finish():
            request.finish()

        await finish()


class DeferView:
    def GET(self, request):
        d = agent.request(
            b'GET', b'http://localhost:8000/counter')

        def get_counter(response):
            counter = CounterProtocol(request)
            response.deliverBody(counter)
            return counter.finish

        d.addCallback(get_counter)
        return d


class AsyncView:
    async def GET(self, request):
        response = await agent.request(
            b'GET', b'http://localhost:8000/counter')

        counter = CounterProtocol(request)
        response.deliverBody(counter)
        await counter.finish


class CounterView:
    def __init__(self):
        self._value = 0

    @property
    def _counter(self):
        self._value += 1
        return self._value

    def GET(self, request):
        return '{}'.format(self._counter).encode()
