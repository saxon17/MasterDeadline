# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import pyshark
import re

def YoutubeVedioDnsExtractor(pcapFilePath):
    d = {}
    cap = pyshark.FileCapture(pcapFilePath,display_filter = 'dns.qry.name.len ==32 && ip.src == 8.8.8.8')

    for pkt in cap:

        # print pkt.dns.get_field_by_showname('CNAME')
        # print pkt.dns.get_field_value('a')
        if not d.has_key( pkt.dns.get_field_value('a')):
            d[pkt.dns.get_field_value('a')] = pkt.dns.get_field_by_showname('CNAME')
    return d
        # if not d.has_key(pkt.dns.get_field_value('a')):
        # 		d[pkt.dns.get_field_value('a')] = pkt.ssl.get_field_by_showname(pkt.dns.get_field_by_showname('CNAME'))
def YoutubeVedioSSLExtractor(pcapFilePath):
    d = {}
    cap = pyshark.FileCapture(pcapFilePath,display_filter = 'ssl.handshake.extensions_server_name_len == 32')

    for pkt in cap:
        # print 'Hello'
        # print
        # print pkt.ip
        SSLServerName = pkt.ssl.get_field_by_showname('Server Name')
        m = re.match(r'(r.*)(.google)', SSLServerName)
        if m:
            print 'OK:'+m.group(0)

        # 	print pkt.ip.get_field_by_showname('Destination') +\
        # ':        ' +  pkt.ssl.get_field_by_showname('Server Name')
            if not d.has_key(pkt.ip.get_field_by_showname('Destination')):
                d[pkt.ip.get_field_by_showname('Destination')] = pkt.ssl.get_field_by_showname('Server Name')
        # priprint pktnt pkt.dns.get_field_by_showname('CNAME')
        # print pkt.dns.get_field_value('a')

    return d
# YoutubeVedioSSLExtractor('E:\MM5.pcap')

def YoutubeIP_Extractor(pcapFilePath):
    DNS_dict = YoutubeVedioDnsExtractor(pcapFilePath)
    SSL_dict = YoutubeVedioSSLExtractor(pcapFilePath)

    DNS_dict.update(SSL_dict)
    return  DNS_dict

def main(argv):
    if len(argv) != 2:
        print "Youtube vedio IP hostname extractor:"
        print "    Usage: python <PCAP dir>"
        print ""
        print argv[1]
        sys.exit(1)

    import glob

    files = glob.glob(argv[1]+"/*.pcapng")
    # print argv[1]+"/*.pcap"
    print files

    Youtube_IP_Host = {}
    for f in files:

        Youtube_IP_Host.update(YoutubeIP_Extractor(f))
    print Youtube_IP_Host

if __name__ == "__main__":
    main(sys.argv)
# print cap[0].dns.get_field_by_showname('CNAME')
# print cap[0].dns.get_field_value('a')


