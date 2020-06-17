import re


class Solution:
    IPV4_pattern = re.compile(
        r'^((25[0-5]|2[0-4][0-9]|1[0-9]{0,2}|2[0-9]{0,1})\.)((25[0-5]|2[0-4][0-9]|1[0-9]{0,2}|2[0-9]{0,1}|0)\.){2}(25[0-5]|2[0-4][0-9]|1[0-9]{0,2}|2[0-9]{0,1}|0)$')

    IPV6_chunk = r'([0-9a-fA-F]{1,4})'
    IPV6_pattern = re.compile(r'^(' + IPV6_chunk + r'\:){7}' + IPV6_chunk + r'$')

    def validIPAddress(self, IP: str) -> str:
        if self.IPV4_pattern.match(IP):
            return "IPv4"

        return "IPv6" if self.IPV6_pattern.match(IP) else "Neither"
