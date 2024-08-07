# Lab 3 Skeleton
#
# Based on of_tutorial by James McCauley

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpid_to_str, str_to_dpid
from pox.lib.util import str_to_bool

log = core.getLogger()


class Firewall (object):
  """
  A Firewall object is created for each switch that connects.
  A Connection object for that switch is passed to the __init__ function.
  """
  def __init__ (self, connection):
    # Keep track of the connection to the switch so that we can
    # send it messages!
    self.connection = connection

    # This binds our PacketIn event listener
    connection.addListeners(self)


  def do_firewall (self, packet, packet_in):
    # The code in here will be executed for every packet.
    def drop(packet, packet_in):
      msg = of.ofp_flow_mod()

      # installing the role onto the switch
      msg.match = of.ofp_match.from_packet(packet)
      msg.idle_timeout = 90
      msg.hard_timeout = 90
      msg.data = packet_in
      self.connection.send(msg)

    def flood(packet, packet_in):
      msg = of.ofp_flow_mod()
      # install the role onto the switch
      msg.match = of.ofp_match.from_packet(packet)
      msg.idle_timeout = 90
      msg.hard_timeout = 90
      msg.data = packet_in
      msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
      self.connection.send(msg)

    # Find for TCP
    tcp = packet.find('tcp')

    # Find for ARP
    arp = packet.find('arp')

    # Find for IPV4
    ipv4 = packet.find('ipv4')

    if arp or (ipv4 and tcp):
      flood(packet, packet_in)
    else:
      drop(packet, packet_in)

    return


  def _handle_PacketIn (self, event):
    """
    Handles packet in messages from the switch.
    """

    packet = event.parsed # This is the parsed packet data.
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return

    packet_in = event.ofp # The actual ofp_packet_in message.
    self.do_firewall(packet, packet_in)



def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Firewall(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)