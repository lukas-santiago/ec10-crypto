class CriptoGaiusIuliusCaesar:
    key = 3
    def crypt(self, data):
        data_bytes = bytes(data, "utf-8")
        encripted = bytearray()
        for byte in data_bytes:
            encripted.append(byte + self.key)
        
        # print(encripted)                
        return encripted
    def decrypt(self, data):
        data_bytes = bytes(data, "utf-8")
        decripted = bytearray()
        for byte in data_bytes:
            decripted.append(byte - self.key)
            
        # print(decripted)
        return str(decripted, "utf-8")