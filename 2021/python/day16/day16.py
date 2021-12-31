import os,re

path = os.path.dirname(os.path.realpath(__file__))

input = ''
with open(path + "\input.txt") as f:
    input = f.read().strip()

class Packet():
    """A node class for A* Pathfinding"""

    def __init__(self, binary):
        self.binary = binary
        self.index = 0
        self.decode()

        
    def decode(self):
        self.readVersion()
        self.readTypeId()
        if(self.typeId == 4): # literal
            self.readLiteral()
        else:
            self.readOperator()


    def readVersion(self):
        self.version = int(self.binary[self.index:self.index+3],2)
        self.index += 3


    def readTypeId(self):
        self.typeId = int(self.binary[self.index:self.index+3],2)
        self.index += 3


    def readOperator(self):
        self.lengthTypeId = int(self.readBits(1))
        self.subpackets = []
        if self.lengthTypeId == 0: # 15 bit length field
            self.subpacketlength = int(self.readBits(15),2)
            counter = 0
            while counter < self.subpacketlength:
                subbinary = self.binary[self.index:]
                subpacket = Packet(subbinary)
                self.subpackets.append(subpacket)
                counter += subpacket.index
                self.index += subpacket.index
        else:
            self.subpacketcount = int(self.readBits(11),2)
            counter = 0
            while counter < self.subpacketcount:
                subbinary = self.binary[self.index:]
                subpacket = Packet(subbinary)
                self.subpackets.append(subpacket)
                counter += 1
                self.index += subpacket.index


    def readLiteral(self):
        bits = self.readbinarysequence()
        self.literal = int(bits,2)

    def readbinarysequence(self,include_more_packets=False):
        bits = ''
        bit = self.readBits(1)
        morePackets = bool(int(bit))
        if include_more_packets:
            bits += bit
        while morePackets:
            bits += self.readBits(4)
            bit = self.readBits(1)
            morePackets = bool(int(bit))
            if include_more_packets:
                bits += bit
        bits += self.readBits(4)
        return bits


    def readBits(self,count):
        bits = self.binary[self.index:self.index+count]
        self.index += count
        return bits

    def calculate(self):
        result = 0
        if self.typeId == 0: # sum
            for sub in self.subpackets:
                result += sub.calculate()
        elif self.typeId == 1: # product
            result = 1
            for sub in self.subpackets:
                result *= sub.calculate()
        elif self.typeId == 2: # minimum
            result = None
            for sub in self.subpackets:
                subresult = sub.calculate()
                if result == None or subresult < result:
                    result = subresult
        elif self.typeId == 3: # maximum
            result = None
            for sub in self.subpackets:
                subresult = sub.calculate()
                if result == None or subresult > result:
                    result = subresult
        elif self.typeId == 4: # literal
            return self.literal
        elif self.typeId == 5: # greater than
            sub1 = self.subpackets[0].calculate()
            sub2 = self.subpackets[1].calculate()
            if sub1 > sub2:
                result = 1
            else:
                result = 0
        elif self.typeId == 6: # less than
            sub1 = self.subpackets[0].calculate()
            sub2 = self.subpackets[1].calculate()
            if sub1 < sub2:
                result = 1
            else:
                result = 0
        elif self.typeId == 7: 
            sub1 = self.subpackets[0].calculate()
            sub2 = self.subpackets[1].calculate()
            if sub1 == sub2:
                result = 1
            else:
                result = 0
        return result


def to_bin(input):
    #to binary
    binlen = len(input)*4
    integer = int(input, 16)
    binary = f'{integer:0>{binlen}b}'
    return binary


def get_version_sum(packet:Packet):
    try:
        return packet.version + sum([get_version_sum(p) for p in packet.subpackets])
    except AttributeError:
        return packet.version





binary = to_bin(input)

packet = Packet(binary)

#recurse through structure and sum version
versionsum = get_version_sum(packet)

print("Part 1: Version sum = " + str(versionsum))

result = packet.calculate()

print("Part 2: packet result = " + str(result))