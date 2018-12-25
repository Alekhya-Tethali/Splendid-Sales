from django.shortcuts import render_to_response, render
import time
from web3 import Web3, HTTPProvider
from . import contract_abi
from django.http import HttpResponseRedirect
from django.contrib import messages

from general_customers.models import Employee
bonusdata= Employee.objects.all()



def sendbonus(salesmanAddress, etherstopay):
    contract_address1 = "0x5ace542521c7c3186d50269687979ae3e00c0496"
    wallet_private_key = "0x7b52b24d4ab8c7ee31a4b3320d09721a9346974e70c831d0860d38e415edd968"
    wallet_address1 = "0x2C5766dD6c9D77db6e6F215FF909249d3154B7e2"

    w3 = Web3(HTTPProvider("https://ropsten.infura.io/br3FlVOPi0bXVyO4oAzz"))
    contract_address = Web3.toChecksumAddress(contract_address1)
    wallet_address = Web3.toChecksumAddress(wallet_address1)
    w3.eth.enable_unaudited_features()
    contract = w3.eth.contract(address=contract_address, abi=contract_abi.abi)

    nonce = w3.eth.getTransactionCount(wallet_address)
    ethers = etherstopay
    txn_dict = contract.functions.payBonus( Web3.toChecksumAddress(salesmanAddress)).buildTransaction({
        'value': w3.toWei(ethers,'ether'),
        'chainId': 3,
        'gas': 140000,
        'gasPrice': w3.toWei('40', 'gwei'),
        'nonce': nonce,
    })

    signed_txn = w3.eth.account.signTransaction(txn_dict, private_key=wallet_private_key)

    result = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

    tx_receipt = w3.eth.getTransactionReceipt(result)

    count = 0
    while tx_receipt is None and (count < 30):
        time.sleep(10)

        tx_receipt = w3.eth.getTransactionReceipt(result)

        print(tx_receipt)

    if tx_receipt is None:
        return {'status': 'failed', 'error': 'timeout'}

    return {'status': 'added'}

def payoutbonus(request):
    to=''
    success=''
    for b in bonusdata:
        pk1=str(b.pk)
        if pk1 in request.GET:
            emp=Employee.objects.get(pk=b.pk)
            to=b.toid
            etherstopay = b.etherstopay
            success = sendbonus(to, etherstopay)
            if success:
                emp.pay='y'
                emp.save()


    bonusdata2=Employee.objects.filter(pay='n')


    if success:
        messages.success(request, 'Transferred Successfully')
        return HttpResponseRedirect('/refbonus')
    return render(request, 'referralbonus.html',{'bonusdata':bonusdata2})