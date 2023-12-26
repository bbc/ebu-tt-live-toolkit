Scripts and their functions
===========================

The ebu-run script
------------------
This script is capable of picking up a structured configuration file and use
that to create the nodes and carriage mechanism objects that we would like to
use. They can be even wired in the same configuration file together so in the
end a complex system can be modeled using a single json file. Please refer to
:py:mod:`ebu_tt_live.scripts.ebu_run` as well as :py:mod:`ebu_tt_live.config` to
learn more about the way the configuration logic works. To get help on permitted
options for the specified node(s) run ``ebu-run`` with a ``--help``. See
:doc:`configurator`.

Simple Producer
---------------
This script loads static text from a file
(``ebu-tt-live-toolkit/ebu_tt_live/examples/simple_producer.txt``) and breaks it
into a sequence of EBU-TT Live documents using natural language processing. Use
``ebu-run`` to start it: ``ebu-run
--admin.conf=ebu_tt_live/examples/config/simple_producer.json``

The default carriage mechanism is WebSocket, so you will need to listen to
``ws://127.0.0.1:9000``. Conveniently, we've created an HTML page that does just
that. After you launch the Simple Producer, open `docs/build/ui/test/index.html <../ui/test/index.html>`_
or the `current release pre-built test page <http://ebu.github.io/ebu-tt-live-toolkit/ui/test/>`_ in your
browser. The 'Broadcast message' field should be populated with the correct
address (``ws://localhost:9000``). Click 'Connect' and then 'Subscribe'. You can
also change the identifier for the sequence. The documents should appear in the
window below.

Alternatively, the Simple Producer can use the file system as the carriage
mechanism. To do this, create a configuration file and specify the carriage
mechanism and output folder options as described in :doc:`configurator` . This
saves the documents in the specified output folder together with a manifest file
that can be used by the Simple Consumer (below). See
:doc:`filesystem_carriage_mechanism` for more details about the file system
carriage mechanism.

Simple consumer
---------------
This script reads and validates documents in a sequence. It performs both
semantic and syntactic validation of the XML. By default, it uses WebSocket and
listens to ``ws://localhost:9000``. To start this default configuration, run
``ebu-run --admin.conf=ebu_tt_live/examples/config/simple_consumer.json``.
You can also point the Simple Consumer to the file system. If you saved the documents
in a folder (using the folder export configuration option
of the Simple Producer), you can write a configuration file as
described in :doc:`configurator` and pass this file to ``ebu-run``.

User Input Producer
-------------------
This is a web page that adds a user interface and various configurations to the
Simple Producer. It needs to connect to a node that can receive incoming
``/publish`` style WebSocket connections, for example a Simple Consumer, a
Distributor or a Handover Manager Node. First, with your virtual environment
activated and the code built, start one, with a command line such as  ``ebu-run
--admin.conf ebu_tt_live/examples/config/user_input_producer_consumer.json`` -
this one runs a simple consumer. Then, in your browser, open
`docs/build/ui/user_input_producer/index.html <../ui/user_input_producer/index.html>`_ or the
`current release pre-built UIP page <http://ebu.github.io/ebu-tt-live-toolkit/ui/user_input_producer/>`_ and click
'Connect'. Select the sending mode (manual, scheduled or asynchronous). You
should see the documents arriving in the command line window where the simple
consumer is listening. See detailed instructions here:
:doc:`user_input_producer`.

Distributor
-----------
This script mimics a distribution node. To see it forwarding documents from the
Simple Producer to the Simple Consumer using Websocket, run ``ebu-run
--admin.conf=ebu_tt_live/examples/config/sproducer_dist_sconsumer_ws.json``. A
more interesting scenario is distributing documents from the User Input Producer
to two consumer nodes: ``ebu-run
--admin.conf=ebu_tt_live/examples/config/user_input_producer_dist_consumers.json``.

Like the Simple Producer, the Distributor can also save the documents it
receives to the file system. To do that, create you own configuration file as
described in :doc:`configurator` and pass this file to ``ebu-run``.

Handover Manager
----------------
This node implements the 'Who claimed control most recently' algorithm defined
in the specification, with added functionality to allow messages to be broadcast
between members of the authors group, which may be added to a future
specification. This algorithm determines the output from multiple input
sequences. The Handover Manager is a specialised case of the switching node that
bases its decisions on handover-related attributes in the document and its
previous decisions. There is no separate command to run this script. Start it
with the ``ebu-run``, for example ``ebu-run
--admin.conf=ebu_tt_live/examples/config/user_input_producer_handover.json`` for
the default configuration. For detailed instruction on setting up the Handover
Manager with the UIP see :doc:`user_input_producer`.

Buffer Delay Node
-----------------
This script buffers each received Document and emits it after a fixed
non-negative delay offset period. Since this is a passive node, essentially
equivalent to a longer carriage latency, no modification to the documents is
required. The Buffer Delay Node is primarily intended for delaying implicitly
timed documents for resynchronisation. Use ``ebu-run`` to start this script, for
example ``ebu-run --admin.conf=ebu_tt_live/examples/config/buffer_delay.json``

DeDuplicator Node
-----------------
This node addresses instances where ``style`` and ``region`` elements and
attributes are duplicated, which can occur for example when sequences are
resequenced.
For the default configuration of the node, see:
``ebu-run --admin.conf=ebu_tt_live/examples/config/deduplicator_fs.json``

Denester Node
-------------
This node flattens nested ``div`` and ``span`` elements such that no
``div`` ends up containing a ``div`` and no ``span`` ends up containing
a ``span``. It also removes any ``p`` elements that specify a ``region``
attribute that differs from a specified region on an ancestor element.

If nested ``div`` or ``span`` elements might be present in a document, the
Denester node should be used to flatten them before passing them to the
EBU-TT-D Encoder, because EBU-TT-D does not permit such nested elements.

Resequencer Node
----------------
This node consumes documents from one sequence and
creates a new sequence of documents based on the content in that input sequence,
where every document in the output sequence has the same duration. The
resequencer repeatedly extracts and then outputs a document of the specified
duration, then waits for a period equal to that 
duration before extracting the next document. It can be configured to begin
extracting the first document immediately when it is run, or to wait until a
specific time until extracting the first document. 

The resequencer is
particularly useful upstream of an EBU-TT-D Encoder, to generate segmented
EBU-TT-D, for example prior to wrapping in fragmented MPEG-4 and serving
with a DASH or HLS manifest; those onward steps are not part of this project.
This pattern effectively converts an asynchronous stream of input documents
into something that can be delivered synchronously downstream, which is
useful for distribution to media players.

Note that the resequencer output can contain duplicated ``style`` and ``region``
elements. These can be cleaned up by passing the output to a DeDuplicator
node before downstream encoding to other formats.

In general the resequencer does not begin emitting any documents until it has received
at least one input document. To immediately start to emit documents an
initial document can be configured. Necessary initial parameters like
language or sequence ID are retrieved from that document.

Note that the resequencer accepts only input documents which all have the
same sequence ID. This sequence ID is determined by the first received input
document (or the configured initial document instead, if applicable).

Use ``ebu-run`` to start
this script, for example ``ebu-run --admin.conf=ebu_tt_live/examples/config/sproducer_resequencer_direct_ebuttd_encoder_fs.json``

Retiming Delay Node
-------------------
This script modifies the times within each Document and issues them without
further emission delay as part of a new sequence with a new sequence identifier.
The times are modified such that all of the computed begin and end times within
the document are increased by a non-negative fixed delay offset period. The
Retiming Delay Node is primarily intended for delaying explicitly timed
documents. Use ``ebu-run`` to start this script, for example ``ebu-run
--admin.conf=ebu_tt_live/examples/config/retiming_delay.json.``

EBU-TT-1 Producer
-----------------
This script produces an EBU-TT Part 3 document from an EBU-TT Part 1 source.
If SMPTE timecode is used (``ttp:timeBase="smpte"``) then the script looks for
an ``ebuttm:documentStartOfProgramme`` element in the input document, and if
present, maps that to the zero media time, and discards any elements that
begin or end before that time. If that element is absent, then times are
converted assuming that media time zero is SMPTE timecode ``00:00:00:00``.
Alternatively both of those values can be overridden by specifying a
start of programme timecode to use with the ``smpte_start_of_programme``
configuration parameter.
The timecode conversion currently assumes that
the timecode is continuous.

The default output sequence identifier can be specified. There is also a
parameter to allow the value of the input ``ebuttm:documentIdentifier`` element
to be used as the output sequence identifier, if present, overriding the
specified default.

EBU-TT-D Encoder
----------------
This script is an extension of simple consumer and is responsible for
converting the incoming EBU-TT Live documents into EBU-TT-D
documents that can later be embedded in video streams for example by
wrapping MPEG 4 (ISO BMFF) and serving with a manifest such as DASH or HLS,
or for serving as a sidecar distribution subtitle file.

There are configuration file options for controlling the media time conversion
reference point and the output file name format; these are described in
:doc:`configurator`.

To see the Encoder in action, using output from the Simple Producer and the
'direct' carriage mechanism, run ``ebu-run
--admin.conf=ebu_tt_live/examples/config/sproducer_ebuttd_direct.json``.

IMPORTANT: the Encoder depends on some features of its input document.
In particular, EBU-TT-D does not permit nested ``div`` or ``span`` elements,
and the Encoder cannot deal with input documents that have these. One way
to avoid this is to pass the input file through the Denester before encoding.

If segments of EBU-TT-D are needed, use the Resequencer upstream of the
Encoder to generate documents
corresponding to the desired periods on the timeline, prior to encoding.

Element Remover
---------------
This script iterates through the EBU-TT Part 3 and EBU-TT Metadata elements
in the document and removes any whose element name matches one of the names
in the ``remove_list``, supplied as a configuration parameter. The elements
are removed regardless of their location in the hierarchy.

The list is a comma separated list of names, with optional white space.

For example, to remove all elements called ``documentReadingSpeed`` or
``binaryData`` set the ``remove_list`` to ``documentReadingSpeed, binaryData``.

Validator
---------
This script loads a file from the file system and attempts to validate it
as the specified format, either EBU-TT Part 1, EBU-TT Part 3 or EBU-TT-D.
By default the expected format is EBU-TT-D.

Additionally, EBU-TT-D documents can be validated against the
`IMSC-HRM <https://www.w3.org/TR/imsc-hrm/>`_ by adding the ``--hrm`` flag.

Example command lines:

``validator -i path/to/ebu-tt-1-file-to-test.xml -f 1``

``validator -i path/to/ebu-tt-3-file-to-test.xml -f 3``

``validator -i path/to/ebu-tt-d-file-to-test.xml -f D``

``validator -i path/to/ebu-tt-d-file-to-test.xml -f D --hrm``
