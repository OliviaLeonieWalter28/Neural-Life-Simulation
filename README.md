# Activate Env

.\.env\Scripts\Activate.ps1

# maybe also need this?

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

pip install pygame

installed packages:

- pygame 2.6.1
- numpy-2.2.6

### What is needed:

- The creature needs to be able to eat, sleep, and walk. It also needs to procreate.
- It loses energy and gets hungry when walking and procreating.
- When energy is at 0, it will automatically fall asleep (but it can choose to fall sleep earlier than that)
- it should have hunger and energy
- if hungerpoints reach 10 then it will die.
- it should always try to procreate with someone stronger or equal to themselfs. (This will be advance in the GA)
- some kind of vision (raycast? how far?)
- Food can be both static and move around, moving food provides more hungerpoints
- [strengh = energy - hunger] could be a good way to determind the stronger matingpartner, but is this good? ( what if the partner just eaten and slept and was bad att finding food before?)
- (age + energy + offspring count) this one is more "natural" but also slow and hard to simulate in the beginning.
- Create a Debug menu on the right side, including stearing, hunger point decrease multiplier, energy decrease multiplier, NN + GA options, Pause?

### Ideas for the future

- should I add thirst?
- Later also include some nature zones
