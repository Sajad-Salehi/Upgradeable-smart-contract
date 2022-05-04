// contracts/ContractV1.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";


contract ContractV1 {
    
    mapping(address => uint256) public balances;
    address public USDC = 0x7079f3762805CFf9C979a5bDC6f5648bCFEE76C8;
    address constant admin = 0x2ba6e735C4f4e27aEE308c9a0e20921E853Ac0F6;

    function deposit(uint256 amount, address token_addrs) public payable {

        bool result = IERC20(USDC).transferFrom(msg.sender, address(this), amount);
        require(result == true);
        balances[msg.sender] += amount;
    }

    function witdraw(uint256 amount) public payable {

        require(balances[msg.sender] > amount, 'you do not have enough balance');
        balances[msg.sender] -= amount;
        IERC20(USDC).transfer(msg.sender, amount);
    }
}
