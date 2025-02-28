---
title: 20 - Thinking on the game loop and starting the UI
date: 2025-02-26
---
So far, I have been working on the game without taking the time to write down the logic of the game loop. But without it, it is not possible to start working on the GameState or on the UI.

So, I started by drawing a diagram with a basic color scheme: white background means I am sure about the step, yellow means it will be in the game but I don't know exactly how it will be setup and red means that I am not sure about the step so it is not a priority as this point. For exemple in the picture bellow, working on a story introduction video or on some kind of items store does not make any sense for the moment.

<p style="text-align:center;"><img src="/images/Game%20loop%20logic.svg" alt="Image Description"></p>

This image gave me a clear idea of the areas where I need to brainstorm but also where I can already start working. On one hand, I need to focus on the game loop so I can begin playing with the GameState in Unreal. On the other hand, I can already start designing the UI and the main menu.
