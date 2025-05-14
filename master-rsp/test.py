import canopen

network = canopen.Network()
network.connect(channel='can0', bustype='socketcan')

# Interagir avec LSS
lss = network.lss

# Rechercher l'esclave LSS (optionnel)
# lss.wait_for_slave()
# lss.identify_remote_slave(vendor_id, product_code, revision, serial)

# Configurer l'esclave
lss.configure_node_id(1)
lss.store_configuration()

# Passer en mode opérationnel
lss.switch_state("WAITING")

# Ajouter le noeud
node = network.add_node(1, "'/home/vacop/Desktop/can-open-rsp/ODs/Slave_STM32/Slave_STM32.eds'")
node.nmt.state = 'PRE-OPERATIONAL'

# Lire un SDO
print(node.sdo[0x1018][1].raw)

