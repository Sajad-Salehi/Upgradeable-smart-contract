from brownie import ContractV1, ContractV2, ProxyAdmin, TransparentUpgradeableProxy, accounts, network
from scripts.upgrade import upgrade, encode_function_data

def main():
    
    account = accounts.load('mywallet')
    print(f"ContractV1 Deploying to {network.show_active()}")
    
    contract = ContractV1.deploy({"from": account})
    proxy_admin = ProxyAdmin.deploy({"from": account})
    contract_encoded_initializer_function = encode_function_data()
    
    
    proxy = TransparentUpgradeableProxy.deploy(
        contract.address,
        account.address,
        contract_encoded_initializer_function,
        {"from": account, "gas_limit": 1000000},
    )
    
    print(f"Contract V1 deployed at {proxy}")
    
    
    print(f"Deploying to {network.show_active()}")
    contract2 = ContractV2.deploy({"from": account})
    
    proxy = TransparentUpgradeableProxy[-1]
    proxy_admin = ProxyAdmin[-1]
    upgrade(account, proxy, contract2, proxy_admin_contract=proxy_admin)
    print("Proxy has been upgraded!")
    
    
