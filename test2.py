import eet

CERT_PATH="/home/milda/Dokumenty/pyEET/eet odoo funguje/pos_fisc/eet/cert/EET_CA1_Playground-CZ683555118.p12"
CERT_PASS="eet"
eet_client = eet.EET(CERT_PATH, CERT_PASS, 1, 'pokladna1')
payment = eet_client.create_payment('P12322', 3248, test=False)
#payment.set_amount(eet.TAX_BASIC, 1000, 210)
result = eet_client.send_payment(payment)
print (result)

< field
name = "journal_id"
position = "after" >
< div


class ="row mt16" title="EET." >

< label
string = "EET Configuration"
for ="eet_config_id" class ="col-lg-3 o_light_label" widget="selection" / >
< group
name = "EET config ID" >
< field
name = "eet_config_id" / >
< / group >
< / div >
< / field >
