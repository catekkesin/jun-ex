import ipaddress

def ip_to_int(ip):
    """
    Convert an IPv4 address to a 32-bit integer.
    """
    return int(ipaddress.ip_address(ip))

def int_to_ip(n):
    """
    Convert a 32-bit integer to an IPv4 address.
    """
    return str(ipaddress.ip_address(n))

def min_subnet(ips):
    """
    Find a minimal spanning subnet for a set of IPv4 addresses.
    """

    # Convert IPs to integers
    ints = [ip_to_int(ip) for ip in ips]

    # Find min and max IP
    min_ip, max_ip = min(ints), max(ints)

    # Find subnet
    for prefix in range(32, -1, -1):
        net = ipaddress.ip_network(f'{int_to_ip(min_ip)}/{prefix}', strict=False)

        if min_ip >= int(net.network_address) and max_ip <= int(net.broadcast_address):
            return str(net)
    return None

def test_min_subnet():
    assert min_subnet({'192.0.2.0', '192.0.2.1'}) == '192.0.2.0/31', 'should be /31'
    assert min_subnet({'192.0.2.0', '192.0.2.130'}) == '192.0.2.0/24', 'should be /24'
    assert min_subnet({'192.0.2.255', '192.0.3.0'}) == '192.0.2.0/23', 'should be /23'
    assert min_subnet({'192.0.2.0', '192.0.2.1', '192.0.2.2', '192.0.2.3'}) == '192.0.2.0/30', 'should be /30'
    assert min_subnet({'192.0.2.0'}) == '192.0.2.0/32', 'should be /32'
    assert min_subnet({'192.0.2.0', '192.0.2.255'}) == '192.0.2.0/24', 'should be /24'
    



if __name__ == "__main__":
    test_min_subnet()
    print("All tests are passed")
    