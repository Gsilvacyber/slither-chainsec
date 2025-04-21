// SPDX-License-Identifier: MIT
pragma solidity ^0.8.29;

contract SimpleContract {
    uint256 public balance;

    function deposit() public payable {
        balance += msg.value;
    }

    function withdraw(uint256 amount) public {
        require(amount <= balance, "Insufficient balance");
        payable(msg.sender).transfer(amount);
        balance -= amount;
    }
}
