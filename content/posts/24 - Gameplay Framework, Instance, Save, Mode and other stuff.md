---
title: 24 - Gameplay Framework, Instance, Save, Mode and other stuff
date: 2025-03-20
---
I wanted to go back to the game loop logic and introduce a `PlayerScore`, basically the nomber of snakes killed, and, `PlayersCoins`, coins system for upgrading weapons, buying pickups and so on. But soon I had a problem of understanding: which class should handle what? How do I update the HUD values? Which class modifies what?

I took couple of days to read some documentation, read articles, watch tutorials. Here is the list of sources I found useful in my quest to master the Unreal Gameplay Framework:
- [Gameplay Framework](https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-framework-in-unreal-engine) from Unreal documentation (what a surprise)
- [The Unreal Engine Game Framework: From int main() to BeginPlay](https://www.youtube.com/watch?v=IaU2Hue-ApI) by Alex Forsythe, an deep-dive on how the engine works
- [Saving and Loading Your Game](https://dev.epicgames.com/documentation/en-us/unreal-engine/saving-and-loading-your-game-in-unreal-engine) also from Unreal documentation
- [Gameplay Framework](https://cedric-neukirchen.net/docs/multiplayer-compendium/common-classes/) blog posts by Cedric Neukirchen

After digesting all this information, and with the help of ChatGPT, here is what I have decided to do for my game:
- A `SaveGame` class to be able the pass player info from on game to another
- A `GameInstance` class managing the loading/saving system and being the source for global variables like `PlayerName`, `PlayerScore` and `PlayerCoins`
- The `GameMode` class managing play rules, win or defeat conditions based on player health, score and so on
- The `PlayerController` class being responsible to update the `HUD` and interacting with the `GameMode` and the `GameInstance`

To fit this "framework" I had to rework some of my classes as the `PlayerController` and the `GameMode`. Here is a detailed example of how my classes interact with each other in the shooting snakes workflow:

<p style="text-align:center;"><img src="/images/Pasted%20image%2020250329114533.png" alt="Image Description"></p>
<p style="text-align:center; font-style:italic;">An example of my new framework implementation.</p>
