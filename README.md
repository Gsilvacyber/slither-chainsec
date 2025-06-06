﻿# slither-chainsec
1. Arbitrary ETH Send
**Impact**: High
**Confidence**: Medium
**Description**:
The `withdraw(uint256)` function in SimpleContract (SimpleContract.sol#11-15) sends ETH to an arbitrary
user.
- Dangerous Call: `address(msg.sender).transfer(amount)` at line 13
**Recommendation**:
Ensure access control is properly implemented. Avoid sending ETH to arbitrary addresses unless explicitly
needed.


2. Reentrancy Risk
**Impact**: Informational
**Confidence**: Medium
**Description**:
Potential reentrancy issue in `withdraw(uint256)` function (SimpleContract.sol#11-15).
- External Call: `address(msg.sender).transfer(amount)` at line 13
- State Change After Call: `balance -= amount` at line 14




**Recommendation**:
Follow Checks-Effects-Interactions pattern:
1. Validate conditions
2. Update state
3. Perform external calls
