joe_purchase=1000
one_share=32.87
tota_purcase=joe_purchase*one_share
broker=(tota_purcase*2)/100
net_purchase=tota_purcase-broker

#after two weeks

joe_sales=1000
one_sharee=33.92
tota_sales=joe_sales*one_sharee
brokerr=(tota_sales*2)/100
net_sales=tota_sales-brokerr

result=net_sales-net_purchase
if result<0:
    print(result ,"is lost")
else:
    print(result,"is Profit")
