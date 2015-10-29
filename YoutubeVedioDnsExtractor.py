import sys  
reload(sys)  
sys.setdefaultencoding('utf8') 
import pyshark


def YoutubeVedioDnsExtractor(pcapFilePath):

	cap = pyshark.FileCapture(pcapFilePath,display_filter = 'dns.qry.name.len ==32 && ip.src == 8.8.8.8')

	for pkt in cap:
		
		print pkt.dns.get_field_by_showname('CNAME')
		print pkt.dns.get_field_value('a')

YoutubeVedioDnsExtractor('E:\\E.pcapng')


# print cap[0].dns.get_field_by_showname('CNAME')
# print cap[0].dns.get_field_value('a')


