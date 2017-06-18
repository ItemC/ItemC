
### what is it and why is it useful

Example:
MMORPG could use the service to save ingame items in the blockchain.
why:
This confirms that the item belongs to one person, wont get lost, will not change (depends on the implementation of the MMORPG), and gives the owner the possiblity to trade it.

Trading works with a coin system.

Needed protocols:

Gift (Item)
Gift is every transaction which is not sending the currency.
It consists of:
 - sender (PublicKey)
 - receiver (PublicKey)
 - item hash (UUID)
 - provide public key (PublicKey)
 - (opional) splitable count (Float)
 - signing of sender (SIGN)

Item API
the most interesting part is the item hash (UUID) which can be though of like an ID for the item which is send. Important is, that the hash is the result of a hashed file representing the item. for example a json describing an ingame item like a sword. Or a json describing a card. Or a shash of an image file to proof that you are the real owner with rights for a specific image. The provider is the second part of it. Whoever wants to create items on the blockchain has to become a provider. acessible via their public key. They are responsible to always give you access to the json or file of the item. (Of course you also can make sure that you have a backup version of the file in case the provide itself fucks up. and Miners have the option to also backup different item files.)
Noone can change the item anymore now. because that would change the hash so you would not be a valid owner. So you OWN this one specific file/json or any other digital object and can proove this ownership by querying the blockchain. Of course ppl still can copy the item but they wont be able to proove their ownsership. Services than would not allow them to use it.
(for example in a computer game they could not use the item becaus they fail to proove ownership in the blockchain.)

Another value is the splitable count (FloatingPointNumber) which allows to split items. this makes the item system extreamly flexible since you can even use amounts of stomething, which basically allows any service to build their own currency as an item. A game could use wood as the ingame currency which than could be send as a wood item to associate the wood ppl have with their wallet. Since it is a splitable item 10 wood can be used to create multiple transaction to send fractions of the item to other ppl or use it for trading.

Send (currancy)

consists of:
 - sender (PublicKey)
 - receiver (PublicKey)
 - amount (Float)
 - signing of sender (SIGN)
This is a basic transaction with the blockchain currency.
Verified when hashed sender + amount + receiver is the same than verification result of senderPublickey with the signing.


Trading

basically a combination of the two transaction from type Gift or Send which are depend on each other and only work together.
To refer to the trading card game example again:
Cards could be traded with that system.

In this case the transaction would consist of the following:
 - A timestamp when it was created
 - A timeperiod until it is still valid
 - the First tranaction (userA -> userB)
 - the second transaction (userB -> userA)
 - the First sign of UserA (SIGN)
 - the second sign of UserB (SIGN)

This setup makes sure that both participating users agree with the tranaction's befor it gets added to the blockchain. Without the signings of both users the transaction is not valid -> will not get added to the blockchain.
If there is not trading partner found in the set time period the transaction gets also invalidated and never added to the blockchain. It of course can be restored with adapted values.



## [Features]()
