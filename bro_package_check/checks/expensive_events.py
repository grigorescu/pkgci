#!/usr/bin/env python3
import os
import sys
from .types import CheckResult
from ..bro_parser import bro_files, bro_tokens

NAME = "expensive_events"

expensive_eventS = set([
    "new_packet",
    "tcp_packet",
    "tcp_option",
    "tcp_contents",
    "connection_SYN_packet",
    "gtpv1_g_pdu_packet",
    "udp_request",
    "udp_reply",
    "teredo_bubble",
    "teredo_origin_indication",
    "teredo_authentication",
    "teredo_packet",
    "new_event",
    "packet_contents",
    "ipv6_ext_headers",
    "raw_packet",
    "new_connection",
])

def check_expensive_events(pkg):
    loaded_files = bro_files(pkg)
    bad = []
    for f in loaded_files:
        for n, line, tokens in bro_tokens(f):
            for token_type, token in tokens:
                if token_type == 'TOKEN' and token in expensive_eventS:
                    msg = "{}:{} expensive event {}".format(f, n, token)
                    bad.append(msg)
    
    return CheckResult(NAME, ok=True, warnings=bad)
