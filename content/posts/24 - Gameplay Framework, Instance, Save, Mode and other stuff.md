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

After digesting all this information, here is what I have decided to do for my game:
