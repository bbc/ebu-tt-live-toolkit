# Migrating autobahn and twisted

## What are autobahn and twisted used for?

[Autobahn](https://pypi.org/project/autobahn/) is a Python WebSocket implementation.
[Twisted](https://twisted.org/) ([Pypi](https://pypi.org/project/Twisted/)) is
a Python event-based framework for internet applications - essentially
allowing asynchonous application behaviour.

The EBU-TT Live Interoperability Toolkit needs to support this asynchronous behaviour
for its core functionality of supporting arbitrarily-timed receipt and issuing of documents
to or from "nodes".

Some nodes only receive and others only emit documents.
It's possible to configure chains of nodes that each do some specific job.
Those nodes may be connected "directly" in memory, or via some network connection, such as WebSocket.

Without this functionality, the EBU-TT Live Interoperability Toolkit can only be used
in a static mode, rather than dynamicslly for the purpose for which it was originally designed.

## Versions

When the BBC fork of the LIT moved from Python2.7 to Python3.7,
many of the tests that relied on twisted and/or autobahn would not run.
Since BBC did not at that time need the dynamic behaviour, for expediency
those tests were simply marked as "skip" and the dependency libraries were
updated to the minimum required to allow the project to be built.

The last version of Autobahn ([changelog](https://autobahn.readthedocs.io/en/latest/changelog.html))
to support Python 2 was 19.11.2. The current version (as of 2024-03-08) is 22.7.1, and the
one used in the project is `^20.0.0`.

The last version of Twisted to support Python 2.7 was 20.3.0. The current version is 24.3.0,
and the one used in the project is `^23.8.0`.

## Documentation

TDD in Twisted: https://docs.twisted.org/en/stable/core/howto/trial.html

WebSocket programming in Autobahn: https://autobahn.readthedocs.io/en/latest/websocket/programming.html

## Skipped tests

The skipped tests are in `ebu_tt_live/twisted/test/test_twisted_websocket.py`.
They are unit tests, and they are skipped by being marked as:

```python
    @pytest.mark.xfail(reason="Twisted deferred testing needs to be reworked.")
```

Pytest uses the `twisted-1.14.0` plugin.

Twisted has documentation about testing at https://docs.twisted.org/en/stable/core/howto/trial.html#core-howto-trial-twisted

If we just unmark those tests and run them, without doing anything else (like upgrading autobahn and twisted!) we get:

```
======================================================= short test summary info ========================================================
FAILED ebu_tt_live/twisted/test/test_twisted_websocket.py::TestProdServerToConsClientProtocols::test_server_prod_client_cons_success - RuntimeError: Cannot unregister a producer unless one is registered
FAILED ebu_tt_live/twisted/test/test_twisted_websocket.py::TestProdServerToConsClientProtocols::test_server_prod_client_cons_wrong_sequence_error - RuntimeError: Cannot unregister a producer unless one is registered
FAILED ebu_tt_live/twisted/test/test_twisted_websocket.py::TestProdServerToConsClientProtocols::test_consumer_send_data_error - RuntimeError: Cannot unregister a producer unless one is registered
FAILED ebu_tt_live/twisted/test/test_twisted_websocket.py::TestProdServerToConsClientProtocols::test_producer_to_producer_error - twisted.trial.unittest.FailTest: builtins.RuntimeError raised instead of AssertionError:
FAILED ebu_tt_live/twisted/test/test_twisted_websocket.py::TestProdServerToConsClientProtocols::test_url_encoded_components - twisted.trial.unittest.FailTest: 'sequence/ünicödé?/Name' != 'sequence%2Fünicödé%3F%2FName'
FAILED ebu_tt_live/twisted/test/test_twisted_websocket.py::TestConsServerToProdClientProtocols::test_serv_cons_client_prod_success - RuntimeError: Cannot unregister a producer unless one is registered
FAILED ebu_tt_live/twisted/test/test_twisted_websocket.py::TestConsServerToProdClientProtocols::test_serv_cons_client_prod_wrong_sequence_error - RuntimeError: Cannot unregister a producer unless one is registered
FAILED ebu_tt_live/twisted/test/test_twisted_websocket.py::TestConsServerToProdClientProtocols::test_consumer_to_consumer_error - twisted.trial.unittest.FailTest: builtins.RuntimeError raised instead of AssertionError:
FAILED ebu_tt_live/twisted/test/test_twisted_websocket.py::TestConsServerToProdClientProtocols::test_consumer_send_data_error - RuntimeError: Cannot unregister a producer unless one is registered
ERROR ebu_tt_live/twisted/test/test_twisted_websocket.py::TestProdServerToConsClientProtocols::test_server_prod_client_cons_success - Failed: NOTE: Incompatible Exception Representation, displaying natively:
ERROR ebu_tt_live/twisted/test/test_twisted_websocket.py::TestProdServerToConsClientProtocols::test_producer_to_producer_error - RuntimeError: Cannot unregister a producer unless one is registered
ERROR ebu_tt_live/twisted/test/test_twisted_websocket.py::TestConsServerToProdClientProtocols::test_serv_cons_client_prod_success - Failed: NOTE: Incompatible Exception Representation, displaying natively:
ERROR ebu_tt_live/twisted/test/test_twisted_websocket.py::TestConsServerToProdClientProtocols::test_consumer_to_consumer_error - RuntimeError: Cannot unregister a producer unless one is registered
=========================================== 9 failed, 5 passed, 1 warning, 4 errors in 4.81s ===========================================
                                                                                          
```

Updating to the latest versions of the dependencies twisted and autobahn doesn't fix any of the tests, but does generate 2 additional warnings!

```
========================================== 9 failed, 5 passed, 3 warnings, 2 errors in 5.37s ===========================================
```

### Structure of the test file

The file `ebu_tt_live/twisted/test/test_twisted_websocket.py` has a common class `_NewWSCommon` that is inherited by
a variety of test classes, as a mix-in alongside `twisted.trial.unittest.TestCase`.

This common class is where the errors seem to originate, which raises the hope that fixing it in one place might
allow all the tests to pass.

It has 4 methods: `_create_server()`, `create_client()`, `_connect()` and `_disconnect()`.

The last of these, `_disconnect()` is where the error arises. For example, the first test almost completes
successfully, but fails in this method, complaining of some kind of unexpected or dirty state.

## What has changed, and what are the errors?

### First error

The first error demonstrates that seemingly all the test steps passed until the call to `_disconnect()`.
In fact there are only two more lines of test left, which are there to asset that `unregister()` methods
on the consumer and the producer are called with the right objects.

```
ebu_tt_live/twisted/test/test_twisted_websocket.py F
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> traceback >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

self = <test_twisted_websocket.TestProdServerToConsClientProtocols testMethod=test_server_prod_client_cons_success>

    def test_server_prod_client_cons_success(self):
        self._create_server(url='ws://localhost:9005', producer=self.prod)
        self._create_client(
            url='ws://localhost:9005/{}/subscribe'.format(
                self.sequence_identifier
            ),
            consumer=self.cons
        )
    
        # This step is supposed to be done by the mocked out twisted consumer on connection registration
        self.cproto.consumer = self.cons
    
        self._connect()
    
        self.cons.register.assert_called_with(self.cproto)
        self.prod.register.assert_called_with(self.sproto)
        self.assertEqual(self.cproto.action, 'subscribe')
        self.assertEqual(self.sproto.action, 'subscribe')
    
        # At this point we are supposed to be able to send data through
        doc = b'dummy message'
        self.sproto.sendSequenceMessage(
            sequence_identifier=self.sequence_identifier,
            payload=doc
        )
    
        self.cons.write.assert_not_called()
    
        # Do the transport step
        self.cproto.dataReceived(self.str.value())
        self.str.clear()
        self.sproto.dataReceived(self.ctr.value())
        self.ctr.clear()
    
        # This should be a successful reception of the data frame
        self.cons.write.assert_called_with(doc, sequence_identifier=self.sequence_identifier)
    
        # Bring a clean disconnect
>       self._disconnect()

ebu_tt_live/twisted/test/test_twisted_websocket.py:118: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
ebu_tt_live/twisted/test/test_twisted_websocket.py:56: in _disconnect
    self.sproto.dataReceived(self.ctr.value())
../../../Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/autobahn/twisted/websocket.py:348: in dataReceived
    self._dataReceived(data)
../../../Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/autobahn/websocket/protocol.py:1243: in _dataReceived
    self.consumeData()
../../../Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/autobahn/websocket/protocol.py:1255: in consumeData
    while self.processData() and self.state != WebSocketProtocol.STATE_CLOSED:
../../../Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/autobahn/websocket/protocol.py:1619: in processData
    fr = self.onFrameEnd()
../../../Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/autobahn/websocket/protocol.py:1715: in onFrameEnd
    self.processControlFrame()
../../../Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/autobahn/websocket/protocol.py:1771: in processControlFrame
    if self.onCloseFrame(code, reasonRaw):
../../../Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/autobahn/websocket/protocol.py:788: in onCloseFrame
    self.dropConnection(abort=False)
../../../Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/autobahn/websocket/protocol.py:887: in dropConnection
    self.unregisterProducer()
../../../Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/autobahn/twisted/websocket.py:413: in unregisterProducer
    self.transport.unregisterProducer()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <twisted.internet.testing.StringTransportWithDisconnection object at 0x10e401e90>

    def unregisterProducer(self):
        if self.producer is None:
>           raise RuntimeError("Cannot unregister a producer unless one is registered")
E           RuntimeError: Cannot unregister a producer unless one is registered

../../../Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/twisted/internet/testing.py:277: RuntimeError
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> entering PDB >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PDB post_mortem (IO-capturing turned off) >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
> /Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/twisted/internet/testing.py(277)unregisterProducer()
-> raise RuntimeError("Cannot unregister a producer unless one is registered")
(Pdb) l
272  	        self.producer = producer
273  	        self.streaming = streaming
274  	
275  	    def unregisterProducer(self):
276  	        if self.producer is None:
277  ->	            raise RuntimeError("Cannot unregister a producer unless one is registered")
278  	        self.producer = None
279  	        self.streaming = None
280  	
281  	    # IPushProducer
282  	    def _checkState(self):
(Pdb) u
> /Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/autobahn/twisted/websocket.py(413)unregisterProducer()
-> self.transport.unregisterProducer()
(Pdb) l
408  	
409  	    def unregisterProducer(self):
410  	        """
411  	        Unregister Twisted producer with this protocol.
412  	        """
413  ->	        self.transport.unregisterProducer()
414  	
415  	
416  	@public
417  	class WebSocketServerProtocol(WebSocketAdapterProtocol, protocol.WebSocketServerProtocol):
418  	    """
(Pdb) u
> /Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/autobahn/websocket/protocol.py(887)dropConnection()
-> self.unregisterProducer()
(Pdb) l
882  	
883  	    def dropConnection(self, abort=False):
884  	        """
885  	        Drop the underlying TCP connection.
886  	        """
887  ->	        self.unregisterProducer()
888  	        if self.state != WebSocketProtocol.STATE_CLOSED:
889  	
890  	            if self.wasClean:
891  	                self.log.debug('dropping connection to peer {peer} with abort={abort}', peer=self.peer, abort=abort)
892  	            else:
(Pdb) u
> /Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/autobahn/websocket/protocol.py(788)onCloseFrame()
-> self.dropConnection(abort=False)
(Pdb) l
783  	                else:
784  	                    self.sendCloseFrame(code=WebSocketProtocol.CLOSE_STATUS_CODE_NORMAL, isReply=True)
785  	
786  	            if self.factory.isServer:
787  	                # When we are a server, we immediately drop the TCP.
788  ->	                self.dropConnection(abort=False)
789  	            else:
790  	                # When we are a client, we expect the server to drop the TCP,
791  	                # and when the server fails to do so, a timeout in sendCloseFrame()
792  	                # will set wasClean = False back again.
793  	                pass
(Pdb) self.factory
<ebu_tt_live.twisted.websocket.BroadcastServerFactory object at 0x111adca10>
(Pdb) self.factory.isServer
True
(Pdb) u
> /Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/autobahn/websocket/protocol.py(1771)processControlFrame()
-> if self.onCloseFrame(code, reasonRaw):
(Pdb) l
1766 	            if ll > 1:
1767 	                code = struct.unpack("!H", payload[0:2])[0]
1768 	                if ll > 2:
1769 	                    reasonRaw = payload[2:]
1770 	
1771 ->	            if self.onCloseFrame(code, reasonRaw):
1772 	                return False
1773 	
1774 	        # PING frame
1775 	        #
1776 	        elif self.current_frame.opcode == 9:
(Pdb) u
> /Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/autobahn/websocket/protocol.py(1715)onFrameEnd()
-> self.processControlFrame()
(Pdb) l
1710 	        End of frame received.
1711 	        """
1712 	        if self.current_frame.opcode > 7:
1713 	            if self.logFrames:
1714 	                self.logRxFrame(self.current_frame, self.control_frame_data)
1715 ->	            self.processControlFrame()
1716 	        else:
1717 	            if self.state == WebSocketProtocol.STATE_OPEN:
1718 	                self.trafficStats.incomingWebSocketFrames += 1
1719 	            if self.logFrames:
1720 	                self.logRxFrame(self.current_frame, self.frame_data)
(Pdb) self
<ebu_tt_live.twisted.websocket.BroadcastServerProtocol object at 0x111b35cd0>
(Pdb) self.state
2
(Pdb) WebSocketProtocol.STATE_CLOSED
0
(Pdb) WebSocketProtocol.STATE_OPEN
3
(Pdb) WebSocketProtocol.STATE_CLOSING
2
(Pdb) u
> /Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/autobahn/websocket/protocol.py(1619)processData()
-> fr = self.onFrameEnd()
(Pdb) l
1614 	                return False
1615 	
1616 	            # fire frame end handler when frame payload is complete
1617 	            #
1618 	            if self.current_frame_masker.pointer() == self.current_frame.length:
1619 ->	                fr = self.onFrameEnd()
1620 	                # noinspection PySimplifyBooleanCheck
1621 	                if fr is False:
1622 	                    return False
1623 	
1624 	            # reprocess when no error occurred and buffered data left
(Pdb) u
> /Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/autobahn/websocket/protocol.py(1255)consumeData()
-> while self.processData() and self.state != WebSocketProtocol.STATE_CLOSED:
(Pdb) l
1250 	        #
1251 	        if self.state == WebSocketProtocol.STATE_OPEN or self.state == WebSocketProtocol.STATE_CLOSING:
1252 	
1253 	            # process until no more buffered data left or WS was closed
1254 	            #
1255 ->	            while self.processData() and self.state != WebSocketProtocol.STATE_CLOSED:
1256 	                pass
1257 	
1258 	        # need to establish proxy connection
1259 	        #
1260 	        elif self.state == WebSocketProtocol.STATE_PROXY_CONNECTING:
(Pdb) u
> /Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/autobahn/websocket/protocol.py(1243)_dataReceived()
-> self.consumeData()
(Pdb) l
1238 	            self.trafficStats.preopenIncomingOctetsWireLevel += len(data)
1239 	
1240 	        if self.logOctets:
1241 	            self.logRxOctets(data)
1242 	        self.data += data
1243 ->	        self.consumeData()
1244 	
1245 	    def consumeData(self):
1246 	        """
1247 	        Consume buffered (incoming) data.
1248 	        """
(Pdb) u
> /Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/autobahn/twisted/websocket.py(348)dataReceived()
-> self._dataReceived(data)
(Pdb) l
343  	                       func=hltype(self.dataReceived),
344  	                       peer=hlval(self.peer),
345  	                       data_len=hlval(len(data)))
346  	
347  	        # bytes received from Twisted, forward to the networking framework independent code for websocket
348  ->	        self._dataReceived(data)
349  	
350  	    def _closeConnection(self, abort=False):
351  	        if abort and hasattr(self.transport, 'abortConnection'):
352  	            self.transport.abortConnection()
353  	        else:
(Pdb) u
> /Users/megitn02/Code/bbc/ebu-tt-live-toolkit/ebu_tt_live/twisted/test/test_twisted_websocket.py(56)_disconnect()
-> self.sproto.dataReceived(self.ctr.value())
(Pdb) l
 51  	        self.cproto.failHandshake.assert_not_called()
 52  	
 53  	    def _disconnect(self):
 54  	        # Do closing handshake
 55  	        self.cproto.sendClose()
 56  ->	        self.sproto.dataReceived(self.ctr.value())
 57  	        self.ctr.clear()
 58  	        self.cproto.dataReceived(self.str.value())
 59  	        self.str.clear()
 60  	
 61  	        # Verify transmission success
(Pdb) exit()
/Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/_pytest/main.py:306: PluggyTeardownRaisedWarning: A plugin raised an exception during an old-style hookwrapper teardown.
Plugin: terminalreporter, Hook: pytest_sessionfinish
AttributeError: 'NoneType' object has no attribute 'stopListening'
For more information see https://pluggy.readthedocs.io/en/stable/api_reference.html#pluggy.PluggyTeardownRaisedWarning
  config.hook.pytest_sessionfinish(
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! _pytest.outcomes.Exit: Quitting debugger !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Traceback (most recent call last):
  File "/Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/bin/pytest", line 8, in <module>
    sys.exit(console_main())
             ^^^^^^^^^^^^^^
  File "/Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/_pytest/config/__init__.py", line 192, in console_main
    code = main()
           ^^^^^^
  File "/Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/_pytest/config/__init__.py", line 169, in main
    ret: Union[ExitCode, int] = config.hook.pytest_cmdline_main(
                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/pluggy/_hooks.py", line 501, in __call__
    return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/pluggy/_manager.py", line 119, in _hookexec
    return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/pluggy/_callers.py", line 138, in _multicall
    raise exception.with_traceback(exception.__traceback__)
  File "/Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/pluggy/_callers.py", line 102, in _multicall
    res = hook_impl.function(*args)
          ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/_pytest/main.py", line 318, in pytest_cmdline_main
    return wrap_session(config, _main)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/_pytest/main.py", line 306, in wrap_session
    config.hook.pytest_sessionfinish(
  File "/Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/pluggy/_hooks.py", line 501, in __call__
    return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/pluggy/_manager.py", line 119, in _hookexec
    return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/pluggy/_callers.py", line 155, in _multicall
    teardown[0].send(outcome)
  File "/Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/_pytest/terminal.py", line 857, in pytest_sessionfinish
    outcome.get_result()
  File "/Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/pluggy/_result.py", line 99, in get_result
    raise exc.with_traceback(exc.__traceback__)
  File "/Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/pluggy/_callers.py", line 102, in _multicall
    res = hook_impl.function(*args)
          ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/_pytest/runner.py", line 108, in pytest_sessionfinish
    session._setupstate.teardown_exact(None)
  File "/Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/_pytest/runner.py", line 537, in teardown_exact
    raise exceptions[0]
  File "/Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/_pytest/runner.py", line 526, in teardown_exact
    fin()
  File "/Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/_pytest/unittest.py", line 208, in teardown
    self._explicit_tearDown()
  File "/Users/megitn02/Code/bbc/ebu-tt-live-toolkit/ebu_tt_live/twisted/test/test_twisted_websocket.py", line 226, in tearDown
    self.ctr.loseConnection()
  File "/Users/megitn02/Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/twisted/internet/testing.py", line 311, in loseConnection
    self.protocol.connectionLost(failure.Failure(error.ConnectionDone("Bye.")))
  File "/Users/megitn02/Code/bbc/ebu-tt-live-toolkit/ebu_tt_live/twisted/websocket.py", line 390, in connectionLost
    WebSocketClientProtocol.transport.stopListening()
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'stopListening'
```

What does this mean? The trouble seems to be happening in _NewWSCommon._disconnect()

The handshake seems to be:
1. Client sends close
2. Server needs to process some data, so we call dataReceived
3. Sure enough, that gets processed as a closure, and down the stack we see an attempt, as part of that closure, to unregister a producer.
4. But there seems to be no producer registered, so BOOM!
5. If we comment out that line in `_disconnect()`: `self.sproto.dataReceived(self.ctr.value())` then we get an assertion failure at line 63:

```
ebu_tt_live/twisted/test/test_twisted_websocket.py:63: in _disconnect
    self.assertEqual(self.sproto.state, self.sproto.STATE_CLOSED)
../../../Library/Caches/pypoetry/virtualenvs/ebu-tt-live-grkDGlyC-py3.11/lib/python3.11/site-packages/twisted/trial/_synctest.py:444: in assertEqual
    super().assertEqual(first, second, msg)
E   twisted.trial.unittest.FailTest: 3 != 0
```

Which is right, because the server hasn't processed the close message, so it's not showing as STATE_CLOSED.

Next step:
* see if the mechanism for closing connections has changed somehow...
* work out if the problem is with the code in `_disconnect()`, or the setup code before it, or something else entirely.
