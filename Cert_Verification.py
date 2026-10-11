n=147394444986683678082068692748811980578808086268637263426506653566375585467229

e=62224867384168083562092953479086476125959079467647903006830380487709566400177

S1="1361db748116fe0a9b550feae5c2f81d458fe74fb72f796db1a358ebe44911dd4"
n1=5007683
e1=19

S2="32a3a1b51a7b30d9c69e9bd8eed8b02ce5fec9748cbedfbe52bebfb10a541b66"
n2=5723911
e2=23

S3="f3d75c2f8a9cb6a5914d88605f516c434bb7caa5ebdda801a4b80debe95d5fb7"
n3=6336887
e3=17

r1=4040673
r2=2183494
r3=1911042

# Test integer = 1234567

print(pow(r1,e1,n1))
print(pow(r2,e2,n2))
print(pow(r3,e3,n3))

# Cert 1 = "Rengoku:Hashira {n=5007683,e=19}"
# Cert 2 = "Akaza:Demon,3rd {n=5723911,e=23}"
# Cert 3 = "Tanjiro:The Hero{n=6336887,e=17}"

CertV1 = pow(int(S1, 16),e,n)
CertV2 = pow(int(S2, 16),e,n)
CertV3 = pow(int(S3, 16),e,n)

print(CertV1.to_bytes((CertV1.bit_length()+7)//8).decode("utf-8"))
print(CertV2.to_bytes((CertV2.bit_length()+7)//8).decode("utf-8"))
print(CertV3.to_bytes((CertV3.bit_length()+7)//8).decode("utf-8"))